import pygame
from project.simulation import Simulation


class GameOfLife:
    """ This class starts the main loop of the Game of Life"""

    GREY = (29, 29, 29)

    # Set screen size (width, height)
    WINDOW_WIDTH = 1600
    WINDOW_HEIGHT = 800

    # Set cell size
    CELL_SIZE = 10

    # Set FPS
    # It defines how many times per second the main loop will run at most
    FPS = 12

    def __init__(self):
        # Initialize the pygame module
        pygame.init()
        # Set screen
        # .set_mode() method takes a tuple as an argument
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        # Set the frame rate of the simulation
        self.clock = pygame.time.Clock()

        self.simulation = Simulation(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.CELL_SIZE)
        self.simulation.fill_random()
        pygame.display.set_caption(f"GAME OF LIFE. Press 'ENTER' to start simulation.")

    def main_loop(self):
        """This function defines the main game loop"""

        running = True

        while running:

            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row = pos[1] // self.CELL_SIZE
                    col = pos[0] // self.CELL_SIZE
                    self.simulation.toggle_cell(row, col)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.simulation.start()
                        pygame.display.set_caption(f"Game of Life is running at FPS {self.FPS}. Press 'SPACE' to pause.")
                    elif event.key == pygame.K_SPACE:
                        self.simulation.stop()
                        pygame.display.set_caption("Game of Life has. Press 'ENTER' to resume.")
                    elif event.key == pygame.K_f:
                        self.FPS += 2
                        pygame.display.set_caption(f"Game of Life is running at FPS {self.FPS}. Press 'SPACE' to pause.")
                    elif event.key == pygame.K_s:
                        if self.FPS <= 5:
                            continue
                        self.FPS -= 2
                        pygame.display.set_caption(f"Game of Life is running at FPS {self.FPS}. Press 'SPACE' to pause.")
                    elif event.key == pygame.K_r:
                        self.simulation.create_random_state()
                    elif event.key == pygame.K_c:
                        self.simulation.clear()

            # 2. Updating State
            self.simulation.update()

            # 3. Drawing Grid
            self.window.fill(self.GREY)
            self.simulation.draw(self.window)
            pygame.display.update()
            self.clock.tick(self.FPS)

    pygame.quit()


if __name__ == "__main__":
    game = GameOfLife()
    game.main_loop()
