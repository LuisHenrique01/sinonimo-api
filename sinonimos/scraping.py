import requests as rs
from bs4 import BeautifulSoup as bs

def buscar_sinonimo(palavra: str) -> list:
    try:
        palavra = palavra.lower()
        response = rs.get(f'https://www.dicio.com.br/{palavra}/')
        soup = bs(response.text, 'html.parser')
        sinonimos = soup.find('p', class_="adicional sinonimos").text
        sinonimos = sinonimos.strip().split('\n')[1].split(', ')
        return sinonimos
    except AttributeError:
        return []     

def retorna_sinonimos(palavras: str) -> dict:
    sinonimos = {}
    if '+' in palavras:
        palavras = palavras.split('+')
    else:
        palavras = palavras.split()
    for palavra in palavras:
        sinonimos[palavra] = buscar_sinonimo(palavra)
    return sinonimos