
    {
    "material": "A1008",
    "thickness": 0.060,
    "bend_radius": 0.045,
    "bend_deduction": 0.061,
    "k_factor": 0.38,
    "relief_depth": 0.095,
    "min_flange_flat": 0.255,
    "min_flange_formed": 0.286,
    "die_width": 0.472
    }

## Material properties (what the material does)

*These exist even if you bent it by hand with a hammer*


**Thickness**

    thickness = 0.060"

That’s the actual steel you chose - everything else is scaled from this




**K-factor**

    k_factor = 0.38

This is where the neutral axis sits inside the thickness during a bend

    0.0  = inside surface
    0.5  = middle
    1.0  = outside surface

0.38 means the neutral axis lives slightly toward the inside face

That is material behavior: how much it stretches vs compresses




     Tool + machine geometry (what the brake does)

     These are properties of SendCutSend’s bending equipment.



Die width

die_width = 0.472"

That is the V-opening in the bottom die.

This single number largely determines:

- bend radius
- force
- minimum flange
- accuracy






Bend radius

bend_radius = 0.045"

This is basically:

the radius of the punch nose + how the metal springs back in this die

You don’t get to choose this — the machine imposes it.




    Hybrid numbers (physics × machine)

    These are what you actually use in CAD.



Bend allowance

Not listed directly — but computed from:

- thickness
- K-factor
- bend angle
- bend radius

This is the length of metal consumed by the bend arc.







Bend deduction

bend_deduction = 0.061"

This is:

how much shorter the finished part is than the flat layout

It is the accountant’s version of bend allowance.

SendCutSend gives you this so you don’t have to do the math.






Relief depth

relief_depth = 0.095"

This is how far a cut must extend past a bend so the metal can deform without tearing.

It is directly related to:

- thickness
- bend radius
- die width





Minimum flange

min_flange_flat = 0.255"
min_flange_formed = 0.286"

This is:

the shortest tab their brake can grab and bend

This is 100% tool geometry + safety margin.























