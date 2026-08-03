# 📖 BibliaIA

> Assistente bíblico inteligente, de código aberto em português, focado em exegese, análise lexical e estudos profundos com base nos textos originais.

---

## 💡 Nota do Criador

> ⚠️ IMPORTANTE: Esta ferramenta é conduzida e desenvolvida por agentes de Inteligência Artificial para auxiliar no estudo e na pesquisa bíblica. Use a IA para ajudar, mas confie e desconfie ao mesmo tempo. Nenhuma tecnologia ou inteligência artificial pode substituir o texto original e a revelação pessoal do Espírito Santo. Jesus te ama!

---

## 🎯 Objetivo do Projeto

O BibliaIA busca unir a precisão dos dados linguísticos bíblicos (textos originais, léxicos e morfologia) com o poder dos modelos de linguagem de inteligência artificial. 

O diferencial do projeto é a separação entre dados e inteligência: a IA nunca "inventa" dados bíblicos ou linguísticos. Ela interpreta e sintetiza os dados extraídos deterministicamente pelo nosso Motor Bíblico.

---

## 🧱 Arquitetura em Camadas

O sistema é construído em um pipeline seguro para evitar alucinações de IA:

1. **Camada de Dados (data/ e database/):** Textos originais em Hebraico, Grego e Aramaico, acompanhados de numeração Strong, dados morfológicos, dicionários e referências cruzadas.
2. **Motor Bíblico (backend/):** API responsável por consultar o banco de dados determinístico e entregar o contexto exato e estruturado.
3. **Agentes de IA (agents/ e prompts/):** Módulos especializados (Lexicógrafo, Historiador, Teólogo, Revisor) que consomem os dados do Motor para gerar exegeses e análises semânticas.
4. **Interface (frontend/):** Aplicação web para navegação interativa, visualização de mapas semânticos e estudos.

---

## 🛠️ Regras e Princípios Veracidade e Precisão:de e Precisão:** A IA nunca atua como fonte primária de dados gramaticais ou lexicais. Ela consome estritamente o retorno do MNeutralidade e Transparência:Transparência:** Separação clara entre fatos históricos/linguísticos e tradições interpretativaGranularidade Lexical:idade Lexical:** Cada palavra do texto original é tratada como uma entidade rica (raiz, ocorrências, campos semânticosModularidade:*Modularidade:** Cada componente, agente e recurso visual deve operar de forma independente.

---

## 🗺️ Roadmap Fase 0: [x] **Fase 0:** Estruturação da arquitetura, governança e repFase 1 (Banco de Dados):nco de Dados):** Compilação dos textos em língua original, dicionários Strong e tabela morfológica eFase 2 (Motor Bíblico):otor Bíblico):** API de consulta determinística de versículos, capítulos Fase 3 (Orquestração de IA):tração de IA):** Integração com APIs de IA para consumo do MotorFase 4 (Interface Web):nterface Web):** MVP do frontend para buscas e visualização deFase 5 & 6 (Especialização):pecialização):** Deploy dos Agentes Especialistas (Lexicógrafo, Historiador, Revisor) e mapas semânticos.

---

## 📚 Documentação do Projeto

Aprofunde-se nos detalhes arquitetônicos e de desenvolvimento:

* 📄 [Visão do Projeto](docs/VISAO_DO_PROJETO.md)
* 🗺️ [Roadmap Detalhado](docs/ROADMAP.md)
* 🏗️ [Arquitetura do Sistema](docs/ARQUITETURA.md)
* 📐 [Padrões de Código e Diretrizes](docs/PADROES.md)
* 🤝 [Guia de Contribuição](CONTRIBUTING.md)

---

## 📄 Licença

Este projeto é disponibilizado sob a licença [MIT](LICENSE).
