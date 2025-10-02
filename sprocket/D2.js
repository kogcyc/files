export class D2 {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  translate(dx, dy) {
    return new D2(this.x + dx, this.y + dy);
  }

  polar(angleDeg, dist) {
    const rad = angleDeg * Math.PI / 180;
    return this.translate(dist * Math.cos(rad), dist * Math.sin(rad));
  }

  rotate(origin, angleDeg) {
    const rad = angleDeg * Math.PI / 180;
    const dx = this.x - origin.x;
    const dy = this.y - origin.y;
    return new D2(
      origin.x + dx * Math.cos(rad) - dy * Math.sin(rad),
      origin.y + dx * Math.sin(rad) + dy * Math.cos(rad)
    );
  }

  mirrorX() {
    return new D2(-this.x, this.y);
  }

  mirrorY() {
    return new D2(this.x, -this.y);
  }

  distanceTo(other) {
    return Math.hypot(this.x - other.x, this.y - other.y);
  }

  midpoint(other) {
    return new D2(
      (this.x + other.x) / 2,
      (this.y + other.y) / 2
    );
  }

  angleTo(other) {
    const dx = other.x - this.x;
    const dy = other.y - this.y;
    return Math.atan2(dy, dx) * 180 / Math.PI;  // returns angle in degrees
  }

  toString() {
    return `(${this.x.toFixed(2)}, ${this.y.toFixed(2)})`;
  }
}
