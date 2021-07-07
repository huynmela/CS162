# Author: Melanie Huynh
# Date: 3/11/2021
# Description: This program allows two players to play Janggi, Korean Chess.

class GamePiece:
    """
    Represents the GamePiece object which inherits a group of pieces with
    general methods for all game pieces for the piece's position, legal moves,
    what type of piece it is, and if it exists on the board anymore. As each piece
    has a commonality (playable, has a position on the board, etc.) it can be part
    of a super class.
    """
    def __init__(self, color):
        """
        Initializes the position of the pieces on the board (x, y), color of piece (color),
        and if it is on the board (True or False).
        """
        self._color = color # Color redefined when placed
        # Palace coords
        self._d = ['d1','d2','d3','d8','d9','d10'] 
        self._e = ['e1','e2','e3','e8','e9','e10']
        self._f = ['f1','f2','f3','f8','f9','f10']
        self._special = self._d + self._f + self._e
        self._corners = ['d1','f1','e2','d3','f3','d8','d10','f8','f10','e9']

    def piece_type(self, pos, board):
        """
        Returns the type of piece in a position on the board
        """
        piece = board[self.ind(pos)[0]][self.ind(pos)[1]]
        return piece

    def get_color(self):
        """
        Returns the color of the piece
        """
        return self._color

    def ind(self, pos):
        """
        Converts the string input to an easier index for the board
        """
        row = int(pos[1:]) - 1
        column = self.letter_to_column(pos[0])
        return row, column

    def letter_to_column(self, pos):
        """
        Method to convert string letters of columns to int to index
        """
        column_dict = {}
        column_dict['a'] = 0
        column_dict['b'] = 1
        column_dict['c'] = 2
        column_dict['d'] = 3
        column_dict['e'] = 4
        column_dict['f'] = 5
        column_dict['g'] = 6
        column_dict['h'] = 7
        column_dict['i'] = 8
        return column_dict[pos[0]]
        
    def check_general(self, gb, gr):
        """
        A check to see if the general can still make moves
        """
        gb = General("BLUE")
        gr = General("RED")
        # Look to see if the generals are in the same column
        
        gr_row = self.ind(new_pos)[0]
        gr_col = self.ind(new_pos)[1]
        gb_row = self.ind(cur_pos)[0]
        gb_col = self.ind(cur_pos)[1]

# SUBCLASSES OF GAMEPIECE OBJECT -----------------------------------------------
class General(GamePiece):
    """
    Represents the General object which is a subclass of GamePiece.
    """
    def __init__(self, color):
        """
        Initializes the General object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """       
        if cur_pos and new_pos in self._special:
            new_row = self.ind(new_pos)[0]
            new_col = self.ind(new_pos)[1]
            cur_row = self.ind(cur_pos)[0]
            cur_col = self.ind(cur_pos)[1]

            if state == "UNFINISHED":
                if new_pos in self._special: # Make sure that the piece it's trying to take isn't it's own
                    if board[new_row][new_col] is not None:
                        if self.piece_type(new_pos, board).get_color() == self._color:
                            return False
                            
                if new_pos in self._special: # if its in the palace
                    # Checking if the movement is left or right (one column apart) from the cur_pos
                    if (new_col == cur_col + 1 or new_col == cur_col - 1) and new_row == cur_row:
                        return True
                    # Checking if forward or backward movement is legal
                    elif (new_row == cur_row - 1 or new_row == cur_row + 1) and (new_col == cur_col):
                        return True
                    # Checking if diagonal lines are possible
                    elif cur_pos in self._corners:
                        if (new_row == cur_row + 1 or new_row == cur_row - 1) and (new_col == cur_col - 1 or new_col == cur_col + 1):
                            return True
                    else:
                        return False
        else:
            return False

class Guard(GamePiece):
    """
    Represents the Guard object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Guard object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        if cur_pos and new_pos in self._special:
            new_row = self.ind(new_pos)[0]
            new_col = self.ind(new_pos)[1]
            cur_row = self.ind(cur_pos)[0]
            cur_col = self.ind(cur_pos)[1]

            if state == "UNFINISHED":
                if new_pos in self._special: # Make sure that the piece it's trying to take isn't it's own
                    if board[new_row][new_col] is not None:
                        if self.piece_type(new_pos, board).get_color() == self._color:
                            return False
                            
                if new_pos in self._special: # if its in the palace
                    # Checking if the movement is left or right (one column apart) from the cur_pos
                    if (new_col == cur_col + 1 or new_col == cur_col - 1) and new_row == cur_row:
                        return True
                    # Checking if forward or backward movement is legal
                    elif (new_row == cur_row - 1 or new_row == cur_row + 1) and (new_col == cur_col):
                        return True
                    # Checking if diagonal lines are possible
                    elif cur_pos in self._corners:
                        if (new_row == cur_row + 1 or new_row == cur_row - 1) and (new_col == cur_col - 1 or new_col == cur_col + 1):
                            return True
                    else:
                        return False
        else:
            return False

class Horse(GamePiece):
    """
    Represents the Horse object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Horse object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]
        piece = self.piece_type(cur_pos, board)

        if state == "UNFINISHED": 
        # Check if the movement left or right is legal
            if (new_row == cur_row - 1) and (new_col == cur_col + 2):
                # checking left and right are valid
                if board[cur_row][cur_col + 1] is not None:
                    print("hello 1")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("1for some reason it thinks the new pos has a color of the same piece")
                    return
                print("Horse moved up and right 2")
                return True

            elif (new_row == cur_row - 1) and (new_col == cur_col - 2):
                print("Hello im here")
                # checking left and right are valid
                if board[cur_row][cur_col + 1] is not None:
                    print("horse attempted to move left and up the board")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return
                print("Horse moved up and left 2")
                return True

            elif (new_row == cur_row + 1) and (new_col == cur_col + 2):
                # checking left and right are valid
                if board[cur_row][cur_col - 1] is not None:
                    print("hello 3")
                    return False
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return False
                print("Horse moved down and right 2")
                return True

            elif (new_row == cur_row + 1) and (new_col == cur_col - 2):
                # checking left and right are valid
                if board[cur_row][cur_col - 1] is not None:
                    print("hello 4")
                    return False
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return False
                print("Horse moved down and left 2")
                return True
            #---------------------------------------------------------------------------------------------------------------
            # Check if the forwards and backwards is legal
            elif (new_row == cur_row - 2) and (new_col == cur_col + 1):
                # checking left and right are valid
                if board[cur_row - 1][cur_col] is not None:
                    print("hello 5")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 5")
                    return
                print("it worked 5")
                return True

            elif (new_row == cur_row - 2) and (new_col == cur_col - 1):
                # checking left and right are valid
                if board[cur_row - 1][cur_col] is not None:
                    print("hello 6")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 6")
                    return
                print("it worked 6")
                return True

            elif (new_row == cur_row + 2) and (new_col == cur_col + 1):
                # checking left and right are valid
                if board[cur_row + 1][cur_col] is not None:
                    print("hello 7")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 7")
                    return
                print("it worked 7")
                return True

            elif (new_row == cur_row + 2) and (new_col == cur_col - 1):
                # checking left and right are valid
                if board[cur_row + 1][cur_col] is not None:
                    print("hello 8")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 8")
                    return
                print("it worked 8")
                return True
#            else:
        #    print("it actually never entered the if statement?"
                #return False
        else:
            print("False")
            return False

class Elephant(GamePiece):
    """
    Represents the Elephant object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Elephant object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]
        piece = self.piece_type(cur_pos, board)

        if state == "UNFINISHED":
            if (new_row == cur_row + 3) and (new_col == cur_col + 2): #F5
                if board[cur_row + 1][cur_col] and board[cur_row + 2][cur_col + 1] is not None:
                    print("hello 1 elephant")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("1for some reason it thinks the new pos has a color of the same piece")
                    return
                print("elephant moved down and right")
                return True

            elif (new_row == cur_row - 3) and (new_col == cur_col - 2): #B1
                print("Hello im here")
                # checking left and right are valid
                if board[cur_row - 1][cur_col] and board[cur_row - 2][cur_col - 1] is not None:
                    print("horse attempted to move left and up the board")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return
                print("e moved up and left")
                return True

            elif (new_row == cur_row + 3) and (new_col == cur_col - 2): #
                # checking left and right are valid
                if board[cur_row + 1][cur_col] and board[cur_row + 2][cur_col - 1] is not None:
                    print("hello e3")
                    return False
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return False
                print("e moved down and right")
                return True

            elif (new_row == cur_row - 3) and (new_col == cur_col + 2): #F1
                # checking left and right are valid
                if board[cur_row - 1][cur_col] and board[cur_row - 2][cur_col + 1] is not None:
                    print("hello e4")
                    return False
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    return False
                print("Horse moved down and left 2")
                return True
            #---------------------------------------------------------------------------------------------------------------
            # Check if the forwards and backwards is legal
            elif (new_row == cur_row - 2) and (new_col == cur_col + 3): #G2
                # checking left and right are valid
                if board[cur_row][cur_col + 1] and board[cur_row - 1][cur_col + 2] is not None:
                    print("hello e5")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 5e")
                    return
                print("it worked e5")
                return True

            elif (new_row == cur_row - 2) and (new_col == cur_col - 3): #A2
                # checking left and right are valid
                if board[cur_row][cur_col - 1] and board[cur_row - 1][cur_col - 2] is not None:
                    print("hello e6")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 6e")
                    return
                print("it worked e6")
                return True

            elif (new_row == cur_row + 2) and (new_col == cur_col + 3): #G6
                # checking left and right are valid
                if board[cur_row][cur_col + 1] and board[cur_row - 1][cur_col - 2] is not None:
                    print("hello 7e")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("ebye 7")
                    return
                print("it worked e7")
                return True

            elif (new_row == cur_row + 2) and (new_col == cur_col - 3): #A6
                # checking left and right are valid
                if board[cur_row][cur_col - 1] and board[cur_row + 1][cur_col - 2] is not None:
                    print("hello 8")
                    return
                elif self.piece_type(new_pos, board) is not None and self.piece_type(new_pos, board).get_color() == self._color:
                    print("bye 8")
                    return
                print("it worked 8")
                return True
#            else:
        #    print("it actually never entered the if statement?"
                #return False
        else:
            print("False")
            return False

class Chariot(GamePiece):
    """
    Represents the Chariot object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Chariot object
        """
        super().__init__(color)

    def check_path(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """

        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]
        cannon_pieces = [Cannon('BLUE'), Cannon('RED')]
        
        # Ensures the range is always in the right order
        if new_row > cur_row: 
            ran_r = range(cur_row + 1, new_row, 1)
        elif cur_row > new_row:
            ran_r = range(cur_row - 1, new_row, -1)
            
        elif new_col > cur_col:
            ran_c = range(cur_col + 1, new_col, 1)
        elif cur_col > new_col:
            ran_c = range(cur_col - 1, new_col, -1)
        else:
            return False
            
        # Checking if the movement is left or right is legal
        if new_row == cur_row:
            print("it's in the new_row == cur_row")
            # Check if there is a legal piece (a non-Cannon) is contained in the path
            counter = 0
            print(counter)
            for col_spot in ran_c:
                if board[cur_row][col_spot] is not None:
                    counter += 1

            if counter == 0: 
                print("jump!")
                return True
               
        # Checking if the movement vertical is legal
        if new_col == cur_col:
            print("it's in the new_col == cur_col")
            # Check if there is a legal piece (a non-Cannon) is contained in the path
            counter = 0
            for row_spot in ran_r:
                if board[row_spot][cur_col] is not None:
                    counter += 1
                    print(board[row_spot][cur_col])
                    print(counter)
            if counter == 0:
                print("jump!")
                return True

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]

        if state == "UNFINISHED":
        # Make sure the position you're going into isn't your own piece
            if board[new_row][new_col] is not None:
                if self.piece_type(new_pos, board).get_color() == self._color:
                    return False
                    
            # Checking diagonals in the palace
            if cur_pos and new_pos in self._special:
                # Checking if the movement is in the same column
                if new_col == cur_col and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True
                # Checking if the movement is in the same row
                elif new_row == cur_row and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True
                # Checking all possible diagonals
                elif new_row == cur_row + 1 and new_col == cur_col + 1 and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True
                elif new_row == cur_row - 1 and new_col == cur_col - 1 and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True
                elif new_row == cur_row + 2 and new_col == cur_col + 2 and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True
                elif new_row == cur_col - 2 and new_row == cur_col - 2 and self.check_path(cur_pos, new_pos, board, state) is True:
                    return True                          
            # Checking if the movement is in the same column
            if new_col == cur_col and self.check_path(cur_pos, new_pos, board, state) is True:
                return True
            # Checking if the movement is in the same row
            elif new_row == cur_row and self.check_path(cur_pos, new_pos, board, state) is True:
                return True
            else:
                return False
        else:
            return False
class Cannon(GamePiece):
    """
    Represents the Cannon object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Cannon object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        print("we are in check legal???")
        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]
        cannon_pieces = [Cannon('BLUE'), Cannon('RED')]
        
        # Ensures the range is always in the right order
        if new_row > cur_row: 
            ran_r = range(cur_row + 1, new_row, 1)
        elif cur_row > new_row:
            ran_r = range(cur_row - 1, new_row, -1)
            
        elif new_col > cur_col:
            ran_c = range(cur_col + 1, new_col, 1)
        elif cur_col > new_col:
            ran_c = range(cur_col - 1, new_col, -1)
        else:
            return False
            
        #cannon = board[cur_row][cur_col]
        
        if state == "UNFINISHED":
        # Make sure the position you're going into isn't your own piece
            if board[new_row][new_col] is not None:
                if self.piece_type(new_pos, board).get_color() == self._color:
                    return False
            print("It entered the unfinished statement")
            # Inside the palace
#            if cur_pos and new_pos in self._special:
                
            # Checking if the movement is left or right is legal
            if new_row == cur_row:
                print("it's in the new_row == cur_row")
                # Check if there is a legal piece (a non-Cannon) is contained in the path
                counter = 0
                print(counter)
                for col_spot in ran_c:
                    if board[cur_row][col_spot] is not None:
                        counter += 1
                        print(board[cur_row][col_spot])
                        print(counter)
                        
                    if board[cur_row][col_spot] in cannon_pieces:
                        print("stopped because its a cannon piece")
                        print(board[row_spot][cur_col])
                        return False
                if counter == 1: 
                    print("jump!")
                    return True
                   
            # Checking if the movement vertical is legal
            if new_col == cur_col:
                print("it's in the new_col == cur_col")
                # Check if there is a legal piece (a non-Cannon) is contained in the path
                counter = 0
                for row_spot in ran_r:
                    if board[row_spot][cur_col] is not None:
                        counter += 1
                        print(board[row_spot][cur_col])
                        print(counter)
                        
                    if board[row_spot][cur_col] in cannon_pieces:
                        print("stopped because its a cannon piece")                    
                        print(board[row_spot][cur_col])
                        return False
                if counter == 1:
                    print("jump!")
                    return True
                    
        else:
           return False

class Soldier(GamePiece):
    """
    Represents the Soldier object which is a subclass of GamePiece
    """
    def __init__(self, color):
        """
        Initializes the Soldier object
        """
        super().__init__(color)

    def check_legal(self, cur_pos, new_pos, board, state):
        """
        Returns whether or not moving a piece to a desired position is a legal move.
        """
        new_row = self.ind(new_pos)[0]
        new_col = self.ind(new_pos)[1]
        cur_row = self.ind(cur_pos)[0]
        cur_col = self.ind(cur_pos)[1]
        
        if state == "UNFINISHED":
        # Make sure the position you're going into isn't your own piece
            if board[new_row][new_col] is not None:
                if self.piece_type(new_pos, board).get_color() == self._color:
                    return False
            # Check if you're in the palace
            if new_pos in self._special: # Make sure that the piece it's trying to take isn't it's own
                    if board[new_row][new_col] is not None:
                        if self.piece_type(new_pos, board).get_color() == self._color:
                            return False                    
            # Checking if the movement is left or right (one column apart) from the cur_pos
            if (new_col == cur_col + 1 or new_col == cur_col - 1) and new_row == cur_row:
                return True

            # Checking if forward movement is legal
            elif self._color == 'BLUE':
                print("this soldier is blue")
                if new_row == cur_row - 1 and new_col == cur_col:
                    print("The blue soldier is trying to move forward")
                    # cant take your own piece
                    if self.piece_type(new_pos, board) is not None:
                        print("There's a piece here")
                        if self.piece_type(new_pos, board).get_color == self._color:
                            print("Trying to take it's own color piece")
                            return False
                    return True
            elif self._color == 'RED':
                print("this soldier is red")
                if new_row == cur_row + 1 and new_col == cur_col:
                    print("The red soldier is trying to move forward")
                    if self.piece_type(new_pos, board) is not None:
                        print("There's a piece here")
                        if self.piece_type(new_pos, board).get_color == self._color:
                            print("Trying to take it's own color piece")
                            return False
                    return True
            else:
                return False
        else:
            return False

# BOARD -------------------------------------------------------------------
class Board:
    """
    Represents the board and its pieces
    """
    def __init__(self):
        """
        Builds the board and places the pieces in its spots
        """
        self._board = []
        for i in range(10):
            self._board.append([None for i in range(9)])
        self.place_pieces()

    def add_piece(self, pos, piece):
        """
        pos is a string of a letter (column) and a number (row)
        for example pos = 'a2' which is the first column in the second row
        """
        self._board[self.ind(pos)[0]][self.ind(pos)[1]] = piece

    def place_pieces(self):
        """
        Places the pieces into the board
        """
        # Soldiers
            # RED
        self.add_piece('a4', Soldier('RED'))
        self.add_piece('c4', Soldier('RED'))
        self.add_piece('e4', Soldier('RED'))
        self.add_piece('g4', Soldier('RED'))
        self.add_piece('i4', Soldier('RED'))
            # BLUE
        self.add_piece('a7', Soldier('BLUE'))
        self.add_piece('c7', Soldier('BLUE'))
        self.add_piece('e7', Soldier('BLUE'))
        self.add_piece('g7', Soldier('BLUE'))
        self.add_piece('i7', Soldier('BLUE'))
        # Cannons
            # RED
        self.add_piece('b3', Cannon('RED'))
        self.add_piece('h3', Cannon('RED'))
            # BLUE
        self.add_piece('b8', Cannon('BLUE'))
        self.add_piece('h8', Cannon('BLUE'))
        # Generals
            # RED
        self.add_piece('e2', General('RED'))
            # BLUE
        self.add_piece('e9', General('BLUE'))
        # Chariots
            # RED
        self.add_piece('a1', Chariot('RED'))
        self.add_piece('i1', Chariot('RED'))
            # BLUE
        self.add_piece('a10', Chariot('BLUE'))
        self.add_piece('i10', Chariot('BLUE'))

        # Horses
            # RED
        self.add_piece('c1', Horse('RED'))
        self.add_piece('h1', Horse('RED'))
            # BLUE
        self.add_piece('c10', Horse('BLUE'))
        self.add_piece('h10', Horse('BLUE'))
        # Elephants
            # RED
        self.add_piece('b1', Elephant('RED'))
        self.add_piece('g1', Elephant('RED'))
            # BLUE
        self.add_piece('b10', Elephant('BLUE'))
        self.add_piece('g10', Elephant('BLUE'))
        # Advisors
            # RED
        self.add_piece('d1', Guard('RED'))
        self.add_piece('f1', Guard('RED'))
            # BLUE
        self.add_piece('d10', Guard('BLUE'))
        self.add_piece('f10', Guard('BLUE'))

    def ind(self, pos):
        """
        Converts the string input to an easier index for the board
        """
        row = int(pos[1:]) - 1
        column = self.letter_to_column(pos[0])
        return row, column

    def letter_to_column(self, pos):
        """
        Method to convert string letters of columns to int to index
        """
        column_dict = {}
        column_dict['a'] = 0
        column_dict['b'] = 1
        column_dict['c'] = 2
        column_dict['d'] = 3
        column_dict['e'] = 4
        column_dict['f'] = 5
        column_dict['g'] = 6
        column_dict['h'] = 7
        column_dict['i'] = 8
        return column_dict[pos[0]]

    def get_board(self):
        return self._board

# JANGGIGAME CLASS -------------------------------------------------------------
class JanggiGame:
    """
    Represents an abstract board game called Janggi
    """
    def __init__(self):
        """
        Initializes the JanggiGame object and any data members within it
        Will also initialize the board and the state of the game
        """
        self._current_state = "UNFINISHED"
        self._start_color = "RED"
        self._board = Board()

    def get_current_state(self):
        """
        Returns the current state of the game
        """
        return self._current_state

    def get_board(self):
        """
        Returns the modified board
        """
        return self._board.get_board()

    def get_game_state(self):
        """
        Returns the state of the game of the JanggiGame object.
        Depending on the game state, it will return 'UNFINISHED', 'RED_WON',
        or 'BLUE_WON'.
        """
        return self._current_state

    def is_in_check(self, player):
        """
        Takes as a parameter a player (red or blue) and returns True if that
        player is in check, but return False otherwise.
        """
        # List of coords in board
        col = ['a','b','c','d','e','f','g','h','i'] # the columns
        a = []
        for i in range(10):
            a.append([j + str(i+1) for j in col])
            
        # Flatten the list
        board_coords = []
        for sublist in a:
            for coord in sublist:
                board_coords.append(coord)
        
        # getting each object in the board for a player
        pieces_coords = []
        pieces_left = []
        for row in range(10):
            for column in range(9):
                if self.get_board()[row][column] is not None and self.get_board()[row][column].get_color() == player.upper():
                    # pieces left on the board for the player
                    pieces_coords.append((row, column))
                    pieces_left.append(self.get_board()[row][column])
        
        p_b_coord = (pieces_coords, board_coords)
        
        counter = 0        
        for piece_coord in pieces_coords: 
            for board_coord in board_coords:              
                translated_index = self.column_to_letter(piece_coord[1]) + str(piece_coord[0])                
                piece = self.get_piece_type(translated_index)
                if piece is not None:
                    if piece.check_legal(translated_index, board_coord, self.get_board(), self.get_game_state()) == True:
                        counter += 1
        print(counter)
        if counter == 0:
            self._current_state = upper(player) + '_WON'
            return True                                
        return False

    def get_piece_type(self, pos):
        """
        Returns the Piece object sitting in the pos of the board
        """
        piece = self.get_board()[self.ind(pos)[0]][self.ind(pos)[1]]
        return piece

    def make_move(self, cur_pos, new_pos):
        """
        Takes two parameters, strings that represent the square to move from
        and the square to move to. If the square being moved from doesn't contain
        an opposing piece, the move is not legal, or if the game has already won,
        then it should return False. Otherwise, make the move, remove any captured
        piece, update the game state if necessary, update whose turn it is,
        and return True.
        """
        print(cur_pos, new_pos)
        # Automatically check if the new_pos is the same color piece             
        piece = self.get_piece_type(cur_pos)             
                         
        # Check if cur_pos is None
        if piece == None:
            print("the current piece is none")
            return False
        
        print("the current piece is " + piece.get_color())
        print("which should not be " + self._start_color)
                
        if piece.get_color() is not self._start_color:
            if cur_pos == new_pos:
                print("passing, switching "+self._start_color+"into "+piece.get_color())
                self._start_color = piece.get_color() # allow a pass
                return True
            elif piece.check_legal(cur_pos, new_pos, self.get_board(), self.get_game_state()) == True:
                print("it returned true into make_move")
                # switch the colors
                print("switching "+self._start_color+"into "+piece.get_color())
                self._start_color = piece.get_color()
                # change the new position to the piece
                self.get_board()[self.ind(new_pos)[0]][self.ind(new_pos)[1]] = piece
                # change current position to None
                self.get_board()[self.ind(cur_pos)[0]][self.ind(cur_pos)[1]] = None
                # then make the movement true
                return True
                # otherwise, the movement is not legal
            else:
                print("its false in make_move")
                return False
        print("its all false")
        return False

    def ind(self, pos):
        """
        Converts the string input to an easier index for the board
        """
        row = int(pos[1:]) - 1
        column = self.letter_to_column(pos[0])
        return row, column

    def letter_to_column(self, pos):
        """
        Method to convert string letters of columns to int to index
        """
        column_dict = {}
        column_dict['a'] = 0
        column_dict['b'] = 1
        column_dict['c'] = 2
        column_dict['d'] = 3
        column_dict['e'] = 4
        column_dict['f'] = 5
        column_dict['g'] = 6
        column_dict['h'] = 7
        column_dict['i'] = 8
        return column_dict[pos[0]]
    
    def column_to_letter(self, pos):
        """
        Method to convert string letters of columns to int to index
        """
        column_dict = {}
        column_dict[0] = 'a'
        column_dict[1] = 'b'
        column_dict[2] = 'c'
        column_dict[3] = 'd'
        column_dict[4] = 'e'
        column_dict[5] = 'f'
        column_dict[6] = 'g'
        column_dict[7] = 'h'
        column_dict[8] = 'i'
        return column_dict[pos]

