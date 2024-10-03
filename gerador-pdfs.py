from fpdf import FPDF

# Perguntas sobre o projeto para obter as informações necessárias 
projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas previstas: ")
valor_hora = input("Digita o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado para conclusão: ")

# Cálculo do valor total estimado
valor_total = str(int(horas_estimadas) * int(valor_hora))

# Criação de um PDF e definição da fonte e do tamanho da fonte
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.set_font_size(14)

# Utilização do template em png no PDF
pdf.image("template.png", x=0, y=0)

# Inserção das informações respondidas nas perguntas nos respectivos campos de preenchimento no PDF
pdf.text(115, 153, projeto)
pdf.text(115, 173, horas_estimadas)
pdf.text(115, 194, valor_hora + ",00")
pdf.text(115, 215, prazo)
pdf.text(118, 243, str(valor_total) + ",00")

# Execução final / Exportação para o arquivo "orcamento.pdf"
pdf.output("orcamento.pdf")
print("Orçamento gerado com sucesso!")
