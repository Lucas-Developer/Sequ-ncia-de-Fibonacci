anterior = 0  
proximo = 0  

while(proximo < 99):  
  print(proximo)  
  proximo = proximo + anterior  
  anterior = proximo - anterior  
   
  if(proximo == 0):  
    proximo = proximo + 1 
