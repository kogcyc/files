#version 3.7;

global_settings { assumed_gamma 1.0 }

// ================= CAMERA =================

camera {
    location <0, 0, -900>
    look_at  <0, 0, 0>
    angle 40
}

light_source { <500, 400, -600> color rgb 1 }
background { color rgb <0.0,0.0,0.0> }


// ================= PARAMETERS =================

#declare Pitch  = 12.7;

#declare Tsmall = 15;    // LEFT
#declare Tlarge = 45;    // RIGHT
#declare C      = 350.352;

#declare Links  = 86;
#declare BallR  = 2;

#declare Step = Pitch / 10;

// ================= PITCH RADII =================

#declare Rs = Pitch / (2*sin(pi/Tsmall));
#declare Rl = Pitch / (2*sin(pi/Tlarge));


// ================= OBLIQUITY =================

#declare alfa = asin((Rl - Rs) / C);


// ================= CENTERS =================

#declare Csx = -C/2;
#declare Clx =  C/2;


// ================= TANGENT POINTS =================
// SMALL sprocket OUTSIDE (left side)

#declare sxt = Csx - Rs*sin(alfa);
#declare syt = Rs*cos(alfa);

#declare sxb = sxt;
#declare syb = -syt;

// LARGE sprocket near side

#declare lxt = Clx - Rl*sin(alfa);
#declare lyt = Rl*cos(alfa);

#declare lxb = lxt;
#declare lyb = -lyt;





// ================= STRAIGHT LENGTH =================

#declare Ls = sqrt((lxt - sxt)*(lxt - sxt) + (lyt - syt)*(lyt - syt));


// ================= WRAP ANGLES =================

// Small OUTSIDE → long wrap
#declare theta_s = pi + 2*alfa;

// Large NEAR → short wrap
#declare theta_l = pi + 2*alfa;

#declare As = Rs * theta_s;
#declare Al = Rl * theta_l;

#declare L = 2*Ls + As + Al;

// ================= REFERENCE CIRCLES =================

torus { Rs,1 rotate <90,0,0> translate <Csx,0,0>
        pigment { rgb <1,0.4,0.4> } }

torus { Rl,1 rotate <90,0,0> translate <Clx,0,0>
        pigment { rgb <0.4,1,0.4> } }


// ================= PATH =================

#macro Roller(s)

#local s = mod(s, L);


// ---- 1) TOP STRAIGHT (small → large)

#if (s < Ls)

    #local pt = s / Ls;
    #local px = sxt*(1 - pt) + lxt*pt;
    #local py = syt*(1 - pt) + lyt*pt;


// ---- 2) LARGE ARC (top → bottom)

#else
#local s = s - Ls;

#if (s < Al)

    #local ang = (pi/2 + alfa) - s/Rl;

    #local px = Clx + Rl*cos(ang);
    #local py = Rl*sin(ang);


// ---- 3) BOTTOM STRAIGHT (large → small)

#else
#local s = s - Al;

#if (s < Ls)

    #local pt = s / Ls;
    #local px = lxb*(1 - pt) + sxb*pt;
    #local py = lyb*(1 - pt) + syb*pt;


// ---- 4) SMALL ARC (bottom → top, OUTSIDE = LEFT HALF)

#else
#local s = s - Ls;

// Start at bottom outside tangent (3/2π − α)
#local ang = (3*pi/2 - alfa) - s/Rs;

#local px = Csx + Rs*cos(ang);
#local py = Rs*sin(ang);

#end
#end
#end


sphere {
    <px, py, 0>, BallR+1
    pigment { rgb <0.95,0.95,1> }
    finish  { phong 0.6 }
}

#end


// ================= DRAW =================

#for (i, 0, Links - 1)
    Roller(i * Pitch + clock * Step)
#end