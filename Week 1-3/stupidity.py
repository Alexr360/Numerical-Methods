def numbers(list1):
    one = sum(r for r in list1)
    two = sum(r**2 for r in list1)
    thr = sum(r**3 for r in list1)
    return one, two, thr

sutpid = numbers([1,5,3,7,8,9,5,5,5,5,5,5,5])

print(f"Thing1: {sutpid[0]}, Thing2: {sutpid[1]}, Thing3: {sutpid[2]}")
