#Predict the output

lst = [10 , 20 , 30]
tpl = (10 , 20 ,30)

lst[0] = 100
#tpl[0] = 100

print(lst)
print(tpl)

#output:
#Tuple does not support assignmnet 

#List are mutable(can be changed after creation)
#but the tuple are immutable whose value cant be changed after creation 
#hence the error came as assignment not supported for tuple