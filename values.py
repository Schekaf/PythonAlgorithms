def fibo():
    a, ad, counter = 1, 0, 0
    print("Enter any integer value")
    n = input()
    while int(counter) != int(n):
        x = a + ad
        ad = x
        a = x - a
        counter = counter + 1
        print(x)


def wolfcheepgrass():
    burası, karsi = [], []
    w = "Wolf"
    c = "Cheep"
    g = "Grass"
    while not all(x in [w,c,g] for x in karsi):
        pass