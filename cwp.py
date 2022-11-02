"""
Introduction to Programming: Coursework 1
Please write your name
@author:Changfeng Wang

"""

# Reminder: You are not allowed to import any modules.
    

def wordsearch(puzzle: list, wordlist: list) -> list:
    words_found = []
    if not valid_puzzle(puzzle):
        print("Invalid puzzle")
        return []
    if not valid_wordlist(wordlist):
        print("Invalid wordlist")
        return []
    for i in wordlist:
        wordposition = get_positions(puzzle,i)
        if wordposition != []:
            print(i, wordposition)
            words_found.append((i,wordposition))
            #coloured_display(puzzle, get_positions(puzzle, i))
        else:
            print(i, wordposition)
    return words_found

def valid_puzzle(puzzle: list) -> bool:
    if len(puzzle) ==0:
        return False
    for i in puzzle:
        if not isinstance(i,str):
            return False
        if len(i) != len(puzzle[0]):
            return False
    return True


def valid_wordlist(wordlist: list) -> bool:
    if not isinstance(wordlist,list):
        return False
    for i in wordlist:
        if not isinstance(i,str):
            return False
    return True
    

def get_positions(puzzle: list, word: str) -> list:
    word = word.upper()
    words = []
    positions = set()
    i = j = 0
    r = len(puzzle)
    c = len(puzzle[0])
    x = 0
    while i < r:
        while j < c:
            if puzzle[i][j] == word[x]:
                if (i,j) not in positions:
                    positions.add((i,j))
            j += 1
        i += 1
        j = 0
    if len(word) == 1:
            return positions
    else:
        for x in positions:
            positions = get_words(x[0],x[1],r,c,1,puzzle,word,"")
            if len(positions) + 1== len(word):
                words.append([x]+positions)
                
    if len(words) == 0:
        print("'{}' not found.".format(word))
    return words

def get_words(i:int, j:int, r:int, c:int, m:int, puzzle:list, word:str, way:str) -> list:
    if m ==len(word):
        if 0 <= i < r and 0 <= j < c:
            if word[m-1] == puzzle[i][j]:
                return [(i,j)]
            else: return []
        else:
            return []
    positions = []
    
    if way == "":
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]:
                if 0 <= x < r and 0 <= y < c:
                    if puzzle[x][y].upper() == word[m]:
                        if x == i:
                            way = "left or right"
                        elif y == j:
                            way = "up or down"
                        else:
                            way = "slanting"
                        
                        positions = get_words(x,y,r,c,m+1,puzzle,word,way)
                        if len(positions) == len(word)-1:
                            return positions                
    elif way == "up or down":
        for x,y in [(i+1,j),(i-1,j)]:
            
            if 0 <= x < r and 0 <= y < c:
                if puzzle[x][y].upper() == word[m]:
                    positions.append((i,j))
                    positions += get_words(x,y,r,c,m+1,puzzle,word,way)
                        
    elif way == "left or right":
        for x,y in [(i,j-1),(i,j+1)]:
            if 0 <= x < r and 0 <= y < c:
                    if puzzle[x][y].upper() == word[m]:
                        positions.append((i,j))
                        positions += get_words(x,y,r,c,m+1,puzzle,word,way)
                        
    else:
        for x,y in [(i-1,j-1),(i+1,j-1),(i+1,j+1),(i-1,j+1)]:
            if 0 <= x < r and 0 <= y < c:
                    if puzzle[x][y].upper() == word[m]:
                        
                        positions = get_words(x,y,r,c,m+1,puzzle,word,way)
                    
                        if len(positions) == len(word) - m :
                            return [(i,j)] + positions
                        
    return positions
    

def basic_display(grid: list) -> None:
    for i in grid:
        print(" ")
        for j in i:
            print(j, end=" ")


def coloured_display(grid: list, positions: list) -> None:

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for x in positions:
                matrix = x[1][0]
                if (i,j) in matrix:
                    print("\033[1;31;40m",grid[i][j], end=" ")
                    break
            else:
                print("\033[1;37;40m",grid[i][j], end=" ")  
 
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
    final_list = wordsearch(puzzle1, good_wordlist2)
    
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
    #test_valid_puzzle()
    #test_valid_wordlist()
    #test_basic_display()
  
    #full solution
   
    #test_get_positions()
    #test_wordsearch()
    test_coloured_display()