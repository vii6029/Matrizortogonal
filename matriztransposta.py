def transposta(matriz):
    matrizT=[]
    for i in range(linhas):
        listainternaT=[]
        for j in range(colunas):
            x=matriz[j][i]
            listainternaT.append(x)
        matrizT.append(listainternaT)
    return matrizT

matriz=[]
linhas=int(input())
colunas=int(input())
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    matriz.append(listainterna)
print(transposta(matriz))
       
       

        
            
          
          

 
        
        
    
  
    

    

    






            

