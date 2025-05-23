# This file is part of tuxCalc
text='''    _____              _________      ______
    __  /____  _____  ___  ____/_____ ___  /______
    _  __/  / / /_  |/_/  /    _  __ `/_  /_  ___/
    / /_ / /_/ /__>  < / /___  / /_/ /_  / / /__
    \__/ \__,_/ /_/|_| \____/  \__,_/ /_/  \___/

               Welcome in tuxCalc!

Here are simple example calculations that show some of textCalc features.

---------------------------------------------------
Assume simple supported beam with line load applied
l := 6*[m] ; span of the beam
p := 30*[plf] ; line load magnitude
Maximum bending moment at the mid of the span
M := p*l^2/8= 1.97*[kNm]
Assume the section is rectangular
b := 15*u.cm ; section width
h := 40*u.cm ; section height
W := b*h^2/6= 4000.00*[cm3]
Maximum stress in section
σ_max := M / W = 0.49*[MPa]
σ_max = 0.07*[ksi]
--------------------------------------------------

tuxCalc is distributed under the terms of GNU General Public License
The full license can be found in 'license.txt'

Project website: https://github.com/lukaszlaba/tuxCalc

Enjoy!

Copyright (C) 2025, Łukasz Laba
'''