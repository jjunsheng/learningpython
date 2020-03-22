#adding one loop inside another loop, inception lol

#(x, y)
#(0, 0)
#(0, 1)
#(0, 2)
#(1, 0)
#(1, 1)

for x in range(4):
    for y in range(3):
        if x == y:
            pass
        else:
            print(f"({x} , {y})")
