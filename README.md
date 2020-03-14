# cbf-bid-scrapper
Scrapper do BID do site da CBF

### Como usar?

```python

from scrapper.scrapper import buscar_dados_bid

registros = buscar_dados_bid('AL', '13/03/2020')

for registro in registros:
    print(registro)

```
