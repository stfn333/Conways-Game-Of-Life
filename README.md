# Conway's Game of Life

![Conway's Game of Life](path_to_image)

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. This Python implementation treats the cellular grid as a toroidal surface, meaning the edges wrap around both horizontally and vertically, allowing for interesting and continuous patterns.

## Table of Contents
- [Introduction](#introduction)
- [How to Build](#how-to-build)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [License](#license)

## Introduction
This project is a Python implementation of Conway's Game of Life, a zero-player game where cells live, die, or multiply based on a few mathematical rules. The grid in this implementation wraps around, forming a toroidal surface, and providing a continuous simulation space. The project is organized into three main classes:

- **Grid:** Manages the cellular grid and visual representation.
- **Simulation:** Implements the game rules and updates the state of the grid.
- **GameOfLife:** Handles the main game loop and user interactions.

## How to Build

### Prerequisites
Before you can build and run this project, ensure you have the following installed:
- Python 3.12
- Pygame (for visualization)

You can install Pygame using pip:
```bash
pip install pygame
```

### Cloning the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/stfn333/Conways-Game-Of-Life.git
cd Conways-Game-Of-Life
```

## How to Run
Running the Simulation
Once you have the repository cloned and dependencies installed, you can run the simulation by executing the main Python script:
```bash
python main.py
```

This will start the simulation in a window, where you can see the cellular grid evolving according to the rules of Conway's Game of Life.

### Key Controls
Enter: Start the simulation.
Space: Pause/Resume the simulation.
- F: Increase the simulation speed (FPS).
- S: Decrease the simulation speed (FPS).
- R: Randomize the grid with a new state.
- C: Clear the grid.
- Mouse Click: Toggle the state of a specific cell between alive and dead.

## How to Use
Customizing the Initial State
You can customize the initial state of the grid by modifying the Simulation.fill_random() method or by manually toggling cells using the mouse.

### Changing the Grid Size and Cell Size
You can adjust the grid and cell sizes by modifying the WINDOW_WIDTH, WINDOW_HEIGHT, and CELL_SIZE variables in the GameOfLife class.

### Visualizing the Grid
The simulation visualizes the grid in a window, where live cells are represented by green squares, and dead cells are represented by grey squares.

### Extending the Simulation
You can extend this implementation by adding new rules, changing the grid size dynamically, or adding more interactive features like different patterns or a more sophisticated UI.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as you see fit.
