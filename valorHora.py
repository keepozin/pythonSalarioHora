# Programa para calcular o valor/hora de uma pessoa que recebe mensalmente.
''' Passos
Receber o valor do salário do usuário:
Receber as horas trabalhadas do usuário:
Dividir o salário por horas trabalhadas:
Imprimir o valor/hora para o usuário: 
'''

salario_mensal = input('Qual é seu salário mensal? (apenas números) ')
horas_trabalhadas = input('Quantas horas você trabalha por mês? (apenas números) ')
valor_por_hora = (int (salario_mensal) / int (horas_trabalhadas))
print("O valor por hora que você recebe é %s reais." % (valor_por_hora))
