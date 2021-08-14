def produto(matriz,matrizT):
    ordem=len(matriz)
    c=[]
    for i in range(ordem):
        linha=[]
        for j in range(ordem):
            linha.append(0)
        c.append(linha)
    for i in range(ordem):
        for j in range(ordem):
            for k in range(ordem):
                c[i][j]+=(matriz[i][k]*matrizT[k][j])
    return c

matriz=[]
linhas=int(input())
colunas=linhas 
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    matriz.append(listainterna)

A=linhas

matrizT=[]
linhas=A
colunas=linhas
for i in range(colunas):
    listainternaT=[]
    for j in range(linhas):
        x=matriz[j][i]
        listainternaT.append(x)
    matrizT.append(listainternaT)

matrizIdentidade=[[1,0],[0,1]]

x=produto(matriz,matrizT)
if(x==matrizIdentidade):
    print("a matriz eh ortogonal")
else:
    print("a matriz n eh ortogonal")

        
            





       

        
            
          
          

 
        
        
    
  
    

    

    






            

