# Crystery user manual

[中文](manual.md) · **English** · [Back to README](../README.md#english)

- [Quick start](#start)
- [Interface overview](#ui)
  - [Left panel pages](#left-panel-pages)
- [File](#file)
  - [Open and Recent](#file-open)
  - [Multi-structure files (data blocks, frames, molecules)](#file-parts)
  - [New structure](#file-new)
  - [Project files (.crystery)](#file-project)
  - [Export](#file-export)
  - [Batch processing](#file-batch)
  - [Preferences and Help](#file-prefs)
  - [Prompt on closing](#file-quit)
- [Structure](#model)
  - [Selection](#model-select)
  - [Labels and measurement](#model-measure)
  - [Range and growth](#model-range)
  - [Display effects, background and view](#view)
- [Tools](#tools)
- [PXRD](#pxrd)
  - [Viewing and exporting the pattern](#viewing-and-exporting-the-pattern)
- [Pores](#pores)
  - [Display and results](#display-and-results)
- [Render](#render)
  - [Style presets](#render-styles)
  - [PyMOL (ray tracing)](#render-pymol)
  - [Mitsuba (path tracing)](#render-mitsuba)
  - [Output, picture, and script](#render-export)
- [Mouse and shortcuts](#keys)
  - [Right-click menus](#right-click-menus)
  - [Keyboard shortcuts](#keyboard-shortcuts)
- [Gallery](#gallery)
- [Supported file formats](#formats)
  - [Structures](#structures)
  - [Other](#other)
- [FAQ](#faq)
- [About](#about)


View and render crystal and molecular structures, simulate PXRD patterns, and analyze pores. Finished pictures can be saved to the gallery or to a project file and reopened exactly as they were.

In this manual, <strong>File › Export structure › CIF</strong> means: the "File" tab in the menu bar at the top, then the "CIF" button in the "Export structure" group of the ribbon.

## <a id="start"></a>Quick start

1. <strong>Open a structure.</strong> Click <strong>File › Open › Open file</strong> (<kbd>Ctrl</kbd>+<kbd>O</kbd>), drag a file into the window, or choose Crystery under "Open with" in Explorer. If you have no file, use "New structure…" (<kbd>Ctrl</kbd>+<kbd>N</kbd>) to enter the cell and atoms. When no file is open, the start page lists recently opened files and the latest drawings in the gallery.
2. <strong>Rotate and select.</strong> Right-drag to rotate, scroll to zoom, <kbd>Ctrl</kbd>+right-drag to pan; left-click to select an atom, left-drag to box-select. See [Mouse and shortcuts](#keys).
3. <strong>Adjust the look.</strong> In "Structure", choose Ball and stick, Sticks, Space-filling, Wireframe, or Thermal ellipsoids; in "Display", choose the unit cell, complete molecules, or asymmetric unit, supercells, and disorder components. The title below each group of buttons (with a ⚙) opens that group's detailed settings.
4. <strong>Render.</strong> On the <strong>Render</strong> tab's ribbon, choose PyMOL (fast) or Mitsuba (realistic, slower), click "Render preview" to see the result, then click "Export image". The image size (width, height, DPI, transparent background) is under <strong>Render › Size › Image size</strong>; the frame in the middle of the 3D view is the render frame.
5. <strong>Save.</strong> <kbd>Ctrl</kbd>+<kbd>S</kbd> saves the current drawing to the gallery; to save it on its own or send it to someone, use <strong>File › Project › Save project</strong> to write a single `.crystery` file.

> When running from source, the first launch shows "Preparing the render environment", which creates a Python environment for the plugin and installs its components (internet access required, once only). The portable version already includes them, so this step is not needed.

## <a id="ui"></a>Interface overview

The window is laid out like PowerPoint:

- <strong>Title bar</strong>: on the left, the Undo and Redo buttons; in the middle, the menu bar (File, Structure, Tools, Render); on the right, the name of the current file (when opened from the gallery it shows "Gallery · name"; for multi-structure files it also shows the current data block, frame, or molecule), "Running…" while a task runs, and the version number.
- <strong>Progress window</strong>: when rendering, exporting, a PXRD simulation, a pore analysis, a structure check and the like take more than half a second, a progress window appears in the middle of the window: what is being done and for how long, with a percentage when the progress can be told (PyMOL's depth-of-field frames, Mitsuba's samples, Zeo++'s calculations, the grid method's atoms). Click "Cancel" to stop the run (with the PyMOL, Mitsuba or Zeo++ it started).
- <strong>Ribbon</strong>: below the menu bar, buttons grouped by purpose. Most buttons are icons; hover over one to see its name and description. Buttons with ▾ open a drop-down menu. When the window is narrow, the ribbon scrolls sideways (you can also use the mouse wheel).
- <strong>Left panel</strong>: the detailed settings of a group of buttons. Click any button of the group, or the title with ⚙ below the group, and the left panel shows that group's settings; the group being shown is highlighted. Click the title again, click ‹ at the top right of the left panel, or click the current menu tab again to collapse the left panel; click › at the left edge of the window to expand it again.
- <strong>3D view</strong>: the middle area, showing the structure in real time. The "Render preview" button is at the top right.
- <strong>PXRD pattern</strong>: after a calculation it appears below the 3D view; drag its top edge to change the height and click × to close it.
- <strong>Messages</strong>: pop up at the bottom right; click to dismiss. Errors are red; hover over one to see the detailed log.

### Left panel pages

| Tab | Pages (ribbon groups) |
| --- | --- |
| File | Recent, Gallery |
| Structure | Model, Styles, Atoms, Bonds (H-bond, Interactions, Polyhedra, and Rings are switched at the top of the left panel), Labels, Add, Range, Contacts, Display (cell box), Background, View |
| Tools | PXRD, Pores |
| Render | Renderer, Export image, Script, Style script |

> <strong>Number fields</strong>: an empty field shows the value actually in use in gray (the model's, the element's, PyMOL's, and so on). Clicking the up/down arrows, scrolling the wheel, or typing starts from that value; if you change nothing, it stays "unset".

## <a id="file"></a>File

The File ribbon contains, from left to right:

| Group | Buttons |
| --- | --- |
| Open | Open file (<kbd>Ctrl</kbd>+<kbd>O</kbd>), Recent, New structure… (<kbd>Ctrl</kbd>+<kbd>N</kbd>) |
| Data block / Frame / Molecule | Appears only when the file contains several structures: choose the one to show, previous, next |
| Project | Save project, Save project as… (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>) |
| Gallery | Save to gallery (<kbd>Ctrl</kbd>+<kbd>S</kbd>), Update this picture, Open gallery (<kbd>Ctrl</kbd>+<kbd>G</kbd>) |
| Location | Open folder, Change location…, Refresh |
| Export | Export ▾: structure files (XYZ / MOL2 / PDB / SDF / CIF / Extended XYZ), 3D models (glTF / OBJ / STL), vector graphics (SVG / PDF); Batch processing… |
| Data | Tables and notes read from the file |
| Options | Preferences |
| Help | Manual (<kbd>F1</kbd>), Getting started, About, Check for updates |

### <a id="file-open"></a>Open and Recent

- <strong>File › Open › Open file</strong> (<kbd>Ctrl</kbd>+<kbd>O</kbd>): the dialog lists structure files and Crystery projects (`.crystery`). For files without an extension, such as POSCAR and CONTCAR, switch the file type to "All files".
- Dragging into the window: only one structure is opened at a time; if you drop several files, the first readable one is opened and a message tells you how many others were skipped. Unsupported formats produce a message.
- <strong>File › Open › Recent</strong>: the left panel lists recently opened files and projects; click one to open it; hover over an entry and click × to remove it from the list; files that no longer exist are shown in gray with a strikethrough. The number of entries kept is set in [Preferences](#file-prefs) (5 to 50, default 20).
- When you open the same file again, its previous display settings (model, range, colors, script, …) are restored automatically. By default the last file is also reopened at startup; you can turn this off in Preferences.

### <a id="file-parts"></a>Multi-structure files (data blocks, frames, molecules)

When a file holds several structures (multiple data blocks in a CIF, multiple frames in an XYZ, multiple molecules in an SDF), an extra group appears after the "Open" group; its title shows which one is current, for example "Data block (2/5)":

- click the ▾ button and choose the one to show from the list;
- use "Previous…" and "Next…" to step through them one by one.

The display settings of each data block, frame, or molecule are remembered separately. At most the first 500 in a file are listed.

### <a id="file-new"></a>New structure

<strong>File › Open › New structure…</strong> (<kbd>Ctrl</kbd>+<kbd>N</kbd>) lets you enter a structure directly. At the top of the dialog, first choose <strong>Crystal</strong> or <strong>Molecule</strong>.

A <strong>crystal</strong> needs:

- <strong>Name</strong>: also used as the file name.
- <strong>Unit cell</strong>: a, b, c (Å, positive) and α, β, γ (°, between 0 and 180).
- <strong>Space group</strong>: a Hermann–Mauguin symbol (such as `P 21/c` or `Fm-3m`) or a number (1 to 230). The program fills in the symmetry operations from the space group.
- <strong>Atoms</strong>: the asymmetric unit, one atom per line: `label element x y z [occupancy] [Uiso]`. x, y, z are fractional coordinates and may be written as fractions (such as `1/2`, `1/3`); occupancy and Uiso (Å²) may be omitted, and occupancy defaults to 1. Lines starting with `#` are ignored. Labels must be unique.

For example, NaCl (space group `Fm-3m` or `225`, a = b = c = 5.64):

`Na1 Na 0 0 0`  
`Cl1 Cl 1/2 1/2 1/2`

A <strong>molecule</strong> needs no cell or space group; enter only a name and atoms: one per line as `element x y z` or `name element x y z`, where x, y, z are Cartesian coordinates (Å). You can paste the contents of an XYZ file directly (the atom count and comment line at the top are skipped). If none of the atoms has a name, it is saved as XYZ; if names are given, it is saved as MOL2 to keep them. For example, water:

`O 0.000 0.000 0.117`  
`H 0.000 0.757 -0.469`  
`H 0.000 -0.757 -0.469`

Click "Save and open…" and choose where to save: crystals are saved as CIF, molecules as XYZ or MOL2, and the file opens automatically after saving. If the input is invalid, the dialog points to the offending line.

<strong>The atoms can be left empty</strong>, which gives a blank structure (a crystal with only a cell and a space group, or a molecule with nothing in it). After opening it, enter atoms in <strong>Structure › Add</strong>, or copy atoms from another structure and paste them in (see [Copying and pasting atoms](#copy-atoms)).

### <a id="file-project"></a>Project files (.crystery)

A project file stores a drawing as <strong>a single file</strong>, convenient for backup or for sending to others: the structure file itself, the display settings, the camera (orientation, center, zoom), the style script, and the pores being shown (results and grid); for multi-structure files it also records which one is shown.

- <strong>Save project</strong>: if the current drawing was opened from a project (or has been saved as one), it is saved back to that project file; otherwise you are asked where to save.
- <strong>Save project as…</strong> (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>): always saves to a new project file.
- <strong>Open a project</strong>: choose a `.crystery` file with "Open file", click it in "Recent", or use "Open with" in Explorer and choose Crystery. The project is restored as it was saved; pores do not need to be recomputed.

Project files and the [gallery](#gallery) store the same content; the difference is that the gallery is a collection with thumbnails, while a project file is a single standalone file.

### <a id="file-export"></a>Export

- <strong>Export structure</strong>:
  - <strong>XYZ, MOL2, PDB, SDF</strong>: export the atoms currently *shown* (which depend on the range, supercell, and growth). For PDB, a CRYST1 record is written when there is a cell (space group recorded as P 1).
  - <strong>CIF</strong>: exports the crystal itself, that is, the cell, symmetry operations, and asymmetric unit, regardless of the range shown; it also writes the space group name and number, the formula, Z, and the cell volume.
  - <strong>Extended XYZ</strong>: exports one unit cell with lattice vectors (`Lattice=`) that other programs can read; independent of the range shown.
  - Molecules (files without a cell) cannot be exported as CIF or Extended XYZ; those two buttons are grayed out.
- <strong>Export graphics › 3D model</strong>: Saves the atoms, bonds, cell box, hydrogen bonds, and polyhedra in the view as a 3D model in the current orientation:
  - <strong>glTF (.glb)</strong>: with colors; opens in PowerPoint, Blender, and web 3D viewers;
  - <strong>OBJ</strong>: saves a `.obj` and a `.mtl` (materials, that is, colors) together; keep the two files in the same folder;
  - <strong>STL</strong>: for 3D printing, without colors, scaled at 1 Å = 10 mm.With more than 4000 atoms, spheres and bonds use fewer faces to keep the file from growing too large.
- <strong>Export graphics › Vector graphics</strong>: <strong>SVG</strong> or <strong>PDF</strong>: spheres and bonds are drawn as editable shapes that stay sharp at any zoom; SVG can be edited in Illustrator or Inkscape, and PDF can be inserted straight into a paper.
- <strong>Data</strong>: Tables and notes read from the file, such as "Structure information", "Cell parameters", "Atom coordinates", and, for CIF, "Bond lengths"; if something needs attention while reading the file, a "Notice" is shown. Click the button to view them in a window; tables can be copied and pasted into Excel.

For exporting images see [Render › Output](#render-export); for exporting patterns see [Tools › PXRD](#pxrd).

### <a id="file-batch"></a>Batch processing

<strong>File › Export › Batch processing…</strong> processes all structure files in a folder one by one:

1. Choose the <strong>input folder</strong> (containing the structure files) and the <strong>output folder</strong> (where results are saved; you can create a new one).
2. Tick what to output:
   - <strong>Exported structure formats</strong>: CIF (default), Extended XYZ, XYZ, PDB, MOL2, SDF. XYZ, PDB, MOL2, and SDF write complete molecules (one unit cell for framework structures); molecules are not written as CIF or Extended XYZ.
   - <strong>3D view</strong>: saves one PNG per structure using the current display settings; if you pick a [style preset](#render-styles) under "Style of the 3D view", every structure is drawn in that style.
   - <strong>Structure check</strong>: writes the number of errors and warnings of each structure into the summary table.
   - <strong>Summary table</strong>: `summary.csv`, one row per structure: file, formula, Z, space group and number, cell parameters and volume, number of independent sites, numbers of errors and warnings, and the reason for any failure. It opens directly in Excel.
   - <strong>Process every structure when a file contains several</strong>: CIF data blocks, XYZ frames, and SDF molecules are processed one by one (at most 50 per file).
3. Click "Start". The window lists the result of each file line by line (✓ success, ✗ failure with the reason); click "Stop" to stop after the current structure has finished.
4. When it finishes, click "Open output folder" to see the results.

Output files never overwrite input files: if the output folder is the same as the input folder and file names collide, `_crystery` is added automatically and the summary table is renamed to `Crystery_batch_summary.csv`. When exporting pictures, each structure is shown in turn; when processing finishes, the drawing you had open is restored.

### <a id="file-prefs"></a>Preferences and Help

<strong>File › Options › Preferences</strong>:

- Open the last file at startup (on by default);
- When closing the window, warn first if the current drawing has unsaved changes (on by default; see below);
- Check GitHub for a new version at startup (off by default);
- Show the keys pressed and where the mouse clicks, with what they do, at the canvas's bottom left (on by default; see [Mouse and shortcuts](#keys));
- Let AI assistants work Crystery over MCP (off by default, this computer only): AI assistants that speak MCP can then connect to `http://127.0.0.1:39217/mcp` and, in the window you are watching, open structures, change the display and the view, write PyMOL commands, change render settings, and render and export pictures, each step shown as it happens (add this address as an HTTP MCP server in the assistant's settings);
- Number of files kept in the Recent list (5 to 50, default 20);
- Default folder for the Save and Open dialogs (leave empty to use the folder of the structure opened last).

"Restore defaults" resets these options to their default values.

<strong>File › Help</strong>:

- <strong>Manual</strong> (<kbd>F1</kbd>): opens this manual in a separate window;
- <strong>Getting started</strong>: a tour shown on first launch that points out each part of the window and what it is for (interface language, menu tabs, opening files, gallery, mouse use in the 3D view, models, left panel, renderers, image size, render preview and export, PXRD and pores, settings and help); move with Back / Next or the arrow keys, end with Esc or Skip, and open it again at any time;
- <strong>About</strong>: the version number, plugin version, and plugin directory, plus links to the GitHub releases page and the author's homepage;
- <strong>Check for updates</strong>: looks up the latest version on GitHub. When there is a new version it shows the version number, release date, and release notes; click "Open GitHub releases page" to download it. When you are up to date, a message appears at the bottom right. You can also go straight to the [releases page](https://github.com/luylin5/Crystery-release/releases/).

### <a id="file-quit"></a>Prompt on closing

When you close the window, if the display settings of the current drawing have been changed (there are changes that can be undone) and differ from what was last saved to the gallery or a project, Crystery asks first. Only rotating and zooming do not count as changes. There are three buttons:

- <strong>The first button saves and then quits</strong>, and depends on where the drawing came from:
  - opened from the gallery: "Update this picture in the gallery";
  - opened from a project, or already saved as a project: "Save project";
  - otherwise: "Save to gallery…".
- <strong>Quit without saving</strong>;
- <strong>Cancel</strong>: go back to Crystery.

If you do not want this prompt, clear "warn first when closing the window…" in Preferences. The display settings of ordinary files are remembered automatically anyway and restored the next time you open the file.

## <a id="model"></a>Structure

- <strong>Model</strong>: Ball and stick (default), Sticks, Space-filling, Wireframe, Thermal ellipsoids. <strong>When atoms are selected, only the selected atoms change</strong> (the group title shows "Model (N)"), for example to draw one ligand as space-filling and leave the rest as ball and stick; with no selection, all atoms change and any per-atom models are removed. With no selection, "Restore defaults" returns to the ball-and-stick model and default sizes and removes per-atom and per-bond settings; with atoms selected, it makes them follow the model of all atoms again. You can also set it from right-click atom › Display mode. The ball size (× radius) and the ellipsoid probability are set by clicking the small ball on the "Atoms" page of the left panel; the radius of all sticks is at the top of the "Bonds" page. When the stick radius is empty, the model's own is used: Sticks 0.18 Å, Ball and stick 0.13 Å, Thermal ellipsoids 0.08 Å, Wireframe 0.06 Å.
- <strong>Atoms</strong>: "Remove H atoms" toggles whether hydrogens are shown; "Show all" restores all hidden molecules, elements, sites, and atoms (colors, sizes, and other settings are unchanged). The left panel holds the atom list, one row per element. Click the small ball to open the style of that row: the model (large ball = Space-filling, small ball = Ball and stick, Thermal ellipsoids; this changes only the balls of that element or site, while its bonds (whether sticks are drawn and how thick) stay as drawn by the model of all atoms, with "Follow the model of all atoms" cleared), Polyhedra (draw coordination polyhedra centered on this element), and the color; below the model are its settings (small ball: the radius of this row's balls and the size of all small balls; large ball: the ball radius; thermal ellipsoids: the ellipsoid probability; polyhedra: hide the center atoms). The radius is the radius of the ball drawn by the current model (for Ball and stick it is the atomic radius times the ball size; for Space-filling it is the atomic radius; for Sticks, Wireframe, and Thermal ellipsoids, which draw no balls, it shows –); it changes along with the model, and clicking it edits this row directly (a faded value is the element's). [3] is the number of atoms each atom is bonded to (in periodic structures a range is written as [1 - 2]); the checkbox on the right shows or hides it; click › to set it per site, and × to remove a per-site setting. Clicking the "Structure" menu tab opens the left panel on this group's page (the page you viewed last, "Atoms" the first time), and the top lets you switch among "Atoms | Bonds | Hydrogen bonds | Weak interactions | Polyhedra | Ring fill"; click "Structure" again to collapse the left panel.
- <strong>Ring fill</strong>: On the "Ring fill" page of the left panel (the "Ring fill" switch at the top of the left panel): tick "Fill aromatic rings" to fill all aromatic rings (PyMOL's cartoon ring faces) and clear it to remove them; with atoms selected, only the rings they belong to are filled (or cleared), and all atoms of a ring must be selected. "Ring mode" chooses how PyMOL draws the rings (ring plane, ring plane plus bonds, spheres, and so on); you can also set how rings are found, and the ring color and transparency.
- <strong>Bonds</strong>: The "Auto bonds" switch; "Restore auto bonds" removes the rules for all element pairs. The left panel sets the bonding tolerance; each element pair gets a two-row card: the first row has the look of the stick (click it to choose the stick radius), the two elements, the number of bonds in the view, "C → [0 - 3] N" (how many N atoms each C atom is bonded to), and whether they bond; the second row has the stick radius and the shortest–longest bonding distance (edit directly; leave empty for automatic), and the histogram button at the far right shows the distance distribution for this element pair in periodic structures, with the bonding range shaded; click in the chart to move the nearer limit there.
- <strong>Hydrogen bonds</strong>: The "Show hydrogen bonds" checkbox at the top of the left panel turns hydrogen bonds on or off. Like bonds, each element gets a two-row card: the first row has the look of the hydrogen bond (click it to choose dashed, round-cap dashed, dotted, or solid and the color), H and this element, the number of hydrogen bonds in the view with it as acceptor, the donors found (such as "N–H···O"), the minimum D–H···A angle, and whether it acts as donor or acceptor; the second row has the hydrogen bond radius, the H···A distance range (edit the longest distance directly), and the distance distribution of H to this element. Distance, angle, radius, color, and style are the same for all hydrogen bonds; the dash length and gap are below the cards.
- <strong>Weak interactions</strong>: The "Show weak interactions" checkbox at the top of the left panel turns weak interactions on or off (it turns on automatically when you add a rule). Choose two elements in the left panel and click "Add rule" (for example C···O, Cl···Cl, C···H); each rule is a two-row card like the one for bonds: the look of the dashed line (click it to choose this rule's color and style: dashed, round-cap dashed, dotted, or solid), the two elements, the number in the view, the sum of van der Waals radii, × (delete), and whether it is in use; the second row has the radius, the shortest and longest distance (edit directly; for a new rule the longest distance defaults to the sum of the van der Waals radii of the two elements), and the distance distribution; a dashed line is drawn between atoms whose distance is within the range. Atoms within three bonds of each other are not counted, and with "Intermolecular only" on (the default) atoms in the same molecule are not counted either. Rules can be set on dummy atoms (for example ring centroids) to draw π interactions. Style and radius are the same for all rules, and the dash length and gap are below the cards; these dashed lines are also included in exported images and 3D models.
- <strong>Coordination polyhedra</strong>: Set on the "Polyhedra" page of the left panel (the "Polyhedra" switch at the top of the left panel): "Show coordination polyhedra" draws a polyhedron around each center atom, with the atoms bonded to it as vertices; choose which elements are centers ("Auto" means all metal atoms, with the bonded non-metal atoms as vertices; once elements are chosen, the vertices are the atoms of other elements bonded to them, so choosing O, for example, draws polyhedra centered on anions); "Hide center atoms" stops drawing the center atoms and their bonds, leaving only the polyhedra. You can also click the small ball of an element on the "Atoms" page and choose "Polyhedra" to center on it. Polyhedra with fewer than 4 vertices are not drawn.
- <strong>Copying and pasting atoms</strong>: Select atoms in the view and press <kbd>Ctrl</kbd>+<kbd>C</kbd> (or right-click atom › Copy, or <strong>Structure › Copy and paste › Copy atoms</strong>); then open another file (or stay in this one) and press <kbd>Ctrl</kbd>+<kbd>V</kbd> (or right-click › Paste atoms). The pasted atoms are placed at their original Cartesian coordinates (Å) as added atoms of this structure: symmetry equivalents are generated, bonds are made automatically, they are saved with the file, they are selected after pasting, and <kbd>Ctrl</kbd>+<kbd>Z</kbd> undoes the paste.
  - Atoms that coincide with existing atoms, or are symmetry equivalents of existing atoms, are not added twice; so if you copy a molecule together with its symmetry equivalents and paste into a crystal of the same space group, only one set is added.
  - When pasting into a molecule, if the original position lies outside the molecule's extent, the pasted atoms are moved as a whole to the middle.
  - The clipboard content is text (one "name element x y z" per line), so it can be pasted into Notepad; conversely, "element x y z" lines copied from other programs, or atom lines (Å) from an XYZ file, can be pasted in directly.
- <strong>Dummy atoms</strong>: Added atoms and dummy atoms are in the same ribbon group ("Add") and on the same page of the left panel: added atoms above, dummy atoms below, sharing the choice between fractional and Cartesian coordinates; the "Clear" menu clears added atoms or dummy atoms separately. Select at least two atoms (for example an aromatic ring; <kbd>Ctrl</kbd> adds to the selection) and click "Create centroid dummy atom" to create Cg1, Cg2, … at the centroid (element recorded as X). With "Create at all symmetry-equivalent positions" ticked, a matching dummy atom appears wherever a symmetry-equivalent group of atoms is shown. Dummy atoms can be used together with atoms for measuring distances and angles; "Clear › Clear dummy atoms" deletes them all, and right-clicking a single dummy atom lets you delete it.

### <a id="model-select"></a>Selection

- In the 3D view, click an atom, bond, cell box, or hydrogen bond to select it; click the same atom again within 0.4 s to select the whole molecule. Hold <kbd>Ctrl</kbd> or <kbd>Shift</kbd> to add to the selection.
- Left-drag draws a box; the atoms inside it are selected (hold <kbd>Ctrl</kbd>/<kbd>Shift</kbd> to add).
- An element button in the ribbon's "Selection" group selects all atoms of that element (<kbd>Ctrl</kbd> adds); "Clear selection", <kbd>Esc</kbd>, or a click on empty space clears the selection.
- When atoms are selected, the left panel opens the "Atoms" page and lists only the selected atoms (one row per element, marked "× count"), with the message "Only changing the N selected atoms" above: clicking the small ball to change the model, radius, or color, or to hide, then affects only the selected atoms and leaves the others unchanged (when you select by element, it affects those elements). When a bond is selected, the "Bonds" page opens and lists only the selected bonds (length and thickness); changing the thickness affects only them (with "Select similar bonds" it affects that element pair). When a hydrogen bond is selected, the "Hydrogen bonds" page opens. Click "Clear selection" in the message or click empty space to return to the previous page and the full list.
- "Selection and measurement" in the left panel offers coloring by property, transparency, labels, and measurement lines; "Apply settings to" chooses all atoms or the selected atoms.

### <a id="model-measure"></a>Labels and measurement

The buttons in this group are all drop-down menus and act on the selected atoms, or on all atoms when nothing is selected:

- <strong>Color by</strong>: <strong>Element</strong>, with colors matching the element table on the left (the color set in the table, or the style script's color if none is set), which can switch other colorings back; <strong>Symmetry equivalent</strong>, where molecules generated by the same symmetry operation share a color, and so do those that differ only by a translation; <strong>Molecule</strong>, one color per molecule; and coloring by displacement parameter B, occupancy (blue → white → red), fractional coordinate x/y/z, or atom order (rainbow).
- <strong>Label</strong>: Atom name, Element, Clear. Labels are drawn in the 3D view and in rendered images.
- <strong>Measure</strong>: after choosing "Distance", "Angle", or "Torsion", <strong>click</strong> 2, 3, or 4 atoms in turn in the view (no need to hold <kbd>Ctrl</kbd>); the next measurement starts automatically. The message bar in the view shows the result and which atom to click next. Press <kbd>Esc</kbd>, click empty space when no atoms are selected, or choose the same item again to end measuring. There are also "Centroid" (puts a point at the centroid of the selected atoms) and "Delete measurements".

Label font size and color, measurement line color and radius, and the number of decimals for distances are set in "Selection and measurement" in the left panel.

### <a id="model-range"></a>Range and growth

- <strong>Display</strong>: Range: unit cell, complete molecules, asymmetric unit; the "Supercell" menu offers 1×1×1, 2×2×2, 3×3×3, and 2×2×1, and other sizes can be entered in the left panel; the "Disorder" menu chooses which disorder components to show: all, major component (disorder groups 0 and ±1), or minor component. The left panel also sets boundary atoms, disorder components, and fragments; clearing a fragment type (such as solvent molecules) hides it. Choosing a range (including clicking the current range again) clears the atoms added by growth and contact growth.
- <strong>Grow</strong>: Each click of "Grow" adds the next layer of atoms bonded to the atoms currently shown (the number of times is shown when you hover over the button); "Undo" reverses the growth. To see the full shape of a molecule cut off by the unit cell, choose "Complete molecules" under "Display".
- <strong>Contacts</strong>: With "Show contacts" on, neighboring atoms that form a hydrogen bond or a short contact (shorter than the sum of the van der Waals radii plus a tolerance) with the atoms shown are drawn as faded balls, joined to the displayed atoms by dashed lines. <strong>Click a faded atom</strong> to add the whole molecule it belongs to; "Grow all one layer" adds all contacts at once; "Undo last" and "Clear" step back. The left panel lets you choose hydrogen bonds, short contacts, and the short-contact tolerance.

Molecules (files without a cell) have no supercell or contact growth.

### <a id="view"></a>Display effects, background and view

- <strong>Display effects</strong>: Cell box and crystal axes (the a, b, c directions are shown at the bottom left of the view and drawn as arrows in rendered images). The axes and the element legend at the top right can be dragged elsewhere with the mouse; a double click puts them back. Exported and rendered images put the axes where you dragged them. The left panel sets the color and radius of the cell box. Coordination polyhedra are in the [Model](#model) group.
- <strong>Background</strong>: White, gray, and black backgrounds, with "Other…" for any color; "Follow style script" removes the background color you set and uses the style script's background instead. Ring fill is on the "Rings" page of the left panel. The "Depth fog" button toggles fog, and "Background and fog" on the left sets the fog density and start: the farther a part is, the more it fades into the background color; the 3D view and both renderers (PyMOL style, Mitsuba style) use the same fog. Lighting and outline are adjusted in [Render › PyMOL](#render-pymol).
- <strong>View</strong>: Look along a, b, c, a\*, b\*, or c\*; "Reset" returns to the initial view; the "Rotate" menu turns one step forward or backward about the screen x, y, or z axis, with the step (5° to 90°) set under "View" in the left panel. The left panel accepts any lattice direction [uvw] or the normal of a lattice plane (hkl).

## <a id="tools"></a>Tools

The "Tools" menu holds PXRD simulation and pore analysis; the ribbon has two groups, PXRD and Pores.

## <a id="pxrd"></a>PXRD

The powder diffraction pattern is calculated from the whole unit cell, regardless of the range shown: IT92 atomic scattering factors, atomic displacement parameters, Lorentz-polarization correction, March–Dollase preferred orientation, and a pseudo-Voigt peak shape.

1. In the settings of <strong>Tools › PXRD</strong>, choose the radiation (Kα1/Kα of Cu, Mo, Co, Fe, Cr, or Ag, or a custom wavelength), set the 2θ range, step, FWHM, and peak shape η, whether to include Kα2, include temperature factors, or exclude H, the preferred-orientation direction and March–Dollase coefficient, and the monochromator angle.
2. Click "Compute PXRD". The pattern appears below the structure (click again to recompute when a pattern is already shown); afterward, changing the settings or opening another structure recomputes it automatically.
3. To compare, use <strong>Tools › PXRD › Overlay…</strong> to load measured data (XRDML, RAS, or two-column data .xy/.xye/.txt/.dat/.csv/.asc); several files can be chosen at once, and "Clear" removes them. A message appears when the wavelength of the measured pattern differs from the calculated one.

### Viewing and exporting the pattern

- Drag in the pattern to select a 2θ range to zoom into, scroll to zoom, and double-click to reset; hovering over a peak shows hkl, d, intensity, and multiplicity.
- Above the pattern you can tick "Peak ticks", "hkl labels", and "Offset measured pattern".
- The × at the top right of the pattern area closes it, and "Compute PXRD" shows it again; "Peak list" shows all peaks (can be copied); "Export XY", "Export peak table" (CSV), and "Save image" (PNG).

Molecules have no unit cell, so PXRD cannot be computed.

## <a id="pores"></a>Pores

Pores are computed for the periodic structure (pores crossing cell boundaries are computed in full) and drawn inside the unit cell shown (including supercells): blue is pores that run through the crystal, and orange is enclosed pockets that the probe cannot enter.

1. Click <strong>Tools › Pores › Show pores</strong>; the upper part of the left panel holds the "Compute" settings. First choose the method:
   - <strong>Zeo++</strong>: gives the pore diameters Di/Df/Dif, the number and dimensionality of the channels, the surface area, the pore volume, and the pore size distribution. You can set the sampling accuracy and high accuracy (-ha); if the Zeo++ program field is empty, it is found automatically (the portable version already includes it).
   - <strong>Grid method</strong>: computes voids and pore volume on a grid and does not need Zeo++.
2. Choose the pore surface (the contact surface, or the solvent-accessible surface reachable by the probe center) and the probe: a common gas (He, H₂O, H₂, CO₂, Ar, N₂, CH₄, Xe) or a custom radius; a grid spacing of 0 means automatic.
3. "Count only the major disorder component" and "Remove fragments hidden in the range panel" are on by default, so that disordered atoms or solvent molecules do not block the pores. Hide the solvent first among the fragments of [Structure › Display](#model-range) and it will not be counted in the calculation.
4. Click "Compute pores" in the left panel (it reads "Recompute pores" once computed).

### Display and results

- <strong>Tools › Pores</strong>: the "Show pores", "Grid lines", and "Enclosed pockets" switches (before anything has been computed, "Show pores" only opens the left panel); "Display" in the lower part of the left panel adjusts the surface position (contact surface inset, or isosurface distance), surface smoothing, the colors of pores and pockets, and opacity. These change only the display and do not trigger a recalculation.
- <strong>Tools › Pores › Pore results</strong>: the left panel lists all values (can be copied) and the pore size distribution plot.
- The pores being shown are drawn into the render preview, exported images, and exported sessions, and are also saved with the gallery and project files.

Molecules have no unit cell, so pores cannot be analyzed.

## <a id="render"></a>Render

On the Render tab's ribbon, the <strong>Size</strong> group holds the image size and blur (depth of field) both renderers use; click a button to adjust it in the left panel. <strong>PyMOL</strong> and <strong>Mitsuba</strong> are one large icon each: click it to choose that renderer (the chosen icon is highlighted), and the left panel shows its own settings, with tabs at the top (for Mitsuba: Material | Outline | Lighting | Scene | Glow | Quality) to switch between them. Numbers are set with a slider or typed; colors with a color picker or typed as #rrggbb, "Default" clearing the color. Both "Render preview" and "Export image" use the selected renderer.

<strong>Blur (depth of field)</strong> (Size group, shared by both renderers): when ticked, set the blur strength, focus (view center or selected atoms), focus shift forward or backward, and the number of frames (8 to 64, PyMOL only). Mitsuba uses a real lens; PyMOL has no depth of field of its own, so it is made by rotating the camera slightly about the focus, taking several frames, and averaging them; the stronger the blur, the more frames are needed, otherwise banding becomes visible.

### <a id="render-styles"></a>Style presets

Save the way you have set up one structure so that you can open another structure and draw it the same way with one click (like the 1:1 and 4:3 image sizes, except that you can save your own). Use <strong>Structure › Styles › Save style…</strong>, give it a name, and choose what the style includes:

- <strong>Model and display</strong>: the model, ball and stick sizes, element colors, coordination polyhedra, hydrogen bond style, cell box and crystal axes, projection, and PyMOL commands for lighting, outline, background, fog, ring fill, coloring by element or by property, labels, and so on.
- <strong>Renderer settings and style script</strong>: the chosen renderer and all of its settings (blur, material, lighting, environment, quality).
- <strong>Image size</strong> (not included by default): width, height, DPI, transparent background.

To apply one: <strong>Structure › Styles › Apply style</strong>, the style list in the left panel, or "Style presets" in the right-click menu. "Default" returns to the plugin's built-in look. A style does not change what belongs to the structure itself: the range, supercell, hidden molecules and elements, per-site and per-atom settings, and the coloring and measurements of selected atoms are all kept. Changes to model and display can be undone with Ctrl+Z. In the left panel each style can be "Update"d (replaced with the current settings), renamed, or deleted. You can also choose a style when [batch processing](#file-batch) exports 3D views.

### <a id="render-pymol"></a>PyMOL (ray tracing)

Consistent with the 3D view, and fast.

- <strong>Lighting and shadows</strong>: ambient, direct, reflect, specular, shininess, number of lights, two-sided lighting, shadows.
- <strong>Outline and antialiasing</strong>: ray trace mode (normal, with black outline, outline only, color blocks with outline), outline thickness and color, antialiasing.

The settings of the first two sections are written as PyMOL commands in the script, and the 3D view changes with them. Fog follows the depth fog in <strong>Structure › Background</strong> and matches the 3D view.

### <a id="render-mitsuba"></a>Mitsuba (path tracing)

Soft shadows, reflections, and glass refraction are all computed physically, which looks more realistic but renders more slowly.

- <strong>Material</strong>: glossy plastic, matte, metal, glass.
- <strong>Outlines</strong>: lines where the depth jumps (the edges of things, where they overlap). Width (scaling with the picture) and color (black by default) can be set; they fade in the fog too.
- <strong>Lighting</strong>: studio, soft, dramatic, or an HDR environment map (.hdr/.exr). Preset lighting can be rotated horizontally and raised or lowered as a whole, with adjustable light size, ambient light, and color temperature; an environment map can only be rotated horizontally and have its color temperature adjusted.
- <strong>Environment</strong>: background, backdrop (catches shadows, on by default), exposure compensation. The background is the background color of the 3D view by default (Structure › Background); it can also be a preset image (light gray gradient, dark spotlight, deep blue gradient, warm vignette, sky) or a custom image (.png/.jpg and others, filling the picture, the excess cropped); with the backdrop, shadows fall on the background image. Fog follows the 3D view and fades into the background; with a transparent background no background is drawn and fog makes distant parts gradually transparent.
- <strong>Glow</strong>: the parts chosen glow, lighting what is around them, with a halo. Glowing atoms (elements, the selected atoms or all; an atom glows by its ball), bonds (Cu for all bonds of Cu, Cu-O for those only), coordination polyhedra (by central element), and hydrogen bonds, weak interactions, unit cell, pores, enclosed pockets, surface (PyMOL's molecular surface) and rings can be chosen; the buttons under the fields pick them. Glow strength (1 is as bright as a white surface), halo size (0 for none) and glow color (empty for each part's own color) can be set. Glow shows best on a dark background.
- <strong>Quality</strong>: Preview 64, Standard 256, Fine 1024 samples; compute device "Auto (try GPU first)" or "CPU only".

> The portable version already includes Mitsuba. When running from source, click <strong>Render › Style › Install Mitsuba renderer</strong> before first use (internet access required, about 50 MB).

### <a id="render-export"></a>Output, picture, and script

- <strong>Output</strong>: "Render preview" renders the current view with the selected renderer and overlays it on the view (the same button is also at the top right of the view); "Export image" produces an image at the width × height (pixels), DPI, and transparent background set in "Image size". Like the camera frame in Blender, the middle of the 3D view shows a render frame with this aspect ratio (the area outside it is dimmed), and the render preview is the image to be exported (same size and settings, scaled down and laid over the frame); when the view and settings have not changed, "Export image" simply saves it. When the height is empty, no render frame is used and the image takes the aspect ratio of the 3D view.
- <strong>Video</strong>: "Render video" renders what is in the render frame frame by frame along the motion set in the left panel, each frame with the selected renderer and all of its settings, and saves an MP4 video (H.264) or a PNG image sequence. The motion can be a turn (about the screen's vertical or horizontal axis, the line of sight, or the crystal axis a, b or c; whole turns of 360° join end to start, so the video loops), rocking back and forth, or travelling from the current view through the views saved in Structure › View; the structure can also zoom in by the end, and the motion can ease in and out. Set the length, the frame rate (24, 30 or 60 fps) and the video width (the height follows the render frame's aspect ratio). The progress card shows which frame is being rendered, and you can cancel at any time; PyMOL usually takes a second or two per frame, while Mitsuba path-traces every frame in full and is slower. A transparent background is used only for PNG image sequences.
- <strong>Picture</strong>: "Copy rendered image" (<kbd>Ctrl</kbd>+<kbd>C</kbd> when no atoms are selected) copies the rendered image at its original size to the clipboard, identical to what "Export image" saves; if there is no render preview of the current view yet, it renders first. "Copy view" copies the 3D view to the clipboard and "Save view" saves it as a PNG; these are screenshots of the view and do not go through the renderer.
- <strong>Session</strong>: "Export session" saves the same scene as a `.pse` file that you can open in PyMOL to keep editing.
- <strong>Script</strong>: The script in the left panel runs after the style script, and most operations in the sidebar are recorded here as PyMOL commands. You can edit it directly and click "Run" (<kbd>Ctrl</kbd>+<kbd>Enter</kbd>); "Undo last" deletes the last command and "Clear" removes everything; type a command in the command line below and press Enter to run it (`sele` is the selected atoms).
- <strong>Style</strong>: "Style script…" specifies your own `.pml`/`.py` style script; when empty, the plugin's built-in default style is used; "Check render environment and style script" reports whether the environment is working; for "Install Mitsuba renderer" see above.

## <a id="keys"></a>Mouse and shortcuts

Mouse actions in the 3D view: <strong>right button rotates, left button selects</strong>.

| Action | Effect |
| --- | --- |
| Left-click | Select an atom, bond, cell box, or hydrogen bond; click empty space to clear the selection |
| Left-click the same atom twice (within 0.4 s) | Select the whole molecule |
| <kbd>Ctrl</kbd>/<kbd>Shift</kbd> + left-click | Add to or remove from the selection |
| Left-drag | Box-select the atoms inside (hold <kbd>Ctrl</kbd>/<kbd>Shift</kbd> to add) |
| Click a faded contact atom | Grow the molecule it belongs to |
| Right-drag | Rotate; if the drag starts at the edge of the view, the whole drag rotates about the axis perpendicular to the screen (turning around the view center, following the pointer) |
| <kbd>Shift</kbd> + right-drag | Drag up and down to zoom, left and right to rotate about the line of sight |
| <kbd>Ctrl</kbd> + right-drag, middle-drag, or dragging with left and right buttons together | Pan |
| Scroll wheel | Zoom |
| Right-click | Open the right-click menu (atoms, bonds, cell box/hydrogen bonds, contact atoms, and empty space each have their own menu); click anywhere outside the menu, press <kbd>Esc</kbd>, or scroll the wheel to close it |

### Right-click menus

- <strong>Atom</strong>: Select (this atom, whole molecule, same element, same site, same kind of molecule, add nearest neighbors), Hide or Show only, Color, Ball size, Label, Set as rotation center, Grow one layer, Atom info. With several atoms selected, it acts on the selected atoms and can create a centroid dummy atom.
- <strong>Bond</strong>: Select this bond or similar bonds, Stick radius, Stop bonding this element pair, Restore auto bonds, Bond length distribution.
- <strong>Cell box, hydrogen bond</strong>: Select, Color, Radius, Style, Hide.
- <strong>Empty space</strong>: Background, Model, Range and supercell, Display, Label, Selection, View, Save to gallery, PXRD, Pores, Render preview, Export image, Export session, Copy view, Save view.
- Grayed-out items would have no effect right now, for example "Show all" when nothing is hidden.

### Keyboard shortcuts

| Key | Effect |
| --- | --- |
| <kbd>Ctrl</kbd>+<kbd>O</kbd> | Open file |
| <kbd>Ctrl</kbd>+<kbd>N</kbd> | New structure |
| <kbd>Ctrl</kbd>+<kbd>S</kbd> | Save to gallery |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd> | Save project as |
| <kbd>Ctrl</kbd>+<kbd>G</kbd> | Open gallery |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | Copy atoms when atoms are selected; otherwise copy the rendered image (original size; renders first if there is no render preview); in a text field or with text selected, copy the text |
| <kbd>Ctrl</kbd>+<kbd>V</kbd> | Paste the copied atoms into the current structure (in a text field, paste text) |
| <kbd>Ctrl</kbd>+<kbd>Z</kbd> | Undo a change to the display settings (in a text field, undo typing) |
| <kbd>Ctrl</kbd>+<kbd>Y</kbd> or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> | Redo |
| <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | In the script box: run the script |
| <kbd>F1</kbd> | Open the manual |
| <kbd>Esc</kbd> | Clear the selection; end measuring while measuring; close an open menu |

<strong>Input hints.</strong> When you press a shortcut or click the mouse, the bottom left of the canvas (the area showing the structure) shows the keys pressed (e.g. <kbd>Ctrl</kbd>+<kbd>C</kbd>) or the mouse button and where it clicked (pixels in the window), with what the action does (e.g. "Copy the 3 selected atoms", "Rotate", "Select atom C1"); it fades after about 2 seconds. Typing in a field is not shown. It can be turned off in the [preferences](#file-prefs).

Undo and redo apply to display settings (model, atoms, bonds, range, script, saved views, …) and not to rotating and zooming; they start over after another structure is opened.

## <a id="gallery"></a>Gallery

The gallery keeps finished pictures: saving stores the structure file together with the display settings, the view and zoom, the style script, the pores being shown, the molecules added by contact growth, and the dummy atoms; opening restores everything exactly as it was, and later moving or editing the original file has no effect on it.

- <strong>Save</strong>: <strong>File › Gallery › Save to gallery</strong> (<kbd>Ctrl</kbd>+<kbd>S</kbd>, or the right-click menu); enter a name and a note.
- <strong>Open</strong>: <strong>File › Gallery › Open gallery</strong> (<kbd>Ctrl</kbd>+<kbd>G</kbd>) opens the large window, or click the group title to see thumbnails in the left panel; click a thumbnail to open it. You can search by name, file, or note.
- <strong>Update</strong>: after opening from the gallery and making further changes, "Update this picture" overwrites the original, while "Save to gallery" saves a new one.
- <strong>Buttons on each picture</strong>: Open, Rename (name and note), Export image (saves the view as it was when saved, as a PNG), Delete (moved to the Recycle Bin, can be restored).
- <strong>Location</strong>: "Open folder" opens it in Explorer; "Change location…" switches to another folder (for example a cloud-synced folder); "Refresh" rereads it.

Each picture is a subfolder of the gallery folder containing `entry.json`, the structure file, the style script, the view and thumbnail as saved, and the pore grid.

## <a id="formats"></a>Supported file formats

### Structures

| Format | Extensions | Read | Write | Notes |
| --- | --- | --- | --- | --- |
| CIF | .cif | ✓ | ✓ | Multiple data blocks can be chosen; if only the space group name is given, the symmetry operations are filled in from the space group. Exports the cell, symmetry operations, and asymmetric unit, plus space group, formula, Z, and cell volume; "New structure" also saves as CIF |
| SHELX | .res .ins | ✓ | — | CELL, LATT, SYMM, SFAC, free variables, PART, riding H |
| MDL MOL / SDF | .mol .sdf | ✓ | ✓ | V2000 and V3000; multiple molecules in an SDF can be chosen |
| Tripos MOL2 | .mol2 | ✓ | ✓ | With CRYSIN, shown with the cell and space group |
| PDB | .pdb .ent | ✓ | ✓ | With CRYST1, shown with the cell; with several models, the first is shown. On export, CRYST1 (P 1) is written when there is a cell |
| XYZ | .xyz | ✓ | ✓ | Multiple frames can be chosen; exports the atoms shown |
| Extended XYZ | .extxyz (and .xyz with Lattice=) | ✓ | ✓ | Lattice= gives the cell; exports one unit cell |
| VASP | POSCAR, CONTCAR, .vasp, .poscar | ✓ | — | Direct and Cartesian coordinates |
| XSF | .xsf | ✓ | — |  |
| Gaussian input | .gjf | ✓ | — | Periodic when there are three Tv; Z-matrices are not supported |
| CSSR | .cssr | ✓ | — |  |
| Crystery project | .crystery | ✓ | ✓ | Everything in a drawing; see [Project files](#file-project) |

Files without a cell are shown as molecules: no cell box is drawn, supercells, PXRD, and pore analysis are unavailable, and CIF and Extended XYZ cannot be exported.

### Other

| Purpose | Format | Read | Write |
| --- | --- | --- | --- |
| Images | PNG (Save view, Export image, PXRD image) | — | ✓ |
| Vector graphics | SVG, PDF | — | ✓ |
| 3D models | glTF (.glb), OBJ (.obj + .mtl), STL (1 Å = 10 mm) | — | ✓ |
| PyMOL session | .pse | — | ✓ |
| Style script | .pml, .py | ✓ | — |
| Environment map (Mitsuba) | .hdr, .exr, etc. | ✓ | — |
| Measured PXRD pattern | XRDML, RAS, two-column data (.xy .xye .txt .dat .csv .asc) | ✓ | — |
| Calculated PXRD pattern | XY, peak table CSV | — | ✓ |
| Batch processing summary table | CSV (summary.csv, opens directly in Excel) | — | ✓ |

## <a id="faq"></a>FAQ

- <strong>The PXRD, Pores, and Supercell buttons are grayed out?</strong> The file you opened is a molecule (it has no unit cell), and these functions need a cell.
- <strong>Atoms have disappeared. How do I get them back?</strong> Click <strong>Structure › Atoms › Show all</strong>, or "Hide › Show all" in the right-click menu. Also check "Remove H atoms", the fragments and disorder components in Range, and "Clipping planes" in View.
- <strong>I box-selected atoms by accident while rotating?</strong> Crystery rotates with the <strong>right button</strong>; the left button is for selecting and box-selecting. Click empty space or press <kbd>Esc</kbd> to clear the selection.
- <strong>Clicking atoms does nothing while measuring / how do I stop measuring?</strong> First choose Distance, Angle, or Torsion in <strong>Structure › Labels › Measure</strong>, then click atoms in turn; the message bar in the view tells you the next step. Press <kbd>Esc</kbd> to end.
- <strong>Mitsuba is very slow, or a message says fewer samples were used than set?</strong> Each render is limited to about 2 minutes; when time runs out, the image is produced from the samples already taken, and the message states the actual number of samples. You can tune the picture with "Preview" quality first and then use Standard or Fine for the final image. If the GPU cannot be used, the message gives the reason (commonly the NVIDIA driver needs updating); CPU rendering is much faster once LLVM is installed.
- <strong>Depth-of-field blur shows banding?</strong> PyMOL's blur is a multi-frame average: increase the number of frames, or reduce the blur strength. When time is short, fewer frames are taken, and the message states the actual number.
- <strong>Pore calculation says Zeo++ cannot be found?</strong> Specify the location of `network.exe` in the pore settings, or switch to the "Grid method", which does not need Zeo++. The portable version already includes Zeo++.
- <strong>Pores are blocked by solvent or disordered atoms?</strong> Keep "Count only the major disorder component" and "Remove fragments hidden in the range panel" on, clear the solvent molecules among the fragments in the left panel of <strong>Structure › Display</strong>, and recompute.
- <strong>The overlaid measured pattern and the calculated peaks do not line up?</strong> Check the radiation wavelength of both: when the measured pattern records a wavelength that differs from the calculation, Crystery shows a message. Change the PXRD settings to the same radiation or a custom wavelength.
- <strong><kbd>Ctrl</kbd>+<kbd>Z</kbd> did not undo a change to the picture?</strong> When the cursor is in a text field, <kbd>Ctrl</kbd>+<kbd>Z</kbd> undoes the typing. Click the 3D view first and then press it, or use the Undo button at the left of the title bar. Rotating and zooming cannot be undone.
- <strong>I want the gallery somewhere else, or synced across several computers?</strong> Use <strong>File › Location › Change location…</strong> to pick a folder (for example a cloud-synced folder). To send one picture to someone, "Save project" to a single `.crystery` file is more convenient.
- <strong>It asks whether to save every time I close?</strong> It asks only when the display settings of the drawing have changed and have not been saved to the gallery or a project; see [Prompt on closing](#file-quit). To turn it off, use <strong>File › Options › Preferences</strong>.
- <strong>Windows shows "Unknown publisher" on first run?</strong> The program is not code-signed. Click "More info → Run anyway".
- <strong>Where does the portable version keep its data?</strong> Settings and output are in `Crystery-data` next to the program, and the default gallery is in `Crystery Gallery`; the whole folder can be moved. If the folder containing the program is not writable (for example Program Files), they go to `%APPDATA%\Crystery` instead.

## <a id="about"></a>About

Crystery is for viewing and rendering crystal and molecular structures. The current version is shown at the right of the main window's title bar (software version · plugin version) and can also be found in <strong>File › Help › About</strong> (which also shows the plugin directory); use "Check for updates" to look for a new version, or download it from the [Crystery releases page](https://github.com/luylin5/Crystery-release/releases/).

Crystery uses the following open-source software; thanks to their authors:

- [PyMOL (open source)](https://github.com/schrodinger/pymol-open-source): the view, PyMOL-style rendering, and sessions;
- [Mitsuba 3](https://www.mitsuba-renderer.org/): Mitsuba-style path-traced rendering;
- [gemmi](https://github.com/project-gemmi/gemmi): space groups and atomic scattering factors;
- [NumPy](https://numpy.org/): numerical computing;
- Zeo++: pore analysis;
- [3Dmol.js](https://3dmol.csb.pitt.edu/): the 3D view;
- [Electron](https://www.electronjs.org/): the desktop application framework.

Author's homepage: [luyulin.com](https://luyulin.com/)
