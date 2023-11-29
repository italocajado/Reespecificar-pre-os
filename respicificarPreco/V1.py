import pandas as pd

# Caminho para a planilha (altere conforme necessário)
caminho_planilha = './Orçamento pessoal.xlsx'  # Altere para o caminho da sua planilha

# Leitura dos dados da planilha
df = pd.read_excel(caminho_planilha)

# Solicitar o valor total desejado
valor_total_desejado = float(input("Informe o valor total desejado: R$ "))

# Calcular os novos valores unitários para atingir o valor total desejado
df['novo_valor_total'] = df['quantidades'] * df['valores_unitarios']
fator_escala = valor_total_desejado / df['novo_valor_total'].sum()
df['novos_valores_unitarios'] = df['valores_unitarios'] * fator_escala
df['novo_total'] = df['novos_valores_unitarios'] * df['quantidades']

# Exibir o DataFrame atualizado
print("\nDados Atualizados:")
print(df)

# Salvar os dados atualizados em uma nova planilha (opcional)
df.to_excel('dados_atualizados4.xlsx', index=False, columns=['itens', 'quantidades', 'novos_valores_unitarios', 'novo_total'])
