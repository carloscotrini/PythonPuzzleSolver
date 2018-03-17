import unittest
from four_queen_state import FourQueenState


class StateTester(unittest.TestCase):

    @staticmethod
    def are_boards_equal(board1, board2):
        if len(board1) != len(board2):
            return False

        for row1, row2 in zip(board1, board2):
            if ''.join(row1) != ''.join(row2):
                    return False

        return True

    def test_apply(self):

        board = [
            ['Q', '-', '-', '-'],
            ['-', '-', '-', 'Q'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-']
        ]
        current_row = 1
        state = FourQueenState(board, current_row)

        expected_board = [
            ['Q', '-', '-', '-'],
            ['-', '-', 'Q', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-']
        ]
        expected_current_row = 2
        expected_state = FourQueenState(expected_board, expected_current_row)

        place_queen_at_col_2 = 2
        result_state = state.apply(place_queen_at_col_2)
        self.assertTrue(StateTester.are_boards_equal(result_state.board, expected_board),
                        msg="We asked your implementation to place a queen at column 2 for the following state:\n" +
                        str(state) + "\n\n" +
                        "We expected this to be the new state:\n" +
                        str(expected_state) + "\n\n" +
                        "but we got this instead:\n" +
                        str(result_state))

    def test_solved(self):

        board = [
            ['-', 'Q', '-', '-'],
            ['-', '-', '-', 'Q'],
            ['Q', '-', '-', '-'],
            ['-', '-', 'Q', '-']
        ]
        current_row = 4
        state = FourQueenState(board, current_row)

        self.assertTrue(state.solved(),
                        msg="Your implementation incorrectly states that this state is not solved.\n" +
                        str(state))

        board = [
            ['-', 'Q', '-', '-'],
            ['-', '-', 'Q', '-'],
            ['Q', '-', '-', '-'],
            ['-', '-', 'Q', '-']
        ]
        current_row = 4
        state = FourQueenState(board, current_row)

        self.assertFalse(state.solved(),
                         msg="Your implementation incorrectly states that this state is solved.\n" +
                             str(state))

    def test_consistent(self):

        board = [
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-']
        ]
        current_row = 0
        consistent_state = FourQueenState(board, current_row)

        self.assertTrue(consistent_state.consistent(),
                        msg="Your implementation incorrectly states that this state is not consistent.\n" +
                            str(consistent_state))

        board = [
            ['-', 'Q', '-', '-'],
            ['-', '-', '-', 'Q'],
            ['Q', '-', '-', '-'],
            ['-', '-', 'Q', '-']
        ]
        current_row = 4
        consistent_state = FourQueenState(board, current_row)

        self.assertTrue(consistent_state.consistent(),
                        msg="Your implementation incorrectly states that this state is not consistent.\n" +
                            str(consistent_state))

        board = [
            ['-', 'Q', '-', '-'],
            ['-', '-', 'Q', '-'],
            ['Q', '-', '-', '-'],
            ['-', '-', 'Q', '-']
        ]
        current_row = 4
        inconsistent_state = FourQueenState(board, current_row)

        self.assertFalse(inconsistent_state.consistent(),
                         msg="Your implementation incorrectly states that this state is consistent.\n" +
                             str(inconsistent_state))


if __name__ == "__main__":
    unittest.main()
