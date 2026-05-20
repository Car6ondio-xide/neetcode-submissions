from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hash_map = defaultdict(int)
            for j in board[i]:
                if j != ".":
                    hash_map[j] += 1
            if any(x > 1 for x in hash_map.values()):
                return False

        for i in range(len(board)):
            hash_map = defaultdict(int)
            for j in range(len(board)):
                if board[j][i] != ".":
                    hash_map[board[j][i]] += 1
            if any(x > 1 for x in hash_map.values()):
                return False



        a = []
        x = 0
        y = 0
        c_y = y

        while c_y < 9:
            while x < 9:
                y = c_y
                while y - c_y < 3:
                    a += board[y][x:x + 3]
                    y += 1


                # print(a)
                hash_map = defaultdict(int)
                for i in range(len(a)):
                    for j in a[i]:
                        # print(j)
                        if j != ".":
                            hash_map[j] += 1
                    # print(hash_map.values())
                    if any(x > 1 for x in hash_map.values()):
                        return False
                    # print(hash_map)




                x += 3
                a = []
            x = 0
            c_y += 3

        return True
