1. A busca é dividida em palavras individuais e armazenada em uma lista chamada buscaComposta usando busca.split().

2. O código verifica se a busca contém mais de uma palavra (ou seja, o comprimento da lista buscaComposta é maior que 1).

3. Se a busca contiver várias palavras, o código inicia um processamento mais complexo.

4. Ele define algumas estruturas de dados, como elementos_info, ids_verificados e keyword_count_soma para rastrear informações relevantes sobre as páginas que correspondem à busca.

5. O código itera sobre cada palavra na busca (for i in buscaComposta:) e verifica se essa palavra está presente em uma tabela hash chamada parseCompleto. A variável parseCompleto  é um dicionário onde apresenta a ordem decrescente de ocorrencia da palavra buscada.

6. Se a palavra da busca estiver presente no parseCompleto, imprime na tela.

7. Não é imprimido a pagina mais de uma vez (EX: se a pagina tiver computer e science, vai imprimir para "computer" mas não vai imprimir quando passar por "science")
