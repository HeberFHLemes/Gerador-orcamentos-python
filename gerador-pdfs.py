from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas previstas: ")
valor_hora = input("Digita o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado para conclusão: ")

valor_total = str(int(horas_estimadas) * int(valor_hora))

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.set_font_size(14)

pdf.image("template.png", x=0, y=0)

pdf.text(115, 153, projeto)
pdf.text(115, 173, horas_estimadas)
pdf.text(115, 194, valor_hora + ",00")
pdf.text(115, 215, prazo)
pdf.text(118, 243, str(valor_total) + ",00")

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
