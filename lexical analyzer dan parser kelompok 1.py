print("TUGAS BESAR BAHASA AUTOMATA | KELOMPOK 1 | IF4310")
print("========LEXICAL ANALYZER=========")

import string

#input example
#sentence = 'brother wear hat'
#input_string = sentence.lower()+'#'


def lexical(sentence):

    #initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
        transition_table[(state, "#")] = "error"
        transition_table[(state, " ")] = "error"

    #start state
    transition_table["q0", " "] = "q0"

    #finish state
    transition_table[("q28", "#")] = "accept"
    transition_table[("q28", " ")] = "q29"

    transition_table[("q29", "#")] = "accept"
    transition_table[("q29", " ")] = "q29"

    #string brother
    transition_table[("q0", "b")] = "q10"
    transition_table[("q10", "r")] = "q11"
    transition_table[("q11", "o")] = "q12"
    transition_table[("q12", "t")] = "q13"
    transition_table[("q13", "h")] = "q14"
    transition_table[("q14", "e")] = "q15"
    transition_table[("q15", "r")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "b")] = "q10"

    #string sister
    transition_table[("q0", "s")] = "q16"
    transition_table[("q16", "i")] = "q17"
    transition_table[("q17", "s")] = "q18"
    transition_table[("q18", "t")] = "q14"
    transition_table[("q14", "e")] = "q15"
    transition_table[("q15", "r")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "s")] = "q16"

    #string you
    transition_table[("q0", "y")] = "q4"
    transition_table[("q4", "o")] = "q7"
    transition_table[("q7", "u")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "y")] = "q4"

    #string read
    transition_table[("q0", "r")] = "q25"
    transition_table[("q25", "e")] = "q26"
    transition_table[("q26", "a")] = "q27"
    transition_table[("q27", "d")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "r")] = "q25"

    #string eat
    transition_table[("q0", "e")] = "q24"
    transition_table[("q24", "a")] = "q23"
    transition_table[("q23", "t")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "e")] = "q24"

    #string wear
    transition_table[("q0", "w")] = "q1"
    transition_table[("q1", "e")] = "q2"
    transition_table[("q2", "a")] = "q3"
    transition_table[("q3", "r")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "w")] = "q1"

    #string book
    transition_table[("q0", "b")] = "q10"
    transition_table[("q10", "o")] = "q8"
    transition_table[("q8", "o")] = "q9"
    transition_table[("q9", "k")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "b")] = "q10"

    #string shoes
    transition_table[("q0", "s")] = "q16"
    transition_table[("q16", "h")] = "q19"
    transition_table[("q19", "o")] = "q20"
    transition_table[("q20", "e")] = "q21"
    transition_table[("q21", "s")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "s")] = "q16"

    #string tofu
    transition_table[("q0", "t")] = "q5"
    transition_table[("q5", "o")] = "q6"
    transition_table[("q6", "f")] = "q7"
    transition_table[("q7", "u")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "t")] = "q5"

    #string hat
    transition_table[("q20", "h")] = "q22"
    transition_table[("q22", "a")] = "q23"
    transition_table[("q23", "t")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "h")] = "q22"

    #lexical analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q28': 
            print('current token: ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print("error")
            break
        idx_char = idx_char + 1

    #conclusion
    if state == "accept":
        print('semua token diinput: ', sentence, ', valid')
    
    return lexical

#Gian Maxmillian Firdaus (1301190209),Rahmatia Primadiati (1301194091),Zakia Syahrini (1301194108)(IF4310)
def parser(sentence):
    print("==========PARSER========== \n")
    print("=========KELOMPOK 1======= \n")

    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'NN', 'VB', 'OB']
    terminals = ['brother', 'sister', 'you', 'book', 'shoes', 'tofu', 'hat', 'read', 'eat', 'wear']

    parse_table = {}

    parse_table[('S', 'brother')] = ['NN', 'VB', 'OB']
    parse_table[('S', 'sister')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'you')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'read')] = ['error']
    parse_table[('S', 'eat')] = ['error'] 
    parse_table[('S', 'wear')] = ['error'] 
    parse_table[('S', 'book')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'shoes')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'tofu')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'hat')] = ['NN', 'VB', 'OB'] 
    parse_table[('S', 'EOS')] = ['error'] 

    parse_table[('NN', 'brother')] = ['brother']
    parse_table[('NN', 'sister')] = ['sister']  
    parse_table[('NN', 'you')] = ['you'] 
    parse_table[('NN', 'read')] = ['error'] 
    parse_table[('NN', 'eat')] = ['error'] 
    parse_table[('NN', 'wear')] = ['error'] 
    parse_table[('NN', 'book')] = ['error'] 
    parse_table[('NN', 'shoes')] = ['error'] 
    parse_table[('NN', 'tofu')] = ['error'] 
    parse_table[('NN', 'hat')] = ['error'] 
    parse_table[('NN', 'EOS')] = ['error'] 
    
    parse_table[('VB', 'brother')] = ['error']
    parse_table[('VB', 'sister')] = ['error']
    parse_table[('VB', 'you')] = ['error']
    parse_table[('VB', 'read')] = ['read'] 
    parse_table[('VB', 'eat')] = ['eat'] 
    parse_table[('VB', 'wear')] = ['wear'] 
    parse_table[('VB', 'book')] = ['error'] 
    parse_table[('VB', 'shoes')] = ['error'] 
    parse_table[('VB', 'tofu')] = ['error'] 
    parse_table[('VB', 'hat')] = ['error'] 
    parse_table[('VB', 'EOS')] = ['error'] 

    parse_table[('OB', 'brother')] = ['error']
    parse_table[('OB', 'sister')] = ['error']
    parse_table[('OB', 'you')] = ['error']
    parse_table[('OB', 'read')] = ['read'] 
    parse_table[('OB', 'eat')] = ['eat'] 
    parse_table[('OB', 'wear')] = ['wear'] 
    parse_table[('OB', 'book')] = ['book'] 
    parse_table[('OB', 'shoes')] = ['shoes']
    parse_table[('OB', 'tofu')] = ['tofu'] 
    parse_table[('OB', 'hat')] = ['hat'] 
    parse_table[('OB', 'EOS')] = ['error'] 
    

    stack = []
    stack.append('#')
    stack.append('S')

    index_token = 0
    symbol = tokens[index_token]

    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('top = ', top)
        print('symbol = ', symbol)
        if top in terminals:
            print('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('isi stack:', stack)
            else:
                print('error')
                break;
        elif top in non_terminals:
            print('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                print('error')
                break;
        else:
            print('error')
            break;
        print('isi stack: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('input string ', '"', sentence, '"', 'diterima, sesuai grammar')
    else:
        print('error, input string:', '"', sentence, '"', ', tidak diterima, tidak sesuai grammar')  
    
    return parser

print("terminal: brother, sister, you, read, eat, wear, book, shoes, tofu, hat \n ")
sentence = input("input masukan: ")
input_string = sentence.lower()+'#'
lexical(sentence)
parser(sentence)


