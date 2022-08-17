# classes:
class Player:
    def __init__(self, char, name, id):
        self.checker = char
        self.name = name
        self.id = id
        self.score = 0

    def __str__(self):
        string = f'\nJogador {self.id}:\n'
        string += f'Nome: {self.name}\nMarcador: {self.checker}\nPontuação: {self.score}'
        return string

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def setScore(self):
        self.score += 1


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.board_dict = {
            'A1': [0, 0],
            'A2': [1, 0],
            'A3': [2, 0],
            'B1': [0, 1],
            'B2': [1, 1],
            'B3': [2, 1],
            'C1': [0, 2],
            'C2': [1, 2],
            'C3': [2, 2],
        }

    def __str__(self):
        string = (
            '######################\n\n'
            '     A      B     C   \n'
            '        #      #      \n'
            f'1    {self.board[0][0]}  #   {self.board[0][1]}  #   {self.board[0][2]}  \n'
            '        #      #      \n'
            '   ################## \n'
            '        #      #      \n'
            f'2    {self.board[1][0]}  #   {self.board[1][1]}  #   {self.board[1][2]}  \n'
            '        #      #      \n'
            '   ###################\n'
            '        #      #      \n'
            f'3    {self.board[2][0]}  #   {self.board[2][1]}  #   {self.board[2][2]}  \n'
            '        #      #      \n\n'
            '######################\n'
        )
        return string

    def marker(self, position, char_checker):
        position = self.board_dict[position]
        self.board[position[0]][position[1]] = char_checker

    def checkDiagonal(self, char_checker):
        if (
            self.board[0][0]
            == self.board[1][1]
            == self.board[2][2]
            == char_checker
        ):
            return True
        elif (
            self.board[2][0]
            == self.board[1][1]
            == self.board[0][2]
            == char_checker
        ):
            return True
        else:
            return False

    def checkLine(self, position, char_checker):
        position = self.board_dict[position]
        if (
            self.board[position[0]][0]
            == self.board[position[0]][1]
            == self.board[position[0]][2]
            == char_checker
        ):
            return True
        else:
            return False

    def checkColumn(self, position, char_checker):
        position = self.board_dict[position]
        if (
            self.board[0][position[1]]
            == self.board[1][position[1]]
            == self.board[2][position[1]]
            == char_checker
        ):
            return True
        else:
            return False

    def resetBoard(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


class Game:
    def __init__(self, player1, player2, board, rounds):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.rounds = rounds

    def start(self):
        for i in range(self.rounds):
            print(f'RODADA #{i+1}')
            if i % 2 == 0:
                player_start = 1
            else:
                player_start = 2
            checker_board_count = 1
            checker_board_list = []
            board_list = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            current = player_start
            while checker_board_count <= 9:
                print(f"Jogador {current}, escolha uma posição (Ex:'A1'):")
                print(self.board)
                position = input('Posição: ')
                while True:
                    if (
                        position in board_list
                        and position not in checker_board_list
                    ):
                        checker_board_list.append(position)
                        char_checker = (
                            self.player1.checker
                            if current == 1
                            else self.player2.checker
                        )
                        self.board.marker(position, char_checker)
                        print(self.board)
                        break
                    else:
                        print(
                            'Escolha uma posição válida e que não tenha sido marcada ainda!'
                        )
                        print(self.board)
                        position = input('Posição: ')
                if checker_board_count >= 5:
                    if self.board.checkLine(position, char_checker):
                        if current == 1:
                            winner = self.player1.getName()
                            self.player1.setScore()
                        else:
                            winner = self.player2.getName()
                            self.player2.setScore()
                        print(f'{winner} ganhou!\n')
                        print(
                            f'{player1.getName()} {player1.getScore()} - {player2.getScore()} {player2.getName()}'
                        )
                        self.board.resetBoard()
                        break
                    elif self.board.checkColumn(position, char_checker):
                        if current == 1:
                            winner = self.player1.getName()
                            self.player1.setScore()
                        else:
                            winner = self.player2.getName()
                            self.player2.setScore()
                        print(f'{winner} ganhou!\n')
                        print(
                            f'{player1.getName()} {player1.getScore()} - {player2.getScore()} {player2.getName()}'
                        )
                        self.board.resetBoard()
                        break
                    elif self.board.checkDiagonal(char_checker):
                        if current == 1:
                            winner = self.player1.getName()
                            self.player1.setScore()
                        else:
                            winner = self.player2.getName()
                            self.player2.setScore()
                        print(f'{winner} ganhou!\n')
                        print(
                            f'{player1.getName()} {player1.getScore()} - {player2.getScore()} {player2.getName()}'
                        )
                        self.board.resetBoard()
                        break
                    elif checker_board_count == 9:
                        self.board.resetBoard()
                        print('Empate: Deu velha!\n')
                        print(
                            f'{player1.getName()} {player1.getScore()} - {player2.getScore()} {player2.getName()}'
                        )

                current = 2 if current == 1 else 1
                checker_board_count += 1


# main:
name = input('Escolha o nome do jogador 1: ')

while True:
    checker = input(
        f'Escolha um marcador para o jogador 1 (X ou O)\nDigite "1" para "X" ou "2" para "O": '
    )
    if checker == '1' or checker == '2':
        break
    else:
        print('\nValor inválido, escolha novamente!')


checker = 'X' if checker == '1' else 'O'
player1 = Player(checker, name, 1)

name = input('\nEscolha o nome do jogador 2: ')
checker = 'O' if checker == 'X' else 'X'
player2 = Player(checker, name, 2)

board = Board()

rounds = int(input('Qual será o número de rodadas? '))
while not isinstance(rounds, int):
    print('Entrada inválida, apenas números!')
    rounds = int(input('Qual será o número de rodadas? '))

game = Game(player1, player2, board, rounds)

game.start()
