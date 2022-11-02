"""
Introduction to Programming: Coursework 1
Please write your name
@author:Changfeng Wang

"""


# Reminder: You are not allowed to import any modules.

def wordsearch(puzzle: list, wordlist: list) -> None:
    if not valid_puzzle(puzzle):
        print("Invalid puzzle")
        return
    if not valid_wordlist(wordlist):
        print("Invalid wordlist")
        return
    for i in wordlist:
        if get_positions(puzzle, i) != []:
            print(i, get_positions(puzzle, i))
            coloured_display(puzzle, get_positions(puzzle, i))
        else:
            print(i, get_positions(puzzle, i))


def valid_puzzle(puzzle: list) -> bool:
    if len(puzzle) == 0:
        return False
    for i in puzzle:
        if not isinstance(i, str):
            return False
        if len(i) != len(puzzle[0]):
            return False
    return True


def valid_wordlist(wordlist: list) -> bool:
    if not isinstance(wordlist, list):
        return False
    for i in wordlist:
        if not isinstance(i, str):
            return False
    return True


# def get_positions(puzzle: list, word: str) -> list:
#     word = word.upper()
#     words = []
#     positions = set()
#     i = j = 0
#     r = len(puzzle)
#     c = len(puzzle[0])
#     x = 0
#     while i < r:
#         while j < c:
#             if puzzle[i][j] == word[x]:
#                 if (i, j) not in positions:
#                     positions.add((i, j))
#             j += 1
#         i += 1
#         j = 0
#     if len(word) == 1:
#         return positions
#     else:
#         for x in positions:
#             positions = get_words(x[0], x[1], r, c, 1, puzzle, word, "")
#             if len(positions) + 1 == len(word):
#                 words.append([x] + positions)
#
#     if len(words) == 0:
#         print("'{}' not found.".format(word))
#     return words


################################################################
def possible_position(puzzle: list, word: str, start_position):
    position_list = []
    word_len = len(word)
    row, col = start_position
    if col + word_len <= len(puzzle[0]):
        one_line = []
        for i in range(word_len):
            one_line.append((row, col + i))
        position_list.append(one_line)
    if row + word_len <= len(puzzle):
        one_line = []
        for i in range(word_len):
            one_line.append((row + i, col))
        position_list.append(one_line)
    if col + word_len <= len(puzzle[0]) and row + word_len <= len(puzzle):
        one_line = []
        for i in range(word_len):
            one_line.append((row + i, col + i))
        position_list.append(one_line)
    return position_list
#################################################################

####################################################
def get_positions(puzzle: list, word: str) -> list:
    word = word.upper()
    possible_start_position_list = []
    result_list = []
    r = len(puzzle)
    c = len(puzzle[0])
    for x in range(r):
        for y in range(c):
            if puzzle[x][y] == word[0]:
                possible_start_position_list.append((x, y))
    for possible_start_position in possible_start_position_list:
        for one_line in possible_position(puzzle, word, possible_start_position):
            compare_word = ""
            for position in one_line:
                compare_word += puzzle[position[0]][position[1]]
            if compare_word == word:
                result_list.append(one_line)
    return result_list
##############################################################################

def get_words(i: int, j: int, r: int, c: int, m: int, puzzle: list, word: str, way: str) -> list:
    if m == len(word):
        if 0 <= i < r and 0 <= j < c:
            if word[m - 1] == puzzle[i][j]:
                return [(i, j)]
            else:
                return []
        else:
            return []
    positions = []

    if way == "":
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),
                     (i + 1, j + 1)]:
            if 0 <= x < r and 0 <= y < c:
                if puzzle[x][y].upper() == word[m]:
                    if x == i:
                        way = "left or right"
                    elif y == j:
                        way = "up or down"
                    else:
                        way = "slanting"

                    positions = get_words(x, y, r, c, m + 1, puzzle, word, way)
                    if len(positions) == len(word) - 1:
                        return positions
    elif way == "up or down":
        for x, y in [(i + 1, j), (i - 1, j)]:

            if 0 <= x < r and 0 <= y < c:
                if puzzle[x][y].upper() == word[m]:
                    positions.append((i, j))
                    positions += get_words(x, y, r, c, m + 1, puzzle, word, way)

    elif way == "left or right":
        for x, y in [(i, j - 1), (i, j + 1)]:
            if 0 <= x < r and 0 <= y < c:
                if puzzle[x][y].upper() == word[m]:
                    positions.append((i, j))
                    positions += get_words(x, y, r, c, m + 1, puzzle, word, way)

    else:
        for x, y in [(i - 1, j - 1), (i + 1, j - 1), (i + 1, j + 1), (i - 1, j + 1)]:
            if 0 <= x < r and 0 <= y < c:
                if puzzle[x][y].upper() == word[m]:

                    positions = get_words(x, y, r, c, m + 1, puzzle, word, way)

                    if len(positions) == len(word) - m:
                        return [(i, j)] + positions

    return positions


def basic_display(grid: list) -> None:
    for i in grid:
        print(" ")
        for j in i:
            print(j, end=" ")


def coloured_display(grid: list, positions: list) -> None:
    positions = positions[0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in positions:
                print("\033[91m" + grid[i][j] + "\033[0m", end=" ")
            if (i, j) not in positions:
                print(grid[i][j], end=" ")
            else:
                pass
        print()


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'j', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    print(final_list)

    # coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    test_valid_puzzle()
    test_valid_wordlist()
    test_basic_display()

    # full solution
    test_coloured_display()
    test_get_positions()
    test_wordsearch()


def new_func():
    print("Ture")
    # basic solution
    test_valid_puzzle()
    test_valid_wordlist()
    test_basic_display()

    # full solution
    test_coloured_display()
    test_get_positions()
    test_wordsearch()
