import pandas as pd

dados = {
    'Nome': ['Gabriel', 'Débora'],
    'Idade': [18, 53],
    'Sala': ['U29', 'U14']
}

df = pd.DataFrame(dados, columns=['Sala', 'Nome', 'Idade'])

print(df)

