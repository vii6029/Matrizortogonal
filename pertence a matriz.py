def estanamatriz(x):
    cont=0
    for i in range(linhas):
        for j in range(colunas):
            if(x==matriz[i][j]):
                cont+=1
        if(cont==0):
            pertence=False
        else:
            pertence=True
    return pertence
                    
x=int(input())
matriz=[]
linhas=2
colunas=3
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    matriz.append(listainterna)
print(estanamatriz(x))    
  
    


        
            




    
       

        
            
          
          

 
        
        
    
  
    

    

    






            

