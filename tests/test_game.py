"""
Unit tests for the Flappy Bird game.

This module includes tests for the Bird and Pipe classes to validate their functionality.
"""

import unittest
from src.flappy_bird import Bird, Pipe

class TestBird(unittest.TestCase):
    def setUp(self):
        self.bird = Bird(100, 200)

    def test_initial_position(self):
        """Tests if the bird is initialized in the correct position."""
        self.assertEqual(self.bird.x, 100)
        self.assertEqual(self.bird.y, 200)

    def test_jump(self):
        """Tests if the bird jumps correctly."""
        self.bird.jump()
        self.assertEqual(self.bird.speed, -10.5)
        self.assertEqual(self.bird.time, 0)

class TestPipe(unittest.TestCase):
    def setUp(self):
        self.pipe = Pipe(300)

    def test_initial_position(self):
        """Tests if the pipe is initialized in the correct position."""
        self.assertEqual(self.pipe.x, 300)

    def test_set_height(self):
        """Tests if the pipe's height is set correctly."""
        self.pipe.set_height()
        self.assertGreater(self.pipe.height, 50)
        self.assertLess(self.pipe.height, 475)

    def test_move(self):
        """Tests if the pipe moves correctly."""
        initial_x = self.pipe.x
        self.pipe.move()
        self.assertEqual(self.pipe.x, initial_x - self.pipe.SPEED)

if __name__ == "__main__":
    unittest.main()
