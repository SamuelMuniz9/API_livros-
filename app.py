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
@app.route ('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

#Consultar por id 
@app.route('/livros/<int:id>', methods=['GET']) #tratando id na url
def consultar_id(id):
    for N in livros: 
        if N.get('id') == id:  #buscando o id de cada livro e comparando com o id colocado na url
            return jsonify(N) 
         #AQUI ESTA SEM TRATAMENTO, ELE DA ERRO CASO COLOQUE UM ID QUE NAO EXISTE. 



#Editar
   #utilizar um request.get_json para editar e o method put que permite a ediçao e alem disso ele esta procurando o indice alem do id 
   #update tambem é bom de utilizar 

#Deletar
 #aqui é delete mas acredito que seja a mesma estrutura que o put do editar 


#URL DO SITE 
app.run(port=5000, host="localhost", debug=True)
