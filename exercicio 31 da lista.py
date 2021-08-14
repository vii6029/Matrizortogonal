def bolha(lista):
    fim=len(lista)
    continuar=True
    while(fim>1) and (continuar):
        Trocou=False
        x=0
        while(x<fim-1):
            if(lista[x]<lista[x+1]):
                Trocou=True
                aux=lista[x]
                lista[x]=lista[x+1]
                lista[x+1]=aux
                x+=1
        if not Trocou:
            continuar=False
        fim-=1
lista=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    if(x>0):
        lista.append(x)
    else:
        x=int(input())

        
        
       
       

        
            
          
          

 
        
        
    
  
    

    

    






            

