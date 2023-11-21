import json

caminho_arquivo_desorganizado = 'recommendation_sys/taco_data_test.json'
caminho_arquivo_organizado = 'recommendation_sys/grupos.json'


# Leitura dos dados desorganizados do arquivo JSON
with open(caminho_arquivo_desorganizado, 'r', encoding='utf-8') as file:
    dados_desorganizados = json.load(file)



# Organização dos dados por grupo
dados_organizados = {}
id_counter = 1 
for item in dados_desorganizados:
    grupo = item['grupo']
    if grupo not in dados_organizados:
        dados_organizados[grupo] = {
            'id': id_counter,
            'name': grupo,
            'items': []
        }
        id_counter += 1

    dados_organizados[grupo]['items'].append({
        'code': item['code'],
        'name': item['name'],
        "homemadePortion": "1, Unidade"
    })




# Conversão do dicionário para uma lista
dados_organizados_lista = list(dados_organizados.values())



# Salvando os dados organizados em um novo arquivo JSON
with open(caminho_arquivo_organizado, 'w', encoding='utf-8') as file:
    json.dump(dados_organizados_lista, file, ensure_ascii=False, indent=2)
