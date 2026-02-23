# 🎓 CRUD de Alunos - Django

Este projeto foi desenvolvido como parte dos meus estudos em **Django** e faz parte do meu roadmap de especialização em **Cyber Security**. A proposta foi construir um sistema completo de gerenciamento de alunos, aplicando na prática conceitos de CRUD, organização de código, boas práticas e noções iniciais de segurança.

---

## 🚀 Tecnologias Utilizadas

*   **🐍 Python / Django** – Estrutura da aplicação, regras de negócio e integração com o banco de dados.
*   **🗄️ SQLite** – Banco de dados relacional utilizado para persistência dos dados.
*   **🎨 HTML + CSS (Vanilla CSS)** – Estrutura das páginas e estilização.
*   **🔡 Google Fonts (Outfit)** – Tipografia utilizada no projeto.

---

## 🧠 Objetivo do Projeto

O principal objetivo foi consolidar meus conhecimentos em:
- [x] Estrutura de projetos Django.
- [x] Modelagem de dados e relacionamentos.
- [x] Implementação completa de um CRUD.
- [x] Uso de `ModelForm`.
- [x] Aplicação de conceitos básicos de segurança.
- [x] Organização de código seguindo boas práticas.

*Mais do que apenas fazer funcionar, a ideia foi entender o que está acontecendo por trás de cada parte do sistema.*

---

## 🛠️ Estrutura e Implementação

### 📦 Modelagem de Dados
Criei dois modelos principais com relacionamento via `ForeignKey`, permitindo associar alunos às suas respectivas turmas:
1.  **Aluno**
2.  **Turma**

### 🔁 CRUD Completo (Function-Based Views)
Implementei as quatro operações fundamentais utilizando **FBVs** para reforçar o entendimento da lógica do Django antes de avançar para CBVs:
*   **✅ Create** – Cadastro de alunos.
*   **📖 Read** – Listagem e visualização.
*   **✏️ Update** – Edição de dados.
*   **❌ Delete** – Exclusão com confirmação via requisição **POST**.

### 📝 Formulários
Utilizei `ModelForm` para garantir validação automática e facilitar a integração com os models.

---

## 🎨 Interface e Estilização

A parte estrutural (HTML) foi organizada por mim, mas a estilização visual (CSS e design da interface) foi desenvolvida com auxílio de uma **IA**. A proposta foi elevar o visual do projeto para algo mais moderno, incluindo:


> Optei por utilizar a IA especificamente na parte de design para focar meu aprendizado principal na lógica, arquitetura e segurança da aplicação.

---

## 🔒 Conceitos de Segurança Aplicados

Mesmo sendo um projeto de estudo, já apliquei práticas importantes:
1.  **Proteção CSRF** em todos os formulários.
2.  **Exclusão via método POST**, evitando deleção por acesso direto à URL.
3.  **Uso da ORM do Django**, prevenindo SQL Injection de forma nativa.
4.  **Separação clara entre responsabilidades** (models, views e templates).

---

## 📈 Próximos Passos

Pretendo evoluir o projeto adicionando:
- [ ] Sistema de autenticação.
- [ ] Controle de permissões.
- [ ] Paginação.
- [ ] Melhor uso do Django Messages.
- [ ] Deploy em VPS.

---

## 📌 Conclusão

Esse projeto representa uma etapa importante na minha evolução com Django. Ele vai além de um CRUD simples: foi um exercício de organização, entendimento da arquitetura do framework e aplicação inicial de conceitos de segurança.

Sigo evoluindo com foco em desenvolvimento web seguro, pensando não apenas como desenvolvedor, mas também começando a enxergar o sistema com **mentalidade de Blue Team**. 🚀
