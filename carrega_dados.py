import random


def gerar_lista_carros():

    marcas = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "Hyundai", "Nissan", "BMW", "Mercedes-Benz", "Fiat"]
    modelos = {
        "Toyota": ["Corolla", "Camry", "RAV4", "Hilux", "Yaris"],
        "Honda": ["Civic", "CR-V", "HR-V", "Fit", "City"],
        "Ford": ["Focus", "Fiesta", "EcoSport", "Ranger", "Mustang"],
        "Chevrolet": ["Onix", "Prisma", "S10", "Tracker", "Cruze"],
        "Volkswagen": ["Gol", "Polo", "Virtus", "T-Cross", "Amarok"],
        "Hyundai": ["HB20", "Creta", "Tucson", "HB20S", "i30"],
        "Nissan": ["March", "Versa", "Kicks", "Frontier", "Sentra"],
        "BMW": ["Série 3", "Série 5", "X1", "X3", "i3"],
        "Mercedes-Benz": ["Classe C", "Classe E", "GLC", "Classe A", "CLA"],
        "Fiat": ["Palio", "Uno", "Strada", "Toro", "Argo"],
    }
    motores = ["1.0", "1.4", "1.6", "1.8", "2.0", "2.0 Turbo", "3.0 V6"]
    combustiveis = ["Gasolina", "Etanol", "Flex", "Diesel"]
    cores = ["Branco", "Preto", "Prata", "Vermelho", "Azul", "Cinza"]
    cambios = ["Manual", "Automático"]

    lista_de_carros = []

    for i in range(1, 101):
        marca_selecionada = random.choice(marcas)
        modelo_selecionado = random.choice(modelos[marca_selecionada])
        ano_fabricacao = random.randint(2010, 2025)
        motor_selecionado = random.choice(motores)
        combustivel_selecionado = random.choice(combustiveis)
        cor_selecionada = random.choice(cores)
        quilometragem_atual = random.randint(0, 200000)
        portas = random.choice([2, 4])
        cambio_selecionado = random.choice(cambios)
        preco_selecionado = round(random.uniform(30000, 150000), 2)
        observacao_aleatoria = ""
        if random.random() < 0.3:  # 30% de chance de ter uma observação
            observacoes_possiveis = ["Único dono", "Revisões em dia", "IPVA pago", "Nunca batido", "Bancos de couro"]
            observacao_aleatoria = random.choice(observacoes_possiveis)

        carro = {
            
            "marca": marca_selecionada,
            "modelo": modelo_selecionado,
            "ano": ano_fabricacao,
            "motor": motor_selecionado,
            "tipo_de_combustível": combustivel_selecionado,
            "cor": cor_selecionada,
            "quilometragem": quilometragem_atual,
            "numero_portas": portas,
            "cambio": cambio_selecionado,
            "observacao": observacao_aleatoria,
            "preco": preco_selecionado
        }
        lista_de_carros.append(carro)

    # O resultado 'lista_de_carros' contém 100 dicionários, cada um representando um carro
    # com os campos especificados.
    # Você pode imprimir a lista ou usá-la para popular seu banco de dados.
    # print(json.dumps(lista_de_carros, indent=4)) # Descomente para imprimir a lista formatada em JSON

    return lista_de_carros

