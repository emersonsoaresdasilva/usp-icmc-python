import spacy

texto = 'A maioria das pessoas que adoece em decorrência da COVID-19 apresenta sintomas leves a moderados e se recupera sem tratamento especial. No entanto, algumas desenvolvem um quadro grave e precisam de atendimento médico.'

nlp = spacy.load('pt_core_news_lg')
doc = nlp(texto) # O texto não tokens!

# IMPORTANTE: no NLTK era utilizado semprea lista de tokens, mas aqui no spaCy, o parâmetro é sempre a string do texto.