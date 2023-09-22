import word_ladder_maze

def main():
    #from https://puzzling.stackexchange.com/questions/122445/the-worlds-smallest-square-maze
    word_sets = [
        {'in'},
        {
            'bag', 'boat', 'bow', 
            'cop', 'fog', 'hug',
            'ox', 'ski', 'un'
        },
        {
            'bat', 'bug', 'cap',
            'cow', 'fox', 'nut',
            'pr', 'si', 'sun'
        },
        {
            'coat', 'fo', 'hut',
            'ne', 'pot', 'row',
            'ru', 'sk', 'sx'
        },
        {
            'cat', 'fr', 'hot',
            'net', 'pt', 'ro',
            'run', 'se', 'six'
        },
        {'out'}
    ]
    edge_set = {
        (0, 1),
        (1, 2), (1, 3),
        (2, 1), (2, 4), (2, 5),
        (3, 1), (3, 4),
        (4, 2), (4, 3)
    }

    ladder = word_ladder_maze.WordLadderMaze(word_sets, edge_set)
    print(f"{ladder.solve(0, 5)}")
    
if __name__ == '__main__':
    main()