camera {
  location < 20, 20, -20 >
    look_at < 0, 0, 0 >
}

light_source {
  <
  480, 480, -40 >
    color rgb < 1, 1, 1 > * 1.4
}

sphere {
  <
  0, 0, 0 > 2
  pigment {
    color rgb < 0.7654, 0.7654, 0.7654 >
  }
}

sphere {
  <
  10, 0, 0 > 2
  pigment {
    color rgb < 1, 0, 0 >
  }
}

sphere {
  <
  0, 10, 0 > 2
  pigment {
    color rgb < 0, 1, 0 >
  }
}

sphere {
  <
  0, 0, 10 > 2
  pigment {
    color rgb < 0, 0.543, 1 >
  }
}

plane {
  < 0, 1, 0 > , -20
  pigment {
    checker color rgb < 0.5, 0.5, 0.5 > , color rgb < 0.4, 0.4, 0.4 >
  }
  scale < 4, 1, 4 >
}
