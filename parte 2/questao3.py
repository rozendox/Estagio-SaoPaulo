import json


with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]


menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)


media_mensal = sum(faturamentos) / len(faturamentos)


dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
