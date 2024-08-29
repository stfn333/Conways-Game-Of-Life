from typing import List
import pygame
import random


class Grid:
    """This class constructs the grid for the 'Game of Life' simulation window"""

    GREEN = (0, 255, 102)
    GREY = (55, 55, 55)

    def __init__(self, width: int, height: int, cell_size: int):
        self.cell_size = cell_size
        self.height = height
        self.width = width
        self.rows: int = self.height // self.cell_size
        self.cols: int = self.width // self.cell_size

        # Binary system represents the state of the cells
        # Initially set to zero (dead)
        # The two possible states are one (alive) or zero (dead)
        # Set a matrix of initially dead cells as instance attribute
        self.cells: List[List[int]] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw(self, window):
        # This method draws the grid of the simulation
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.GREEN if self.cells[row][col] else self.GREY
                x = col * self.cell_size
                y = row * self.cell_size
                pygame.draw.rect(window, color, rect=(x, y, self.cell_size - 1, self.cell_size - 1))

    def fill_random(self):
        # Random seed of alive cells
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = random.choice([1, 0, 0, 0, 0])

    def clear_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = 0

    def toggle_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = not self.cells[row][col]
