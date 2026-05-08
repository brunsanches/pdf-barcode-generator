from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import pandas as pd

# Importação do banco de dados do Excel usando a biblioteca Pandas
bd = "relatoriodbestoque.xlsx"

# Lê o arquivo Excel. O parâmetro 'dtype=str' converte tudo para texto, evitando erros de tipagem.
# O '.fillna('')' limpa os valores nulos (NaN) do Excel quando a célula está em branco, substituindo por texto vazio.
tabela = pd.read_excel(bd, dtype=str).fillna('')

# Extração das colunas específicas para variáveis de fácil acesso e manipulação
items = tabela["ITEM"]
descricoes = tabela["DESCRICAO"]

# Definição das dimensões da etiqueta física (100mm de largura x 40mm de altura)
medida_etiqueta = (100 * mm, 40 * mm)
altura_etiqueta = 40 * mm
largura_etiqueta = 100 * mm
centro_x = largura_etiqueta / 2  # Variável auxiliar para calcular o centro exato da etiqueta

# Inicialização do arquivo PDF que receberá as etiquetas geradas
# ATENÇÃO GITHUB: Ao subir para o repositório, é recomendável trocar o caminho inteiro por apenas "Etiquetas.pdf" (caminho relativo).
pagina = canvas.Canvas(r"C:\Users\Bruno\OneDrive\Desktop\codigoetiqueta2\Etiquetas.pdf", pagesize=medida_etiqueta)

# Configurações visuais do código de barras (altura das barras e largura das linhas)
altura = 15 * mm
largura = 0.8 * mm
codigo_barras = items

# Define a fonte principal utilizada no documento e o tamanho
pagina.setFont('Helvetica-Bold', 12.5)

# Interação com o usuário via terminal: Pergunta se deseja imprimir uma etiqueta específica ou todas
# O '[:3]' garante que pegaremos apenas as 3 primeiras letras e o '.lower()' garante que funcionará mesmo se digitar "SIM"
opcao = input("Você quer apenas uma etiqueta? (sim/nao) ")[:3].lower()

# Bloco executado caso o usuário queira apenas UMA etiqueta específica
if opcao == "sim" or opcao == "s":
    try:
        # Recebe o número do item. O "-1" ajusta o input do usuário para o índice base zero do Python/Pandas
        codnum = int(input("Qual item você deseja imprimir? (Digite a linha): ")) - 1

        # Feedback visual no terminal sobre o item sendo processado
        print(f"Gerando etiqueta {codnum + 1} de {len(tabela)}: {items[codnum]}")

        # Formatação da descrição linha 1: Limita a 34 caracteres, remove espaços extras (strip) e converte para maiúsculas (upper)
        limites1 = str(descricoes[codnum]).strip()[:34].upper()
        # Formatação da descrição linha 2: Pega os caracteres do 34 ao 68 para criar um efeito visual de quebra de linha
        limites2 = str(descricoes[codnum]).strip()[34:68].upper()

        # Geração do elemento gráfico do código de barras no padrão Code 128
        desenho = code128.Code128(codigo_barras[codnum], barWidth=largura, barHeight=altura)
        largura_do_barcode = desenho.width

        # Posicionamento dos textos na etiqueta (coordenadas X e Y a partir da base inferior esquerda)
        pagina.drawCentredString(centro_x, 35 * mm, limites1)  # Descrição superior
        pagina.drawCentredString(centro_x, 30 * mm, limites2)  # Descrição inferior

        # Posicionamento centralizado do código de barras (calculado subtraindo metade da largura do código do centro da página)
        desenho.drawOn(pagina, centro_x - (largura_do_barcode / 2), 11 * mm)

        # Posicionamento do código numérico logo abaixo do código de barras
        pagina.drawCentredString(centro_x, 3.5 * mm, items[codnum])


        # Finaliza a formatação da página atual e salva o arquivo PDF no disco
        pagina.showPage()
        pagina.save()

    except ValueError:
        # Bloco de segurança executado se o utilizador digitar letras ou símbolos em vez de números inteiros
        print("Erro: Por favor, digite apenas números inteiros válidos.")

# Bloco executado caso o usuário opte por gerar etiquetas de TODOS os itens da planilha
else:
    # A função for com range iterando sobre len(tabela) ajusta-se automaticamente ao tamanho do Excel
    for i in range(len(tabela)):
        # Garante a redefinição da fonte correta para cada nova página/etiqueta gerada no loop
        pagina.setFont('Helvetica-Bold', 12.5)

        # Limita e quebra a string de descrição (Linha 1 e Linha 2) da mesma forma da impressão individual
        limites1 = str(descricoes[i]).strip()[:34].upper()
        limites2 = str(descricoes[i]).strip()[34:68].upper()

        # Geração e cálculo da largura do código de barras para o item 'i' do loop
        desenho = code128.Code128(codigo_barras[i], barWidth=largura, barHeight=altura)
        largura_do_barcode = desenho.width

        # Aplica a descrição no topo da etiqueta em duas linhas
        pagina.drawCentredString(centro_x, 35 * mm, limites1)
        pagina.drawCentredString(centro_x, 30 * mm, limites2)

        # Aplica o código de barras
        desenho.drawOn(pagina, centro_x - (largura_do_barcode / 2), 11 * mm)

        # Aplica a numeração do item na base
        pagina.drawCentredString(centro_x, 3 * mm, items[i])

        # Exibe o progresso em tempo real da automação no terminal para controle do usuário
        print(f"Gerando etiqueta {i + 1} de {len(tabela)}: {items[i]}")

        # Fecha a página atual, preparando o PDF para a próxima etiqueta no próximo ciclo do loop
        pagina.showPage()

    # Ao final do loop, salva o documento PDF completo contendo todas as páginas
    pagina.save()
    print("Processo Finalizado com Sucesso!")