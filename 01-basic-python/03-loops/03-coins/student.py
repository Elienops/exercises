# Write your code here

def coins(one, two, five, goal):
    for x in range(one):
        for y in range(two):
            for z in range(five):
                if x + y + z == goal:
                    return True
    return False