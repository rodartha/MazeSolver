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
        self.start_loc = Node(locs[0][0], locs[0][1], None, self.get_f([locs[0][0], locs[0][1]]))
        self.end_pos = locs[1]
        self.end_loc = None

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

    def solve(self):
        open_list = [self.start_loc]
        closed_set = set()

        solved = False

        target_node = None

        while not solved and len(open_list) > 0:
            curr_node = open_list.pop()
            closed_set.add(curr_node)

            # NOTE: following code assumes (0,0) is top left
            # check space one up
            # NOTE: this is assuming that the program will properly handle equality operations for Node() and for lists
            if curr_node.y_pos + 1 < self.maze.shape[0]:
                new_node = Node(curr_node.x_pos, curr_node.y_pos + 1, curr_node, [curr_node.y_pos + 1, curr_node.x_pos])
                if [curr_node.y_pos + 1, curr_node.x_pos] == self.end_pos:
                    target_node = new_node
                    solved = True
                    break
                elif self.maze[curr_node.y_pos + 1, curr_node.x_pos] == 0 and new_node not in closed_set:
                    open_list.append(new_node)
            # check space one down
            # check space one left
            # check space one right
            # Make sure the last element in open_list has the minimal f_score
            open_list = sorted(open_list, key=lambda x: x.f_score, reverse=True)

        return solved, target_node


    def get_f(self, pos):
        return self.find_dist(pos, self.end_pos) + self.find_dist(pos, self.start_loc.get_pos())

    def find_dist(self, pos1, pos2):
        return np.linalg.norm(pos1 - pos2)


class Node:
    def __init__(self, x, y, parent=None, f_score):
        self.x_pos = x
        self.y_pos = y
        self.parent = parent
        self.f_score = f_score

    def get_pos(self):
        return [self.x_pos, self.y_pos]

