# function declarations
def print_field():
    print("---------")
    print(f"| {matrix[0][2]} {matrix[1][2]} {matrix[2][2]} |")
    print(f"| {matrix[0][1]} {matrix[1][1]} {matrix[2][1]} |")
    print(f"| {matrix[0][0]} {matrix[1][0]} {matrix[2][0]} |")
    print("---------")


def get_state(symbol):
    if any([matrix[0].count(symbol) == 3, matrix[1].count(symbol) == 3, matrix[2].count(symbol) == 3, matrix[0][0] == matrix[1][0] == matrix[2][0] == symbol, matrix[0][1] == matrix[1][1] == matrix[2][1] == symbol, matrix[0][2] == matrix[1][2] == matrix[2][2] == symbol, matrix[0][0] == matrix[1][1] == matrix[2][2] == symbol, matrix[2][0] == matrix[1][1] == matrix[0][2] == symbol]):
        return symbol + " wins"
    elif any([" " in matrix[0], " " in matrix[1], " " in matrix[2]]):
        return "Game not finished"
    else:
        return "Draw"


def make_move(symbol):
    number_string = "123456789"
    field_numbers = [1, 2, 3]
    while True:
        coordinates = input("Enter the coordinates: ").split()
        if coordinates[0] in number_string and coordinates[1] in number_string:
            coordinates = [int(x) for x in coordinates]
            if coordinates[0] in field_numbers and coordinates[1] in field_numbers:
                if matrix[coordinates[0] - 1][coordinates[1] - 1] == " ":
                    matrix[coordinates[0] - 1][coordinates[1] - 1] = symbol
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


# execution
matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_field()
is_x = True
while True:
    if is_x:
        symbol = "X"
    else:
        symbol = "O"
    make_move(symbol)
    print_field()
    state = get_state(symbol)
    is_x = not is_x
    if state == "Game not finished":
        continue
    else:
        print(state)
        break
