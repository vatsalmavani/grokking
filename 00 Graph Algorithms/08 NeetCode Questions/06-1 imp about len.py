'''
run this code and see that it runs 6 times even though each time an element is popped
each time the element is popped, len(ls) reduces by 1
but note that when we create range OBJECT, len(ls) is calculated only once
it's like a 'list' object [0,1,2,3,4,5] (actually range iterable) is created
'''

ls = [1,2,3,4,5,6]
for i in range(len(ls)):
    x = ls.pop(0)
    print(ls)