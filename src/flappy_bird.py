"""
Flappy Bird Game

This module implements the Flappy Bird game using Pygame.
It includes the Bird, Pipe, and Base classes, as well as the main game loop.

Classes:
    Bird: Represents the bird in the game, handling its movement, rotation, and rendering.
Constants:
    SCREEN_WIDTH (int): Width of the game screen.
    SCREEN_HEIGHT (int): Height of the game screen.
    PIPE_IMAGE: Image used to represent pipes in the game.
    GROUND_IMAGE: Image used to represent the ground in the game.
    BACKGROUND_IMAGE: Image used to represent the background in the game.
    BIRD_IMAGES: List of images representing the bird's animation states.
    SCORE_FONT: Font used to display the score on the screen.
"""

import os
import random
import logging
import pygame

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
GROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)

class Bird:
    """
    Represents the bird in the Flappy Bird game.
    Handles its movement, rotation, and drawing.

    Attributes:
        x (int): The x-coordinate of the bird.
        y (int): The y-coordinate of the bird.
        angle (int): The current angle of the bird.
        speed (float): The current vertical speed of the bird.
        height (int): The height where the bird last jumped.
        time (int): The time since the last jump.
        image_count (int): Counter for the bird's animation state.
        image (Surface): The current image of the bird.

    Methods:
        jump(): Makes the bird jump upwards.
        move(): Updates the bird's position and rotation based on physics.
        draw(screen): Draws the bird on the screen with the appropriate rotation.
        get_mask(): Returns a Pygame mask for the bird's current image.
    """

    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        """
        Initializes a Bird object with the given position.

        Args:
            x (int): Initial x-coordinate of the bird.
            y (int): Initial y-coordinate of the bird.
        """
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = self.IMGS[0]
        logging.info(f"Bird initialized at position ({self.x}, {self.y}).")

    def jump(self):
        """
        Makes the bird jump upwards by adjusting its velocity.
        """
        self.speed = -10.5
        self.time = 0
        self.height = self.y
        logging.debug("Bird jumped.")

    def move(self):
        """
        Calculates and updates the bird's position based on its speed and time.
        Adjusts the bird's angle depending on its movement.
        """
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.speed * self.time

        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0 or self.y < (self.height + 50):
            self.angle = max(self.angle, self.MAX_ROTATION)
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def draw(self, screen):
        """
        Draws the bird on the screen with appropriate animation and rotation.

        Args:
            screen (Surface): The Pygame surface where the bird will be drawn.
        """
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.image_count < self.ANIMATION_TIME * 2:
            self.image = self.IMGS[1]
        elif self.image_count < self.ANIMATION_TIME * 3:
            self.image = self.IMGS[2]
        elif self.image_count < self.ANIMATION_TIME * 4:
            self.image = self.IMGS[1]
        elif self.image_count >= self.ANIMATION_TIME * 4 + 1:
            self.image = self.IMGS[0]
            self.image_count = 0

        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.image_count = self.ANIMATION_TIME * 2

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        image_center_pos = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_image.get_rect(center=image_center_pos)
        screen.blit(rotated_image, rectangle.topleft)

    def get_mask(self):
        """
        Returns a Pygame mask for the bird's current image.

        Returns:
            Mask: A mask of the bird's current image.
        """
        return pygame.mask.from_surface(self.image)

class Pipe:
    """
    Represents a pipe obstacle in the Flappy Bird game.
    Handles the pipe's position, movement, and collision detection.

    Attributes:
        DISTANCE (int): Vertical distance between the top and bottom pipes.
        SPEED (int): Horizontal speed of the pipe's movement.
        x (int): Horizontal position of the pipe.
        height (int): Height of the top pipe.
        top_pos (int): Y-coordinate of the top pipe.
        bottom_pos (int): Y-coordinate of the bottom pipe.
        PIPE_TOP (Surface): Image of the top pipe (flipped vertically).
        PIPE_BOTTOM (Surface): Image of the bottom pipe.
        passed (bool): Whether the bird has passed this pipe.

    Methods:
        set_height(): Sets the random height of the pipes and adjusts their positions.
        move(): Moves the pipe horizontally to simulate scrolling.
        draw(screen): Draws the top and bottom pipes on the given screen.
        collide(bird): Checks if the pipe collides with the given bird object.
    """

    DISTANCE = 200
    SPEED = 5

    def __init__(self, x):
        """
        Initializes a Pipe object with the given x-coordinate.

        Args:
            x (int): The initial x-coordinate of the pipe.
        """
        self.x = x
        self.height = 0
        self.top_pos = 0
        self.bottom_pos = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True)
        self.PIPE_BOTTOM = PIPE_IMAGE
        self.passed = False
        self.set_height()

    def set_height(self):
        """
        Sets the height of the pipes randomly and updates their positions.
        """
        self.height = random.randrange(50, 475) # nosec
        self.top_pos = self.height - self.PIPE_TOP.get_height()
        self.bottom_pos = self.height + self.DISTANCE

    def move(self):
        """
        Moves the pipe horizontally based on the defined speed.
        """
        self.x -= self.SPEED

    def draw(self, screen):
        """
        Draws the top and bottom pipes on the screen.

        Args:
            screen (Surface): The Pygame surface where the pipes will be drawn.
        """
        screen.blit(self.PIPE_TOP, (self.x, self.top_pos))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom_pos))

    def collide(self, bird):
        """
        Checks if the pipe collides with the bird.
        Uses masks for pixel-perfect collision detection.

        Args:
            bird (Bird): The bird object to check for collision.

        Returns:
            bool: True if there's a collision, False otherwise.
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top_pos - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom_pos - round(bird.y))

        top_point = bird_mask.overlap(top_mask, top_offset)
        bottom_point = bird_mask.overlap(bottom_mask, bottom_offset)

        if top_point or bottom_point:
            return True
        else:
            return False

class Ground:
    """
    Represents the moving ground in the Flappy Bird game.

    Attributes:
        SPEED (int): Speed at which the ground moves to the left.
        WIDTH (int): Width of the ground image.
        IMAGE (Surface): Image of the ground.
        y (int): Vertical position of the ground.
        x1 (int): Horizontal position of the first ground segment.
        x2 (int): Horizontal position of the second ground segment.

    Methods:
        move(): Updates the horizontal positions of the ground segments to simulate movement.
        draw(screen): Draws the ground on the screen.
    """

    SPEED = 5
    WIDTH = GROUND_IMAGE.get_width()
    IMAGE = GROUND_IMAGE

    def __init__(self, y):
        """
        Initializes the Ground object with a vertical position.

        Args:
            y (int): The vertical position of the ground.
        """
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """
        Moves the ground segments to the left to simulate scrolling.
        If a segment moves off-screen, it is repositioned to create an infinite loop effect.
        """
        self.x1 -= self.SPEED
        self.x2 -= self.SPEED

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, screen):
        """
        Draws the ground segments on the screen.

        Args:
            screen (Surface): The Pygame surface where the ground will be drawn.
        """
        screen.blit(self.IMAGE, (self.x1, self.y))
        screen.blit(self.IMAGE, (self.x2, self.y))

def draw_screen(screen, birds, pipes, ground, score):
    """
    Draws all game elements on the screen.

    Args:
        screen (Surface): The Pygame surface to draw on.
        birds (list of Bird): List of bird objects to be drawn.
        pipes (list of Pipe): List of pipe objects to be drawn.
        ground (Ground): The ground object to be drawn.
        score (int): The current game score to be displayed.
    """
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    text = SCORE_FONT.render(f"Score: {score}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))
    ground.draw(screen)
    pygame.display.update()

def game_over_screen(screen, score):
    """
    Displays the game over screen with the final score.

    Args:
        screen (Surface): The Pygame surface to draw on.
        score (int): The final score to be displayed on the game over screen.
    """
    text = SCORE_FONT.render(
        f"Game Over! Score: {score}",
        True,
        (255, 255, 255)
    )
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    screen.blit(
        text,
        (
            SCREEN_WIDTH // 2 - text.get_width() // 2,
            SCREEN_HEIGHT // 2 - text.get_height() // 2
        )
    )
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    """
    The main function for running the Flappy Bird game loop.

    Handles the initialization of game objects, event handling, game logic, and rendering.

    Workflow:
        1. Initializes game objects like birds, ground, and pipes.
        2. Sets up the game screen and clock for managing the frame rate.
        3. Runs the main game loop to handle user input, object movement, collision detection, and drawing.

    Logging:
        - Logs the game start and score updates.

    Game Loop:
        - Listens for user input (e.g., spacebar to make the bird jump).
        - Updates the position of the birds, pipes, and ground.
        - Checks for collisions between the bird and pipes or ground.
        - Adds new pipes and removes off-screen pipes.
        - Draws all game elements on the screen.

    Restart Behavior:
        - If a collision occurs or the bird goes off-screen, the game over screen is displayed, and the game restarts.

    Args:
        None

    Returns:
        None
    """
    logging.info("Game started.")
    birds = [Bird(230, 350)]
    ground = Ground(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(30)

        # user interaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()

        # move things
        for bird in birds:
            bird.move()
        ground.move()

        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                    game_over_screen(screen, score)
                    main()
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            score += 1
            logging.info(f"Score updated: {score}")
            pipes.append(Pipe(600))
        for pipe in remove_pipes:
            pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > ground.y or bird.y < 0:
                birds.pop(i)
                game_over_screen(screen, score)
                main()

        draw_screen(screen, birds, pipes, ground, score)

if __name__ == '__main__':
    main()
