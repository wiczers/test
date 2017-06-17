print "Hello Troll, DevMiau89 here. Making some changes for fun"

# This is fun. Try to figure this out. HueHue.
def linear_search(lst, item):
    i = 0
    found = False
    for i in range(len(lst)):
        if lst[i] == item:
            found = True
            break
        else:
            i += 1
    return found, i        

print linear_search([11,23,58,31,56,77,43,12,65,19],19)      
print "Hello what is going on here ?"
