"""Maze class that will hold the representation of the maze"""
from PIL import Image
import numpy as np

# NOTE: need contingency for mazes that are unsolvable

class Maze:
    def __init__(self, file_path):
        self.maze = self.load_photo(file_path)

        # FIXME: get user input to determine these values:
        self.start_loc = (0, 0)
        self.end_loc = (0, 0)

        # List of (x, y) coordinates that comprise the solution for the maze
        self.correct_path = []
    
    def load_photo(self, file_path):
        img = Image.open(file_path).convert('LA')
        maze = np.array(img)[:,:,0]
        maze[maze > 155] = 1
        maze[maze <= 155] = 0

        return maze

    def display_solved_maze(self):
        maze_color = self.maze
        maze_color[self.maze == 1] = 255
        color_image = np.dstack([maze_color, maze_color, maze_color])

        for loc in self.correct_path:
            # Creates red line showing solved path
            # NOTE: need to determine way to denote the line width of solve line
            color_image[loc[0], loc[1], 0] = 255

        return Image.fromarray(color_image)

