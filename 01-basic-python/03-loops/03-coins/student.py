# Write your code here

def coins(one, two, five, goal):
    print(range(one + 1))
    for x in range(one + 1):
        for y in range(two + 1):
            for z in range(five + 1):
                if x + y * 2 + z * 5 == goal:
                    return True
    return False
