'''What is aliasing :'''
'''it is a memory optimisation technique in which we can save our memory space '''
a= 4
b= 4
print(id(a))
print(id(b))

'''What is garbage collection '''
'''it is unused memeory so you need a program so that it can check which program is consuming memory wothout any use so it removes that  and python handle this by itself:'''


a = 'DSMP 2022-23'
b = a
c = b
import sys 
d = sys.getrefcount('DSMP 2022-23')
print(d)

'''what is mutabilitya and why it is dengerous in certain sceneraio'''

''''''
def func(data):
  data.append(4)

a = [1,2,3]
func(a)
print(a)

L = [ 1,2,3,4]
print(id(L))
L.append(5)
print(id(L))
 

T = (1,2,3)
print(T)
print(id(T))
T = T + (4,)
print(T)
print(id(T))


'''what is cloning :'''
a = [1,2,3]
b = a[:] #cloning , it create a new list 
b.append(4)
print(b)
print(a)

a = {'name':'sid' , 'age':23}
b = a.copy()
b['gender'] = 'male'
print(b)
print(a)

'''Differentiate between deep and shallow copy :'''
a = [ 1,2,3,[4 , 5]]
b = a.copy() #shallow copy 
#or
b = a[:]
print(b)
b[-1][0] = 400
print(b)

#Deep Copy 
import copy
a = [ 1,2,3,[4 , 5]]
b = copy.deepcopy(a)
b[-1][0] = 400
print(b)
print(id(a))
print(id(b))




