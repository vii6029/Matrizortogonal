def soma(matriz):
    soma=0
    for i in range(linhas):
        for j in range(colunas):
            if(i==j):
                soma=soma+matriz[i][j]
    return soma

matriz=[]
linhas=3
colunas=3
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    matriz.append(listainterna)
print(soma(matriz))    
  
    


        
            




    
       

        
            
          
          

 
        
        
    
  
    

    

    






            

