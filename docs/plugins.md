# 写 Crystery 插件

[返回 README](../README.md)

插件给 Crystery 加新功能，可以有两部分，至少要有一部分：

- **Python 部分**：和 Crystery 内置插件一样的 `run(action, inputs, context)`。它拿到当前结构的文件和三维画面里的原子，返回表格、文字、要保存的文件或盖在画面上的图。
- **界面脚本**：在 Crystery 的页面里运行。它可以往功能区（任何标签）加按钮和菜单，往左侧栏加页面，往右键菜单加项目，监听打开结构、选择原子等事件，修改显示设置，转动视角，运行自己的 Python 动作。

完整的例子在 [examples/plugins/hello-crystal](../examples/plugins/hello-crystal)：它计算密度和化学式，在功能区、侧边栏和原子右键菜单里各加了东西，并监听打开结构的事件。

插件就是受信任的代码，Crystery 不做沙箱隔离，安装前会提醒用户。插件功能从 Crystery 0.5.0 开始提供。

## 文件结构

```
hello-crystal/
  plugin.json     清单（必需）
  main.py         Python 部分（可选）
  page.js         界面脚本（可选）
  page.css        样式表（可选）
  …               插件需要的其他文件、自带的纯 Python 包
```

装好的插件放在 `<数据目录>/plugins/<id>/`。插件自己的数据可以写进 `context["plugin_data_dir"]`，也就是 `<数据目录>/plugin-data/<id>/`，卸载、重装时不会删掉。数据目录：便携版在程序旁边的 `Crystery-data`，安装版在 `%APPDATA%/Crystery`。

## plugin.json

```json
{
  "id": "org.crystery.hello-crystal",
  "name": "晶体小工具（示例）",
  "version": "1.0.0",
  "crystery": ">=0.5.0",
  "author": "你的名字",
  "homepage": "https://github.com/…",
  "description": "一句话说明插件做什么。",
  "entry": "main.py",
  "script": "page.js",
  "style": "page.css",
  "inputs": [
    { "id": "digits", "label": "小数位数", "type": "number", "min": 1, "max": 6, "step": 1, "default": 3 }
  ],
  "actions": [
    { "id": "density", "label": "密度与化学式", "title": "鼠标停在按钮上时的说明" },
    { "id": "neighbours", "label": "近邻", "hidden": true }
  ],
  "contributes": { "crystal_actions": [ { "action": "picture", "label": "我的渲染" } ] }
}
```

| 字段 | 说明 |
|---|---|
| `id` | 唯一的 ID，像 `com.example.tool`：只用小写字母、数字、点和连字符，至少两段。安装后的文件夹就用这个名字。 |
| `name`、`version` | 名称和版本号（`1.2.3`）。 |
| `crystery` | 支持的 Crystery 版本，如 `">=0.5.0"`、`">=0.5 <0.7"`。不满足时插件不加载，插件管理里提示更新 Crystery。 |
| `author`、`homepage`、`description` | 显示在插件管理里。 |
| `entry` | Python 入口文件。 |
| `script`、`style` | 界面脚本和样式表，各不超过 4 MB。 |
| `inputs` | 插件的设置项，每项为 `{ id, label, type, default?, options?, min?, max?, step?, placeholder?, group? }`，`type` 是 `text`、`number`、`select`（`options` 给出选项）、`checkbox` 或 `color`。Crystery 自动生成一个设置页，插件的组名旁边带 ⚙，点它打开。设置值会随每次运行一起传给 Python。 |
| `actions` | Python 动作。没有 `hidden` 的动作会自动出现在"插件"标签里插件自己那一组按钮中。 |
| `contributes.crystal_actions` | 三维画面右上角的按钮。点击后运行这个 Python 动作，返回的 `overlay` 图片盖在画面上。 |
| `dependencies` | **不支持**。Crystery 自带的 Python 没有 pip，不会安装依赖，写了只会在插件管理里显示警告。 |

## Python 部分

```python
def run(action, inputs, context):
    if action == "density":
        return {"blocks": [{"type": "table", "title": "结果", "columns": ["项目", "值"], "rows": [["密度", 1.23]]}],
                "notice": "算好了"}
    raise ValueError(f"未知操作 {action}")
```

每次运行都在一个新的 Python 进程里，工作目录是插件文件夹，限时 120 秒。用户点"取消"时，Crystery 会结束这个进程。

**`inputs`**：插件设置项的当前值，加上界面脚本 `api.run(action, inputs)` 传来的值，再加上 `structure_part`（多结构文件里显示的是第几个）。

**`context`** 里常用的字段：

| 键 | 内容 |
|---|---|
| `file` | 打开的结构文件路径，没打开时是 `None` |
| `crystal` | 三维画面里的结构：`cell`、`matrix`（晶格向量，Å）、`atoms`（`label`、`element`、`cart`、`frac`、`occupancy` 等）、`bonds`、`view`（显示设置）、`camera` |
| `output_dir` | 输出文件夹。`overlay` 和 `export` 引用的文件必须写在这里，比如写到 `<output_dir>/<插件 id>/` 下面 |
| `plugin_id`、`plugin_dir`、`plugin_data_dir`、`crystery_version` | 插件自己的信息 |

**能用的包**：Python 标准库、numpy、gemmi、开源 PyMOL（`from pymol import cmd`）、Mitsuba 3。Crystery 内置插件的模块也在 `sys.path` 上，可以直接导入：

- `structure_formats.structure_payload(path, part)`：读出各种格式的结构，包括晶胞、对称操作、原子位点
- `cif_structure`：CIF 解析和晶胞体积
- `pxrd`：粉末衍射
- `pores`：孔道
- `progress.report(fraction, message)`：更新进度条，`fraction` 取 0–1

其他纯 Python 包直接放在插件文件夹里：插件文件夹在 `sys.path` 的最前面。需要编译的包要和 Crystery 自带的 Python（3.14，Windows x64）匹配。

**返回值**（与内置插件相同）：

- `blocks`：`{"type": "table", "title", "columns", "rows"}` 或 `{"type": "text", "title", "text"}`，每个在一个窗口里显示，可以复制。
- `notice`：右下角的提示。
- `export`：`{"file": "<output_dir 下的相对路径>", "name": "建议的文件名"}`，Crystery 弹出另存为对话框。
- `overlay`：`{"file": "<output_dir 下的 PNG>"}`，只对 `crystal_actions` 的按钮有效，图盖在三维画面上。

出错时直接 `raise ValueError("给用户看的说明")`，说明文字会显示在提示里。

## 界面脚本

```js
Crystery.plugin("org.crystery.hello-crystal", api => {
  api.ribbon.addGroup({ title: "示例", tools: () => [
    { label: "密度与化学式", disabled: !api.file(), run: () => void api.run("density") },
  ] });
});
```

脚本在页面加载时运行一次。启用、重新安装插件时也会再运行一次。`Crystery.plugin` 的 ID 必须是插件自己的。停用或卸载时，插件通过 api 添加的东西都会自动去掉，并依次调用 `api.onUnload` 登记的函数。

| api | 作用 |
|---|---|
| `api.ribbon.addGroup({ title, tab?, page?, tools })` | 功能区的一组按钮。`tab` 默认是 `"plugins"`，也可以是 `"file"`、`"structure"`、`"tools"`、`"render"`。`tools` 是数组，或者每次画功能区时都会调用的函数，元素为 `{ label, title?, icon?, active?, disabled?, run }` 或 `{ label, menu: () => [{ label, run, active?, disabled? }] }`。`page` 是 `panel.addPage` 的 id，点组名时打开这一页。返回值是一个函数，调用它就移除这一组。 |
| `api.ribbon.refresh()` | 状态变了以后重画功能区。 |
| `api.panel.addPage({ id, title, render(body) })` | 左侧栏里的一页，放在"插件"标签下。返回 `{ body, refresh(), show(), remove() }`。 |
| `api.menu.atom(atom => items)` | 原子右键菜单里追加的项目。`atom` 是 `api.viewer.scene().atoms` 里的序号，项目格式为 `{ label, run, checked?, disabled?, items? }`。 |
| `api.menu.background(() => items)` | 在空白处右键时菜单里追加的项目。 |
| `api.viewer.settings()` / `update(patch)` | 读、改显示设置，常用的键：`model`（`ballstick`、`stick`、`spacefill`、`wire`、`ellipsoid`）、`background`、`range`（`cell`、`molecules`、`asym`、`sphere`）、`supercell`、`labels`、`cell`、`axes`、`hide_h`、`hbonds`、`polyhedra`、`orthographic`、`ball_scale`、`bond_radius`、`elements`（按元素的 `color`、`radius`、`hidden`、`model`）、`sphere_center`、`sphere_radius`。 |
| `api.viewer.scene()`、`select(atoms)`、`selected()`、`turn(axis, degrees)`、`script(pml)` | 场景（原子、键）、选择原子、转动视角、运行 PyMOL 命令。 |
| `api.viewer.crystal()` | Python 拿到的那份 `context.crystal`。 |
| `api.viewer.addButton({ action, label })` | 三维画面上的按钮，作用同 `crystal_actions`。 |
| `api.viewer.raw()`、`api.app()` | 查看器和应用对象本身，api 不够用时再用。它们的成员在新版本里可能改变。 |
| `api.run(action, inputs?, { title?, quiet?, show? })` | 运行插件自己的 Python 动作，带进度卡和"取消"。结果会自动显示，`show: false` 时不显示；`quiet: true` 时没有进度卡，出错会抛异常。返回值是 Python 的返回值。 |
| `api.file()`、`api.open(path)`、`api.render()` | 当前文件、打开文件、渲染预览（返回输出文件夹里的图）。 |
| `api.inputs.get()` / `set(values)` | 插件设置项的值。 |
| `api.storage.get(key?)` / `set(key, value)` | 插件自己的少量数据，存在 Crystery 的设置里。 |
| `api.on(event, fn)` | 事件：`structure-opened`（`{ file, part }`）、`selection-changed`（`{ atoms }`）、`view-changed`、`language`（`{ language }`）。 |
| `api.onUnload(fn)` | 插件停用、卸载或重装时调用，用来清理定时器、加在 document 上的监听器等。 |
| `api.toast(text, error?)` | 右下角的提示。 |
| `api.dialog.form(title, fields)`、`alert(title, text)`、`confirm(title, text)` | 对话框。`fields` 的格式同 `inputs`，可以带 `value`。`form` 返回填写的值，取消时返回 `null`。 |
| `api.i18n.add({ "中文": "English" })` | 英文界面的翻译。Crystery 按这张表翻译插件显示的中文。 |
| `api.crystery.version`、`api.crystery.language()` | Crystery 的版本号和当前界面语言。 |

页面的内容安全策略不允许脚本联网（`fetch` 外部地址会失败），需要联网的工作放在 Python 部分做。样式表里可以用 Crystery 的 CSS 变量，比如 `var(--ink)`、`var(--muted)`、`var(--line)`。

## 开发和调试

1. 在 Crystery 里打开 **插件 › 插件管理 › 从文件夹安装…**，选择插件文件夹。安装时会把文件夹复制一份。
2. 改了代码以后，再"从文件夹安装"一次。界面脚本马上重新运行，Python 部分在下次运行时生效。
3. 脚本出错时，插件会被停用，插件管理里显示错误信息。Python 出错时，提示里显示错误，鼠标停在提示上可以看到日志。
4. 某个插件让窗口打不开时，用 `Crystery.exe --safe-mode` 启动（这次不加载任何插件），然后在插件管理里停用它。

也可以不开窗口，用安装版自带的 Python 单独测试 Python 部分。在安装目录（例如 `C:\Users\<你>\AppData\Local\Programs\Crystery`）下运行，把 `entry` 和 `file` 换成自己的路径：

```bash
echo '{"entry":"D:/hello-crystal/main.py","paths":["resources/plugin"],"action":"density","inputs":{},"context":{"file":"D:/rutile.cif"}}' | resources/python-runtime/python.exe -I resources/python/runner.py
```

## 打包和发布

1. 把插件文件夹压缩成 zip。zip 里可以直接放文件，也可以再套一层文件夹。路径里不能有 `..`、绝对路径或链接，解压后总大小不超过 300 MB。
2. 用户可以用"从文件安装…"安装这个 zip。
3. 要进插件仓库：把 zip 放到一个固定的 https 地址（比如自己仓库的 GitHub Release），算出 sha256，再向 [luylin5/Crystery-plugins](https://github.com/luylin5/Crystery-plugins) 提交 PR，在 `index.json` 的 `plugins` 里加一条：

```json
{ "id": "org.crystery.hello-crystal", "name": "晶体小工具（示例）", "version": "1.0.0", "crystery": ">=0.5.0",
  "author": "…", "homepage": "https://github.com/…", "description": "…",
  "download": "https://github.com/…/releases/download/v1.0.0/hello-crystal-1.0.0.zip",
  "sha256": "…" }
```

Windows 上算 sha256：`certutil -hashfile hello-crystal-1.0.0.zip SHA256`。macOS 和 Linux 用 `shasum -a 256`。发布新版本时，更新这一条的 `version`、`download` 和 `sha256`。Crystery 会核对 sha256，对不上就不安装。
