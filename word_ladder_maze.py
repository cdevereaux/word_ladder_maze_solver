import networkx as nx;

class WordLadderMaze:

    def __init__(self, word_sets: "list[set[str]]", edge_set: "set[tuple[int, int]]") -> None:
        self.word_sets = word_sets
        self.edge_set = edge_set

        self.__verify_edge_set()
        self.__verify_word_sets()
        self.__build_digraph()

    def solve(self, start: int, end: int) -> "list[str]":
        self.__verify_end_points(start, end)    
        self.end = end
        total_word_count = sum([len(word_set) for word_set in self.word_sets])
        for word in self.word_sets[start]:
            ladder = self.__solve_recursive([word], start)
            if len(ladder) == total_word_count:
                return ladder
        return []
    
    def __solve_recursive(self, words_so_far: "list[str]", current_node: int) -> "list[str]":
        best_list = words_so_far
        for neigh in self.digraph.neighbors(current_node):
            for word in self.word_sets[neigh]:
                if word in words_so_far:
                    continue
                if len(words_so_far) == 0 or self.__is_valid_word_transition(words_so_far[-1], word):
                    tentative_list = self.__solve_recursive(words_so_far + [word], neigh)
                    if len(tentative_list) !=0 and tentative_list[-1] in self.word_sets[self.end]:
                        if len(tentative_list) > len(best_list):
                            best_list = tentative_list
        return best_list
                

    def __is_valid_word_transition(self, prev: str, next: str) -> bool:
        match len(prev) - len(next):
            #insert a letter
            case -1:
                return self.__is_valid_word_transition(next, prev)
            #change a letter
            case 0:
                disagreements = 0
                for (c1, c2) in zip(prev, next):
                    if c1 != c2:
                        disagreements += 1
                return disagreements == 1
            #delete a letter
            case 1:
                prev = list(prev)
                next = list(next)
                for i in range(len(prev)):
                    if next == prev[0:i] + prev[i+1:len(prev)]:
                        return True
                return False

    def __verify_index(self, i: int):
        if i < 0 or i >= len(self.word_sets):
            raise ValueError(f"Invalid node index: {i}")

    def __verify_edge_set(self) -> None:
        for (a, b) in self.edge_set:
            self.__verify_index(a)
            self.__verify_index(b)
            
    def __verify_end_points(self, start, end) -> None:
        self.__verify_index(start)
        self.__verify_index(end)

    def __verify_word_sets(self) -> None:
        total_word_count = sum([len(word_set) for word_set in self.word_sets])
        total_word_set = set()
        for word_set in self.word_sets:
            total_word_set = total_word_set.union(word_set)
        if len(total_word_set) != total_word_count:
            raise ValueError(f"Graph contains duplicate words")


    def __build_digraph(self) -> None:
        self.digraph = nx.DiGraph()
        for i in range(len(self.word_sets)):
            self.digraph.add_node(i)
        for (i, j) in self.edge_set:
            self.digraph.add_edge(i, j)
