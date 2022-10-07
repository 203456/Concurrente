from automata.fa.gnfa import GNFA
from pdfReader import pdfReaderfun




# GNFA which matches strings beginning with 'a', ending with 'a', and containing
# no consecutive 'b's
gnfa = GNFA(
    states={'q_in','q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26'},
    input_symbols={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' 'V', 'W', 'X', 'Y', 'Z',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' 'w', 'x', 'y', 'z',
       '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'á','é', 'í', 'ó', 'ú',
       ',', '.', '-', '/', '(', ')', '"', '&', '!', '¡', '¿', '?', '=','#', '(Vol.', },
    transitions={
        'q0': {'q1': 'a',  'q_f': None, 'q2': None, 'q0': None},
        'q1': {'q1': 'a', 'q2': '', 'q_f': '', 'q0': None},
        'q2': {'q0': 'b', 'q_f': None, 'q2': None, 'q1': None},
        'q_in': {'q0': '', 'q_f': None, 'q2': None, 'q1': None}
    },
    initial_state='q_in',
    final_state='q22, q26'
)

pdfReaderfun()
