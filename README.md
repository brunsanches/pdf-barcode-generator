# pdf-barcode-generator
Automação em Python para geração de etiquetas PDF com códigos de barras (Code128) a partir de dados do Excel.
# 🏷️ Gerador de Etiquetas em PDF com Código de Barras (Code128)

## 📌 Sobre o Projeto
Este é um script de automação desenvolvido em Python que lê dados de uma planilha do Excel e gera um arquivo PDF contendo etiquetas formatadas com códigos de barras no padrão Code128. O projeto foi criado para otimizar o processo de etiquetagem de produtos/itens, permitindo a geração de uma única etiqueta específica ou de todo o lote presente no banco de dados.

## 🚀 Funcionalidades
- Leitura automatizada de dados via Excel (`.xlsx`).
- Geração de código de barras padrão **Code128**.
- Interface via terminal para escolher entre imprimir uma etiqueta específica ou todas.
- Formatação automática de tamanho, quebra de linha e centralização de texto no PDF.

## 🛠️ Pré-requisitos e Tecnologias
Para rodar este projeto, você precisará do Python instalado e das seguintes bibliotecas:
- `pandas` e `openpyxl` (Para manipulação e leitura de dados do Excel)
- `reportlab` (Para a criação do PDF e geração do código de barras)

## ⚙️ Como executar o projeto

1. **Clone o repositório:**
