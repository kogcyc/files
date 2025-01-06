```openscad
module roundChamferedBox(l, w, h, r, fn) {
    minkowski() {
        cube(
            [
                l - 2*r,
                w - 2*r,
                h - 2*r
            ],
            center = true
        );
        sphere(r=r, $fn=fn);
    }
}
roundChamferedBox(40,20,10, 2, 36);
```
