# banco_de_dados.py
from sqlalchemy import create_engine, and_, func
from sqlalchemy.orm import sessionmaker
from models import Base, Carro  # Importe Base e Carro de models
from carrega_dados import gerar_lista_carros


# Configuração do banco de dados SQLite
engine = create_engine('sqlite:///carros.db')
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Criando objetos Carro a partir da lista apenas se estiver vazio
if session.query(Carro).count() == 0:
    carros = gerar_lista_carros()
    objetos_carros = [Carro(**carro) for carro in carros]
    session.add_all(objetos_carros)
    session.commit()

def consultar_carros(marca, modelo, ano_minimo, ano_maximo, tipo_de_combustivel, preco_minimo, preco_maximo, cor):
    
    # Criar uma lista para armazenar os filtros dinamicamente
    filtros = []

    if marca:
        # filtros.append(Carro.marca == marca)
        filtros.append(func.lower(Carro.marca).ilike(func.lower(marca)))

    if modelo:
        # filtros.append(Carro.modelo == modelo)
        filtros.append(func.lower(Carro.modelo).ilike(func.lower(modelo)))

    if ano_minimo:
        filtros.append(Carro.ano >= ano_minimo)

    if ano_maximo:
        filtros.append(Carro.ano <= ano_maximo)

    if tipo_de_combustivel:
        # filtros.append(Carro.tipo_de_combustível <= tipo_de_combustivel)
        filtros.append(func.lower(Carro.tipo_de_combustível).ilike(func.lower(tipo_de_combustivel)))

    
    if preco_minimo:
        filtros.append(Carro.preco >= preco_minimo)

    if preco_maximo:
        filtros.append(Carro.preco <= preco_maximo)
    
    if cor:
        #filtros.append(Carro.cor == cor)
        filtros.append(func.lower(Carro.cor).ilike(func.lower(cor)))


    carros_encontrados = session.query(Carro).filter(and_(*filtros)).all()
    resultado = []
    for carro in carros_encontrados:
        resultado.append({
            'id': carro.id,
            'marca': carro.marca,
            'modelo': carro.modelo,
            'ano': carro.ano,  
            'cor': carro.cor,
            'tipo': carro.tipo_de_combustível,
            'quilometragem': carro.quilometragem,
            'preco': carro.preco
        })
    
    return resultado

def consultar_carros_por_atributos(marca=None, modelo=None):
    """
    Consulta carros no banco de dados SQLite com base em múltiplos filtros.

    Args:
        session (Session): Sessão do SQLAlchemy.
        marca (str, optional): A marca do carro a ser consultada.
        modelo (str, optional): O modelo do carro a ser consultado.
        ano_min (int, optional): O ano mínimo do carro.
        ano_max (int, optional): O ano máximo do carro.
        tipo_combustivel (str, optional): O tipo de combustível do carro.
        preco_min (float, optional): O preço mínimo do carro.
        preco_max (float, optional): O preço máximo do carro.

    Returns:
        list: Uma lista de dicionários contendo as informações dos carros encontrados.
    """
    query = session.query(Carro)

    if marca:
        query = query.filter(Carro.marca == marca)
    if modelo:
        query = query.filter(Carro.modelo == modelo)
    

    carros_encontrados = query.all()

    resultado = []
    for carro in carros_encontrados:
        resultado.append({
            'marca': carro.marca,
            'modelo': carro.modelo,
            'ano': carro.ano,
            'cor': carro.cor,
            'quilometragem': carro.quilometragem,
            'preco': carro.preco
        })
    
    return resultado