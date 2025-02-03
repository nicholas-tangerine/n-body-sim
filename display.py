import constants

SCREEN_LENGTH = constants.SCREEN_LENGTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

MIN_X = constants.MIN_X
MAX_X = constants.MAX_X
MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y

class Display:
    def __init__(self, height = SCREEN_HEIGHT, length = SCREEN_LENGTH):
        self.height = height
        self.length = length

        self.wipe_screen()

    def wipe_screen(self):
        screen_line = [" "] * self.length
        self.screen = [screen_line[:] for _ in range(self.height)]

    def update_screen(self, coords):
        self.wipe_screen()
        for coord in coords:
            x = round((coord[0] - MIN_X) * self.length / (MAX_X - MIN_X))
            y = round((coord[1] - MIN_Y) * self.height / (MAX_Y - MIN_Y))

            if (0 <= x < self.length and 0 <= y < self.height):
                self.screen[y][x] = "#"

    def display_screen(self):
        
        # for each row
        for i in range(self.height):
            row = self.screen[i]

            # print y coordinate numbers
            print(f"{i}\t|", end = '')

            # row values
            print("".join(row), end = '')

            # end of row; start new line
            print("|")

        # print x coordinate numbers % 10
        print("\t ", end = '')
        for i in range(self.length):
            print(i % 10, end = '')

        print()
        # start new line for next display

