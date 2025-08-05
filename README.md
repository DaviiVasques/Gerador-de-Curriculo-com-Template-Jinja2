# 📄 Gerador de Currículo com Template Jinja2

## 🧠 Descrição

Este projeto é um **gerador de currículo automatizado**, criado com Python e utilizando o mecanismo de template **Jinja2**. O usuário insere seus dados pessoais em um arquivo `.json` e o programa gera um currículo formatado em **HTML**, pronto para visualização ou exportação para PDF.

O projeto foi totalmente estruturado com **Programação Orientada a Objetos (POO)** para garantir organização, reutilização e escalabilidade do código.

---

## ✅ Funcionalidades

- Lê os dados de um currículo a partir de um arquivo JSON
- Utiliza **Jinja2** para gerar um currículo formatado em HTML
- Separa responsabilidades em diferentes classes e arquivos
- Organiza os dados do usuário de forma clara, acessível e personalizável
- Ideal para automatizar geração de múltiplos currículos com formatos padrão

---

## 🧱 Estrutura do Projeto

gerador_curriculo/
├── main.py # Script principal

├── models/
│ ├── init.py # Torna models um pacote Python
│ └── pessoa.py # Define a classe Pessoa (dados do usuário)

├── templates/
│ └── curriculo.html # Template HTML com marcações Jinja2

├── dados/
│ └── dados.json # Dados do currículo do usuário
└── curriculo_gerado.html # Resultado final (gerado automaticamente)

---

## 🧩 Tecnologias utilizadas

| Tecnologia       | Finalidade                                            |
|------------------|-------------------------------------------------------|
| `Python 3`        | Linguagem principal do projeto                        |
| `Jinja2`          | Motor de template para gerar o currículo em HTML     |
| `JSON`            | Armazenar os dados do currículo de forma estruturada |
