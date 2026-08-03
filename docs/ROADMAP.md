# 🗺️ Roadmap de Desenvolvimento: BibliaIA

Este documento detalha o planejamento em fases para a construção do BibliaIA. Cada fase foi desenhada para gerar valor utilizável de forma incremental, garantindo que o sistema tenha fundações sólidas antes de evoluir para funcionalidades mais complexas.

---

## 🎯 Visão Geral do Cronograma

| Fase | Nome da Fase | Objetivo Principal | Status |
| :---: | :--- | :--- | :---: |
| 0 | Governança & Estrutura | Arquitetura de pastas, documentação inicial e gitkeep | 🔄 Em Progresso |
| 1 | Base de Dados Bíblica | Compilação dos textos originais, dicionários Strong e morfologia | 📅 Planejado |
| 2 | Motor Bíblico (API) | Endpoints determinísticos para consulta sem IA | 📅 Planejado |
| 3 | Orquestração de IA | Conexão dos prompts e LLMs ao Motor Bíblico | 📅 Planejado |
| 4 | Interface Web (MVP) | Frontend simples para consultas e pesquisas | 📅 Planejado |
| 5 | Agentes Especialistas | Módulos dedicados (Lexicógrafo, Historiador, Revisor...) | 📅 Planejado |
| 6 | Recursos Avançados | Entidades lexicais ricas, gráficos e mapas semânticos | 📅 Planejado |

---

## 📑 Detalhamento das Fases

### 🔹 Fase 0: Governança, Arquitetura e Estruturação
* [x] Criação da árvore de diretórios do projeto (docs/, agents/, data/, assets/, etc.).
* [x] Redação dos documentos oficiais de arquitetura e contexto (README.md, VISAO_DO_PROJETO.md).
* [ ] Criação do CONTRIBUTING.md e regras de versionamento.
* [ ] Configuração do ambiente virtual Python e dependências básicas.

---

### 🔹 Fase 1: Compilação da Base de Dados (data/ & database/)
* [ ] Coleta e estruturação de textos bíblicos de domínio público (Hebraico, Grego, Aramaico).
* [ ] Estruturação do dicionário de numeração Strong (Léxicos).
* [ ] Mapeamento das tabelas de dados morfológicos e referências cruzadas (*Cross-references*).
* [ ] Construção do script de povoamento do banco de dados relacional local (SQLite).

---

### 🔹 Fase 2: Motor Bíblico (backend/)
> *Objetivo: Garantir que a aplicação funcione e responda consultas com precisão sem a necessidade de IA.*
* [ ] Endpoint 1: Consulta de versículos e capítulos completos.
* [ ] Endpoint 2: Detalhamento de palavra (Léxico Strong + Morfologia).
* [ ] Endpoint 3: Busca de ocorrências e referências cruzadas.
* [ ] Endpoint 4: Comparativo de traduções em português.

---

### 🔹 Fase 3: Camada de IA e Síntese (agents/ & prompts/)
* [ ] Conexão da API de IA (LLM) aos dados estruturados do Motor Bíblico.
* [ ] Criação do pipeline de prevenção contra alucinações (IA consulta apenas os dados retornados pelo Motor).
* [ ] Testes de geração de exegeses e resumos baseados estritamente em contexto determinístico.

---

### 🔹 Fase 4: Interface Web MVP (frontend/)
* [ ] Interface web intuitiva e rápida.
* [ ] Campo de pesquisa para buscar por versículo (Daniel 5), palavra (Graça) ou código Strong (H2555).
* [ ] Painel de exibição do texto com marcadores de morfologia e original.

---

### 🔹 Fase 5: Agentes Especialistas de IA
* [ ] Agente Lexicógrafo: Focado em explicar o sentido das palavras originais.
* [ ] Agente Historiador: Focado no contexto sociocultural e histórico do texto.
* [ ] Agente Teólogo: Relaciona temas e conexões bíblicas no Antigo e Novo Testamento.
* [ ] Agente Revisor: Audita a resposta antes de exibir ao usuário, verificando se as citações condizem com o banco de dados.

---

### 🔹 Fase 6: Expansão de Recursos
* [ ] Visualizador de entidades lexicais ricas (navegação por raiz, família de palavras e mapa semântico).
* [ ] Integração de recursos gráficos na pasta assets/ (mapas históricos, cronologias, linhas do tempo e diagramas).
