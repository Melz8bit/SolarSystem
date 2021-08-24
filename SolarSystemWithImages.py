import pygame
import math
import sys
import os

from pygame.version import PygameVersion, ver

# Fixes the pygame.init and pygame.quit errors
# pylint: disable=no-member

pygame.init()

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h - 50  # Offset for menu bar
OFFCENTER = 75
CENTER_SCREEN = ((WIDTH / 2) - OFFCENTER, HEIGHT / 2)

SCREEN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT_SIZE = 24
FONT_PADDING = 30
FONT_NAME = "Arial"
FONT = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
IMAGE_PATH = "D:\\Melz\\Programming\\Solar System\\Images\\"
APP_ICON = pygame.image.load(IMAGE_PATH + '\\icon\\sun_icon.ico')

ORBIT_LINE_THICKNESS = 1
ORBIT_SPEED_ADJUSTMENT = 50
SUN_RADIUS = 100
EARTH_RADIUS = 50

BACKGROUND_IMG = pygame.image.load(
    IMAGE_PATH + "\\background\\stars.jpg"
).convert_alpha()

# Image files
SUN_IMG = pygame.image.load(IMAGE_PATH + "\\sun\\" + "sun.png").convert_alpha()
MERCURY_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "mercury.png").convert_alpha()
VENUS_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "venus.png").convert_alpha()
EARTH_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "earth.png").convert_alpha()
MARS_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "mars.png").convert_alpha()
JUPITER_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "jupiter.png").convert_alpha()
SATURN_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "saturn.png").convert_alpha()
URANUS_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "uranus.png").convert_alpha()
NEPTUNE_IMG = pygame.image.load(
    IMAGE_PATH + "\\planets\\" + "neptune.png").convert_alpha()

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
    def __init__(self, img_name, radius, orbital_speed, distance_from_sun):
        self.img_name = img_name
        self.radius = radius
        self.orbital_speed = orbital_speed
        self.distance_from_sun = distance_from_sun

    def draw_planet(self, orbit_angle=0):

        orbit_angle = orbit_angle * \
            (self.orbital_speed / ORBIT_SPEED_ADJUSTMENT)

        position_x = ((WIDTH / 2) + (int(math.cos(orbit_angle)
                      * self.distance_from_sun)) - OFFCENTER)
        position_y = (HEIGHT / 2) + \
            (int(math.sin(orbit_angle) * self.distance_from_sun))

        self.draw_orbit_circle()

        img = pygame.transform.scale(self.img_name, (self.radius, self.radius))
        img_rect = img.get_rect()
        img_rect.center = (position_x, position_y)
        SCREEN.blit(img, img_rect)

    def draw_orbit_circle(self):
        pygame.draw.circle(
            SCREEN,
            WHITE,
            CENTER_SCREEN,
            self.distance_from_sun,
            width=ORBIT_LINE_THICKNESS
        )


class solar_system_object_name:

    obj_count = 1  # Starting at one because the Sun is 0

    def __init__(self, object_name, color):
        solar_system_object_name.obj_count += 1
        self.name = object_name
        self.color = color
        self.vertical_pos = FONT_PADDING * solar_system_object_name.obj_count
        self.horizontal_pos = WIDTH - 200

    def display_name(self):
        planet_diplay_name = FONT.render(self.name, False, self.color)
        SCREEN.blit(planet_diplay_name,
                    (self.horizontal_pos, self.vertical_pos))


def main():
    # Variables
    angle = 0
    running = True

    pygame.display.set_caption("Solar System For Lucas")
    pygame.display.set_icon(APP_ICON)

    # Create planet objects
    solar_system = [
        {
            "object_name": solar_system_object_name("Mercury", GRAY),
            "object_properties": solar_system_object(
                MERCURY_IMG, int(
                    EARTH_RADIUS * 0.38), 48, SUN_RADIUS
            ),
        },
        {
            "object_name": solar_system_object_name("Venus", ORANGE),
            "object_properties": solar_system_object(
                VENUS_IMG, int(
                    EARTH_RADIUS * 0.95), 35, SUN_RADIUS + 50
            ),
        },
        {
            "object_name": solar_system_object_name("Earth", GREEN),
            "object_properties": solar_system_object(
                EARTH_IMG, EARTH_RADIUS, 30, SUN_RADIUS + 110
            ),
        },
        {
            "object_name": solar_system_object_name("Mars", RED),
            "object_properties": solar_system_object(
                MARS_IMG, int(
                    EARTH_RADIUS * 0.53), 24, SUN_RADIUS + 170
            ),
        },
        {
            "object_name": solar_system_object_name("Jupiter", BROWN),
            "object_properties": solar_system_object(
                JUPITER_IMG, int(
                    EARTH_RADIUS * 2), 13, SUN_RADIUS + 250
            ),
        },
        {
            "object_name": solar_system_object_name("Saturn", TAN),
            "object_properties": solar_system_object(
                SATURN_IMG, int(
                    EARTH_RADIUS * 1.5), 10, SUN_RADIUS + 350
            ),
        },
        {
            "object_name": solar_system_object_name("Uranus", LIGHT_BLUE),
            "object_properties": solar_system_object(
                URANUS_IMG, int(
                    EARTH_RADIUS * 1.25), 7, SUN_RADIUS + 430
            ),
        },
        {
            "object_name": solar_system_object_name("Neptune", BLUE),
            "object_properties": solar_system_object(
                NEPTUNE_IMG, int(
                    EARTH_RADIUS * 1.10), 5, SUN_RADIUS + 510
            ),
        }
    ]

    while running:
        CLOCK.tick(60)

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw Background
        SCREEN.blit(BACKGROUND_IMG, (0, 0))

        # Display box for planet names
        # rect values: left, top, width, height
        pygame.draw.rect(SCREEN, BLACK, (WIDTH-220, 20, 150, 300))

        # Draw the Sun
        sun = pygame.transform.scale(SUN_IMG, (SUN_RADIUS, SUN_RADIUS))
        sun_rect = sun.get_rect()
        sun_rect.center = CENTER_SCREEN
        SCREEN.blit(sun, sun_rect)

        # Display Sun name
        SCREEN.blit(FONT.render("Sun", False, YELLOW),
                    (WIDTH - 200, FONT_PADDING))

        # Draw the planets
        for planet in solar_system:
            planet["object_properties"].draw_planet(angle)
            planet["object_name"].display_name()

        angle += 0.05

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
