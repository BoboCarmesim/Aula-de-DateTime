from datetime import datetime
# Pedir e converter data
venc = datetime.strptime(input("Data do vencimento (DD/MM/AAAA): "), "%d/%m/%Y")
dias = (venc - datetime.now()).days

# Mostrar resultado
print(f"\nFaltam {dias} dias" if dias > 0 else f"Venceu há {-dias} dias")