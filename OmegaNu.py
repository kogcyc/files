import pygame, math, sys, random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ωmega Nu – Bouncing Ship Edition")
clock = pygame.time.Clock()

CYAN   = (0, 255, 255)
BLUE   = (100, 150, 255)
RED    = (255, 100, 100)
YELLOW = (255, 255, 0)

ROTATE_STEP = 12       # degrees per wheel tick
BOUNCE_DAMP = 0.9      # how much velocity is retained after bounce

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.angle = 0.0
        self.vx = self.vy = 0.0
        self.thrust_power = 0.4
        self.drag = 0.999
        self.flash_timer = 0
        self.rect = pygame.Rect(0, 0, 60, 60)
        self.rect.center = (400, 300)

    def rotate(self, direction):
        self.angle = (self.angle + direction * ROTATE_STEP) % 360

    def thrust(self):
        rad = math.radians(self.angle)
        self.vx += math.cos(rad) * self.thrust_power
        self.vy += math.sin(rad) * self.thrust_power
        self.flash_timer = 5

    def update(self, thrusting):
        if thrusting:
            self.thrust()

        # Apply drag
        self.vx *= self.drag
        self.vy *= self.drag

        # Move
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce off walls
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = -self.vx * BOUNCE_DAMP
        elif self.rect.right > 800:
            self.rect.right = 800
            self.vx = -self.vx * BOUNCE_DAMP

        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = -self.vy * BOUNCE_DAMP
        elif self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vy = -self.vy * BOUNCE_DAMP

    def draw(self, surface):
        surf = pygame.Surface((80, 80), pygame.SRCALPHA)
        cx, cy = 40, 40

        # "V" hull
        pygame.draw.lines(
            surf, CYAN, False,
            [(cx-20, cy+20), (cx, cy-20), (cx+20, cy+20)], 2
        )

        # Yellow flame
        if self.flash_timer > 0:
            self.flash_timer -= 1
            pygame.draw.polygon(
                surf, YELLOW,
                [(cx, cy+22), (cx-6, cy+42), (cx+6, cy+42)]
            )

        visual_angle = -(self.angle - 90 + 180)
        rotated = pygame.transform.rotate(surf, visual_angle)
        rect = rotated.get_rect(center=self.rect.center)
        surface.blit(rotated, rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, vel):
        super().__init__()
        self.image = pygame.Surface((4,4))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=pos)
        rad = math.radians(angle)
        self.vx = math.cos(rad)*10 + vel[0]
        self.vy = math.sin(rad)*10 + vel[1]

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (10,10), 8, 2)
        self.rect = self.image.get_rect(center=(random.randint(50,750),
                                                random.randint(50,550)))
        self.vx = random.uniform(-1,1)
        self.vy = random.uniform(-1,1)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > 800:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.vy *= -1

# --- setup ---
ship = Ship()
target = Target()
bullets = pygame.sprite.Group()
targets = pygame.sprite.Group(target)

# --- game loop ---
while True:
    thrusting = pygame.mouse.get_pressed()[2]  # right button held?

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                ship.rotate(+1)
            elif e.button == 5:
                ship.rotate(-1)
            elif e.button == 1:
                b = Bullet(ship.rect.center, ship.angle, (ship.vx, ship.vy))
                bullets.add(b)

    ship.update(thrusting)
    bullets.update()
    targets.update()

    hits = pygame.sprite.groupcollide(targets, bullets, True, True)
    for _ in hits:
        targets.add(Target())

    screen.fill((0,0,0))
    ship.draw(screen)
    bullets.draw(screen)
    targets.draw(screen)
    pygame.display.flip()
    clock.tick(60)
