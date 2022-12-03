import pandas as pd
import math as m
import os
if os.path.exists('./pasta'):
    print('Já existe')
else: 
    os.mkdir('./pasta')


Df = pd.DataFrame(columns=['Pressão Cil. Mestre [Pa]','Coeficiente de atrito','Area da Pastilha Furada [m²]','Raio do furo (mm)','Força Pinça [N]','Força Fricção [N]' ,'Torque de frenagem [N/m]','Area Max Furada [m²]', 'Num. furos'])
c = ''
while c != 'N':  
    
    RaioEf = (99.875)/1000 
    Pressure = float(input('Pressão Cilindro Mestre [Pa]: '))
    AreaCaliper = float(706.86)*(10**(-6)) #não condiz com a realidade (5mm de raio)
    AreaPastilha = float(3521.856)*(10**(-6)) #não condiz com a realidade eu acho
    ForcaCaliper = 2*((Pressure*AreaCaliper)/AreaPastilha)
    print(f'Força Pinça: {ForcaCaliper}')

    mi = float(input('Coeficiente de atrito: '))
    ForcaFriccao = ForcaCaliper*mi
    print(f'Força Fricção: {ForcaFriccao}')

    TorqueFrenagem = ForcaFriccao*RaioEf
    print(f'Torque de frenagem: {TorqueFrenagem}')

    AreaPastilhaF = float(input('Area da Pastilha Furada [m**2]: '))
    AreaMaximaFurada = AreaPastilha-AreaPastilhaF
    print(f'Area Máxima que pode ser furada: {AreaMaximaFurada}')

    RaioFuro = float(input()) 
    NumFuros = AreaMaximaFurada//(m.pi*((RaioFuro/1000)**2))
    print(f'Numero de furos que podem ser feitos: {NumFuros}')    
        
    c = str(input('Continuar? ')).capitalize()
    Df = Df.append(pd.Series( {'Pressão Cil. Mestre [Pa]': Pressure ,'Coeficiente de atrito': mi,'Area da Pastilha Furada [m²]': AreaPastilhaF ,'Raio do furo (mm)': RaioFuro,'Força Pinça [N]': ForcaCaliper,'Força Fricção [N]': ForcaFriccao,'Torque de frenagem [N/m]':TorqueFrenagem,'Area Max Furada [m²]': AreaMaximaFurada, 'Num. furos': NumFuros}), ignore_index=True)
print(Df)
continuar = str(input('Deseja salvar o arquivo?[S] ou [N] ')).capitalize()
if continuar == 'S':
    pasta='./pasta'
    cont = 1
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            cont = cont+1
            print(os.path.join(diretorio, arquivo))
            print(cont)
    writer = pd.ExcelWriter(f'./pasta/Dados de frenagem teste {cont}.xlsx')
    Df.to_excel(writer)
    writer.save()
    print("DataFrame is exported successfully to 'Dados de frenagem teste' Excel File.")

    df_novo= pd.read_excel(f'pasta\dados de frenagem teste {cont}.xlsx')
else:
    print('O programa foi encerrado sem salvar os dados!')
    
    
    
    
    
    #colocar na tabela os valores que foram input
    
