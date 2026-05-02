"""
Sistema de Automação de Etiquetas de Código de Barras
Este script lê dados de uma planilha Excel e gera um PDF formatado com
etiquetas padrão Code128, permitindo impressão individual ou em lote.
"""

from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import pandas as pd

# --- CONFIGURAÇÕES E CARREGAMENTO DE DADOS ---

# Definição do arquivo de entrada e carregamento via Pandas
# dtype=str garante que códigos com zeros à esquerda não sejam corrompidos
# .fillna('') remove valores nulos que poderiam quebrar a geração do PDF
#importação do banco de dados do excel por meio do panda
bd = ("databasemodel.slsx")
tabela = pd.read_excel(bd, dtype=str). fillna('')

# Mapeamento das colunas do Excel para variáveis do sistema
items = tabela["ITEM"]
descricoes = tabela["DESCRICAO"]
localizacao = tabela["LOCALIZACAO"]

# Configurações dimensionais da etiqueta
LARGURA_ETIQUETA = 100 * mm
ALTURA_ETIQUETA = 40 * mm
MEDIDA_ETIQUETA = (LARGURA_ETIQUETA, ALTURA_ETIQUETA)
CENTRO_X = LARGURA_ETIQUETA / 2

# --- INICIALIZAÇÃO DO PDF ---

# O arquivo de saída é gerado no diretório atual para maior portabilidade
ARQUIVO_SAIDA = "Etiquetas_Geradas.pdf"
pagina = canvas.Canvas(ARQUIVO_SAIDA, pagesize=MEDIDA_ETIQUETA)

# Configurações técnicas do código de barras
ALTURA_BARCODE = 13 * mm
LARGURA_BARRA = 0.8 * mm

# --- INTERAÇÃO COM O USUÁRIO E LÓGICA DE GERAÇÃO ---
i=0
opcao = input("Deseja imprimir apenas uma etiqueta ? (sim/não): ").lower()[:3]

if opcao == "sim" or opcao == "s":
    try:
        codnum= int(input("Qual seria o codigo da etiqueta? "))-1
    print(f"Gernado etiqueta {[codnum]} de {len(tabela)}: {items[codnum]}")

    # Tratamento de texto: limita a descrição em duas linhas para não transbordar na etiqueta
    # Converte para maiúsculas para melhor legibilidade na impressão
    linha1 = str(descricoes[codnum]).strip()[:34].upper()
    linha2 = str(descricoes[codnum]).strip()[34:68].upper()
    # Instanciação e cálculo de largura do código de barras
    desenho = code128.Code128(items[codnum], barWidth=LARGURA_BARRA, barHeight=ALTURA_BARCODE)
    largura_barcode = desenho.width

    # Renderização dos elementos na página (Coordenadas em mm)
    pagina.drawCentredString(CENTRO_X, 35 * mm, linha1)
    pagina.drawCentredString(CENTRO_X, 30 * mm, linha2)
    desenho.drawOn(pagina, CENTRO_X - (largura_barcode / 2), 14 * mm)
    pagina.drawCentredString(CENTRO_X, 7.5 * mm, items[codnum])
    pagina.drawCentredString(CENTRO_X, 1.5 * mm, str(localizacao[codnum]))

    pagina.showPage()
    pagina.save()

else:
    print(f"Gerando etiqueta {i + 1} de {len(tabela)}: {items[i]}")

    for i in range(len(tabela)):
        # Processamento de strings para cada etiqueta no loop
        linha1 = str(descricoes[i]).strip()[:34].upper()
        linha2 = str(descricoes[i]).strip()[34:68].upper()

        # Geração do elemento gráfico do código de barras
        desenho = code128.Code128(items[i], barWidth=LARGURA_BARRA, barHeight=ALTURA_BARCODE)
        largura_barcode = desenho.width

        # Posicionamento dos elementos visuais
        pagina.drawCentredString(CENTRO_X, 35 * mm, linha1)
        pagina.drawCentredString(CENTRO_X, 30 * mm, linha2)
        desenho.drawOn(pagina, CENTRO_X - (largura_barcode / 2), 14 * mm)
        pagina.drawCentredString(CENTRO_X, 7.5 * mm, items[i])
        pagina.drawCentredString(CENTRO_X, 1.5 * mm, str(localizacao[i]))
        pagina.showPage()


