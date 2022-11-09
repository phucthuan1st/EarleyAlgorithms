from nltk import Tree
from State import State
from WordDictionary import get_word_dictionary

class Earley:
    def __init__(self, setences, grammar, terminals):
        self.table = [[] for _ in range(len(setences) + 1)]
        self.current_id = 0
        self.setences = setences
        self.grammar = grammar
        self.terminals = terminals

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def is_terminal(self, tag):
        return tag in self.terminals

    def is_complete(self, state):
        return len(state.rules) == state.dot_idx

    def enqueue(self, state, table_entry):
        if state not in self.table[table_entry]:
            self.table[table_entry].append(state)
        else:
            self.current_id -= 1

    def predict(self, state):
        for production in self.grammar[state.next()]:
            self.enqueue(State(state.next(), production, 0, state.end_idx, state.end_idx, self.get_new_id(), [], 'predictor'), state.end_idx)

    def scan(self, state):
        if self.setences[state.end_idx] in self.grammar[state.next()]:
            self.enqueue(State(state.next(), [self.setences[state.end_idx]], 1, state.end_idx, state.end_idx + 1, self.get_new_id(), [], 'scanner'), state.end_idx + 1)

    def complete(self, state):
        for s in self.table[state.start_idx]:
            if not s.is_complete() and s.next() == state.label and s.end_idx == state.start_idx and s.label != 'gamma':
                self.enqueue(State(s.label, s.rules, s.dot_idx + 1, s.start_idx, state.end_idx, self.get_new_id(), s.made_from + [state.idx], 'completer'), state.end_idx)

    def parse(self):
        self.enqueue(State('gamma', ['S'], 0, 0, 0, self.get_new_id(), [], 'dummy start state'), 0)
        
        # for EACH table in parse table
        for i in range(len(self.setences) + 1):
            # with EACH state on parse table
            for state in self.table[i]:
                # if state not complete and next state is not a terminal
                if not state.is_complete() and not self.is_terminal(state.next()):
                    self.predict(state)
                # if state not complete and next state is a terminal    
                elif i != len(self.setences) and not state.is_complete() and self.is_terminal(state.next()):
                    self.scan(state)
                else:
                    self.complete(state)
                    
        return self.has_parsed()
    def get_state_at_index(self, idx):
        for table in self.table:
            for state in table:
                if state.idx == idx:
                    return state
                
        return None
        
    def has_parsed(self):
        for index, state in enumerate(self.table[-1]):
            if state.is_complete() and state.label == 'S' and index == len(self.setences):
                return True
            
        return False
    
    def __str__(self):
        res = ''
        
        for i, table in enumerate(self.table):
            res += '\nTable[%d]\n' % i
            for state in table:
                res += str(state) + '\n'

        return res
    
    def make_tree(self, state):
        if state.label in self.terminals:
            return Tree(state.label, state.rules)
        
        child = [self.make_tree(child_state) for child_state in [self.get_state_at_index(index) for index in state.made_from]]
        return Tree(state.label, child)
    
    def print_tree(self):
        if not self.has_parsed():
            return
        
        start_state = self.table[-1][-1]
        
        parse_tree = self.make_tree(start_state)
        parse_tree.pretty_print()
        
def parse(document, grammar):
    adjs, nouns, verbs, det, preps = get_word_dictionary()
    # don't change anything below this line
    grammar['a'] = adjs
    grammar['n'] = nouns
    grammar['v'] = verbs
    grammar['d'] = det
    grammar['p'] = preps
    grammar['aux'] = ['do', 'does', 'did', 'had', 'have', 'has']
    # define what are terminal
    terminals = ['d', 'n', 'v', 'a', 'aux', 'p']
    
    # simple preprocessor
    setence = document.split(" ")
    
    # run parsing test
    earley = Earley(setence, grammar, terminals)
    successful = earley.parse()
    
    # print out the result
    if successful:
        print(earley)
        earley.print_tree()
    else:
        print("Invalid state with provided grammar")