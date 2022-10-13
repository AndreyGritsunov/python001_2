a = [True,False]

for x in a:
    for y in a:
        for z in a:
            print("¬(" + str(x) + "⋁" + str(y) + "⋁" + str(z) + ") = ¬" + str(x) + "⋀¬" + str(y) + "⋀¬" + str(z) + " = ", -(x+y+z)==-x*-y*-z)