import xml.etree.cElementTree as ET


class Tratamento():

    def __init__(self, caminho):
        self.caminho = caminho



    tree = ET.parse(self.caminho)
    root = tree.getroot()


    # Função para remover stopwords

    for page in root.findall('page'):
        text_element = page.find('text')
        if text_element is not None:
            text = text_element.text

            palavras = text.split()



    def removerStopWord(palavras, caminhoStop):

        stopwords_file = caminhoStop
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

            palavras_sem_stopwords = removerStopWord(
                palavras, 'stoplist-ingles.txt')

            novo_texto = ' '.join(palavras_sem_stopwords)
            text_element.text = novo_texto

    # Salve o XML modificado
    tree.write("verbetesWikipedia_sem_stopwords.xml")
