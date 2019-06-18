tri=[i*(i+1)/2 for i in range(286,100000)]
pen=[i*(3*i-1)/2 for i in range(166,100000)]
hexa=[i*(2*i-1) for i in range(144,100000)]

for i in tri:
    if i in pen and i in hexa:
        print("Next triangle number that is pentagonal and hexagonal: %d"%i)
        break
