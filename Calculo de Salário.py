#8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora=float(input("Qual o valor de sua hora de trabalho? \n")) #Entrada do valor da hora-trabalho em 'float' por poder conter casas decimais
qtd_hora=float(input("Qual a quantidade de horas realizadas no mês? \n")) #Entrada da quantidade de horas em 'float' por poder conter casas decimais
salario=valor_hora * qtd_hora #fórmula do cálculo multiplicando a quantidade de VALOR HORA RABALHO X QUANTIDADE DE HORAS
print("O salário mensal correspondente à R$", "%.2f" % salario) # Formatação com a função ("%.2f" %) para limitar o número de casas decimais
print ("")