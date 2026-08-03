# 🤝 Guia de Contribuição: BibliaIA

Ficamos muito felizes pelo seu interesse em contribuir com o BibliaIA! Para manter a organização, a clareza e o rigor do projeto, pedimos que siga este guia simples ao fazer alterações no código ou na documentação.

---

## 🛠️ Regras Fundamentais de Arquitetura

Ao contribuir com código ou instruções para agentes de IA, atente-se às seguintes regras inegociáveis:

1. A IA é uma camada de síntese, não a fonte de dados: Nunca implemente funcionalidades onde a IA gere ou adivinhe informações linguísticas (morfologia, Strong, originais). Ela deve sempre consumir dados do Motor Bíblico.
2. Separação clara: Separe dados históricos e gramaticais objetivos de opiniões/interpretações teológicas.
3. Modularidade: Mantenha os módulos do backend/, frontend/ e agents/ independentes e desacoplados.

---

## 📝 Padronização de Commits (Conventional Commits)

Para manter o histórico do Git limpo e compreensível, utilize o padrão de mensagens de commit com prefixos:

* feat: Para novas funcionalidades (ex: feat: endpoint de busca por Strong).
* fix: Para correção de bugs ou erros no código/dados (ex: fix: erro de acentuação no léxico).
* docs: Para alterações na documentação (ex: docs: atualiza o README.md).
* style: Para ajustes de formatação de código ou criação de arquivos sem lógica de código (ex: style: adiciona arquivo gitkeep).
* refactor: Para refatoração de código sem alterar o comportamento externo.

---

## 🚀 Fluxo de Trabalho Recomendado

1. Faça o clone ou fork do repositório.
2. Crie uma branch para sua alteração:
   `bash
   git checkout -b minha-nova-feature