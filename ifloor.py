#!usr/bin/python
print(int(5.8))
print(float(5.8))
#print(bytes(5.8))
print(long(5.8))
#python dosent have built in_functions for byes,double and short
print((10.0).is_integer())#checking the float is finite
print((10.1).is_integer())
print(1.1e0)
print(1.1e2)
print(1.1e3)#multiplying a number i.e 1.1 with 1000(e3->10^3)
print("hello"[2])#slicing the word by using a value in  the array
print("hello"[0:2])#slicing the word by using start and stop value in  the array
string="hey"
print string
escaped='can \'t nn'
print escaped
escape='can \' b'  # "\'" is still the same as "'" - you have to escape the backslash.
print escape
print escape.capitalize()
#do format() functioning
what_are_you_doing_now='\t working on u \t'
print what_are_you_doing_now.strip()
print ["Hello",[1,2,3],False,1,2.3212222][-1]#its a mixed list and the o/p wl b the last element
print ["Hello",[1,2,3],False,1,2.3212222][1][1]
sis=["amu","nayak"]
sis_=["nayak","aku"]
sis1={"amu","nayak"}
sis2={"nayak","aku"}
print sis+sis_#concatenating two strings
print '\t'.join( sis+sis_)
print sis1.union(sis2)
print '\t'.join(sis1.union(sis2))
a_list=["Hello",[1,2,3],False,1,2.3212222]
a_list.append(["aku",1])
a_list.append([1,"aku"])
print a_list
a_list.sort()
x=a_list.pop()
print x
a_list.pop(3)
print a_list
my_health=(1,2,3,)#tuples are list but there are immutable as they cant be changed after creation
list(my_health)
#my_health.append(0)##this wont work as tuples as as tuples are immutable list methods wont work
print my_health[1]
creating_dictionaries={"aku":23,23:1111,"o":False}
print creating_dictionaries[23]
