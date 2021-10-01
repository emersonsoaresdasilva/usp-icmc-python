from start_spacy import *

tokens_lemmas = [token.lemma_ for token in doc if token.pos_ == 'VERB']

print(f'{tokens_lemmas}')