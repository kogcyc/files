```openscad
module roundChamferedBox(size=[l,w,h], r, fn) {
  minkowski() {
    cube([l - 2*r,w - 2*r,h - 2*r],center = true);
    sphere(r=r, $fn=fn);
  }
}
roundChamferedBox([80,40,20], 2, 36);
```
