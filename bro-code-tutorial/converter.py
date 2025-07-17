prefixes=[
    ("quecto", "q", 10**-30),
    ("ronto",  "r", 10**-27),
    ("yocto",  "y", 10**-24),
    ("zepto",  "z", 10**-21),
    ("atto",   "a", 10**-18),
    ("femto",  "f", 10**-15),
    ("pico",   "p", 10**-12),
    ("nano",   "n", 10**-9),
    ("micro",  "µ", 10**-6),   # You can use 'u' if 'µ' causes issues
    ("milli",  "m", 10**-3),
    ("centi",  "c", 10**-2),
    ("deci",   "d", 10**-1),
    ("",       "",  10**0),    # Base unit
    ("deka",   "da", 10**1),
    ("hecto",  "h",  10**2),
    ("kilo",   "k",  10**3),
    ("mega",   "M",  10**6),
    ("giga",   "G",  10**9),
    ("tera",   "T",  10**12),
    ("peta",   "P",  10**15),
    ("exa",    "E",  10**18),
    ("zetta",  "Z",  10**21),
    ("yotta",  "Y",  10**24),
    ("ronna",  "R",  10**27),
    ("quetta", "Q",  10**30)
]

suffixes={
    "Length/Distance": [
        "meter (m)", "centimeter (cm)", "inch (in)", "foot (ft)", "yard (yd)",
        "mile (mi)", "furlong (fur)", "chain (ch)", "rod (rd)", "link (li)",
        "hand (hh)", "barleycorn (bc)", "mil (mil)", "nautical mile (nmi)",
        "angstrom (Å)", "micron (µm)", "light-year (ly)", "parsec (pc)",
        "astronomical unit (AU)", "cubit (no common symbol)", "span (no common symbol)",
        "digit (no common symbol)", "palm (no common symbol)", "pace (no common symbol)",
        "league (lea)", "perch (no common symbol)", "bohr (a0 or au)", "planck length (lP)",
        "electron radius (re)"
    ],
    "Area": [
        "acre (ac)", "square foot (ft²)", "square yard (yd²)", "square mile (mi²)",
        "hectare (ha)", "hide (no common symbol)", "virgate (no common symbol)"
    ],
    "Volume/Capacity": [
        "litre (L or l)", "fluid ounce (fl oz)", "gill (gi)", "cup (cp)", "pint (pt)",
        "quart (qt)", "gallon (gal)", "barrel (bbl)", "peck (pk)", "bushel (bu)",
        "cubic inch (in³)", "cubic foot (ft³)", "cubic yard (yd³)", "cord (cd)",
        "firkin (no common symbol)", "butt (no common symbol)", "hogshead (hhd)",
        "tun (no common symbol)", "kilderkin (no common symbol)"
    ],
    "Mass/Weight": [
        "kilogram (kg)", "gram (g)", "ounce (oz)", "pound (lb)", "stone (st)",
        "hundredweight (cwt)", "ton (t or short ton/long ton)", "grain (gr)",
        "dram (dr)", "slug (slug)", "carat (ct)", "atomic mass unit (u or amu)",
        "dalton (Da)", "talent (no common symbol)", "mina (no common symbol)",
        "shekel (no common symbol)", "drachma (no common symbol)",
        "obol (no common symbol)", "planck mass (mP)"
    ],
    "Time": [
        "second (s)", "minute (min)", "hour (h)", "day (d)", "week (wk)", "year (yr)",
        "decade (no common symbol)", "century (no common symbol)",
        "millennium (no common symbol)", "planck time (tP)"
    ],
    "Electric Current": [
        "ampere (A)", "abampere (abA or Bi)"
    ],
    "Temperature": [
        "kelvin (K)", "fahrenheit (°F)", "planck temperature (TP)"
    ],
    "Amount of Substance": [
        "mole (mol)"
    ],
    "Luminous Intensity": [
        "candela (cd)"
    ],
    "Force": [
        "newton (N)", "dyne (dyn)", "pound-force (lbf)", "kilogram-force (kgf or kp)"
    ],
    "Energy/Work/Heat": [
        "joule (J)", "erg (erg)", "calorie (cal)", "BTU (BTU)", "electronvolt (eV)",
        "kwh (kWh)", "therm (thm)", "hartree (Eh or Ha)", "rydberg (Ry)",
        "joule per tesla (J/T)" # Magnetic moment/energy related
    ],
    "Power": [
        "watt (W)", "horsepower (hp)", "erg per second (erg/s)", "joule per second (J/s)",
        "watt per steradian (W/sr)", "watt per square meter per steradian (W/(m²·sr))",
        "watt per kelvin (W/K)", "watt per meter-kelvin (W/(m·K))",
        "watt per square metre (W/m²)", "watt per cubic metre (W/m³)",
        "lumen per watt (lm/W)", "lux per watt (lx/W)"
    ],
    "Pressure": [
        "pascal (Pa)", "bar (bar)", "atm (atm)", "torr (Torr)", "mmhg (mmHg)", "psi (psi)",
        "newton per square metre (N/m²)"
    ],
    "Frequency": [
        "hertz (Hz)", "becquerel (Bq)"
    ],
    "Electric Charge": [
        "coulomb (C)", "statcoulomb (statC or esu)", "faraday (Fd)", "planck charge (qP)"
    ],
    "Electric Potential (Voltage)": [
        "volt (V)", "statvolt (statV)"
    ],
    "Electric Resistance": [
        "ohm (Ω)", "ohm-meter (Ω·m)"
    ],
    "Electric Conductance": [
        "siemens (S)", "siemens per meter (S/m)"
    ],
    "Capacitance": [
        "farad (F)", "farad per meter (F/m)"
    ],
    "Inductance": [
        "henry (H)", "henry per meter (H/m)"
    ],
    "Magnetic Flux": [
        "weber (Wb)", "maxwell (Mx)", "weber per meter (Wb/m)"
    ],
    "Magnetic Field Strength (B-field)": [
        "tesla (T)", "gauss (G)", "tesla-meter (T·m)", "weber per square meter (Wb/m²)"
    ],
    "Magnetic Field Strength (H-field)": [
        "oersted (Oe)", "ampere per metre (A/m)"
    ],
    "Magnetomotive Force": [
        "gilbert (Gb)"
    ],
    "Luminous Flux": [
        "lumen (lm)", "lumen-second (lm·s)", "lumen per square meter (lm/m²)"
    ],
    "Illuminance": [
        "lux (lx)", "phot (ph)", "lambert (L)", "lux second (lx·s)", "lux per watt (lx/W)"
    ],
    "Radioactivity": [
        "curie (Ci)", "rutherford (Rd)", "becquerel (Bq)", "becquerel per kilogram (Bq/kg)",
        "becquerel per mole (Bq/mol)", "becquerel-second (Bq·s)"
    ],
    "Absorbed Dose (Radiation)": [
        "gray (Gy)", "rad (rad)", "gray per second (Gy/s)", "gray per mole (Gy/mol)",
        "gray-second (Gy·s)"
    ],
    "Equivalent Dose (Radiation)": [
        "sievert (Sv)", "rem (rem)", "sievert per second (Sv/s)",
        "sievert per mole (Sv/mol)", "sievert-second (Sv·s)"
    ],
    "Exposure (Radiation)": [
        "roentgen (R)"
    ],
    "Catalytic Activity": [
        "katal (kat)", "katal per second (kat/s)", "katal per mole (kat/mol)",
        "katal-second (kat·s)"
    ],
    "Plane Angle": [
        "radian (rad)", "degree (°)", "arcminute (')", "arcsecond ('')"
    ],
    "Solid Angle": [
        "steradian (sr)", "steradian per second (sr/s)", "steradian per second squared (sr/s²)"
    ],
    "Velocity/Speed": [
        "knot (kn)", "mach (M)", "metre per second (m/s)"
    ],
    "Acceleration": [
        "metre per second squared (m/s²)", "radian per second squared (rad/s²)",
        "steradian per second squared (sr/s²)"
    ],
    "Density": [
        "kilogram per cubic metre (kg/m³)", "mole per cubic metre (mol/m³)"
    ],
    "Moment of Force (Torque)": [
        "newton-meter (N·m)", "dyne-centimeter (dyn·cm)", "newton-meter per radian (N·m/rad)"
    ],
    "Viscosity (Dynamic)": [
        "poise (P)", "pascal-second (Pa·s)", "newton-second per meter (N·s/m)",
        "kilogram per meter-second (kg/(m·s))"
    ],
    "Viscosity (Kinematic)": [
        "stokes (St)"
    ],
    "Information/Data": [
        "bit (bit)", "byte (B)", "baud (Bd)", "pixel (px)", "dpi (dpi)", "lpi (lpi)"
    ],
    "Printing/Typography": [
        "point (pt)", "pica (pc)"
    ],
    "Luminance": [
        "candela per square meter (cd/m²)", "nit (nit)", "stilb (sb)", "lambert (L)"
    ],
    "Irradiance/Radiant Flux Density": [
        "watt per square metre (W/m²)"
    ],
    "Radiant Intensity": [
        "watt per steradian (W/sr)"
    ],
    "Specific Energy/Enthalpy": [
        "joule per kilogram (J/kg)"
    ],
    "Molar Energy/Enthalpy": [
        "joule per mole (J/mol)"
    ],
    "Heat Capacity/Entropy": [
        "joule per kelvin (J/K)", "joule per kilogram-kelvin (J/(kg·K))"
    ],
    "Thermal Conductivity": [
        "watt per meter-kelvin (W/(m·K))"
    ],
    "Electrical Conductivity": [
        "siemens per meter (S/m)"
    ],
    "Electrical Resistivity": [
        "ohm-meter (Ω·m)"
    ],
    "Electric Field Strength": [
        "volt per metre (V/m)"
    ],
    "Energy Density": [
        "joule per cubic metre (J/m³)"
    ],
    "Surface Charge Density": [
        "coulomb per square metre (C/m²)"
    ],
    "Volume Charge Density": [
        "coulomb per cubic metre (C/m³)"
    ],
    "Radiance": [
        "watt per square meter per steradian (W/(m²·sr))"
    ],
    "Angular Velocity": [
        "radian per second (rad/s)"
    ],
    "Mass Flow Rate": [
        "kilogram per second (kg/s)"
    ],
    "Volume Flow Rate": [
        "cubic meter per second (m³/s)", "sverdrup (Sv)" # Moved from Volume/Capacity to Flow Rate
    ],
    "Thermal Resistance": [
        "unit of thermal resistance (K/W or °C/W)"
    ],
    "Permeability": [
        "darcy (D)"
    ],
    "Luminous Exposure": [
        "lux-second (lx·s)"
    ],
    "Area Density": [
        "kilogram per square meter (kg/m²)"
    ],
    "Linear Density": [
        "kilogram per meter (kg/m)"
    ],
    "Molar Flow Rate": [
        "mole per second (mol/s)", "mole per cubic metre per second (mol/(m³·s))"
    ],
    "Specific Volume": [
        "cubic meter per kilogram (m³/kg)" # Implicit, added for completeness
    ],
    "Molar Volume": [
        "cubic meter per mole (m³/mol)" # Implicit, added for completeness
    ],
    "Momentum": [
        "kilogram meter per second (kg·m/s)", # Implicit, added for completeness
        "newton-second (N·s)" # Impulse, equivalent to momentum
    ],
    "Angular Momentum": [
        "joule-second (J·s)" # Implicit, added for completeness
    ],
    "Spring Constant": [
        "newton per meter (N/m)" # Implicit, added for completeness
    ],
    "Jerk": [
        "meter per second cubed (m/s³)" # Implicit, added for completeness
    ],
    "Radiation Intensity": [
        "jansky (Jy)", "rayleigh (R)" # For astronomical and atmospheric radiation
    ],
    "Magnetic Reluctance": [
        "inverse henry (H⁻¹)" # Implicit, added for completeness
    ],
    "Hydraulic Conductivity": [
        "meter per second (m/s)" # Used in hydrology, distinct from general velocity
    ],
    "Volume Flux Density": [
        "pascal-second per cubic metre (Pa·s/m³)" # This is quite specific, usually related to flow in porous media
    ],
    "Frequency-Length Product": [
        "hertz-meter (Hz·m)"
    ],
    "Fundamental Constants (Planck Units)": [
        "planck length (lP)", "planck mass (mP)", "planck time (tP)",
        "planck temperature (TP)", "planck charge (qP)"
    ]
}

print(suffixes.keys())