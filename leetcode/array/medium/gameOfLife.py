""" Summary
对于需要在遍历中修改源数组状态但又需要保留源状态的情况,
为了节省内存不重新新建数组, 可以使用新的值代表状态, 从而扩大数组里的信息量。

二进制: 第一位代表当前状态, 第二位代表将来状态

- 00: dead -> dead
- 01: live -> dead
- 10: dead -> live
- 11: live -> live

num & 0b01 == 0b11 时, live -> live
num | 0b01 == 0b00 时, dead -> dead
num | 0b01 == 0b11 时, * -> live
num | 0b10 == 0b11 时, * -> dead
...

"""
import copy


class Solution(object):
    """
    Problem:
        https://leetcode.com/problems/game-of-life/
    Example:
        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时， 该细胞变成死亡状态。（模拟生命数量稀少）
        当前细胞为存活状态时，当周围有2个或3个存活细胞时， 该细胞保持原样。
        当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
        当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
    """

    def neighbors(self, board, r, c):
        nbs = []
        last_row = r - 1 if r > 0 else None
        left_col = c - 1 if c > 0 else None
        next_row = r + 1 if r < len(board) - 1 else None
        right_col = c + 1 if c < len(board[0]) - 1 else None
        if last_row is not None:
            if left_col is not None:
                nbs.append(board[last_row][left_col])
            nbs.append(board[last_row][c])
            if right_col is not None:
                nbs.append(board[last_row][right_col])

        if left_col is not None:
            nbs.append(board[r][left_col])

        if right_col is not None:
            nbs.append(board[r][right_col])

        if next_row is not None:
            if left_col is not None:
                nbs.append(board[next_row][left_col])
            nbs.append(board[next_row][c])
            if right_col is not None:
                nbs.append(board[next_row][right_col])

        return nbs

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        _board = copy.deepcopy(board)
        for r in range(len(board)):
            for c in range(len(board[r])):
                lives = len([x for x in self.neighbors(_board, r, c) if x == 1])
                print(lives)

                if board[r][c]:
                    print(lives)

                    if lives < 2:
                        board[r][c] = 0
                    elif lives > 3:
                        board[r][c] = 0
                else:
                    if lives == 3:
                        board[r][c] = 1

    def gameOfLifeBest(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.

        2 * O(mn) 的时间复杂度换来节省 O(mn) 的空间从而达到 O(1) 空间复杂度
        """
        for r in range(len(board)):
            for c in range(len(board[r])):
                lives = len([x for x in self.neighbors(board, r, c) if (x | 0b10) == 0b11])
                if (board[r][c] | 0b10) == 0b11:
                    if lives < 2 or lives > 3:
                        board[r][c] = 0b01
                    else:
                        board[r][c] = 0b11
                else:
                    if lives == 3:
                        board[r][c] = 0b10
                    else:
                        board[r][c] = 0b00

        for r in range(len(board)):
            for c in range(len(board[r])):
                board[r][c] >>= 1


if __name__ == '__main__':
    # m * n
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    print(board)
    # result = Solution().gameOfLife(board)
    result = Solution().gameOfLifeBest(board)
    print(board)
