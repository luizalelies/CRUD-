Algoritmos e programação
CRUD  - Spotify Premium

IDEIA:
Programa inspirado em plataformas de streaming musical, como o Spotify, com o objetivo de permitir que o usuário cadastre, visualize, busque, modifique e exclua músicas de um catálogo.


--> Estrutura das músicas:

id --> Identificador único de cada música
titulo --> Título da música
artista --> Nome do artista ou banda
duracao --> Duração da música (em minutos)

--> Variáveis de identidade:

musica --> Dicionário responsável por guardar as informações de cada música
titulo --> Variável que identifica o título da música
artista --> Variável que guarda o nome do artista
duracao --> Variável que identifica a duração da música
proximo_id --> Contador que gera o identificador único de cada música


Bibliotecas:
Não foram utilizadas bibliotecas externas. O projeto utiliza apenas recursos nativos do Python para realizar as operações do CRUD.

CRUD:
O projeto utiliza as quatro operações básicas de um CRUD:

Criar --> Cadastrar novas músicas
Ler --> Listar e buscar músicas cadastradas
Atualizar --> Modificar informações de músicas
Excluir --> Excluir músicas do catálogo

Menu do programa:
1. Cadastrar nova música (Create)
2. Listar músicas (Read)
3. Buscar música por título ou artista (Read)
4. Atualizar dados de uma música (Update)
5. Excluir música do catálogo (Delete)
0. Sair
