lista1=[]
lista2=[]
novalista=[]
soma=0
cont=0
for i in range(0,10):
    x1=int(input())
    x2=int(input())
    lista1.append(x1)
    lista2.append(x2)
for i in range(0,10):
    media=lista1[i]+lista2[i]/2
    novalista.append(media)
    soma=soma+media
    if(media>8):
        cont+=1
print(cont,soma/10)
    

        
       
       

        
            
          
          

 
        
        
    
  
    

    

    






            

