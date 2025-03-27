# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import random

'''
Modelagem de Dados
Crie um esquema para representar automóveis com, no mínimo, 10 atributos
relevantes. Fique à vontade para incluir dados como marca, modelo, ano,
motorização, tipo de combustível, cor, quilometragem, número de portas,
transmissão, entre outros.
'''

Base = declarative_base()

class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    motor = Column(String)
    tipo_de_combustível = Column(String)
    cor = Column(String)
    quilometragem = Column(Integer)
    preco = Column(Float)  
    numero_portas = Column(Integer)
    cambio = Column(String)
    observacao = Column(String)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.cor}, {self.preco} - {self.motor}, {self.tipo_de_combustível}, {self.observacao}"