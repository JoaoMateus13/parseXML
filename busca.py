import xml.etree.cElementTree as ET

arquivo = "verbetesWikipedia.xml"
tree = ET.parse(arquivo)



root = tree.getroot()

cache = {}

data_dict = {}

"""
# Função para remover stopwords
def removerStopWord(palavras, caminho):

    stopwords_file = caminho
    with open(stopwords_file, "r", encoding="utf-8") as f:
        stopwords = [linha.strip() for linha in f]

    result = []
    for palavra in palavras:
        if palavra not in stopwords:
            result.append(palavra)
    return result

# Itere sobre as páginas
for page in root.findall('page'):
    text_element = page.find('text')
    if text_element is not None:
        text = text_element.text

        palavras = text.split()


        palavras_sem_stopwords = removerStopWord(palavras, 'stoplist-ingles.txt')

        novo_texto = ' '.join(palavras_sem_stopwords)
        text_element.text = novo_texto

# Salve o XML modificado
tree.write("verbetesWikipedia_sem_stopwords.xml")"""

keyword = ''
while True:
    busca = input("Digite a busca: ").lower()
    if busca not in cache:
        keyword = busca
        for page in root.findall('page'):

            # Acesse os elementos dentro de cada página
            page_id = page.find('id').text
            page_title = page.find('title').text
            page_text = page.find('text').text
        
            keyword_count = page_text.lower().count(keyword)


            data_dict[page_id] = {'title': page_title, 'text': page_text, 'keyword': keyword_count}

        elementosOrdenados = dict(
            sorted(data_dict.items(), key=lambda x: x[1]['keyword'], reverse=True))

        cache[keyword] = list(elementosOrdenados.items())

    else:
        primeiro_elemento = cache[busca][0]

        if (primeiro_elemento[1]['keyword'] == 0):
            print("NÃO TEM NADA COM ISSO AI OH")
            print(primeiro_elemento[0], primeiro_elemento[1]['keyword'] == 0)
            cache.pop(busca)

        else:
            print(primeiro_elemento[0], primeiro_elemento[1]['title'], primeiro_elemento[1]['keyword'])

