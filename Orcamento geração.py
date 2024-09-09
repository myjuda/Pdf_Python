
import os

print("Directorio actual:", os.getcwd())

from fpdf import FPDF
Projeto= input("Digite a descripção do projeto:")
horas_estimadas=input("Digite o total de horas estimadas:")
valor_hora=input("Digite o valor da hora trabalhada:")
prazo=input ("Digite o prazo estimado para conclusão:")

Valor_total= int(horas_estimadas)*int(valor_hora)

pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial")

#Importante, darle siempre la ubicación exacta.
pdf.image("/Users/juanlozadacalderon/Downloads/Curso Python Brasil/template.png", x=0, y=0)

pdf.image()

pdf.text(115,145,Projeto)
pdf.text(115,160,horas_estimadas)
pdf.text(115,175,valor_hora)
pdf.text(115,190,prazo)
pdf.text(115,205,str(Valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")


