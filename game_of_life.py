# Conway's Game Of Life
import argparse
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Cell board values
ON = 255
OFF = 0
cell_values = [ON, OFF]

def main():
    # Command line args
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_argument('-b', '--board-size', dest='board', type=int, default=150, required=False)
    args = parser.parse_args()

    # Start game
    start_game(args.board)

def start_game(board_size):
    board = generate_grid(board_size)
    
    # Setup grid and animations
    fig, ax = plt.subplots()
    img = ax.imshow(board, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, board, board_size), frames=10, interval=20, save_count=100)

    # Show board
    plt.show()

def generate_grid(board_size):
    # Generate game board giving board size arguments for the grid.
    # With 65% - ON and 35% - OFF values in each cell.
    return numpy.random.choice(cell_values, board_size * board_size, p=[.5, .5]).reshape(board_size, board_size)

def update(frameNum, img, board, board_size):
    updated_board = board.copy()
    
    for i in range(board_size):
        for j in range(board_size):
            # Retrieve the number of neighbors has the current cell 
            neighbors = int(
                board[(i-1) % board_size, (j-1) % board_size] +
                board[(i-1) % board_size, j] +
                board[(i-1) % board_size, (j+1) % board_size] +
                board[i, (j-1) % board_size] +
                board[i, j] +
                board[i, (j+1) % board_size] +
                board[(i+1) % board_size, (j-1) % board_size] +
                board[(i+1) % board_size, j] +
                board[(i+1) % board_size, (j+1) % board_size])

            neighbors = neighbors / ON

            if board[i, j] == ON:
                if neighbors < 2 or neighbors > 3:
                    updated_board[i, j] = OFF
            else:
                if neighbors == 3:
                    updated_board[i, j] = ON
    
    # Update board
    img.set_data(updated_board)
    board[:] = updated_board[:]
    return img


if __name__ == '__main__':
    main()
