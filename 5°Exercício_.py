#Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
#1,68 e pese 75kg.
 

def IMC (peso,altura):    
    c = peso /(altura**2)
    print(f"o se imc é {c:.2f}")
   

IMC( 75, 1.68)

