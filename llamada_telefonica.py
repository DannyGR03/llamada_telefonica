# programa en python para 

# input 
dl=int(input("digite dl= "))

# procesing
if dl<=3:
    cl=300
else:
    cl=300+50*(dl-3)

# output
print("el costo de la llamda es " + str(cl))