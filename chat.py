# parseXML
import itertools
import string
import xml.etree.cElementTree as ET

arquivo = "verbetesWikipedia.xml"
tree = ET.parse(arquivo)


root = tree.getroot()

cache = {}


parseCompleto = {}

i = 1
palavras_encontradas = set()
for page in root.findall('page'):

    # Acesse os elementos dentro de cada página
    page_id = page.find('id').text
    page_title = page.find('title').text.lower()
    page_text = page.find('text').text.lower()

    # pega o titulo e o texto da page
    palavras = page_title.split() + page_text.split()
    for palavra in palavras:
        # verifica se é uma palavra maior que 4 caracteres e se a palavra é composta por letras
        if len(palavra) > 4 and palavra.isalpha():
            palavras_encontradas.add(palavra)

print(len(palavras_encontradas))

# ordena em ordem alfabetica
lista = sorted(list(palavras_encontradas))

# delimita a quantidade de palavras para ser armazenado em hash
primeiros_10000 = set(itertools.islice(lista, 100000))

for palavra in primeiros_10000:
    if palavra not in parseCompleto:
        data_dict = {}
        # delimita a quantidade de pagina que ele vai verificar a ocorrencia da palavra
        for page in itertools.islice(root.findall('page'), 5):

            # Acesse os elementos dentro de cada página
            page_id = page.find('id').text
            page_title = page.find('title').text
            page_text = page.find('text').text

            # conta a quantidade de ocorrencia da palavra no titulo/texto e calculando os pesos
            keyword_count = page_text.lower().count(
                palavra)*10 + page_title.lower().count(palavra)*20

            # cria um dicionario da pagina com o número de pontos feitos pela ocorrencia daquela palavra
            # só é criado se tiver ocorrencia da palavra naquela pagina
            if keyword_count > 0:
                data_dict[page_id] = {
                    'page_id': page_id, 'title': page_title, 'text': page_text, 'keyword': keyword_count}

        lista_de_dicionarios = list(data_dict.values())

        # Ordene a lista de dicionários por 'keyword'
        elementos_ordenados = sorted(
            lista_de_dicionarios, key=lambda x: x['keyword'], reverse=True)

        # Armazene elementos_ordenados em parseCompleto
        parseCompleto[palavra] = elementos_ordenados
        print("completo" + str(i))
        i += 1


while True:
    busca = input("Digite a busca: ").lower()


    #A frase é divida em um vetor
    buscaComposta = busca.split()

    if len(buscaComposta) > 1:

        #elementos únicos
        elementos_info = set()
        ids_verificados = set()  #IDs já verificados
        keyword_count_soma = {}
        #Itera em cada palavra da frase
        for i in buscaComposta:
            #Verifica se existe tem a palavra na tabela hash 
            if i in parseCompleto:
                #Pega um elemento da lista Ordenada por ocorrecia da palavra
                for elemento in parseCompleto[i]:
                    page_data = elemento

                    page_id = page_data.get('page_id', '')
                    keyword_count = page_data.get('keyword', '')

                    if page_id in ids_verificados:
                        keyword_count_soma[page_id] += keyword_count
                    # Verifique o ID
                    #Garante que não vai aparece a mesma pagina quando na mesma tiver mais de uma palavra buscada
                    else:
                        ids_verificados.add(page_id)
                        keyword_count_soma[page_id] = keyword_count
                        # Converta para tupla para torná-los imutáveis
                        elemento_tuple = tuple(elemento.items())
                        elementos_info.add(elemento_tuple)

                        # Acesse os dados do dicionário
                        title = page_data.get('title', '')
                        text = page_data.get('text', '')
                        #keyword_count = page_data.get('keyword', '')
                        print("----------------------------")
                        print(f"Page ID: {page_id}")
                        print(f"Title: {title}")
                       # print(f"Text: {text}")
                        print(f"Keyword Count: {keyword_count_soma[page_id]}")
                        print("----------------------------")
            else:
                print("Busca não encontrada. Tente novamente.")

    if len(buscaComposta) == 1:
        if busca in parseCompleto:
            for elemento in parseCompleto[busca]:
                page_data = elemento

                page_id = page_data.get('page_id', '')
                title = page_data.get('title', '')
                text = page_data.get('text', '')
                keyword_count = page_data.get('keyword', '')
                print("----------------------------")
                print(f"Page ID: {page_id}")
                print(f"Title: {title}")
                # print(f"Text: {text}")
                print(f"Keyword Count: {keyword_count}")
                print("----------------------------")
        else:
            print("Busca não encontrada. Tente novamente.")
