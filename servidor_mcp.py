from flask import Flask, request, jsonify
from database import consultar_carros


app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def mcp_endpoint():
    try:
        payload = request.get_json()
        tool_name = payload.get('tool_name')
        tool_input = payload.get('tool_input')

        if tool_name == 'consultar_carros' and tool_input:
            marca = tool_input['marca']
            modelo = tool_input['modelo']
            ano_minimo = tool_input['ano_minimo']
            ano_maximo = tool_input['ano_maximo']
            tipo_de_combustivel = tool_input['tipo_de_combustivel']
            preco_minimo = tool_input['preco_minimo']
            preco_maximo = tool_input['preco_maximo']
            cor = tool_input['cor']
            carros_encontrados = consultar_carros(marca, modelo, ano_minimo, ano_maximo, tipo_de_combustivel, preco_minimo, preco_maximo, cor)
            return jsonify({'resultados': carros_encontrados})
        else:
            return jsonify({'erro': 'Requisição MCP inválida'}), 400
    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
