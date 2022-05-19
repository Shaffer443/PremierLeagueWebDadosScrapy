<h1>Documentação</h1>
<h4>Atualizada em: 19/05/2022</h4>

**Objetivo:**

<p>Criação de API para captação de determinados dados estatísticos de uma página web, com a premissa de atualização de de web, planilhas e outrso dados estatísticos.</p>

**Bibliotecas | Frameworks**

_Flask_- Ferramenta para criar sites e API's com Python.</br>
_Pandas_- Ferramenta que permite analisar dados</br>
_Scrapy_- Ferramenta de captação de dados web</br>
_json_ - abrindo arquivo json

**Instalações no python**

- pip install flask</br>
- pip install pandas</br>
- pip install scrapy</br>
- pip install json

**Importações**

**Linha de Raciocínio**

**Comandos scrapy**

_Teste de Funcionamento das informações:_

- scrapy crawl dadospremierleague
  
_Criação de arquivos das informações:_

-O (Sobrepõe os dados (caso exista))</br>
-o (Não Sobrepões os dados. Vai adicionando as novas informações)</br>

- scrapy crawl dadospremierleague -o premierleaguedados.csv<br>
- scrapy crawl dadospremierleague -o premierleaguedados.json<br>
- scrapy crawl dadospremierleague -o premierleaguedados.xml<br>

Set a supported one (('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'))

**Comandos Flesk**

1 passo: Inicializar aplicativo (padrão) 

- _app = Flask(___ name ___)_

2 passo: Construir as funionalidades

- @app.route('endereço') - resumidamente, informa em qual link vai estar a página.</br>
exemplo: @app.route('/homepage')</br>
exemplo: @app.route('/contatos')</br>
exemplo: @app.route('/') - Primeira página, assim que abrir.

OBS: Para se tornar uma API precisa-se retornar um dicionário dos dados alvos. A resposta da API precisa ser um dicionário do python.

Logo, precisa-se, no **return**, retornar um dicionário .json (para este caso em questão)

Para tal ação, usaremos o **jsonify**, que tem a função de transformar o _return_ em um dicionário _json_.


3 passo: requisição da API



X passo: rodar a API

- _**app.run()**_

Para usar, rodando dentro doReplit, é sugirod pela página usar o seguinte host:

- _**app.run(host='0.0.0.0')**_

**links**

_Páginas_

- json - https://diegomariano.com/lendo-json-com-python/


_Video_

- scrapy - https://www.youtube.com/watch?v=QdLgNr1mKQU
- flask - https://www.youtube.com/watch?v=WWVEymSt1iI


**Falta Terminar...**