"""晶体小工具（示例插件）的 Python 部分：run(action, inputs, context)，与 Crystery 内置插件相同的约定。

Crystery 的内置模块（structure_formats、cif_structure、pxrd、pores）在 sys.path 上，可以直接导入；
自带的 numpy、gemmi 也可以用。返回值和内置插件一样：notice（提示）、blocks（表格、文字）、export（另存文件）。
"""
import math

import gemmi
import structure_formats
from cif_structure import cell_volume

AVOGADRO = 0.602214076  # g/cm³ 换算：质量 (g/mol) / (体积 (Å³) × 0.6022)


def density(inputs, context):
    if not context.get("file"):
        raise ValueError("先打开一个结构文件")
    digits = int(inputs.get("digits") or 3)
    payload = structure_formats.structure_payload(context["file"], int(inputs.get("structure_part") or 0))
    if not payload.get("periodic", True):
        raise ValueError("分子没有晶胞，算不了密度")
    counts = {}
    for site in payload["sites"]:
        copies = structure_formats.multiplicity(site["frac"], payload["symops"], payload["cell"]) if len(payload["symops"]) > 1 else 1
        counts[site["element"]] = counts.get(site["element"], 0) + copies * float(site.get("occupancy", 1.0))
    mass = sum(n * gemmi.Element(element).weight for element, n in counts.items())
    volume = cell_volume(payload["cell"])
    formula = structure_formats.cell_formula(payload)
    rows = [["晶胞体积 / Å³", round(volume, 2)], ["晶胞内容的质量 / (g/mol)", round(mass, digits)],
            ["密度 / (g/cm³)", round(mass / (volume * AVOGADRO), digits)]]
    if formula:
        rows[1:1] = [["化学式", formula["sum"]], ["Z", formula["z"]]]
    content = [[element, round(n, digits)] for element, n in sorted(counts.items())]
    return {"blocks": [{"type": "table", "title": f"{payload['title']}：密度与化学式", "columns": ["项目", "值"], "rows": rows},
                       {"type": "table", "title": "晶胞内容", "columns": ["元素", "个数"], "rows": content}],
            "notice": f"密度 {round(mass / (volume * AVOGADRO), digits)} g/cm³"}


def neighbours(inputs, context):
    """The atoms closest to inputs["atom"] among those shown (context.crystal: the view's atoms, Cartesian Å)."""
    crystal = context.get("crystal") or {}
    atoms = crystal.get("atoms") or []
    index = int(inputs.get("atom", -1))
    if not 0 <= index < len(atoms):
        raise ValueError("没有这个原子")
    center = atoms[index]["cart"]
    near = sorted((math.dist(center, atom["cart"]), atom["label"]) for i, atom in enumerate(atoms) if i != index)[:8]
    digits = int(inputs.get("digits") or 3)
    return {"blocks": [{"type": "table", "title": f"{atoms[index]['label']} 的近邻", "columns": ["原子", "距离 / Å"],
                        "rows": [[label, round(d, digits)] for d, label in near]}]}


def run(action, inputs, context):
    return {"density": density, "neighbours": neighbours}[action](inputs, context)
