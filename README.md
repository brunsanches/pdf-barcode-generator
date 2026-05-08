# 📦 Gerador Automatizado de Etiquetas de Estoque (PDF)

Este é o meu primeiro projeto focado em automação de tarefas do mundo real! Desenvolvi um script em **Python** capaz de ler dados de uma planilha do Excel e gerar automaticamente etiquetas de inventário com Códigos de Barras (padrão Code128) formatadas diretamente em um arquivo PDF pronto para impressão.

## 🚀 O Problema que este projeto resolve
A criação manual de etiquetas de estoque é um processo demorado e sujeito a erros humanos. Este script automatiza o processo. O usuário pode escolher gerar uma etiqueta específica com base no índice ou gerar, em segundos, um lote completo com todos os itens cadastrados no Excel.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12:** Linguagem base do projeto.
* **Pandas:** Para extração, leitura e tratamento dos dados do arquivo Excel (`.xlsx`).
* **ReportLab:** Biblioteca poderosa para desenhar e renderizar o PDF e os códigos de barras matematicamente na folha.

## ⚙️ Funcionalidades
- [x] Leitura de banco de dados Excel com prevenção de erros em células vazias (`NaN`).
- [x] Geração automática de Códigos de Barras Code 128.
- [x] Limitação inteligente de caracteres e quebra de linha (evita que textos grandes desconfigurem a etiqueta).
- [x] Menu interativo via terminal (Escolha entre Impressão Única ou Impressão em Lote).
- [x] Tratamento de erros (`try/except`) para evitar crashes na digitação do usuário.

## 📥 Como executar o projeto na sua máquina

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)