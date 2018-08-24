import math
import copy

class Grid:
    
    """Represent the state of a grid: state, path_history, and heuristic score."""

    
    def __init__(self, input_state):
        
        # don't just bind to input state. we want the object to have its OWN state
        # https://docs.python.org/2/library/copy.html
        self.state = copy.deepcopy(input_state)

        self.path_history = list()

        # TODO: we're calculating n here, but passing it between objects elsewhere. Tidy? 
        self.n = len(input_state[0])

        # determined by (manhattan) heuristic
        self.score = 0



    def move(self, direction):
        """Slide a tile in one of 4 directions.

        Return True if successful (with side-effect of changing the state).
        Return False if movement in that direction not possible. 
        """

        zero_coords = self.locate_tile(0, self.state)        

        # find the offset of the moving tile relative to the '0' tile
        # when we say 'move left' we mean the tile, not the space (0)
        if direction == 'up':
            y, x = 1, 0
        elif direction == 'down':
            y, x = -1, 0
        elif direction == 'left':
            y, x = 0, 1
        elif direction == 'right':
            y, x = 0, -1
        else:
            raise ValueError('Invalid direction: must be \'up\', \'down\', \
                \'left\' or \'right\'') # TODO: is this good design?

        # return false if move not possible
        if zero_coords[0] + y not in range(0, self.n):
            return False
        if zero_coords[1] + x not in range(0, self.n):
            return False

        # swap tiles
        tile_to_move = self.state[zero_coords[0] + y][zero_coords[1] + x]
        self.state[zero_coords[0]][zero_coords[1]] = tile_to_move
        self.state[zero_coords[0] + y][zero_coords[1] + x] = 0              

        return True



    def locate_tile(self, tile, grid_state):
        """Return the co-ordinates of a given tile, given as a tuple.
        Assumes one unique tile in grid."""

        # TODO: should this be a static method: doesn't always operate on self?
        for (y, row) in enumerate(grid_state):
            for (x, value) in enumerate(row):
                if value == tile:
                    return (y, x)


    
    def manhattan_score(self, goal_state):
        """Manhattan Priority Function.

        https://heuristicswiki.wikispaces.com/Manhattan+Distance

        Return the sum of the distances that each tile is
        from its goal position.
        """

        sum = 0
        for (y, row) in enumerate(self.state):
            for (x, tile) in enumerate(row):
                if tile == 0:
                    continue
                sum += self.manhattan_distance(tile, (y, x), goal_state)

        return sum


    
    def manhattan_distance(self, tile, tile_position, goal_state):
        """Calculates the Manhattan distance between a given tile's position
        and its position in goal_state"""
        
        goal_position = self.locate_tile(tile, goal_state)

        distance = (abs(goal_position[0] - tile_position[0]) 
                   + abs(goal_position[1] - tile_position[1]))

        return distance









        

	
