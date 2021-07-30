import pygame, math, sys

# Fixes the pygame.init and pygame.quit errors
# pylint: disable=no-member

pygame.init()
pygame.display.init()

WIDTH = 800
HEIGHT = 600
CENTER_SCREEN = ((WIDTH / 2) - 75, HEIGHT / 2)

SCREEN = pygame.display.set_mode(size = (WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Colors
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (105, 105, 105)
ORANGE = (255, 69, 0)
RED = (255, 0, 0)
BROWN = (160, 82, 45)
TAN = (245, 222, 179)
LIGHT_BLUE = (30, 144, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (211, 211, 211)

class solar_system_object:
    def __init__(self, radius, orbital_speed, distance_from_sun, color, has_rings, is_vertical=False):
        self.radius = radius
        self.orbital_speed = orbital_speed
        self.distance_from_sun = distance_from_sun
        self.color = color
        self.has_rings = has_rings
        self.is_vertical = is_vertical
    
    def draw_object(self, orbit_angle=0):
        position_x = (WIDTH / 2) + (int(math.cos(orbit_angle) * self.distance_from_sun))
        position_y = (HEIGHT / 2) + (int(math.sin(orbit_angle) * self.distance_from_sun))

        pygame.draw.circle(SCREEN, self.color, (position_x, position_y), self.radius)

        if self.has_rings:
            if not self.is_vertical:
                pygame.draw.line(SCREEN, self.color, (position_x - 15, position_y), (position_x + 15, position_y))
            else:
                pygame.draw.line(SCREEN, self.color, (position_x, position_y - 15), (position_x, position_y + 15))


# Variables
angle = 0
orbit_line_thickness = 1
orbital_speed_adjustment = 50
sun_radius = 20
running = True

# Create planet objects
mercury = solar_system_object(4, 48, sun_radius + 20, GRAY, False)
venus = solar_system_object(5, 35, sun_radius + 40, ORANGE, False)
earth = solar_system_object(6, 30, sun_radius + 60, GREEN, False)
mars = solar_system_object(4, 24, sun_radius + 80, RED, False)
jupiter = solar_system_object(10, 13, sun_radius + 110, BROWN, False)
saturn = solar_system_object(8, 10, sun_radius + 145, TAN, True)
uranus = solar_system_object(7, 7, sun_radius + 180, LIGHT_BLUE, True, True)
neptune = solar_system_object(7, 5, sun_radius + 205, BLUE, False)

while running:    
    msElapsed = CLOCK.tick(60)

    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(BLACK)
    
    # Draw the Sun
    pygame.draw.circle(SCREEN, YELLOW, CENTER_SCREEN, sun_radius)

    # Draw the orbit lines
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, mercury.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, venus.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, earth.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, mars.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, jupiter.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, saturn.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, uranus.distance_from_sun, width=orbit_line_thickness)
    pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN, neptune.distance_from_sun, width=orbit_line_thickness)

    # Draw the planets in motion
    mercury.draw_object(angle * (mercury.orbital_speed / orbital_speed_adjustment))
    venus.draw_object(angle * (venus.orbital_speed / orbital_speed_adjustment))
    earth.draw_object(angle * (earth.orbital_speed / orbital_speed_adjustment))
    mars.draw_object(angle * (mars.orbital_speed / orbital_speed_adjustment))
    jupiter.draw_object(angle * (jupiter.orbital_speed / orbital_speed_adjustment))
    saturn.draw_object(angle * (saturn.orbital_speed / orbital_speed_adjustment))
    uranus.draw_object(angle * (uranus.orbital_speed / orbital_speed_adjustment))
    neptune.draw_object(angle * (neptune.orbital_speed / orbital_speed_adjustment))

    angle += 0.05

    pygame.display.flip()


pygame.quit()
