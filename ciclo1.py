# --- CICLOS 01 A 04: Estrutura Base e Cadastro com Validação ---

# Lista principal que armazenará o nosso catálogo de músicas/podcasts (CRUD)
catalogo_musicas = []

def exibir_menu():
    print("\n--- SPOTIFY PREMIUM - GESTÃO DE CATÁLOGO ---")
    print("1. Cadastrar nova música")
    print("2. Listar músicas")
    print("3. Sair")

def cadastrar_musica():
    print("\n--- Cadastro de Música ---")
    titulo = input("Digite o título da música: ").strip()
    artista = input("Digite o nome do artista: ").strip()
    
    # Validação de entrada usando condicionais (Ciclo 04)
    if titulo == "" or artista == "":
        print("❌ Erro técnico: O título e o artista não podem estar vazios!")
        return

    try:
        duracao = float(input("Digite a duração da música (em minutos): "))
        if duracao <= 0:
            print("❌ Erro técnico: A duração deve ser maior que zero.")
            return
    except ValueError:
        print("❌ Erro técnico: Digite um valor numérico válido para a duração!")
        return

    # Criando o dicionário representando a música (base para o Ciclo 08)
    musica = {
        "titulo": titulo,
        "artista": artista,
        "duracao": duracao
    }

    catalogo_musicas.append(musica)
    print(f"Sucesso! A música '{titulo}' de {artista} foi cadastrada.")

def listar_musicas():
    print("\n--- Catálogo de Músicas ---")
    if len(catalogo_musicas) == 0:
        print("O catálogo está vazio.")
        return
    
    # Estrutura de repetição para listar os itens (Ciclo 06/07)
    for indice, musica in enumerate(catalogo_musicas):
        print(f"[{indice}] Título: {musica['titulo']} | Artista: {musica['artista']} | Duração: {musica['duracao']} min")

# Loop principal do programa (Ciclo 06 - while)
rodando = True
while rodando:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cadastrar_musica()
    elif opcao == "2":
        listar_musicas()
    elif opcao == "3":
        print("Encerrando o sistema. Até logo!")
        rodando = False
    else:
        print("❌ Opção inválida! Escolha entre 1, 2 ou 3.")