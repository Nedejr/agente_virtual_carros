import json
from requisicao_mcp import fazer_requisicao_mcp


def agente_virtual():

    print("\n\n### AGENTE VIRTUAL - CARROS ###")

    while True:

        resposta = input("\n\nOlá, Como posso ajudar? ")
        if ("procurando" in resposta.lower()
            or "procurar" in resposta.lower()
            or "procuro" in resposta.lower()
            or "carro" in resposta.lower()
            or "veículo" in resposta.lower()
            or "veiculo" in resposta.lower()):

            print("\n\nÓtimo! Vou precisar de algumas informações para encontrar o veículo ideal.")
            marca = input("Qual marca do veículo você procura?: ")
            modelo = input("Qual modelo específico você deseja? (ou pressione Enter para qualquer modelo): ")
            ano_min = input("Ano mínimo do veículo? (ou pressione Enter para ignorar): ")
            ano_max = input("Ano máximo do veículo? (ou pressione Enter para ignorar) :")
            tipo_de_combustivel = input("Qual tipo de combustível? (Gasolina, Diesel, Etanol, Flex, etc.): ")
            preco_min = input("Preço mínimo? (ou pressione Enter para ignorar): ")
            preco_max = input("Preço máximo? (ou pressione Enter para ignorar): ")
            cor = input("Qual cor específico você deseja? (ou pressione Enter para ignorar): ")

            print("\nObrigado! Buscando veículos com os seguintes critérios:")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo if modelo else ''}")
            print(f"Ano: {ano_min if ano_min else ''} - {ano_max if ano_max else ''}")
            print(f"Combustível: {tipo_de_combustivel if tipo_de_combustivel else ''}")
            print(f"Faixa de preço: {preco_min if preco_min else ''} - {preco_max if preco_max else ''}")
            print(f"Cor: {cor}")
            print("\n\nPesquisando...")

            payload = {
                "marca": str(marca),
                "modelo": str(modelo) if modelo else "",
                "ano_minimo": int(ano_min) if ano_min else "",
                "ano_maximo": int(ano_max) if ano_max else "",
                "tipo_de_combustivel": str(tipo_de_combustivel) if tipo_de_combustivel else "",
                "preco_minimo": float(preco_min) if preco_min else "",
                "preco_maximo": float(preco_max) if preco_max else "",
                "cor": str(cor),
            }
            conectar_no_serivodr_mcp(payload)

        continuar = input("\n\nDeseja continuar? (s/n): ")
        if continuar.lower() != 's':
            print("\n\nObrigado por usar o ### AGENTE VIRTUAL - CARROS ###. Até logo!")
            break


def conectar_no_serivodr_mcp(payload):

    url_servidor_mcp = "http://localhost:8080/mcp"
    payload_requisicao = {
        "tool_name": "consultar_carros",
        "tool_input": payload
    }
    resposta_mcp = fazer_requisicao_mcp(url_servidor_mcp, payload_requisicao)
    if resposta_mcp:
        carros_encontrados = resposta_mcp['resultados']
        if carros_encontrados:
            print(f"Veículos encontrados: {len(carros_encontrados)} veículos(s)")
            print(json.dumps(carros_encontrados, indent=4))
        else:
            print("Nenhum veículo encontrado com o filtro selecionado")


if __name__ == '__main__':
    agente_virtual()
