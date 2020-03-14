import requests
from bs4 import BeautifulSoup

_CABECALHOS_ = {
    'Host': 'bid.cbf.com.br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5' ,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://bid.cbf.com.br',
    'Referer': 'https://bid.cbf.com.br/',
    'Cookie': 'PHPSESSID=hsbi4vn5m29bj54ii3rsncvoh2',
    'Connection': 'keep-alive',
    'Content-Length': '85'
}

def buscar_dados_bid(uf, data_publicacao):
    dados = {
        'uf': uf,
        'dt_pesquisa': data_publicacao,
        'tp_contrato': 'TODOS',
        'n_atleta': '',
        'codigo_clube': '',
        'exercicio': ''
    }

    response = requests.post('https://bid.cbf.com.br/a/bid/carregar/json/', data = dados, headers = _CABECALHOS_)

    if not (response.status_code == 200) or response.text == '':
        raise Exception('Could not retrieve data')

    response_json = response.json()

    bs = BeautifulSoup(response_json['dados'], features="html.parser")

    registros = []

    for nodo_jogador in bs.select('h1.nameplayer'):
        nodos_dados = nodo_jogador.parent.parent.parent.select('.box')

        registros.append(
            {
                'jogador': nodo_jogador.text,
                'operacao': nodos_dados[0].text,
                'publicacao': nodos_dados[1].text,
                'clube': nodos_dados[2].text,
            }
        )

    return registros
