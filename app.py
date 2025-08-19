#API basica para busca de livros 

# Entendo melhor API
#
#
#
from flask import Flask, request, jsonify 
#flask é um framework do python, que ajuda a trabalhar com URL em API  

app = Flask(__name__) #basicamente criando uma aplicação flask com o nome do arquivo 

#Fazendo um dicionario aqui para agir como o banco de dados
livros = [ 
        {"id":1, "Titulo": "O pequeno Principe", "autor":  "Antoine de Saint-Exupéry"},
        {"id":2, "Titulo": "A volta ao mundo em 80 dias", "autor":  "Júlio Verne"},
        {"id":3, "Titulo": "Percy Jackson e o Mar de Monstros", "autor": "Rick Riordan"}
 ]
    
#configurando a rota



#metodo para pegar e exibir as informações de todos
@app.route ('/livros')
def get_livros():
    return jsonify(livros)

#Consultar por id 
#Editar
#Deletar


#URL DO SITE 
app.run(port=5000, host="localhost", debug=True)
