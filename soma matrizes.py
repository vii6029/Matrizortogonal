def somamatrizes(m1,m2,linhas,colunas):
    m3=[]
    for i in range(linhas):
        listainterna=[]
        for j in range(colunas):
            x=(m1[i][j]+m2[i][j])
            listainterna.append(x)
        m3.append(listainterna)
    return m3

m1=[]
linhas=int(input())
colunas=int(input())
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    m1.append(listainterna)
    
A1=linhas
A2=colunas

m2=[]
linhas=A1
colunas=A2
for i in range(linhas):
    listainterna=[]
    for j in range(colunas):
        n=int(input())
        listainterna.append(n)
    m2.append(listainterna)

print(somamatrizes(m1,m2,linhas,colunas))
        
            
          
          

 
        
        
    
  
    

    

    






            

