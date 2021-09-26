import nltk

# STEMMING: Consiste em reduzir a palavra ao seu radical.
# amig: amigo, amiga, amigão
# gat: gato, gata, gatos
# prop: propõem, propuseram, propondo

# LEMATIZAÇÃO: Consiste em reduzir a palavra à sua forma canônica, levando em conta sua classe gramatical.
# propor: propõem, propuseram, propondo
# estudar: estudando, estudioso, estudei

# RSLP - Removedor de Sufixos da Língua Portuguesa
words = ['amigão', 'amigo', 'propuseram', 'propõem', 'propondo']

def remove_suffixes_from_words(words):
    stemmer = nltk.RSLPStemmer()
    for word in words:
        print(f'{stemmer.stem(word)}')

remove_suffixes_from_words(words)

# Infelizmente o NLTK ainda não tem um lematizador para o Português bom o bastante.
# Tentativa: WordNetLemmatizer → Funciona somente para o inglês...

words = ['studied', 'studying', 'sings']

def lemmatizer(words):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    for word in words:
        print(f'{lemmatizer.lemmatize(word, pos="v")}')

lemmatizer(words)