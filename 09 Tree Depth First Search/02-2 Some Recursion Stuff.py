# visualize this entire file in python tutor to understand a thing about recursion

def dfs(i, val):
    if i == 0:
        return
    val += 1
    dfs(i-1, val)
    return val

print(dfs(5,0))

# list works by refernce while variable works by value.
# hence, above code returns 1 (instead of 5) while this code returns [5,4,3,2,1]
def dfs(i, ls):
    if i == 0:
        return
    ls += [i]
    dfs(i-1, ls)
    return ls

print(dfs(5, []))



def dfs(i, val):
    if i == 0:
        return 0
    val += 1
    return val + dfs(i-1, val)

print(dfs(5,0))

# correct code to add up 1, i times
def dfs(val, i):
    if i == 0:
        return val
    return dfs(val+1, i-1)

print(dfs(0,5))