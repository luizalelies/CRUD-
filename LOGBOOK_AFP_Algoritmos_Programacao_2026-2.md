# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | _Maria Luiza Lelis Fróes_ |
| **Engenharia de Software / 2º período** | _ex.: ADS · 2º período_ |
| **Algoritmos e Programação — UnDB 2026.* | Algoritmos e Programação — UnDB 2026.2 |
| **Professor Rondineli Seba Salomão** | Rondineli Seba Salomão |
| **App-base do meu CRUD Spotify Premium (Gestão de catálogo de músicas e playlists)** | _ex.: um app de delivery, um app de músicas…_ |
| **Link do meu repositório** | _https://github.com/…_ |
| **Dupla de revisão (Campo 05) Licia Coimbra** | _nome do colega cujo CRUD vou revisar / que revisa o meu_ |
| **Função neste ciclo : Analista de Testes e Qualidade e REVISOR** | _Autor do meu CRUD · Revisor do CRUD de um colega_ |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ⬜ | OK |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ⬜ | OK |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ⬜ | OK |
| 1 | Campo 02 — Aprofundamento | 16/11 | ⬜ | OK|
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ⬜ | ⬜ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ⬜ | ⬜ |
| 2 | Campo 04 — Interação com IA | 21/11 | ⬜ | ⬜ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ⬜ | ⬜ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [ ] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [ ] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [ ] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [ ] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [ ] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** _Entender como guardar os dados básicos de uma música (título, artista e duração) usando variáveis e tipos corretos em Python._
2. **O que implementei (commits / arquivos / links):** _Criei a estrutura inicial do arquivo main.py com as entradas via input() e exibição simples via print()._
3. **Objeto(s) de conhecimento mobilizado(s):** _Variáveis, tipos primitivos (str, int, float) e comandos de entrada/saída (input(), print())_
4. **Desvio ou erro encontrado + causa técnica:** _Tentei somar ou validar a duração da música logo após o input(), mas deu erro porque o input() sempre devolve texto (str) em vez de número (float)._
5. **Decisão de ajuste + fonte:** _Converti a entrada de duração usando float() e adicionei .strip() para limpar espaços extras antes de processar (livro Pense em Python, cap. 2)._
6. **Feedback recebido e o que mudei:** _Fui orientada a deixar as mensagens de input() mais claras para o usuário saber o formato esperado (ex: minutos)._
7. **Próximo passo:** _Desenhar a lógica de decisão e aplicar operadores para validar se os campos não estão vazios._

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Estruturas de dados compostas, combinando listas (list) para o armazenamento sequencial do catálogo e dicionários (dict) para representar os atributos individuais de cada música.
2. Comandos de entrada, saída e tipagem básica em console utilizando input(), print() e conversões explícitas de tipo (float, int).
3. Estruturas de controle condicional simples e compostas (if, elif, else) para validação de regras de negócio essenciais.


**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Como tratar exceções e entradas incorretas do usuário (como digitar texto em um campo numérico) para evitar falhas do tipo ValueError na execução.
2. Como realizar buscas textuais parciais e case-insensitive em dicionários alocados dentro de listas utilizando list comprehensions.
3. Como modularizar o código em funções independentes e implementar exclusão segura de elementos em listas por ID sem corromper a indexação.

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

>O sistema apresenta falhas iniciais de robustez por processar dados brutos sem validação prévia de tipo ou consistência. A implementação de condicionais, blocos de tratamento de exceção e modularização garantirá que entradas inválidas sejam tratadas adequadamente, preservando a integridade do CRUD.

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** _…_ — **Contribuição:** DOWNEY, Allen B. Pense em Python: Pense como um cientista da computação. São Paulo: Novatec, 2016. — Contribuição: Consolidou o entendimento sobre manipulação de dicionários, listas, loops e escopo de funções essenciais para a arquitetura do catálogo de músicas.
- **Referência 2:** _…_ — **Contribuição:** Documentação Oficial Python: Built-in Exceptions. Disponível em: <docs.python.org>. — Contribuição: Orientou a construção de blocos try/except robustos para validar a conversão de durações e IDs numéricos inseridos pelo operador.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> Além da validação básica de campos vazios, verificou-se que a gestão completa de um CRUD com funções, busca textual refinada e operações de atualização/exclusão requer o uso de funções auxiliares de validação, controle estrito de IDs únicos e algoritmos recursivos para cálculos agregados.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
|Horas de desenvolvimento e testes|14 horas| Necessárias para codificar as funções de CRUD, validar laços e testar a recursividade.|
|Casos de teste de validação | 6 cenários de entrada | Essenciais para cobrir inserções válidas, campos vazios, letras em campos numéricos e IDs inexistentes. |
| Arquivos de script modularizado| 1 arquivo principal (main.py)|Suficiente para centralizar o menu de controle, laço while principal e as funções de manipulação de dados.|
| _…_ | _…_ | _…_ |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** _…_
2. **O que implementei (commits / arquivos / links):** _…_
3. **Objeto(s) de conhecimento mobilizado(s):** _…_
4. **Desvio ou erro encontrado + causa técnica:** _…_
5. **Decisão de ajuste + fonte:** _…_
6. **Feedback recebido e o que mudei:** _…_
7. **Próximo passo:** _…_

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** _Organizar o fluxo de cadastro e validação das músicas usando fluxogramas e operadores lógicos e relacionais._
2. **O que implementei (commits / arquivos / links):** _Montei o fluxograma do cadastro e implementei as verificações iniciais de ID e campos obrigatórios no main.py._
3. **Objeto(s) de conhecimento mobilizado(s):** _Operadores relacionais (==, !=, >), operadores lógicos (or, and) e construção de fluxogramas._
4. **Desvio ou erro encontrado + causa técnica:** _Usei = (atribuição) em vez de == (comparação) dentro da verificação de texto vazio, gerando erro de sintaxe (SyntaxError)._
5. **Decisão de ajuste + fonte:** _Corrigi para == e revisei o fluxograma para garantir que todo caminho inválido volte ao início sem travar (anotações de aula e Pense em Python, cap. 5)._
6. **Feedback recebido e o que mudei:** _Um colega apontou que eu não tinha previsto o que acontece se a duração for zero ou negativa; adicionei a verificação duracao <= 0._
7. **Próximo passo:** _Implementar as estruturas condicionais completas (if, elif, else) para as regras de negócio do catálogo._

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** _Conectar cada regra de negócio do Spotify Premium (campos obrigatórios e opções do menu) a estruturas condicionais._
2. **O que implementei (commits / arquivos / links):** _Implementei o roteamento das opções do menu principal e as travas de validação no cadastro no commit do Ciclo 04._
3. **Objeto(s) de conhecimento mobilizado(s):** _Estruturas condicionais (if, elif, else) e regras de validação de entrada._
4. **Desvio ou erro encontrado + causa técnica:** _Quando o usuário digitava apenas espaços em branco no título, o if titulo == "" deixava passar como válido porque espaços contam como caracteres._
5. **Decisão de ajuste + fonte:** _Passei a usar .strip() antes da condicional para remover espaços vazios nas pontas. Como previsto no Campo 02, validar texto vazio exigiu cuidado extra (Documentação Python: String Methods)._
6. **Feedback recebido e o que mudei:** _O professor sugeriu centralizar as mensagens de erro com um padrão visual claro (❌ Erro:) para facilitar os testes._
7. **Próximo passo:** _Combinar múltiplas regras de validação usando condicionais aninhadas e operadores lógicos._

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [ ] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [ ] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [ ] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [ ] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _Maria Luiza Lelis Fróes_ |
| **Data de realização** | _19/11/2026_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _: Estruturas condicionais permitem que o programa tome decisões diferentes dependendo se uma expressão lógica é verdadeira ou falsa. No meu CRUD do Spotify Premium, uso condicionais combinadas com o operador or (if titulo == "" or artista == "") para impedir o cadastro de músicas incompletas, garantindo que nenhum dado corrompido entre na lista do catálogo._

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _O laço while repete um bloco enquanto uma condição for verdadeira, sendo ideal quando não sabemos quantas vezes o usuário vai usar o sistema (como no menu principal while True). Já o laço for percorre uma sequência com tamanho definido, sendo usado no meu CRUD para varrer item por item da lista de músicas na hora de listar ou buscar um artista._

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _Uma lista armazena vários itens em sequência ordenados por índice, enquanto um dicionário guarda dados no formato chave: valor. No meu projeto, cada música é um dicionário (com chaves como "id", "titulo" e "artista") guardado dentro de uma lista principal (catalogo_musicas), o que evita confundir índices numéricos e facilita buscar informações específicas de cada faixa._

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. _…_ — *Objeto de conhecimento:* _Descobri que usar apenas listas simples (uma lista para títulos, outra para artistas) desorganiza os dados facilmente; juntar dicionários dentro de uma lista resolveu o vínculo de cada música. — Objeto de conhecimento: Listas e Dicionários (list e dict)._
2. _…_ — *Objeto de conhecimento:* _Descobri que buscar textos digitados pelo usuário falha se ele escrever em letras maiúsculas ou minúsculas diferentes do cadastrado, sendo necessário padronizar tudo com .lower(). — Objeto de conhecimento: Manipulação de Strings e Laços de Repetição (for)._
3. _…_ *(opcional)*

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** _No Campo 02 eu tinha planejado validar números apenas com condicionais simples e float(), mas o programa quebrava quando alguém digitava letras no campo de ID ou duração._
- **Causa técnica:** _A tentativa de conversão direta com int() ou float() em uma string não numérica gera uma exceção ValueError em tempo de execução, encerrando o script antes de chegar no if._

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** _Implementei a verificação .isdigit() antes de converter IDs para inteiro (na versão simples) e blocos try/except ValueError nas versões modularizadas para segurar o erro e pedir o dado novamente._
- **Fonte:** _Aulas, pesquisas e livro Pense em Python._

**Objeto de conhecimento mobilizado nesta decisão:** _Validação de tipos, condicionais e tratamento de exceções._

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** _Gemini (Google)_  **Data:** _DD/MM/AAAA_

**4b. Pergunta formulada (transcrita integralmente):**

> _vou precisar que você reescreva os codigos  esse codigo que envei FEITO POR MIM, INICIANTE NA LIGUAGEM, melhorando a escrita a e ideia em alguma coisa, após feito coloque em baixo um feedback do que foi mudado para eu avaliar se estar igual ao meu codigo inicial ok? _

**4c. Resposta da IA (resumida em parágrafo):**

> _A IA reescreveu a estrutura do codigo inical , corrigiandop e auxiliando recursos como funções em while True, laços for, condicionais if/elif/else e listas de dicionários, além de usar .isdigit() para validar entradas numéricas, fuinção adcionada pela propia ia para o intuito de melhorar a estrutura._

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> _Aceitei as substituições feitas para melhora, além da estrutura de dicionários dentro de uma lista (catalogo_musicas), pois isso usa exatamente os objetos de conhecimento vistos em aula._

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> _Na primeira resposta, a IA juntou todos os grupos em um código único e ainda sugeriu recursos fora do escopo inicial sem que pedisse, pois a ideia do codigo priemiro teria que vim de mim para que depois ela melhorasse e corrigisse a estrutura.

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** _Combinar múltiplas regras de validação no cadastro e na busca usando condicionais aninhadas e operadores lógicos._ 
2. **O que implementei (commits / arquivos / links):** _Adicionei verificações combinadas para impedir cadastro sem título/artista e busca com termo vazio._
3. **Objeto(s) de conhecimento mobilizado(s):** _Condicionais aninhadas (if dentro de else) e operadores lógicos (and, or, not)._
4. **Desvio ou erro encontrado + causa técnica:** _Na busca, escrevi if termo in m['titulo'] or m['artista']:, o que sempre dava verdadeiro porque uma string não vazia em Python é avaliada como True._
5. **Decisão de ajuste + fonte:** _Repeti a comparação completa dos dois lados do or (if termo in m['titulo'].lower() or termo in m['artista'].lower():_
6. **Feedback recebido e o que mudei:** _Durante a revisão para a P1, percebi que faltava avisar o usuário quando a busca não encontrava nada; criei uma variável booleana encontrou = False para controlar a mensagem final._
7. **Próximo passo:** _Implementar laços de repetição para manter o menu funcionando continuamente sem fechar o programa._

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** _Transformar o script de execução única em um sistema contínuo com menu interativo usando laços de repetição._
2. **O que implementei (commits / arquivos / links):** _Envolvi o menu do Spotify Premium em um laço while True com opção de saída (break)._
3. **Objeto(s) de conhecimento mobilizado(s):** _Laços de repetição (while, for) e controle de fluxo (break)._
4. **Desvio ou erro encontrado + causa técnica:** _Esqueci de colocar o break na opção "0" (Sair), fazendo o programa entrar em loop infinito mesmo quando o usuário queria encerrar._
5. **Decisão de ajuste + fonte:** _Adicionei o comando break dentro do elif opcao == "0": para interromper o while True com segurança (Documentação Python: More Control Flow Tools)._
6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** _NÃO FOI ENTREGUE PROVA_
7. **Próximo passo:** _

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** _Armazenar múltiplas músicas em uma lista e percorrer os registros para listagem sem perder dados._
2. **O que implementei (commits / arquivos / links):** _Implementei a lista catalogo_musicas = [], o método .append() para inserir e len() para verificar se o catálogo está vazio._ 
3. **Objeto(s) de conhecimento mobilizado(s):** _Listas (list), métodos de inserção/remoção (.append(), .pop()), função len() e iteração com for._ 
4. **Desvio ou erro encontrado + causa técnica:** _Tentei acessar catalogo_musicas[1] quando havia apenas 1 item cadastrado, gerando IndexError: list index out of range porque índices em Python começam em 0._
5. **Decisão de ajuste + fonte:** _Passei a percorrer a lista diretamente com for m in catalogo_musicas: em vez de chutar índices fixos (Pense em Python, cap. 10)._ 
6. **Feedback recebido e o que mudei:** _O professor recomendou sempre testar if len(catalogo_musicas) == 0: antes de tentar listar ou buscar, exibindo uma mensagem amigável._ 
7. **Próximo passo:** _Trocar listas soltas por dicionários dentro da lista para organizar melhor os campos de cada música._

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** _Estruturar cada música como um dicionário (chave: valor) e implementar a busca textual por título ou artista._
2. **O que implementei (commits / arquivos / links):** _Modelei cada música com as chaves "id", "titulo", "artista" e "duracao", e implementei a busca ignorando maiúsculas/minúsculas._
3. **Objeto(s) de conhecimento mobilizado(s):** _Dicionários (dict), acesso por chaves, listas de dicionários e comparação de strings com .lower()_
4. **Desvio ou erro encontrado + causa técnica:** _A busca pelo ID falhava porque eu comparava o ID digitado no input() (tipo str, ex: "1") direto com o ID guardado no dicionário (tipo int, ex: 1), e "1" == 1 retorna False._
5. **Decisão de ajuste + fonte:** _Converti a entrada do ID para int() antes de comparar com m["id"] (Pense em Python, cap. 11)._
6. **Feedback recebido e o que mudei:** _Minha dupla de revisão sugeriu permitir a busca parcial (termo in m["titulo"].lower()) em vez de exigir o nome exato da música (==), o que melhorou muito o uso._
7. **Próximo passo:** _Implementar as operações de atualização (Update) e exclusão (Delete) para fechar o CRUD completo._

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [ ] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [ ] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [ ] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** _Completar o ciclo CRUD implementando a atualização e a exclusão segura de músicas por ID sem quebrar a lista._
2. **O que implementei (commits / arquivos / links):** _Adicionei as opções 4 (Atualizar) e 5 (Excluir) no main.py, localizando o índice pelo ID antes de remover._
3. **Objeto(s) de conhecimento mobilizado(s):** _Manipulação de dicionários (alteração de valores por chave) e remoção segura em listas por índice (.pop(indice))._
4. **Desvio ou erro encontrado + causa técnica:** _Ao tentar excluir usando catalogo_musicas.remove(m) dentro do próprio for m in catalogo_musicas:, a lista mudou de tamanho durante a iteração e pulou o elemento seguinte._
5. **Decisão de ajuste + fonte:** _Primeiro percorro a lista para descobrir o índice (indice_remover) e, somente depois que o for termina, executo catalogo_musicas.pop(indice_remover) (Pense em Python, cap. 10)._
6. **Feedback recebido e o que mudei:** _Na revisão por pares com a Licia Coimbra, ajustei a atualização para que, se o usuário apertar Enter em branco, o valor antigo seja mantido em vez de apagar o dado._
7. **Próximo passo:** _Organizar o código dividindo cada funcionalidade em funções separadas (modularização)._

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | _Licia Coimbra_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _Maria Luiza Lelis Froes_ |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 21/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 11. Clonar/abrir o código do CRUD da dupla	Revisor	21/10	☑ Concluída	Sem desvios; código acessível e legível.
2. Testar fluxo de Cadastro e Listagem (Create/Read)	Revisor	21/10	☑ Concluída	Cadastro funcionando corretamente com listas e dicionários.
3. Testar atualização e exclusão (Update/Delete)	Revisor	21/10	☑ Concluída	Identificado comportamento ao tentar excluir ID inexistente.
4. Ler o código-fonte e verificar estruturas	Revisor	21/10	☑ Concluída	Verificado uso correto de laços for e condicionais.
5. Registrar achados e devolver feedback ao Autor	Revisor / Autor	21/10	☑ Concluída	Feedback entregue via GitHub/sala para ajuste da mensagem de ID inválido.

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _Casos de teste manuais (CRUD)_ | _5 cenários_ | _5 cenários_ | _0_ | _Cobriram criação, leitura, busca, atualização e exclusão._ |
| _Entradas inválidas (ID inexistente/vazio)_ | _3 testes_ | _3 testes_ | _+1_ | _Foi necessário testar um caso extra de exclusão com lista vazia._ |
| _Arquivo principal do colega (main.py)_ | _1 arquivo_ | _1 arquivo_ | _0_ | _Suficiente para auditar toda a lógica implementada até o Ciclo 09._ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _O CRUD deve executar as 4 operações básicas (Create, Read, Update, Delete) sem encerrar abruptamente ao buscar ou excluir um ID inexistente._
- **A solução atende?** ☑ Parcialmente (Atendia ao fluxo normal, mas precisava de aviso claro quando o ID não era encontrado na exclusão).

**5d. GESTÃO DE RISCOS:**
- **Risco:** _Diferença de versão do Python ou falta de dados pré-cadastrados dificultar a reprodução dos testes de exclusão._
- **Estratégia de mitigação:** _Criar um roteiro padrão de 3 cadastros iniciais antes de rodar os testes de atualização e exclusão._

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _21/10/26_ | _Validar se a lista está vazia antes de pedir ID na exclusão_ | _Revisor_ | _Estruturas condicionais (if) e função len()_ | _Pense em Python, cap. 10 (Listas)._ |
| _21/10/26_ | _Evitar remoção direta dentro do laço for_ | _Revisor_ | _Estruturas condicionais (if) e função len()_ | _Documentação Oficial Python (Data Structures)._ |
| _21/10/26_ | _Padronizar busca textual com .lower()_ | _Autor_ | _Autor_ | _Iteração e mutabilidade de listas (.pop())_ |
| _21/10/26_ | _Manter valor original se o input de edição vier vazio_ | _Autor_ | _Métodos de String e operadores lógicos_ | _Estruturas condicionais (if campo != "")_ |
| _21/10/26_ | _Exibir feedback visual quando ID não é localizado_ | _Revisor_ | _Variáveis de controle (flags booleanas/índice -1)_ | _Anotações de aula — Ciclo 09 (CRUD completo)._ |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** _Organizar o menu de opções e as rotinas do CRUD mantendo todo o fluxo integrado dentro de um laço principal._
2. **O que implementei (commits / arquivos / links):** _Estruturei todas as opções do menu (cadastro, listagem, busca, atualização e exclusão) utilizando condicionais elif encadeadas._
3. **Objeto(s) de conhecimento mobilizado(s):** _Estruturas de controle de fluxo e ramificações condicionais (if, elif, else)._
4. **Desvio ou erro encontrado + causa técnica:** _Algumas opções do menu executavam ações duplicadas porque as condições dos elif sobrepunham-se._
5. **Decisão de ajuste + fonte:** _Organizei a ordem lógica das verificações e isolei cada opção com checagens estritas de string_
6. **Feedback recebido e o que mudei:** _Um colega sugeriu manter a estrutura direta para facilitar a leitura visual de quem está a começar na programação._
7. **Próximo passo:** _Aprimorar a validação de dados numéricos (como IDs) sem quebrar o programa._

## 🔵 CICLO 11 — 04/11 — Recursividade


<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** _Validar entradas numéricas de forma segura utilizando métodos de string integrados do Python._
2. **O que implementei (commits / arquivos / links):** _Adicionei a verificação .isdigit() nas opções de atualização e exclusão para checar se o ID digitado é um número válido._
3. **Objeto(s) de conhecimento mobilizado(s):** _Métodos de string (.isdigit()), conversão de tipos (int()) e condicionais de validação._
4. **Desvio ou erro encontrado + causa técnica:** _O método .isdigit() rejeita números decimais ou negativos; ao testar com durações com ponto, gerava erro._
5. **Decisão de ajuste + fonte:** _Defini o caso base if indice >= len(catalogo): return 0.0 e passei indice + 1 na chamada recursiva (Pense em Python, cap. 5 — Recursividade)._
6. **Feedback recebido e o que mudei:** _O professor confirmou que validar com .isdigit() é uma alternativa simples e correta para o nível inicial sem precisar de tratamento avançado de exceções._
7. **Próximo passo:** _Fazer a revisão final do código e limpar redundâncias.._

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> _Decidi separar a busca do índice por ID (buscar_indice_por_id) da operação de exclusão/atualização e validar entradas numéricas antes da conversão de tipo. Essa estrutura foi pensada por mim para evitar que o catálogo fosse modificado enquanto era percorrido e para garantir que nenhum erro de digitação do usuário derrubasse o sistema durante a execução._

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** _Os dados do catálogo ainda ficam apenas na memória RAM (listas e dicionários) e somem quando o programa é fechado, além de eu precisar aprofundar a persistência em arquivos._
- **Plano de ação (passos e datas):** _Revisar manipulação básica de listas, dicionários e condicionais até 17/11; 2) Testar todos os cenários de erro do CRUD no terminal antes da defesa em 18/11; 3) Estudar leitura e escrita de arquivos .txt/.json após a entrega final (27/11)._

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** _Por que você optou por armazenar cada música como um dicionário dentro de uma lista e como você garante que a exclusão de um item pelo ID não cause erro de índice no programa?_
- **Resposta:**

> _Optei por combinar listas e dicionários porque a lista permite armazenar uma coleção dinâmica de músicas em sequência, enquanto o dicionário organiza os atributos de cada música por chaves nomeadas ("id", "titulo", "artista", "duracao"), evitando o risco de confundir posições numéricas como ocorreria em listas aninhadas. Para realizar a exclusão com segurança, não removo o elemento diretamente dentro do laço for que percorre o catálogo, pois alterar o tamanho da lista durante a iteração faz com que índices sejam pulados ou gerem IndexError. Em vez disso, primeiro percorro a lista para encontrar a posição exata correspondente ao ID digitado e, somente após encerrar a busca, utilizo o método .pop(indice) para remover o registro com precisão._

**Objeto de conhecimento mobilizado:** _Estruturas de dados compostas (list e dict), iteração e mutabilidade de listas._
**Fonte:** _DOWNEY, Allen B. Pense em Python (cap. 10 e 11) e Documentação Oficial Python (Data Structures)._

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** _Refatorar o código final garantindo que todas as regras de negócio do CRUD funcionem perfeitamente em um fluxo linear único._
2. **O que implementei (commits / arquivos / links):** _Limpei o código do main.py, padronizei as mensagens de erro com emojis e revisei a lógica de busca e exclusão por índice._
3. **Objeto(s) de conhecimento mobilizado(s):** _Listas, dicionários, laços de repetição (for, while) e refatoração de código._
4. **Desvio ou erro encontrado + causa técnica:** _Na exclusão, apagar o item iterando diretamente na lista alterava o tamanho dela; resolvi buscando o índice exato com range(len()) primeiro._
5. **Decisão de ajuste + fonte:** _Armazenei o índice encontrado na variável indice_remover e executei o .pop(indice_remover) apenas após o laço terminar (Pense em Python, cap. 10)._
6. **Feedback recebido e o que mudei:** _A revisão com a dupla de colegas validou que o código está totalmente limpo, funcional e restrito aos conteúdos ensinados em sala._
7. **Próximo passo:** _Subir a versão final para o repositório do GitHub e preparar os últimos detalhes do Logbook._

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | _nome_ |
| **Repositório revisado** | _link_ |
| **Revisor** | _Maria Luiza Lelis Froes|_ |
| **Ciclo / data** | _Ciclo 12 · 11/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. _…_ | Revisor  | _11/11_ | ☑ Concluída | _A validação de ID inexistente na exclusão foi devidamente corrigida._ |
| 2. _…_ | Revisor  | _11/11_ | ☑ Concluída | _O sistema resistiu às entradas inválidas sem gerar ValueError._ |
| 3. _…_ | Revisor  | _11/11_ | ☑ Concluída| _Código organizado em funções pequenas e legíveis._ |
| 4. _…_ | Revisor  | _11/11_ | ☑ Concluída | _Caso base funcionando mesmo quando a lista está vazia (retorna 0)._ |
| 5. _…_ | Revisor / Autor | _11/11_ | ☑ Concluída| _Aprovado para a entrega final do Grupo 3._ |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| _Casos de teste de estresse (entradas inválidas)_ | _6 cenários_ | _6 cenários_ | _0_ | _Testados textos vazios, espaços, letras em ID, números negativos e lista vazia._ |
| _Checklist de qualidade de código (refatoração)_ | _4 critérios_ | _4 critérios_ | _0_ | _Verificados: ausência de código duplicado, nomes claros, funções coesas e tratamento de erros._ |
| _Repositório GitHub atualizado_ | _1 repositório_ | _1 repositório_ | _0_ | _Histórico de commits coerente com a evolução dos ciclos._ |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** _O código deve estar modularizado em funções coesas, sem repetição de lógica, e resistir a entradas inválidas ou vazias sem quebrar em tempo de execução._
- **A solução atende?** ☑ Sim
**5d. GESTÃO DE RISCOS:**
- **Risco:** _Alguma refatoração de última hora quebrar uma funcionalidade que já funcionava antes (regressão)._
- **Estratégia de mitigação:** _Executar novamente todo o fluxo completo (Create → Read → Search → Update → Delete → Recursão) após cada alteração no código._

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| _11/11/26_ | _Extrair validação numérica para função reutilizável_ | _Autor_ | _Modularização e funções com retorno (def / return)_ | _Pense em Python, cap. 3 e 6._ |
| _11/11/26_ | _Proteger conversões numéricas contra letras_ | _Autor_ | _Tratamento de exceções (try/except ValueError) ou .isdigit()_ | _Documentação Oficial Python (Built-in Exceptions)._ |
| _11/11/26_ | _Garantir caso base para lista vazia na recursividade_ | _Revisor_ | _Recursividade e condição de parada_ | _Pense em Python, cap. 5._ |
| _11/11/26_ | _Remover código duplicado nas mensagens de menu_ | _Autor_ | _Qualidade de código e refatoração (DRY)_ | _Material de aula — Ciclo 12 (Refatoração)._ |
| _11/11/26_ | _Validar fluxo completo após refatoração (teste de regressão)_ | _Revisor_ | _Testes funcionais e lógica de controle_ | _Boas práticas de engenharia de software / Ciclo 12._ |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> _No início (Campo 01), eu achava que bastava usar input(), print() e alguns if/else simples para o sistema funcionar, e minha hipótese era que apenas checar campos vazios já resolveria os problemas de robustez. Eu ainda não sabia como lidar com erros de tipo (ValueError) quando o usuário digitasse texto no lugar de número, nem como fazer buscas parciais ou excluir itens de uma lista sem bagunçar os índices._

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|OBJETO DE CONHECIMENTO|O QUE EU NÃO DOMINAVA|O QUE APRENDI E CONSIGO DEMONSTRAR|---|
| _Listas e Dicionários (list e dict)_ | _Não sabia como relacionar vários atributos de uma mesma música sem criar listas separadas que se desorganizavam._ | _Aprendi a modelar cada registro como um dicionário (chave: valor) dentro de uma lista principal, facilitando buscas e atualizações por ID._ | _Campo 01, Ciclo 07, Ciclo 08 e Campo 06 (6c)._ |
| _Laços de Repetição e Mutabilidade (for, while, .pop())_ | _Não sabia manter o menu rodando continuamente nem por que excluir um item durante um for fazia o programa pular registros._ | _Aprendi a controlar o fluxo com while True e a localizar primeiro o índice alvo para só depois excluir com .pop(indice) com segurança._ | _Ciclo 06, Ciclo 09 e Campo 05 (Revisão nº 1)._ |
| _Modularização, Exceções e Recursividade (def, try/except)_ | _Não sabia dividir um código grande em partes menores, nem impedir o programa de travar ao digitar letras em campos numéricos._ | _Aprendi a criar funções independentes para cada operação do CRUD, validar tipos numéricos com segurança e construir função recursiva com caso base._ | _Campo 03 (3b), Ciclo 10, Ciclo 11 e Ciclo 12._ |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** _Eu achava que comparar if termo in m['titulo'] or m['artista']: verificava o termo nos dois campos, e também confundia str com int na busca por ID ("1" == 1)._
   **O que corrigiu:** _Entendi que cada lado do or precisa da comparação completa e que dados vindos do input() sempre nascem como texto (str), precisando ser convertidos antes de comparar com inteiros.O que corrigiu: Testes práticos no terminal, leitura do livro Pense em Python e registros dos Ciclos 05 e 08._
2. **Equívoco:** _Eu achava que podia remover um elemento da lista diretamente dentro do laço for que a estava percorrendo._ — **Correção:** _Aprendi que alterar o tamanho da lista durante a iteração desloca os índices internos; o correto é buscar o índice primeiro e usar .pop(indice) fora do laço.O que corrigiu: Revisão por pares (Peer Review no Ciclo 09) e documentação oficial do Python._
   **O que corrigiu:** _…_

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> _Toda a lógica construída neste CRUD de músicas pode ser transferida diretamente para um sistema de controle de estoque ou cadastro de pacientes/clientes. A estrutura de armazenar registros em dicionários dentro de uma lista, validar entradas antes de salvar, buscar por termos parciais e atualizar/excluir por um identificador único (ID ou código de barras) funciona exatamente da mesma forma em qualquer sistema de gestão comercial ou administrativa._

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> _Ainda não domino o armazenamento permanente de dados (persistência em arquivos .json, .csv ou bancos de dados SQL), pois no meu projeto atual todos os cadastros são perdidos quando o programa é encerrado. Também quero aprofundar Programação Orientada a Objetos (POO) no próximo módulo para estruturar entidades como Musica e Playlist de forma ainda mais profissional._

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _…_ |
| **Curso / Time / Função** | _…_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 25/11
1. **O que apresentei/defendi (em 1 frase):** _…_
2. **Objeto(s) de conhecimento que a banca mais explorou:** _…_
3. **Pergunta que mais me desafiou e como respondi:** _…_
4. **O que levo deste semestre para o próximo módulo:** _…_

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
