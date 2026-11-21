# --- SISTEMA CRUD BÁSICO: CATÁLOGO DE MÚSICAS ---

catalogo_musicas = []
proximo_id = 1

while True:
    print("\n=== SPOTIFY PREMIUM — GESTÃO DE CATÁLOGO ===")
    print("1. Cadastrar nova música (Create)")
    print("2. Listar músicas (Read)")
    print("3. Buscar música por título ou artista (Read)")
    print("4. Atualizar dados de uma música (Update)")
    print("5. Excluir música do catálogo (Delete)")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ").strip()

    # --- OPÇÃO 1: CADASTRAR ---
    if opcao == "1":
        print("\n--- Cadastro de Música ---")
        titulo = input("Título da música: ").strip()
        artista = input("Artista: ").strip()
        duracao = input("Duração (em minutos): ").strip()

        if titulo == "" or artista == "" or duracao == "":
            print("❌ Erro: Todos os campos são obrigatórios.")
        else:
            musica = {
                "id": proximo_id,
                "titulo": titulo,
                "artista": artista,
                "duracao": duracao
            }
            catalogo_musicas.append(musica)
            print(f"✅ Música '{titulo}' cadastrada com ID {proximo_id}.")
            proximo_id = proximo_id + 1

    # --- OPÇÃO 2: LISTAR ---
    elif opcao == "2":
        print("\n--- Catálogo de Músicas ---")
        if len(catalogo_musicas) == 0:
            print("O catálogo está vazio.")
        else:
            for m in catalogo_musicas:
                print(f"ID: {m['id']} | Título: {m['titulo']} | Artista: {m['artista']} | Duração: {m['duracao']} min")

    # --- OPÇÃO 3: BUSCAR ---
    elif opcao == "3":
        print("\n--- Buscar Música ---")
        if len(catalogo_musicas) == 0:
            print("O catálogo está vazio.")
        else:
            termo = input("Digite o título ou artista para buscar: ").strip().lower()
            if termo == "":
                print("❌ Erro: O termo de busca não pode estar vazio.")
            else:
                encontrou = False
                for m in catalogo_musicas:
                    if termo in m['titulo'].lower() or termo in m['artista'].lower():
                        print(f"ID: {m['id']} | Título: {m['titulo']} | Artista: {m['artista']} | Duração: {m['duracao']} min")
                        encontrou = True
                if encontrou == False:
                    print("❌ Nenhuma música encontrada com esse termo.")

    # --- OPÇÃO 4: ATUALIZAR ---
    elif opcao == "4":
        print("\n--- Atualizar Música ---")
        if len(catalogo_musicas) == 0:
            print("O catálogo está vazio.")
        else:
            id_str = input("Digite o ID da música que deseja atualizar: ").strip()
            # Validação simples sem try/except
            if id_str.isdigit() == False:
                print("❌ Erro: O ID deve ser um número inteiro.")
            else:
                id_alvo = int(id_str)
                musica_encontrada = None
                for m in catalogo_musicas:
                    if m['id'] == id_alvo:
                        musica_encontrada = m

                if musica_encontrada == None:
                    print("❌ Erro: ID não encontrado no catálogo.")
                else:
                    print(f"Editando: {musica_encontrada['titulo']} - Deixe em branco para manter.")
                    novo_titulo = input(f"Novo título [{musica_encontrada['titulo']}]: ").strip()
                    novo_artista = input(f"Novo artista [{musica_encontrada['artista']}]: ").strip()
                    nova_duracao = input(f"Nova duração [{musica_encontrada['duracao']}]: ").strip()

                    if novo_titulo != "":
                        musica_encontrada['titulo'] = novo_titulo
                    if novo_artista != "":
                        musica_encontrada['artista'] = novo_artista
                    if nova_duracao != "":
                        musica_encontrada['duracao'] = nova_duracao

                    print("✅ Música atualizada com sucesso.")

    # --- OPÇÃO 5: EXCLUIR ---
    elif opcao == "5":
        print("\n--- Excluir Música ---")
        if len(catalogo_musicas) == 0:
            print("O catálogo está vazio.")
        else:
            id_str = input("Digite o ID da música que deseja excluir: ").strip()
            if id_str.isdigit() == False:
                print("❌ Erro: O ID deve ser um número inteiro.")
            else:
                id_alvo = int(id_str)
                indice_remover = -1
                
                # Procurando o índice manualmente com for
                for i in range(len(catalogo_musicas)):
                    if catalogo_musicas[i]['id'] == id_alvo:
                        indice_remover = i

                if indice_remover == -1:
                    print("❌ Erro: ID inexistente.")
                else:
                    removida = catalogo_musicas.pop(indice_remover)
                    print(f"🗑️ Música '{removida['titulo']}' removida com sucesso.")

    # --- OPÇÃO 0: SAIR ---
    elif opcao == "0":
        print("Encerrando o Spotify Premium CRUD. Até logo!")
        break
    else:
        print("❌ Opção inválida. Escolha um número de 0 a 5.")