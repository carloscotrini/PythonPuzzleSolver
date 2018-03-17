from algo_search.rec_solve import rec_search
from algo_search.state import State
import copy


class FourQueenState(State):

    def __init__(self, board, current_row):
        self.board = board
        self.current_row = current_row

    def next_actions(self):
        return [0, 1, 2, 3]

    def apply(self, action):
        new_state = FourQueenState(copy.deepcopy(self.board), self.current_row)
        new_state.board[new_state.current_row] = ['-', '-', '-', '-']
        new_state.board[new_state.current_row][action] = 'Q'
        new_state.current_row += 1
        return new_state

    def solved(self):
        return self.consistent() and self.current_row == 4

    def consistent(self):

        def find_queen_col(row):
            for i in range(4):
                if row[i] == 'Q':
                    return i
            return None

        def no_two_queens_same_col():
            for i in range(self.current_row):
                for j in range(i):
                    q_i_col = find_queen_col(self.board[i])
                    q_j_col = find_queen_col(self.board[j])
                    if q_i_col == q_j_col:
                        return False
            return True

        def no_two_queens_same_diag():
            for i in range(self.current_row):
                for j in range(i):
                    q_i_col = find_queen_col(self.board[i])
                    q_j_col = find_queen_col(self.board[j])
                    if abs(i - j) == abs(q_i_col - q_j_col):
                        return False
            return True

        return no_two_queens_same_col() and no_two_queens_same_diag()

    def __str__(self):
        return "Current row: " + str(self.current_row) + "\nBoard:\n" + '\n'.join(map(str, self.board))


if __name__ == "__main__":
    board = [
        ['-', '-', '-', '-']
    ] * 4
    current_row = 0
    solved_state = rec_search(FourQueenState(board, current_row))
    print(str(solved_state))
