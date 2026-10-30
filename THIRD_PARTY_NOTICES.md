# Third-party notices

Crystery is distributed under its own license (see [LICENSE](LICENSE)). It bundles the open-source components below,
each under its own license; nothing in Crystery's license limits the rights these licenses give you. The full license
texts are also included in the installed program (the folders named in the table).

| Component | Used for | License | License file in the program |
|---|---|---|---|
| [PyMOL (open-source)](https://github.com/schrodinger/pymol-open-source) 3.2 | 3D view and PyMOL rendering | Open-Source PyMOL license (BSD-style) | `resources/python-runtime/Lib/site-packages/pymol_open_source_whl-3.2.0.2.dist-info/licenses/` |
| [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) 3.9 | Mitsuba rendering | BSD 3-Clause | `…/mitsuba-3.9.1.dist-info/licenses/LICENSE` |
| [Dr.Jit](https://github.com/mitsuba-renderer/drjit) 1.5 | Mitsuba's compute backend | BSD 3-Clause | `…/drjit-1.5.0.dist-info/licenses/LICENSE` |
| [gemmi](https://github.com/project-gemmi/gemmi) 0.7 | Atomic scattering factors for PXRD | MPL 2.0 (source: https://github.com/project-gemmi/gemmi) | `…/gemmi-0.7.5.dist-info/` |
| [NumPy](https://numpy.org) 2.5 | Numerics | BSD 3-Clause and others | `…/numpy-2.5.4.dist-info/LICENSE.txt` |
| [Python](https://www.python.org) 3.14 | Runtime of the computations | PSF License | `resources/python-runtime/LICENSE.txt` |
| [Zeo++](https://www.zeoplusplus.org) 0.3 | Pore analysis | BSD-style (below) | `resources/tools/zeopp/bin/LICENSE-zeo++.txt` |
| [Voro++](https://math.lbl.gov/voro++/) (in Zeo++) | Pore analysis | BSD-style (below) | `resources/tools/zeopp/bin/LICENSE-voro++.txt` |
| [Eigen](https://eigen.tuxfamily.org) 3.2.7 (in Zeo++) | Pore analysis | MPL 2.0 (source: https://www.zeoplusplus.org/zeo++-0.3.tar.gz) | `resources/tools/zeopp/bin/LICENSE-eigen.txt` |
| [3Dmol.js](https://3dmol.csb.pitt.edu) | Parts of the 3D viewer | BSD 3-Clause (https://github.com/3dmol/3Dmol.js/blob/master/LICENSE) | — |
| [Electron](https://www.electronjs.org) / Chromium | Application window | MIT / Chromium licenses | `LICENSE.electron.txt`, `LICENSES.chromium.html` |

If you use Crystery's pore analysis in published work, please also cite Zeo++:
T. F. Willems, C. H. Rycroft, M. Kazi, J. C. Meza, M. Haranczyk, *Microporous Mesoporous Mater.* **2012**, 149, 134–141.

The notices below are reproduced as their licenses require for binary redistribution.

## Zeo++

```
Zeo++ Copyright (c) 2011, The Regents of the University
of California, through Lawrence Berkeley National Laboratory (subject
to receipt of any required approvals from the U.S. Dept. of Energy).
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

(1) Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

(2) Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

(3) Neither the name of the University of California, Lawrence
Berkeley National Laboratory, U.S. Dept. of Energy nor the names of
its contributors may be used to endorse or promote products derived
from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

You are under no obligation whatsoever to provide any bug fixes,
patches, or upgrades to the features, functionality or performance of
the source code ("Enhancements") to anyone; however, if you choose to
make your Enhancements available either publicly, or directly to
Lawrence Berkeley National Laboratory, without imposing a separate
written license agreement for such Enhancements, then you hereby grant
the following license: a  non-exclusive, royalty-free perpetual
license to install, use, modify, prepare derivative works, incorporate
into other computer software, distribute, and sublicense such
enhancements or derivative works thereof, in binary and source code
form.
```

## Voro++

```
Voro++ Copyright (c) 2008, The Regents of the University of California, through
Lawrence Berkeley National Laboratory (subject to receipt of any required
approvals from the U.S. Dept. of Energy). All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

(1) Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. 

(2) Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution. 

(3) Neither the name of the University of California, Lawrence Berkeley
National Laboratory, U.S. Dept. of Energy nor the names of its contributors may
be used to endorse or promote products derived from this software without
specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

You are under no obligation whatsoever to provide any bug fixes, patches, or
upgrades to the features, functionality or performance of the source code
("Enhancements") to anyone; however, if you choose to make your Enhancements
available either publicly, or directly to Lawrence Berkeley National
Laboratory, without imposing a separate written license agreement for such
Enhancements, then you hereby grant the following license: a  non-exclusive,
royalty-free perpetual license to install, use, modify, prepare derivative
works, incorporate into other computer software, distribute, and sublicense
such enhancements or derivative works thereof, in binary and source code form.
```

## Eigen

```
network.exe contains code from Eigen 3.2.7 (http://eigen.tuxfamily.org),
which is bundled with Zeo++ 0.3 (directory Eigen/ of
https://www.zeoplusplus.org/zeo++-0.3.tar.gz).

Eigen is subject to the terms of the Mozilla Public License, v. 2.0. If a copy
of the MPL was not distributed with this file, you can obtain one at
https://mozilla.org/MPL/2.0/. The Eigen source code is available from the
URLs above.
```
