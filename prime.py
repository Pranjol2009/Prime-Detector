def prime(n):
    
    if n==1:
        return False
    
    elif  n<1:
        
        return False
    
    else:
        
        for i in range(2,int((n**0.5)+1)):
            
            if n%i==0:
                
               return False
        return True
inp=int(input("Enter:")) 

if prime(inp):
    
    print("yes") 
    
else:
    
    print("no")         