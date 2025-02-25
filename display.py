import constants

SCREEN_LENGTH = constants.SCREEN_LENGTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

CH_WIDTH_TO_HEIGHT_RATIO = constants.CH_WIDTH_TO_HEIGHT_RATIO

CIRCLE_TOLERANCE = constants.CIRCLE_TOLERANCE

BORDER_THRESHOLD = constants.BORDER_THRESHOLD

MIN_X = constants.MIN_X
MAX_X = constants.MAX_X

MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y

MIN_Z = constants.MIN_Z
MAX_Z = constants.MAX_Z

Z_PRIME = constants.Z_PRIME

class Display:
    def __init__(self, height: int = SCREEN_HEIGHT, length: int = SCREEN_LENGTH):
        self.height = height
        self.length = length

        self.wipe_screen()

    def wipe_screen(self):
        """Wipes screen"""
        screen_line = [" "] * self.length
        self.screen = [screen_line[:] for _ in range(self.height)]


    def add_circle(self, coord: list[int], radius: int):
        """
        Recursively draws circles
        
        Args: 
            list[int] coords:   list of x,y coordinates
            int radius:         radius of circle in characters
        """
        x = coord[0]
        y = coord[1]
        
        # If out of bounds, raise error
        if not(BORDER_THRESHOLD <= x <= self.length - BORDER_THRESHOLD) or not(BORDER_THRESHOLD <= y <= self.height - BORDER_THRESHOLD):
            return

        self.screen[y][x] = "#"


    def _draw_circle(self, currCoord, centerCoord, radius, covered = set()):
        """
        Recursively draws circle

        Args:
            list[int] currCoord:        x,y coordinates on screen currently being set
            list[int] centerCoord:      x,y coordinates of the center of the circle
            int radius:                 radius of the circle
            covered:                    set of covered (x,y) coordinates as to not repeat any
        """
        x = int(currCoord[0])
        y = int(currCoord[1])
        dX = round((centerCoord[0] - x) * CH_WIDTH_TO_HEIGHT_RATIO)
        dY = round(centerCoord[1] - y)

        if (x,y) in covered:
            return

        if not (0 <= x <= self.length - 1) or not(0 <= y <= self.height - 1):
            return

        if dX ** 2 + dY ** 2 <= radius ** 2:
            self.screen[y][x] = "#"

            covered.add((x,y))

            self._draw_circle([x+1, y], centerCoord, radius, covered)
            self._draw_circle([x-1, y], centerCoord, radius, covered)
            self._draw_circle([x, y+1], centerCoord, radius, covered)
            self._draw_circle([x, y-1], centerCoord, radius, covered)


    def update_screen(self, coords: list[int], radius: int):
        """Updates screen but does not send to stdout"""
        pass

    def display_screen(self):
        """Outputs screen to terminal'"""

        for i in range(self.height):
            row = self.screen[i]

            # Print y-coordinate
            print(f"{i}\t|", end = '')

            # row values
            print("".join(row), end = '')

            # end of row; start new line
            print("|")

        # print x coordinate numbers % 10
        print("\t ", end = '')
        for i in range(self.length):
            val = i % 10
            if val % 2 == 0:
                print(val, end = '')
            else:
                print(" ", end = '')

        # start new line for next display
        print()
