# Crystery

**中文** · [English](#english)

Crystery 是一个 Windows 桌面软件，用来查看晶体和分子结构、画出可以发表的结构图，并模拟粉末衍射（PXRD）图谱、分析孔道。下载即可使用，不需要另外安装 Python、PyMOL 或其他程序。

> ⭐ **如果 Crystery 对你有帮助，请给这个仓库点一个 Star；在论文、报告或演示中用它作图或计算时，请写明使用了 Crystery（引用格式见[下文](#引用)）。** 这是对开发最大的支持。

## 下载

在 [Releases](https://github.com/luylin5/Crystery-release/releases) 页面下载最新版本：

| 文件 | 说明 |
|---|---|
| `Crystery-<版本>-setup.exe` | **安装包（推荐）**：双击安装，可以选择安装位置，创建桌面和开始菜单快捷方式 |
| `Crystery-<版本>-portable.exe` | 便携版：不用安装，双击即可运行 |

- 系统要求：Windows 10 / 11，64 位。Mitsuba 渲染有 NVIDIA 显卡时更快，没有显卡也能用 CPU 渲染。
- 安装版的设置保存在用户的 AppData 中，图库在“文档\Crystery 图库”，升级或卸载都不会删除；便携版保存在程序旁边的 `Crystery-data` 文件夹中，整个文件夹可以直接拷走。
- Windows 可能提示“无法识别的应用”（安装包没有代码签名）：点“更多信息” › “仍要运行”。
- 软件内 **文件 › 帮助 › 检查更新** 可以查看是否有新版本。

## 功能

- **打开结构**：CIF、SHELX RES/INS、MOL/SDF、MOL2、PDB、XYZ / 扩展 XYZ、VASP POSCAR、XSF、Gaussian 输入、CSSR；一个文件中有多个结构（多个数据块、多帧）时可逐个查看。
- **调整画面**：球棍、棍状、空间填充、线框、热椭球模型；元素颜色和半径、键和氢键、弱作用、配位多面体、芳环填充；超胞、生长、无序组分；沿晶轴或任意 [uvw] / (hkl) 观察、透视或正交投影、剪切平面；选择、测量和标注。
- **渲染出图**：两种渲染器——**PyMOL**（光线追踪，快，和画面一致）和 **Mitsuba 3**（路径追踪：柔和阴影、反射、玻璃、发光、景深）；自定义图片尺寸、DPI 和透明背景；逐帧渲染旋转、摇摆等**视频**。
- **PXRD 模拟**：从晶胞计算粉末衍射图谱（波长、2θ 范围、峰宽、温度因子、择优取向），可叠加实验图谱（XRDML、RAS、两列数据）对比。
- **孔道分析**：用 Zeo++ 或网格法计算孔径、比表面积、孔体积和孔径分布，并把孔道画进结构。
- **图库与风格**：画好的图连同设置存进图库；把一套画法存成风格，打开别的结构一键套用；批量处理多个文件。
- **中文 / English 界面**，内置操作手册（F1）和首次启动的新手引导。

## 引用

如果你在发表的工作中使用了 Crystery 作图或计算，请在方法、致谢或图注中写明软件名称，例如：

> 结构图使用 Crystery 绘制（https://github.com/luylin5/Crystery-release）。

或使用以下引用格式：

```
luylin5. Crystery (version 0.1.0) [Computer software]. 2026. https://github.com/luylin5/Crystery-release
```

```bibtex
@software{crystery,
  author  = {luylin5},
  title   = {Crystery},
  version = {0.1.0},
  year    = {2026},
  url     = {https://github.com/luylin5/Crystery-release}
}
```

用 Crystery 计算孔道时，请同时引用 Zeo++；用 Mitsuba 渲染时，可以同时注明 Mitsuba 3。

## 许可

Crystery 可以**免费使用**，包括学术和商业用途，可以原样分享官方发布的文件；不得修改、反编译后再发布，也不得出售。用 Crystery 生成的图片和数据归你所有。详见 [LICENSE](LICENSE)。

Crystery 内含的第三方开源组件（PyMOL、Mitsuba 3、Zeo++、gemmi、NumPy、Electron 等）按各自的许可发布，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 反馈

遇到问题或有建议，请在 [Issues](https://github.com/luylin5/Crystery-release/issues) 中提出；附上出错的结构文件和截图会更容易定位问题。

---

<a id="english"></a>

# Crystery (English)

Crystery is a Windows desktop application for viewing crystal and molecular structures, making publication-quality structure figures, simulating powder X-ray diffraction (PXRD) patterns and analysing pores. Download it and run it: there is no need to install Python, PyMOL or anything else.

> ⭐ **If Crystery is useful to you, please star this repository, and when you use it for figures or calculations in a paper, report or talk, please mention Crystery by name (see [Citing](#citing)).** It is the best way to support its development.

## Download

Get the latest version from the [Releases](https://github.com/luylin5/Crystery-release/releases) page:

| File | What it is |
|---|---|
| `Crystery-<version>-setup.exe` | **Installer (recommended)**: choose where to install; desktop and Start-menu shortcuts |
| `Crystery-<version>-portable.exe` | Portable app: nothing to install, double-click to run |

- Requirements: Windows 10 / 11, 64-bit. Mitsuba renders faster with an NVIDIA GPU, and falls back to the CPU without one.
- The installed app keeps its settings in your AppData and its gallery in Documents\Crystery 图库, so updating or uninstalling keeps them; the portable app keeps them in a `Crystery-data` folder next to the program, so the whole folder can be moved as it is.
- Windows may warn about an unrecognised app (the installer is not code-signed): click "More info" › "Run anyway".
- **File › Help › Check for updates** in the app tells you when a new version is out.

## Features

- **Open structures**: CIF, SHELX RES/INS, MOL/SDF, MOL2, PDB, XYZ / extended XYZ, VASP POSCAR, XSF, Gaussian input, CSSR; files holding several structures (data blocks, frames) can be stepped through.
- **Shape the view**: ball-and-stick, stick, space-filling, wireframe and thermal-ellipsoid models; element colours and radii, bonds and hydrogen bonds, weak interactions, coordination polyhedra, ring fill; supercells, growth, disorder; views along cell axes or any [uvw] / (hkl), perspective or orthographic projection, clipping planes; selection, measurement and labels.
- **Render pictures**: two renderers — **PyMOL** (ray tracing: fast, matches the view) and **Mitsuba 3** (path tracing: soft shadows, reflections, glass, glow, depth of field); image size, DPI and transparent background; frame-by-frame **videos** of turning and rocking structures.
- **PXRD simulation**: the powder pattern from the cell (wavelength, 2θ range, peak width, temperature factors, preferred orientation), with measured patterns (XRDML, RAS, two-column data) overlaid for comparison.
- **Pore analysis**: pore sizes, surface area, pore volume and pore size distribution with Zeo++ or a grid method, with the pores drawn in the structure.
- **Gallery and styles**: save drawings with their settings to a gallery; save a look as a style and apply it to other structures with one click; batch-process many files.
- **Chinese / English interface**, a built-in manual (F1) and a getting-started tour on first launch.

## Citing

If you use Crystery for figures or calculations in published work, please name it in the methods, acknowledgements or figure captions, for example:

> Structure figures were made with Crystery (https://github.com/luylin5/Crystery-release).

or cite it as:

```
luylin5. Crystery (version 0.1.0) [Computer software]. 2026. https://github.com/luylin5/Crystery-release
```

```bibtex
@software{crystery,
  author  = {luylin5},
  title   = {Crystery},
  version = {0.1.0},
  year    = {2026},
  url     = {https://github.com/luylin5/Crystery-release}
}
```

When you use Crystery's pore analysis, please also cite Zeo++; for Mitsuba renderings you may also credit Mitsuba 3.

## License

Crystery is **free to use**, including for academic and commercial work, and the official release files may be shared unchanged; it may not be modified, decompiled and redistributed, or sold. Pictures and data you make with Crystery are yours. See [LICENSE](LICENSE).

The open-source components bundled with Crystery (PyMOL, Mitsuba 3, Zeo++, gemmi, NumPy, Electron and others) are distributed under their own licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Feedback

Please report problems and suggestions in [Issues](https://github.com/luylin5/Crystery-release/issues); attaching the structure file and a screenshot makes problems much easier to track down.
