import pygame
import math
import sys
import os

from pygame.version import PygameVersion, ver

# Fixes the pygame.init and pygame.quit errors
# pylint: disable=no-member

pygame.init()
pygame.display.set_caption('Solar System For Lucas')

WIDTH = 1280
HEIGHT = 1024
OFFCENTER = 75
CENTER_SCREEN = ((WIDTH / 2) - OFFCENTER, HEIGHT / 2)

SCREEN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT_SIZE = 24
FONT_PADDING = 30
FONT_NAME = 'Arial'
FONT = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
IMAGE_PATH = os.getcwd() + '/Images'

ORBIT_LINE_THICKNESS = 1
ORBIT_SPEED_ADJUSTMENT = 50
SUN_RADIUS = 50

BACKGROUND_IMG = pygame.image.load(
    IMAGE_PATH + '/background/stars.jpg').convert_alpha()
SUN_IMG = pygame.image.load(IMAGE_PATH + '/sun/sun.png').convert_alpha()

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
    def __init__(self, name, radius, orbital_speed, distance_from_sun, color, has_rings, is_vertical=False):
        self.name = name
        self.radius = radius
        self.orbital_speed = orbital_speed
        self.distance_from_sun = distance_from_sun
        self.color = color
        self.has_rings = has_rings
        self.is_vertical = is_vertical

    def draw_planet(self, orbit_angle=0):

        orbit_angle = orbit_angle * \
            (self.orbital_speed / ORBIT_SPEED_ADJUSTMENT)

        position_x = (WIDTH / 2) + (int(math.cos(orbit_angle)
                                        * self.distance_from_sun)) - OFFCENTER
        position_y = (HEIGHT / 2) + \
            (int(math.sin(orbit_angle) * self.distance_from_sun))

        self.draw_orbit_circle()

        pygame.draw.circle(SCREEN, self.color,
                           (position_x, position_y), self.radius)

        if self.has_rings:
            if not self.is_vertical:
                pygame.draw.line(
                    SCREEN, self.color, (position_x - 15, position_y), (position_x + 15, position_y))
            else:
                pygame.draw.line(SCREEN, self.color, (position_x,
                                 position_y - 15), (position_x, position_y + 15))

    def draw_orbit_circle(self):
        pygame.draw.circle(SCREEN, WHITE, CENTER_SCREEN,
                           self.distance_from_sun, width=ORBIT_LINE_THICKNESS)


class solar_system_object_name:

    obj_count = 1  # Starting at one because the Sun is 0

    def __init__(self, object_name, color):
        solar_system_object_name.obj_count += 1
        self.name = object_name
        self.color = color
        self.vertical_pos = FONT_PADDING * solar_system_object_name.obj_count
        self.horizontal_pos = WIDTH - 100

    def display_name(self):
        planet_diplay_name = FONT.render(self.name, False, self.color)
        SCREEN.blit(planet_diplay_name,
                    (self.horizontal_pos, self.vertical_pos))


def main():
    # Variables
    angle = 0
    running = True

    # Create planet objects
    solar_system = [
        {'object_name': solar_system_object_name('Mercury', GRAY), 'object_properties': solar_system_object(
            'Mercury', 4, 48, SUN_RADIUS + 18, GRAY, False)},
        {'object_name': solar_system_object_name('Venus', ORANGE), 'object_properties': solar_system_object(
            'Venus', 5, 35, SUN_RADIUS + 34, ORANGE, False)},
        {'object_name': solar_system_object_name('Earth', GREEN), 'object_properties': solar_system_object(
            'Earth', 6, 30, SUN_RADIUS + 46, GREEN, False)},
        {'object_name': solar_system_object_name('Mars', RED), 'object_properties': solar_system_object(
            'Mars', 4, 24, SUN_RADIUS + 72, RED, False)},
        {'object_name': solar_system_object_name('Jupiter', BROWN), 'object_properties': solar_system_object(
            'Jupiter', 10, 13, SUN_RADIUS + 100, BROWN, False)},
        {'object_name': solar_system_object_name('Saturn', TAN), 'object_properties': solar_system_object(
            'Saturn', 8, 10, SUN_RADIUS + 150, TAN, True)},
        {'object_name': solar_system_object_name('Uranus', LIGHT_BLUE), 'object_properties': solar_system_object(
            'Uranus', 7, 7, SUN_RADIUS + 200, LIGHT_BLUE, True, True)},
        {'object_name': solar_system_object_name('Neptune', BLUE), 'object_properties': solar_system_object(
            'Neptune', 7, 5, SUN_RADIUS + 250, BLUE, False)}
    ]

    while running:
        CLOCK.tick(60)

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw Background
        SCREEN.blit(BACKGROUND_IMG, (0, 0))

        # Draw the Sun
        sun = pygame.transform.scale(SUN_IMG, (SUN_RADIUS, SUN_RADIUS))
        sun_rect = sun.get_rect()
        sun_rect.center = CENTER_SCREEN
        SCREEN.blit(sun, sun_rect)

        # Display Sun name
        SCREEN.blit(FONT.render('Sun', False, YELLOW),
                    (WIDTH - 100, FONT_PADDING))

        # Draw the planets
        for planet in solar_system:
            planet['object_properties'].draw_planet(angle)
            planet['object_name'].display_name()

        angle += 0.05

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
