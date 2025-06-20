conversion = {'1': (1, 1), '2': (1, 2), '3': (1, 3),
              '4': (2, 1), '5': (2, 2), '6': (2, 3),
              '7': (3, 1), '8': (3, 2), '9': (3, 3)}

reverse_conversion = {(1, 1): '1', (1, 2): '2', (1, 3): '3',
                      (2, 1): '4', (2, 2): '5', (2, 3): '6',
                      (3, 1): '7', (3, 2): '8', (3, 3): '9'}

win_combs = (('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), 
             ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'), 
             ('1', '5', '9'), ('3', '5', '7'))


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.history = []
    
    def add_history(self, loc):
        self.history.append(loc)


class MiniBoard:
    def __init__(self) -> None:
        self.cell = [[' ', ' ', ' '], \
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
        self.tagged = set()
        self.crossed = False
    
    def mark(self, num) -> bool:
        x, y = conversion[num]
        if int(num) < 1 or int(num) > 9:
            return 'invalid num'
        else: 
            if self.cell[x-1][y-1] == ' ':
                self.cell[x-1][y-1] = 'X'
                self.tag()
                return 'valid'
            elif self.cell[x-1][y-1] == '-':
                return 'crossed off'
            else:
                return 'invalid'
    
    def tag(self) -> None:
        for x in range(1, 4):
            for y in range(1, 4):
                if self.cell[x-1][y-1] != ' ':
                     self.tagged.add(reverse_conversion[(x, y)])
    
    def cross_out(self, text) -> None:
        self.cell = [[f'{text}', f'{text}', f'{text}'], \
                     [f'{text}', f'{text}', f'{text}'], \
                     [f'{text}', f'{text}', f'{text}']]
        self.crossed = True
    
    def to_string(self) -> str:
        out = ''''''
        for row in range(len(self.cell)-1):
            out += f'{self.cell[row]}\n'
        out += f'{self.cell[-1]}'
        return out


class BigBoard:
    def __init__(self) -> None:
        self.board = [[MiniBoard(), MiniBoard(), MiniBoard()], \
                      [MiniBoard(), MiniBoard(), MiniBoard()], \
                      [MiniBoard(), MiniBoard(), MiniBoard()],]
        self.players = []
        self.tagged = set()
        self.current_board = None
        self.current_player = None
        self.winner = None
        self.winner_board = False

    def add_player(self, name) -> None:
        self.players.append(name)
    
    def mark(self, num1, num2) -> str:
        x, y = conversion[num1]
        mb = self.board[x-1][y-1]
        value = mb.mark(num2)
        if not self.winner and value == 'valid' and not self.winner_board:
            self.current_player.add_history((num1, num2))
            if self.check_mini(mb):
                mb.cross_out('-')
        self.tag()
        return value

    def tag(self) -> None:
        for x in range(1, 4):
            for y in range(1, 4):
                if self.board[x-1][y-1].crossed:
                     self.tagged.add(reverse_conversion[(x, y)])
    
    def check_mini(self, mb) -> bool:
        for comb in win_combs:
            if all(num in mb.tagged for num in comb):
                return True
        return False
    
    def check_big(self) -> bool:
        for comb in win_combs:
            if all(num in self.tagged for num in comb):
                return True
        return False
    
    def to_string(self) -> str:
        def add_vert(lines) -> str:
            split_lines = lines.split('\n')
            for i in range(len(split_lines)):
                split_lines[i] += ' | '
            lines = '\n'.join(split_lines)
            return lines
        
        def concatenate_hor(col1, col2, col3):
            spilt_lines = zip(col1.split('\n'), col2.split('\n'), col3.split('\n'))
            joint = '\n'.join([x + y + z for x, y, z in spilt_lines])
            return joint

        out = ''''''
        for row in range(3):
            col1 = self.board[row][0].to_string()
            col2 = self.board[row][1].to_string()
            col3 = self.board[row][2].to_string()
            col1 = add_vert(col1)
            col2 = add_vert(col2)
            line = concatenate_hor(col1, col2, col3)
            print(line)
            if row != 2:
                print('-' * 51)
        return out


if __name__ == '__main__':
    player1 = input('Enter Name (Player 1): ')
    print(f'Welcome to the game, {player1}!')
    player2 = input('Enter Name (Player 2): ')
    print(f'Welcome to the game, {player2}! \n')
    
    board = BigBoard()
    board.add_player(Player(player1))
    board.add_player(Player(player2))
    
    first_mark_big = input(f'({board.players[0].name}) What board would you like to mark: ')
    first_mark_mini = input(f'({board.players[0].name}) What cell would you like to mark: ')
    board.current_player = board.players[0]
    current_player = board.current_player
    board.mark(first_mark_big, first_mark_mini)
    board.current_board = first_mark_mini
    print(board.to_string())
    
    while True:
        try:
            current_player = board.players[0] if board.current_player == board.players[1] else board.players[1]
            other_player = board.players[1] if board.current_player == board.players[1] else board.players[0]
            board.current_player = current_player

            mark_mini = input(f'({current_player.name}) What cell would you like to mark: ')
            result = board.mark(board.current_board, mark_mini)
            
            if result == 'valid':
                board.current_board = mark_mini
                print(board.to_string())
                
                if board.check_big(): # if there's a winner
                    print(f'{other_player.name} WON!')
                    board.winner = other_player
                    winner_board = BigBoard()
                    winner_board.winner_board = True
                    for x, y in board.winner.history:
                        winner_board.mark(x, y)
                    print(f'Here are {other_player}\'s game-winning mark placements!')
                    print(winner_board.to_string())
                    break
            elif result == 'crossed off':
                print('THE MINI BOARD IS CROSSED OFF! Select a new board instead.')
                mark_big = input(f'({current_player.name}) What board would you like to mark: ')
                mark_mini = input(f'({current_player.name}) What cell would you like to mark: ')
                board.mark(mark_big, mark_mini)
                board.current_player = current_player
                board.current_board = mark_mini
                print(board.to_string())
                
                if board.check_big(): # if there's a winner
                    print(f'{other_player.name} WON!')
                    board.winner = other_player
                    winner_board = BigBoard()
                    winner_board.winner_board = True
                    for x, y in board.winner.history:
                        winner_board.mark(x, y)
                    print(winner_board.to_string())
                    break
            elif result == 'invalid num':
                print('NUMBER IS OUT OF RANGE! Try again.')
            else:
                print('WRONG LOCATION! Try again.')
        except KeyboardInterrupt:
            # Ctrl-C to exit
            exit()