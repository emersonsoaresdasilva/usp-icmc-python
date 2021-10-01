from start_spacy import *

tokens_label_pos = [(token.orth_, token.pos_) for token in doc] # Basta chamar o atributo pos_ no token e assim é retornada a classe gramatical referente.

print(f'{tokens_label_pos}')

# O spaCy tem um atributo que contém informações mais detalhadas: omorph.

tokens_label_morph = [(token.orth_, token.morph) for token in doc]

print(f'{tokens_label_morph}')