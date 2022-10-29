"""
Introduction to Programming: Coursework 1
Please write your name
@author:

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    '''
    This function takes a list of strings (puzzle) and a list of words (wordlist)
    and prints out the words in wordlist that can be found in the puzzle.
    '''
    if not valid_puzzle(puzzle):
        print("Invalid puzzle")
        return
    if not valid_wordlist(wordlist):
        print("Invalid wordlist")
        return
    for i in wordlist:
        if get_positions(puzzle, i) != []:
            print(i, get_positions(puzzle, i))
            
    # coloured_display(puzzle, get_positions(puzzle, i))



def valid_puzzle(puzzle: list) -> bool:
    '''
      Checks if the puzzle is valid or not
      :param puzzle: list
      :return: bool
    '''
    if len(puzzle) == 0:
        return False
    if not isinstance(puzzle, list):
        return False
    for i in puzzle:
        if not isinstance(i, str):
           return False
        if len(i) != len(puzzle[0]):
            return False
    return True


def valid_wordlist(wordlist: list) -> bool:
    '''
      Check if the wordlist is valid or not
      :param wordlist: list
      :return: bool
    '''
    if len(wordlist) == 0:
        return False
    if not isinstance(wordlist, list):
        return False
    for i in wordlist:
        if not isinstance(i, str):
            return False
    return True


def get_positions(puzzle: list, word: str) -> list:
    '''
      Get the positions of the word in the puzzle
      :param puzzle: list  # the puzzle to search
      :param word: str  # the word to search for
      :return: list  # a list of tuples of the positions of the word
    '''
    positions = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == word[0]:
                positions.append((i, j))
    return positions

def basic_display(grid: list) -> None:
    '''
      Display the puzzle
      :param grid: list
      :return: None
    '''
    for i in grid: 
        for j in i:
            print(j, end=" ")
        print()

def forfor(a):
    return [item for sublist in a for item in sublist]

def coloured_display(grid: list, positions: list) -> None:
    '''
      Display the puzzle with the positions coloured
      :param grid: list
      :param positions: list
      :return: None
    '''
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
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "RUN"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["run", "scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    print(final_list)
    coloured_display(puzzle1, final_list)


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
