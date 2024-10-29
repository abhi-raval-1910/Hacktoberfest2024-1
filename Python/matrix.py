import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(50)  # Refresh screen every 50 milliseconds

    # Get screen height and width
    sh, sw = stdscr.getmaxyx()

    # Create a list to hold the positions of the "raindrops" (one for each column)
    rain_positions = [0] * sw

    while True:
        # Loop through each column and decide where to print the raindrop
        for i in range(sw):
            # Print a random character at the current rain position in the column
            char = chr(random.randint(33, 126))  # Random ASCII character
            stdscr.addstr(rain_positions[i], i, char, curses.color_pair(1))

            # Move the raindrop position down or reset to top if off screen
            rain_positions[i] += 1
            if rain_positions[i] >= sh:
                rain_positions[i] = 0

        # Refresh the screen
        stdscr.refresh()

        # Clear the screen to create the rain effect
        stdscr.clear()

        # Check if 'q' has been pressed to quit
        key = stdscr.getch()
        if key == ord('q'):
            break

# Start curses and set up color pair
curses.wrapper(main)
