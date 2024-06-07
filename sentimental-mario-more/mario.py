while True:
    height = int(input("Height: "))
    if 0 < height < 9: 
        break

for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i + "  " + "#" * i)

