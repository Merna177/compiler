from .LexicalAnalyzer import LexicalAnalyzer
from .getInput import read_input
from .NFA import convert_regex_to_nfa, definitions_to_nfa, combine_nfas
from .DFA import nfa_to_dfa
from .DFAminimization import minimize
class LexicalAnalyzerGenerator:
    """
    Factory class that is instantiated to create a Lexical Analyzer object and encapsulates the whole creation process
    """

    def __init__(self):
        self.NFAs = []
        self.rules = {}
        # use the functions defined outside
        self.read_input_file = read_input()
        self.regex_to_nfa = convert_regex_to_nfa()
        self.def_to_nfa = definitions_to_nfa()
        self.combine = combine_nfas()
        self.nfa_to_dfa = nfa_to_dfa()
        self.minimize_dfa = minimize()


    def make_transition_table(self):
        print("TODO")
        tt= None
        return tt

    def make_lexical_analyzer(self,min_dfa):
        print("call lexical analyzer class constructor and return and object")
        la=LexicalAnalyzer()
        return la

    def generate(self,input_file):
        regex, rest= self.read_input_file(input_file)
        nfa_rest = self.def_to_nfa(rest)
        nfa = self.regex_to_nfa(regex, rest)
        combined_nfa = self.combine([nfa_rest , nfa])
        dfa = self.nfa_to_dfa(combined_nfa)
        min_dfa = self.minimize_dfa(dfa)
        lex_analyzer = self.make_lexical_analyzer(min_dfa)
        trans_table = self.make_transition_table()

        return lex_analyzer,trans_table




if __name__ == '__main__':
    # for testing only, then all those functions will be incapsulated in one
    input_file = "rules.txt"
    LAG = LexicalAnalyzerGenerator()
    regex , rest= LAG.read_input_file(input_file)
    nfa_rest = LAG.def_to_nfa(rest)
    nfa = LAG.regex_to_nfa(regex, rest)
    combined_nfa = LAG.combine( [nfa_rest, nfa] )
    dfa = LAG.nfa_to_dfa(combined_nfa)
    min_dfa = LAG.minimize_dfa(dfa)
    # the only line that will actually be used:
    lexical_analyzer, transition_table = LAG.generate(input_file)
