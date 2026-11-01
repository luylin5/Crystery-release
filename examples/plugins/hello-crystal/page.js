// 晶体小工具（示例插件）的界面脚本：Crystery 把它放进页面运行，它调用 Crystery.plugin 拿到 api。
Crystery.plugin("org.crystery.hello-crystal", api => {
  // 英文界面的翻译（中文 → 英文）。
  api.i18n.add({
    "晶体小工具（示例）": "Crystal tools (example)", "密度与化学式": "Density and formula", "近邻": "Neighbours",
    "最近打开的结构": "Structures opened", "这个原子的近邻": "Neighbours of this atom", "示例": "Example",
    "打开结构后，这里记下每次打开的文件。": "Once a structure is open, the files opened are listed here.",
    "示例插件的页面：记录打开过的结构。": "The example plugin's page: the structures opened.",
  });

  // 侧边栏的一页（在“插件”标签下）。
  const opened = [];
  const page = api.panel.addPage({
    id: "log", title: "最近打开的结构",
    render(body) {
      body.classList.add("hello-crystal-page");
      const hint = document.createElement("p"); hint.className = "panel-hint"; hint.textContent = "示例插件的页面：记录打开过的结构。";
      const log = document.createElement("pre"); log.className = "hello-crystal-log";
      log.textContent = opened.length ? opened.join("\n") : "打开结构后，这里记下每次打开的文件。";
      body.replaceChildren(hint, log);
    },
  });

  // 功能区：“插件”标签里一组按钮，“工具”标签里也放一个。
  api.ribbon.addGroup({ title: "示例", page: "log", tools: () => [
    { label: "密度与化学式", title: "从结构文件算晶胞内容、化学式和密度", disabled: !api.file(), run: () => void api.run("density") },
    { label: "最近打开的结构", run: () => page.show() },
  ] });
  api.ribbon.addGroup({ title: "晶体小工具", tab: "tools", tools: () => [
    { label: "密度与化学式", disabled: !api.file(), run: () => void api.run("density") },
  ] });

  // 原子的右键菜单：这个原子的近邻（Python 用 context.crystal 计算）。
  api.menu.atom(atom => [{ label: "这个原子的近邻", run: () => void api.run("neighbours", { atom }, { title: "近邻" }) }]);

  // 事件：打开结构时记下来。
  api.on("structure-opened", detail => {
    opened.unshift(detail.file);
    opened.length = Math.min(opened.length, 20);
    page.refresh();
  });
});
