#Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
#é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
#mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas

def salario():
    SalarioBase = float(input('Digite o salario do funcionario: ').replace(',','.'))
    Extra = int(input('Digite a quantidade de hora extra trabalhada: '))
    ValorHora = SalarioBase / 40
    HoraExtra = (ValorHora * Extra) * 1.5 + SalarioBase
    print(f'Salario atual: R$ {SalarioBase}')
    print(f'Total de hora extra trabalha: {Extra}')
    print(f'Total do salario:R$ {HoraExtra:.2f}')

salario()
