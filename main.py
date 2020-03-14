from scrapper.scrapper import buscar_dados_bid

registros = buscar_dados_bid('AL', '13/03/2020')

print('jogador,operacao,data_publicacao,clube')

for registro in registros:
    print("{};{};{};{}".format(registro['jogador'], registro['operacao'], registro['publicacao'], registro['clube']))
