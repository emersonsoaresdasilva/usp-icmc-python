import nltk
from nltk.tokenize import RegexpTokenizer

# Tokenizar é separar as palavras do texto.
text = 'O jogador, que está de camisa verde, marcou o gol da vitória!'

# Retorna os tokens.
def token(text):
    return nltk.word_tokenize(text)

# Retorna apenas os tokens sem pontuação.
def token_accent(text):
    tokenizer = RegexpTokenizer(r'\w+') # Sem numerais = RegexpTokenizer(r'[A-z]\w*')
    return tokenizer.tokenize(text)

# Conta ocorrências de tokens pelo NLTK.
def token_frequency(text):
    frequency = nltk.FreqDist(letter.lower() for letter in text) # Considera letras MAIÚSCULAS e minúsculas como iguais.
    return frequency.most_common()

# Stopwords: Artigos, preposições e conjunções.
def token_portuguese():
    return nltk.corpus.stopwords.words('portuguese')

# Stopwords: Frequência dos tokens sem stopwords.
def token_frequency_without_stopwords(text):
    tokenizer = RegexpTokenizer(r'[A-z]\w*')
    tokens = tokenizer.tokenize(text)
    stopwords = nltk.corpus.stopwords.words('portuguese')
    tokens_without_stopwords = [letter.lower() for letter in tokens if letter not in stopwords]
    frequency = nltk.FreqDist(tokens_without_stopwords)
    return frequency.most_common()

# Exibe o retorno das funções:
print(f'{token(text)}')
print(f'{token_accent(text)}')
print(f'{token_frequency(text)}')
print(f'{token_portuguese()}')
print(f'{token_frequency_without_stopwords(text)}')