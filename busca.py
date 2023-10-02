import xml.etree.cElementTree as ET

arquivo = "verbetesWikipedia.xml"
tree = ET.parse(arquivo)



root = tree.getroot()


for page in root.findall('page'):
    # Acesse os elementos dentro de cada página
    page_id = page.find('id').text
    title = page.find('title').text
    text = page.find('text').text


    print(page_id)
    print(title)
    print('text')
    print("=" * 50)
