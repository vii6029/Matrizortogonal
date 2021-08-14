def vetor(matriz):
    vetorR=[]
    for i in range(linhas):
        for j in range(colunas):
            if(i%2==0):
                if(matriz[i][j]%5==0):
                    vetorR.append(matriz[i][j])
    return vetorR

matriz=[]
linhas=4
colunas=4
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    matriz.append(listainterna)
print(vetor(matriz))    
  
    


        
            




    
       

        
            
          
          

 
        
        
    
  
    

    

    






            

