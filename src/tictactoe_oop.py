# tictactoe_oop.py, An object-oriented Tic Tac Toe game.
# By Al Sweigart al@inventwithpython.com

# Setting up constants:
ALL_SPACES = list('123456789') # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = TTTBoard() # Create a TTT board object.
    currentPlayer, nextPlayer = X, O # X goes first, O goes next.

    while True:
        print(gameBoard.getBoardStr()) # Display the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = None
        while move not in ALL_SPACES or gameBoard.spaces[move] != BLANK:
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer) # Make the move.

        # Check if the game is over:
        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' has won the game!')
            break
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # Swap turns.

class TTTBoard:
    def __init__(self):
        """Create a new, blank tic tac toe board."""
        self.spaces = {} # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self.spaces[space] = BLANK # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return f'''
      {self.spaces['1']}|{self.spaces['2']}|{self.spaces['3']}  1 2 3
      -+-+-
      {self.spaces['4']}|{self.spaces['5']}|{self.spaces['6']}  4 5 6
      -+-+-
      {self.spaces['7']}|{self.spaces['8']}|{self.spaces['9']}  7 8 9'''

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        b, p = self.spaces, player # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((b['1'] == b['2'] == b['3'] == p) or # Across the top
                (b['4'] == b['5'] == b['6'] == p) or # Across the middle
                (b['7'] == b['8'] == b['9'] == p) or # Across the bottom
                (b['1'] == b['4'] == b['7'] == p) or # Down the left
                (b['2'] == b['5'] == b['8'] == p) or # Down the middle
                (b['3'] == b['6'] == b['9'] == p) or # Down the right
                (b['3'] == b['5'] == b['7'] == p) or # Diagonal
                (b['1'] == b['5'] == b['9'] == p))   # Diagonal

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self.spaces[space] == BLANK:
                return False # If a single space is blank, return False.
        return True # No spaces are blank, so return True.

    def updateBoard(self, space, player):
        """Sets the space on the board to player."""
        self.spaces[space] = player

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
