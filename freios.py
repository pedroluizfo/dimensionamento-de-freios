import matplotlib.pyplot as plt
import os
import pandas as pd
if os.path.exists('./pasta'):
    print('Já existe')
else: 
    os.mkdir('./pasta')

Df = pd.DataFrame(columns=['distância', 'aceleração', 'Força Freio'])
c = ''
while c != 'N':  
    vf = 19.44
    vi = 22.22
    d = float(input('Distância: '))
    aceleração = (((vf*2)-(vi*2))/(2*d))
    print (f'Desaceleração: {aceleração*-1}')
    massa_carro = 850
    força_freio = ((massa_carro*(aceleração*-1))/9.81)
    print(f'Força freio: {força_freio}')
    c = str(input('Continuar? ')).capitalize()
    Df = Df.append(pd.Series( {"distância": d, "aceleração": (aceleração*-1), "Força Freio": força_freio}), ignore_index=True)
print(Df)
continuar = str(input('Deseja salvar o arquivo?[S] ou [N] ')).capitalize()
if continuar == 'S':
    pasta = './pasta'
    cont = 1
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            cont = cont+1
            print(os.path.join(diretorio, arquivo))
            print(cont)
    writer = pd.ExcelWriter(f'./pasta/Dados de frenagem {cont}.xlsx')
    Df.to_excel(writer)
    writer.save()
    print("DataFrame is exported successfully to 'Arquivo_excell' Excel File.")
else:
    print('O programa foi encerrado sem salvar os dados!')
print('graficos')



df_novo = pd.read_excel(f'pasta\dados de frenagem {cont}.xlsx')
print(df_novo)


df_novo.plot(kind='line',figsize=(10,5))
plt.title('distância X aceleração')




