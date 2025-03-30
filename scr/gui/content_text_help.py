# This file is part of tuxCalc
text='''
tuxCalc help
------------

----------
1. General
----------
All her is just text.

Lines can start with math:
2 + 2 = 4 

You can add comments:
2 + 2 = 4 ; your comment

Define variables using:
a := 3
b := 2 + 4 ; comments still possible
c := b + 2 = 8 

--------------------
2. Calculate options
--------------------
There are two calculate option available - Calculate and Auto Calculate.
Each time you push Calculate icon in toolbar text will be calculated.
By pushing Auto Calculate icon you turn on/off mode that make the text is auto calculated each time you make any change.

------------------
3. Math operations
------------------
All is common and base on Python.
I additional you can rise to power by using ^ to make it looks more common.
+ Addition x
- Subtraction
* Multiplication
/ Division
% Modulus
** Exponentiation
^ Exponentiation alternative
// Floor division

Examples:
3**2 = 9 ; rise to power python style
3^2 = 9 ; rise to power more human style
2 + 2 = 4 
3 - 1 = 2 
3 / 2 = 1.5 

-----------------
4. Math functions
-----------------
Python itself and math module power available.

Some of functions are available directly:
sin, asin, cos, acos, tan, atan, log, log10, sqrt
log(10) = 2.3 

The rest can be used via math object, so:
math.exp(3) = 20.09 

All functions available via math:
ceil(x) Returns the smallest integer greater than or equal to x.
copysign(x, y) Returns x with the sign of y
fabs(x) Returns the absolute value of x
factorial(x) Returns the factorial of x
floor(x) Returns the largest integer less than or equal to x
fmod(x, y) Returns the remainder when x is divided by y
frexp(x) Returns the mantissa and exponent of x as the pair (m, e)
fsum(iterable) Returns an accurate floating point sum of values in the iterable
isfinite(x) Returns True if x is neither an infinity nor a NaN (Not a Number)
isinf(x) Returns True if x is a positive or negative infinity
isnan(x) Returns True if x is a NaN
ldexp(x, i) Returns x * (2**i)
modf(x) Returns the fractional and integer parts of x
trunc(x) Returns the truncated integer value of x
exp(x) Returns e**x
expm1(x) Returns e**x - 1
log(x[, b]) Returns the logarithm of x to the base b (defaults to e)
log1p(x) Returns the natural logarithm of 1+x
log2(x) Returns the base-2 logarithm of x
log10(x) Returns the base-10 logarithm of x
pow(x, y) Returns x raised to the power y
sqrt(x) Returns the square root of x
acos(x) Returns the arc cosine of x
asin(x) Returns the arc sine of x
atan(x) Returns the arc tangent of x
atan2(y, x) Returns atan(y / x)
cos(x) Returns the cosine of x
hypot(x, y) Returns the Euclidean norm, sqrt(x*x + y*y)
sin(x) Returns the sine of x
tan(x) Returns the tangent of x
degrees(x) Converts angle x from radians to degrees
radians(x) Converts angle x from degrees to radians
acosh(x) Returns the inverse hyperbolic cosine of x
asinh(x) Returns the inverse hyperbolic sine of x
atanh(x) Returns the inverse hyperbolic tangent of x
cosh(x) Returns the hyperbolic cosine of x
sinh(x) Returns the hyperbolic cosine of x
tanh(x) Returns the hyperbolic tangent of x
erf(x) Returns the error function at x
erfc(x) Returns the complementary error function at x
gamma(x) Returns the Gamma function at x
lgamma(x) Returns the natural logarithm of the absolute value of the Gamma function at x
pi Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
e mathematical constant e (2.71828...)

Full math module specification: https://docs.python.org/3/library/math.html

--------------
5. Using units
--------------
You can use u prefix:
r := 20*u.cm ; radius
Or brackets:
h := 10*[m] ; height
Then the volume is:
V := pi*r^2 * h = 1256637.06*[cm3] 
To get result in different unit just change into unit you want:
V := pi*r^2 * h = 1256637061.44*[mm3] 
To change u.cm in to [cm] use Format udot option.

Units are provided based on Python Unum package.
See Unum documentation https://unum.readthedocs.io/

Available units: A, AA, ACD, AG, AK, AM, AMOL, ANGSTROM, ARCDEG, ARCMIN, ARCSEC, ARE, AU, B, BAR, BQ, Bq, C, CA, CCD, CD, CELSIUS, CG, CI, CK, CM, CMOL, Ci, D, DA, DAA, DACD, DAG, DAK, DAM, DAMOL, DCD, DECIBEL, DG, DK, DM, DMOL, EA, ECD, EG, EK, EM, EMOL, EV, Ecd, Eg, Em, Emol, Es, F, FA, FCD, FG, FK, FM, FMOL, GA, GCD, GG, GK, GM, GMOL, GPa, GY, Gcd, Gg, Gm, Gmol, Gs, Gy, H, HA, HCD, HENRY, HG, HK, HM, HMOL, HZ, Hz, J, K, KA, KAT, KCD, KG, KK, KM, KMOL, KNOT, L, LM, LX, M, MA, MCD, MG, MILE, MIN, MK, MM, MMOL, MOL, MPa, Mcd, Mg, Mm, Mmol, Ms, N, NA, NCD, NG, NK, NM, NMILE, NMOL, NP, Nm, Np, OHM, PA, PCD, PG, PK, PM, PMOL, Pa, Pcd, Pg, Pm, Pmol, Ps, R, RAD, REM, S, SIEMENS, SR, SV, Sv, T, TA, TCD, TG, TK, TM, TMOL, TON, Tcd, Tg, Tm, Tmol, Ts, U, UA, UCD, UG, UK, UKton, UM, UMOL, USton, V, W, WB, Wb, YA, YCD, YG, YK, YM, YMOL, Ycd, Yg, Ym, Ymol, Ys, ZA, ZCD, ZG, ZK, ZM, ZMOL, Zcd, Zg, Zm, Zmol, Zs, a, aA, aK, acd, ag, am, amol, angstrom, arcmin, arcsec, b, bar, cA, cK, ccd, cd, celsius, cg, cm, cm2, cm3, cm4, cmol, cs, d, dA, dB, dK, daA, daK, dacd, dag, dam, damol, das, dcd, deg, degree, dg, dm, dm3, dmol, ds, eV, fA, fK, fcd, fg, fm, fmol, fs, ft, ft2, ft3, ft4, ft_inch, g, gn, h, hA, hK, ha, hcd, hg, hm, hmol, hs, inch, inch2, inch3, inch4, kA, kK, kN, kNm, kPa, kat, kcd, kcf, kg, kip, kipft, kipinch, klf, km, kmol, knot, ks, ksf, ksi, l, lb, lbf, lbfft, lbfinch, lm, lx, m, m2, m3, m4, mA, mK, mcd, mg, mile, min, mm, mm2, mm3, mm4, mmol, mol, ms, nA, nK, ncd, ng, nm, nmile, nmol, ns, ohm, pA, pK, pcd, pcf, pci, pg, plf, pm, pmol, ps, psf, psi, rad, radian, rem, s, sr, t, u, uA, uK, ua, ucd, ug, um, umol, us, yA, yK, ycd, yd, yd2, yg, ym, ymol, ys, zA, zK, zcd, zg, zm, zmol, zs.

-----------------------------------
6. Greek letters and Unicode signs
-----------------------------------
You can simply paste the needed Unicode characters into your text. For Greek letters however there is a build in feature included. To write Greek letter, write its roman equivalent and when the cursor is after the letter use Ctrl+G shortcut.
Here is the list of available Greek letters and its roman equivalent:
α - a, A - A, β - b, B - B,
χ - c, X - C, δ - d, Δ - D,
ϵ - e, E - E, η - h, H - H,
γ - g, Γ - G, ι - i, I - I,
κ - k, K - K, λ - l, Λ - L,
μ - m, M - M, ν - n, N - N,
ω - w, Ω - W, o - o, O - O,
ϕ - f, Φ - F, φ - j, π - p,
Π - P, ψ - y, Ψ - Y, ρ - r,
P - R, σ - s, Σ - S, τ - t,
T - T, θ - q, Θ - Q, ϑ - J,
υ - u, ϒ - U, ξ - x, Ξ - X,
ζ - z, Z - Z.

Sometime you need name your variable with prime sign. Unicode prime sign ʹ has special shortcut in toolbar. The common quotation sign ' is not possible to be used as it will cause error since this is used for string definition i Python.
So you can have this variable name for example:
αʹ := 40*[degree]

-----------------
7. Spelling check
-----------------
Use spelling icon to activate spelling check, then spelling errors highlight appear and right click menu will be available with spelling correction options and language selection. 

----------------
8. Undo and redo 
----------------
Just use [Ctrl+Z] for undo and [Ctrl+Y] fro redo.

-------------------
9. Background color
-------------------
As you probably noticed background color may change.
White color mean the text is not calculated.
Green color mean the text has been just calculated with no bugs and since that you did not make any changes.
Red color mean the text has been just calculated with bugs and since that you did not make any changes.
To find out which lines cause bugs use Debug option.

----------------
10. Debug option 
----------------
Push Debug icon to turn on/off Debug mode.
If Debug mode is on you will see calculation status on the right side of lines that were recognized as including math and were calculated.
To solve bugs always start fixing the bugs from the top to bottom of your document.

----------------------
11. Clipboard features 
----------------------
Basic clipboard functions Cut [Ctrl+X], Copy [Ctrl+C], Paste [Ctrl+V] available.
There are three additional functions available in toolbar to work with clipboard content.
Paste in from clipboard - if clipboard include text data it clear entire content and paste text from clipboard

---------------------------
12. Float display precision 
---------------------------
You can change float numbers display precision by using Float display precision from toolbar.
'''