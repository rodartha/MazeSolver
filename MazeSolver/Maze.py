"""Maze class that will hold the representation of the maze"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# NOTE: need contingency for mazes that are unsolvable

class Maze:
    def __init__(self, file_path):
        self.maze = self.load_photo(file_path)

        # FIXME: get user input to determine these values:
        locs = self.get_start_end()
        self.start_loc = locs[0]
        self.end_loc = locs[1]

        # List of (x, y) coordinates that comprise the solution for the maze
        self.correct_path = []
    
    def load_photo(self, file_path):
        img = Image.open(file_path).convert('LA')
        maze = np.array(img)[:,:,0]
        maze[maze > 155] = 1
        maze[maze <= 155] = 0

        return maze

    def get_start_end(self):
        print("Please click the start position of the maze, then the end position")
        fig = plt.figure(frameon=False)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        ax.imshow(self.maze, aspect='auto')
        locs = fig.ginput(n=2, timeout=0)
        plt.close()
        return locs

    def display_solved_maze(self):
        maze_color = self.maze
        maze_color[self.maze == 1] = 255
        color_image = np.dstack([maze_color, maze_color, maze_color])

        for loc in self.correct_path:
            # Creates red line showing solved path
            # NOTE: need to determine way to denote the line width of solve line
            color_image[loc[0], loc[1], 0] = 255

        return Image.fromarray(color_image)

