from project.grid import Grid


class Simulation(Grid):
    """ This class inherits the grid structure from class Grid and implements Conways's Game of Life"""

    # Disposition of neighboring cells
    NEIGHBOR_OFFSETS = [(-1, -1),
                        (-1, 0),
                        (-1, 1),
                        (0, -1),
                        (0, 1),
                        (1, -1),
                        (1, 0),
                        (1, 1)]

    def __init__(self, width: int, height: int, cell_size: int):
        super().__init__(width, height, cell_size)
        self.run: bool = False

    def count_live_neighbors(self, row: int, col: int) -> int:
        live_neighbors = 0
        for offset in self.NEIGHBOR_OFFSETS:
            new_row = (row + offset[0]) % self.rows
            new_col = (col + offset[1]) % self.cols
            if self.cells[new_row][new_col] == 1:
                live_neighbors += 1
        return live_neighbors

    def update(self):
        if self.is_running():
            # Create a new grid to hold the next state of the cells
            next_state = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

            # Update the state of every cell
            for row in range(self.rows):
                for col in range(self.cols):
                    cell_value = self.cells[row][col]
                    live_neighbors = self.count_live_neighbors(row, col)
                    if cell_value == 1:  # Cell is alive
                        if live_neighbors < 2 or live_neighbors > 3:  # State of underpopulation or overpopulation
                            next_state[row][col] = 0  # Cell dies
                        else:
                            next_state[row][col] = 1  # Cell survives
                    else:  # Cell is dead
                        if live_neighbors == 3:
                            next_state[row][col] = 1  # A cell is born
                        else:
                            next_state[row][col] = 0  # Cell remains dead

                    # If live_neighbors is 2 or 3 and the cell is alive, it survives by stasis

            # Update the grid with the next state
            self.cells = next_state

    def is_running(self):
        return self.run

    def start(self):
        # Start simulation
        self.run = True

    def stop(self):
        # Stop simulation
        self.run = False

    def clear(self):
        if not self.is_running():
            self.clear_cells()

    def create_random_state(self):
        if not self.is_running():
            self.fill_random()
