from start_spacy import *

tokens = [token for token in doc]
tokens_string = [token.orth_ for token in doc]
tokens_alpha = [token .orth_ for token in doc if token.is_alpha]
tokens_numbers = [token .orth_ for token in doc if token.is_digit]
tokens_puncnts = [token .orth_ for token in doc if token.is_punct]

print(f'{tokens}')
print(f'{tokens_string}')
print(f'{tokens_alpha}')
print(f'{tokens_numbers}')
print(f'{tokens_puncnts}')