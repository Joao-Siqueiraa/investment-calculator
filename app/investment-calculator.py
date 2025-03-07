valoresperado   =   float(input("qual valor voce deseja chegar"))
aporteinicial   =   float(input("quanto voce ja tem pra investir?"))
aportemensal    =   float(input("qual valor do deposito mensal?"))
taxajurosanual  =   13.75 / 100     #Convertendo para decimal 
inflacaoanual   =   4.8 / 100       #Convertendo para decimal
taxajurosmensal =   taxajurosanual / 12
inflacaomensal  =   inflacaoanual / 12


# inicializa o montante com o aporteinicial

m     = aporteinicial
month = 0
years = 0

# #loop ate o montante atingir 1 milhão
while m < valoresperado:
    m = aporteinicial * (1 + taxajurosmensal) ** (month + 1) + aportemensal * ((1 + taxajurosmensal) ** (month + 1) - 1) / taxajurosmensal
    month += 1  # Incrementa o mês

    years = month / 12

print(f"Você atingirá R$ {valoresperado} em {month} meses aproximadamente {years:.0f} anos!")