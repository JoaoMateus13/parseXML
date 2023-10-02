from tratamento import Tratamento




data_dict = {}


preProcessamento = Tratamento('verbetesWikipedia.xml')


preProcessamento.removerStopWord()





for page in root.findall('page'):
    # Acesse os elementos dentro de cada página
    page_id = page.find('id').text
    page_title = page.find('title').text
    page_text = page.find('text').text

    data_dict[page_id] = {'title': page_title, 'text': page_text}
