# Possible inputs

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

list1 = l3
prev_element_type = type(list1[0])
strings = ""
sum_int = 0
mixed = False

for i in list1:
    if (type(i) != prev_element_type):
        mixed = True
    else:
        prev_element_type = type(i)
    
    if ((type(i) == int) or (type(i) == float)):
        sum_int += i
    elif type(i) == str:
        strings += " " + i
if (mixed == True):
    print "The list you entered is of mixed type"
else:
    print "The list you entered is of type " + prev_element_type.__name__
if (strings != ""):
    print "String:" + strings
if (sum_int != 0):
    print "Sum: " + str(sum_int)        