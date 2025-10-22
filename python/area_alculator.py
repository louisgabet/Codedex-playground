# Write code below 💖
area = 0
choice = 0
print("==================")
print("Area Calculator 📐 ")
print("==================\n")
while choice != 5:
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit\n")
    choice = int(input("wich shape: "))
    print("\n")

    if choice == 1:
        base = int(input("Base: "))
        Height = int(input("Height: "))
        print("\n")
        area = (base * Height) / 2
        print(f"The area is {area}")

    elif choice == 2:
        length = int(input("Length: "))
        width = int(input("Width: "))
        print("\n")
        area = length * width
        print(f"The area is {area}")

    elif choice == 3:
        side = int(input("Side: "))
        print("\n")
        area = side**2
        print(f"The area is {area}")

    elif choice == 4:
        radius = int(input("Radius: "))
        print("\n")
        area = 3.14 * (radius**2)
        print(f"The area is {area}")
