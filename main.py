import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for member in updatable:
            member.update(dt)
            for asteroid in asteroids:
                if asteroid.collided(player):
                    print("Game over!")
                    exit()
                for shot in shots:
                    if asteroid.collided(shot):
                        shot.kill()
                        asteroid.split()

        screen.fill("black")

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60FPS
        dt = clock.tick(60) / 1000


if (
    __name__ == "__main__"
):  # This line ensures the function is only called when this file is run directly
    main()
