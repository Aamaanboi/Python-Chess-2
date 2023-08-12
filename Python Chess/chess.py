import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

white_peices = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_peices = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_peices_white = []
captured_peices_black = []
turn_step = 0
selection = 100
valid_move = []


# Black pieces
black_queen = pygame.image.load('black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_bishop = pygame.image.load('black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_king = pygame.image.load('black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_knight = pygame.image.load('black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_pawn = pygame.image.load('black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

black_rook = pygame.image.load('black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

# White pieces
white_queen = pygame.image.load('white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_bishop = pygame.image.load('white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_king = pygame.image.load('white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_knight = pygame.image.load('white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_pawn = pygame.image.load('white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_rook = pygame.image.load('white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

# White images
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

# Black images
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

peices_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# Draw main game board
def draw_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (232, 235, 239), [i * 100, j * 100, 100, 100])
            else:
                pygame.draw.rect(screen, (125, 135, 150), [i * 100, j * 100, 100, 100])

    pygame.draw.rect(screen, (0, 0, 0), [0, 800, WIDTH, 100])
    pygame.draw.rect(screen, (255, 215, 0), [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(screen, (255, 215, 0), [800, 0, 200, HEIGHT], 5)

    status_text = ['White: Select a piece to move!', 'White: Select a destination!', 'Black: Select a piece to move!!!',
                   'Black: Select a destination!']

    screen.blit(big_font.render(status_text[turn_step], True, (0, 0, 0)), (20, 820))
    for i in range(9):
        pygame.draw.line(screen, (0, 0, 0), (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(screen, (0, 0, 0), (100 * i, 0), (100 * i, 800), 2)

# Draw pieces onto the board
def draw_pieces():
    for i in range(len(white_peices)):
        x, y = white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10
        if white_locations[i] not in black_locations:
            if white_peices[i] == 'pawn':
                screen.blit(white_pawn, (x, y))
            else:
                index = peices_list.index(white_peices[i])
                screen.blit(white_images[index], (x, y))

            if turn_step < 2 and selection == i:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, 80, 80), 2)

    for i in range(len(black_peices)):
        x, y = black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10
        if black_locations[i] not in white_locations:
            if black_peices[i] == 'pawn':
                screen.blit(black_pawn, (x, y))
            else:
                index = peices_list.index(black_peices[i])
                screen.blit(black_images[index], (x, y))

            if turn_step >= 2 and selection == i:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, 80, 80), 2)


         # Function to check all the valid moves on the board
def check_options(pieces, location, turn, white_locations, black_locations):
    all_moves_list = []

    for i in range(len(pieces)):
        piece_location = location[i]  # Get the location of the current piece
        piece_type = pieces[i]         # Get the type of the current piece

        moves_list = []  # Initialize moves_list here

        if piece_type == 'pawn':
            moves_list = check_pawn(piece_location, turn, white_locations, black_locations)
        ''' elif piece == 'rook':
            moves_list = check_rook(locations, turn)
        elif piece == 'knight':
            moves_list = check_knight(locations, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(locations, turn)
        elif piece == 'queen':
            moves_list = check_queen(locations, turn)
        elif piece == 'king':
            moves_list = check_king(locations, turn)'''
        
        all_moves_list.append(moves_list)  # Append outside the if/elif block

    return all_moves_list
# Check valid pawn moves

def check_pawn(position, color, white_locations, black_locations):
    moves_list = []

    if color == 'white':
        if (position[0], position[1] - 1) not in white_locations and \
           (position[0], position[1] - 1) not in black_locations and \
           position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
           (position[0], position[1] - 2) not in black_locations and \
           position[1] == 6 and \
           (position[0], position[1] - 1) not in white_locations and \
           (position[0], position[1] - 1) not in black_locations:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        if (position[0], position[1] + 1) not in white_locations and \
           (position[0], position[1] + 1) not in black_locations and \
           position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
           (position[0], position[1] + 2) not in black_locations and \
           position[1] == 1 and \
           (position[0], position[1] + 1) not in white_locations and \
           (position[0], position[1] + 1) not in black_locations:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 2) in white_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 2) in white_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    return moves_list

    # Assuming white_locations and black_locations are lists of piece positions
white_locations = [(2, 2), (3, 3)]  # List of white piece positions
black_locations = [(5, 5), (4, 4)]  # List of black piece positions

position = (2, 1)  # Example pawn's position
color = 'white'    # Example pawn's color

valid_moves = check_pawn(position, color, white_locations, black_locations)
print("Valid moves:", valid_moves)



# Check for valid moves for just selected piece
def check_valid_moves(options_list):
    if turn_step < 2:
        if 0 <= selection < len(options_list):
            valid_options = options_list[selection]
        else:
            valid_options = []
    else:
        if 0 <= selection < len(options_list) + len(white_peices):
            valid_options = options_list[selection]
        else:
            valid_options = []
    return valid_options
#valid moves options
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'  # Red for white's turn
    else:
        color = 'blue'  # Blue for black's turn
    for i in range (len(moves)):
        pygame.draw.circle(screen, color,(moves[i][0] * 100 +50, moves[i][1] *100 + 50),5)

# Main game loop
black_options = check_options(black_peices, black_locations, 'black', white_locations, black_locations)

white_options = check_options(white_peices, white_locations, 'white')


while run:
    timer.tick(fps)
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)

            # Check if it's white's turn and the click is on a white piece
            if turn_step < 2 and click_coords in white_locations:
                selection = white_locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1
                valid_moves = check_valid_moves(white_options)

            # Check if it's black's turn and the click is on a black piece
            elif turn_step >= 2 and click_coords in black_locations:
                selection = black_locations.index(click_coords)
                if turn_step == 2:
                    turn_step = 3
                valid_moves = check_valid_moves(black_options)

            # Check if the clicked position is a valid move for the selected piece
            elif selection != 100 and click_coords in valid_moves:
                # Update the selected piece's position
                if turn_step < 2:
                    if click_coords not in black_locations:
                        white_locations[selection] = click_coords
                    else:
                        captured_piece_index = black_locations.index(click_coords)
                        captured_peices_black.append(black_peices[captured_piece_index])
                        black_peices.pop(captured_piece_index)
                        black_locations.pop(captured_piece_index)
                        white_locations[selection] = click_coords
                else:
                    if click_coords not in white_locations:
                        black_locations[selection - len(white_peices)] = click_coords
                    else:
                        captured_piece_index = white_locations.index(click_coords)
                        captured_peices_white.append(white_peices[captured_piece_index])
                        white_peices.pop(captured_piece_index)
                        white_locations.pop(captured_piece_index)
                        black_locations[selection - len(white_peices)] = click_coords

                # Switch to the next turn step
                turn_step = 2 if turn_step == 1 else 0
                selection = 100
                valid_moves = []

    # Calculate valid moves based on the current player's turn
    if turn_step < 2:
        valid_moves = check_valid_moves(white_options)
    else:
        valid_moves = check_valid_moves(black_options)

    draw_board()
    draw_pieces()
    if selection != 100:
        draw_valid(valid_moves)

    pygame.display.flip()

pygame.quit()
