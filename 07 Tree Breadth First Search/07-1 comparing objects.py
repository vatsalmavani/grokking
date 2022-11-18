# how to compare two objects?
class compare:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = compare(1)
b = compare(1)
c = compare(2)
a.next = c
b.next = c
print(a == b)   # this gives False since a and b are not at the same memory location
print(a == a)   # same object gives True
print(a.val == b.val and a.next == b.next)



# to use double equals, ==
class compare:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other: object) -> bool:
        return self.val == other.val and self.next == other.next

a = compare(1)
b = compare(1)
c = compare(2)
a.next = c
b.next = c
print(a == b)