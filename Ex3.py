from datetime import datetime

# Pedir datas
d1 = datetime.strptime(input("Nascimento 1º irmão (DD/MM/AAAA): "), "%d/%m/%Y")
d2 = datetime.strptime(input("Nascimento 2º irmão (DD/MM/AAAA): "), "%d/%m/%Y")

# Calcular e mostrar diferença
diff = abs(d1 - d2).days
print(f"\nDiferença: {diff//365} anos e {(diff%365)//30} meses")