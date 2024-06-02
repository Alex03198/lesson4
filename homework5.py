immutable_var=1,2,False,"Hi Alex"
print(immutable_var,type(immutable_var))

mutable_list=[1,2,True,"hi Mary"]
print(mutable_list,type(mutable_list))
mutable_list[1]=50
mutable_list[2]=False
mutable_list[3]="Hi, Rambo"
print(mutable_list)

immutable_var[0]=10  #'tuple' object does not support item assignment. Класс tuple - неизменный.
print(immutable_var)

