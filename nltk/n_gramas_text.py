import nltk
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams
from nltk.tokenize import RegexpTokenizer

# Brigramas.
text = '''
        Com um passe de Eli Manning para Plaxico Burress a 39 segundos do fim,
        o New York Giants anotou o touchdown decisivo e derrubou o favorito New England
        Patriots por 17 a 14 neste domingo, em Glendale, no Super Bowl XLII. O resultado,
        uma das maiores zebras da história do Super Bowl, acabou com a temporada perfeita
        de Tom Brady e companhia, que esperavam fazer história ao levantar o troféu da NFL
        sem sofrer uma derrota no ano.
        '''

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)

def text_bigrams(text):
    return list(bigrams(tokens)) # Já com o texto tokenizado

def text_trigrams(text):
    return list(trigrams(tokens))

def text_ngrams(text):
    return list(ngrams(tokens, 4)) # Testando com 4-gram

print(f'{text_bigrams(text)}')
print(f'{text_trigrams(text)}')
print(f'{text_ngrams(text)}')