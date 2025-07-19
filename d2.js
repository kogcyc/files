// d2.js

export function degreesToRadians(deg) {
  return (deg * Math.PI) / 180;
}

export function radiansToDegrees(rad) {
  return (rad * 180) / Math.PI;
}

export function quadrant(p, q) {
  let x = (q === 2 || q === 3) ? -p.x : p.x;
  let y = (q === 3 || q === 4) ? -p.y : p.y;
  return new D2(x, y);
}

export class D2 {
  constructor(x = 0.0, y = 0.0) {
    this.x = parseFloat(x);
    this.y = parseFloat(y);
  }

  toString() {
    return `D2(x=${this.x.toFixed(2)}, y=${this.y.toFixed(2)})`;
  }

  round2() {
    return new D2(parseFloat(this.x.toFixed(2)), parseFloat(this.y.toFixed(2)));
  }

  mirrorX() {
    return new D2(this.x, -this.y).round2();
  }

  mirrorY() {
    return new D2(-this.x, this.y).round2();
  }

  translate(dx, dy) {
    return new D2(this.x + dx, this.y + dy).round2();
  }

  rotate(center, angleDeg) {
    const angleRad = degreesToRadians(angleDeg);
    const dx = this.x - center.x;
    const dy = this.y - center.y;
    const x = center.x + Math.cos(angleRad) * dx - Math.sin(angleRad) * dy;
    const y = center.y + Math.sin(angleRad) * dx + Math.cos(angleRad) * dy;
    return new D2(x, y).round2();
  }

  vector(distance, angleDeg) {
    const dx = Math.cos(degreesToRadians(angleDeg)) * distance;
    const dy = Math.sin(degreesToRadians(angleDeg)) * distance;
    return new D2(this.x + dx, this.y + dy).round2();
  }

  angleAndLengthTo(other) {
    const dx = other.x - this.x;
    const dy = other.y - this.y;
    const angleDeg = radiansToDegrees(Math.atan2(dy, dx));
    const length = Math.hypot(dx, dy);
    return [angleDeg, length];
  }
}
