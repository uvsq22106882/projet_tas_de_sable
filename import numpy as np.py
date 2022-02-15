import numpy as np
import matplotlib.pyplot as plt

class Sandpile:

    def __init__(self, grid, pile_height=4):
        self.grid = np.array(grid)
        self.pile_height = pile_height

    def topple(self):
        while np.any(self.grid >= self.pile_height):
            new_grid = self.grid[:]
            for i, row in enumerate(self.grid):
                for j, col in enumerate(row):
                    if self.grid[i][j] >= self.pile_height:
                        new_grid[i][j] -= self.pile_height
                        if i - 1 >= 0:
                            new_grid[i-1][j] += 1
                        if i + 1 <= self.grid.shape[0] - 1:
                            new_grid[i+1][j] += 1
                        if j - 1 >= 0:
                            new_grid[i][j-1] += 1
                        if j + 1 <= self.grid.shape[1] - 1:
                            new_grid[i][j+1] += 1
            self.grid = new_grid[:]

    def collapse(self):
        while np.any(self.grid >= self.pile_height):
            new_grid = self.grid[:]
            for i, row in enumerate(self.grid):
                for j, col in enumerate(row):
                    while self.grid[i][j] >= self.pile_height:
                        new_grid[i][j] -= self.pile_height
                        if i - 1 >= 0:
                            new_grid[i-1][j] += 1
                        if i + 1 <= self.grid.shape[0] - 1:
                            new_grid[i+1][j] += 1
                        if j - 1 >= 0:
                            new_grid[i][j-1] += 1
                        if j + 1 <= self.grid.shape[1] - 1:
                            new_grid[i][j+1] += 1
            self.grid = new_grid[:]

    def settle(self):
        while np.any(self.grid >= self.pile_height):
            new_grid = self.grid[:]
            for i, row in enumerate(self.grid):
                for j, col in enumerate(row):
                    if self.grid[i][j] >= self.pile_height:
                        new_grid[i][j] -= self.pile_height
                        if i - 1 >= 0 and new_grid[i-1][j] < new_grid[i][j]:
                            new_grid[i-1][j] += 1
                        if i + 1 <= self.grid.shape[0] - 1 and new_grid[i+1][j] < new_grid[i][j]:
                            new_grid[i+1][j] += 1
                        if j - 1 >= 0 and new_grid[i][j-1] < new_grid[i][j]:
                            new_grid[i][j-1] += 1
                        if j + 1 <= self.grid.shape[1] - 1 and new_grid[i][j+1] < new_grid[i][j]:
                            new_grid[i][j+1] += 1
            self.grid = new_grid[:]
        
        
                            
    def save_grid(self, file_name):
        plt.imsave(file_name, self.grid, cmap='Greys')
        plt.close()

if __name__ == "__main__":
    a = 11
    test_grid = np.zeros((a, a))
    middle = round(a / 2)
    test_grid[middle][middle] += 1000
    test_pile = Sandpile(test_grid)
    test_pile.topple()
    test_pile.save_grid('test_sandpile.png')