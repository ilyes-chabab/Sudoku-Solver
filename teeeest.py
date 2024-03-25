class Verif:
    def __init__(self, filename="evilsudoku.txt"):
        with open(filename) as my_file:
            content = my_file.readlines()

        self.grid = [list(line.strip()) for line in content]

    def is_row_valid(self, row):
        """
        Check if the row is valid.
        """
        num = set()
        for col in range(9):
            if self.grid[row][col] in num:
                return False
            if self.grid[row][col] != '0':
                num.add(self.grid[row][col])
        return True

    def is_col_valid(self, column):
        """
        Check if the column is valid.
        """
        num = set()
        for row in range(9):
            if self.grid[row][column] in num:
                return False
            if self.grid[row][column] != '0':
                num.add(self.grid[row][column])
        return True

    def is_square_valid(self, square_row, square_column):
        """
        Check if the 3x3 square is valid.
        """
        num = set()
        for row in range(3):
            for column in range(3):
                val = self.grid[square_row * 3 + row][square_column * 3 + column]
                if val in num:
                    return False
                if val != '0':
                    num.add(val)
        return True
    
    def is_grid_full(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == '_' :
                    print("no")
                return False

    def is_grid_valid(self):
        """
        Check if the entire grid is valid.
        """

        if self.is_grid_full():
            print("no")
            return False
        
        for i in range(9):
            if not self.is_row_valid(i) or not self.is_col_valid(i):
                print("no")
                return False

        for i in range(3):
            for j in range(3):
                if not self.is_square_valid(i, j):
                    print("no")
                    return False

        return True

verif=Verif()
verif.is_grid_valid()

     
