import requests
import json


def fazer_requisicao_mcp(url, payload):
    """
    Realiza uma requisição MCP para a URL especificada com o payload fornecido.

    Args:
        url (str): A URL do servidor MCP.
        payload (dict): O payload da requisição no formato JSON.

    Returns:
        dict: A resposta do servidor MCP como um dicionário Python.
        None: Se ocorrer um erro durante a requisição.
    """
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição MCP: {erro}")
        return None