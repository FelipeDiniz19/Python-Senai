km = input("Digite quantos KM:")
km = int (km)

if km <= 150:
    valor = km * 0.50
else:
    valor = (150 * 0.50) + ((km - 150) * 0.80)

print (f"Voce ira pagar : {valor_corrido:}")
