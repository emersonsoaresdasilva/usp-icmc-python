infile = open('qbdata.txt', 'r')
outfile = open('result.txt', 'w')

# Importante: atenção nos parâmetros para abertura de arquivo.

# r = read, ouseja, apenas para leitura do arquivo;
# w = write, ouseja, apenas para escrita no arquivo;
# a = append, ouseja, escrita no final do arquivo.

# Ao final do uso do arquivo, sempre fechá-lo com o comando close().
def content_file():
    print(f'{infile.read()}')

content_file()

def content_file_list():
    print(f'{infile.readlines()}')

content_file_list()

# Escrita em arquivos.
outfile.write('Números de 1 a 10\n')
for i in range(1, 11): # A função range() retorna uma série numérica no intervalo enviado como argumento.
    outfile.write(str(i)+'\n')

# Escrita com append(a).
outfile = open('result.txt', 'a')
outfile.write('Adicionando números de 11 a 20\n')
for i in range(11, 21):
    outfile.write(str(i)+'\n')

# Dado o arquivo qbdata.txt, retorne o rating de cada QB na forma "nome do QB teve valor XX.X"
content = infile.readlines()

def qbdata(content):
    for line in content:
        smash = line.split(" ")
        print(f'Nome do QB: {smash[0]} {smash[1]}\nValor: R$ {smash[-1]}')

# Pensando em uma agenda, construa um dicionário com informações do contato sendo: 
# CPF, nome, telefone e user no Twitter. 
# A ofinal, imprima todos os contatos na forma → CPF: nome, telefone (user)

def dict_person(person):
    print(f'CPF: {person["cpf"]}\nNome: {person["nome"]}\nTwitter: {person["user"]}')
    for telefone in person["telefones"]: print(f'Telefone: {telefone}')

person = {
    'cpf': 86412463037,
    'nome': 'Pedro Henrique',
    'telefones': ['1140042020', '11955639568'],
    'user': 'pedro.henrique'
}

dict_person(person)