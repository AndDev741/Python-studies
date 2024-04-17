#An algorithm that checks the fermat last theorem, thats afirm that don't have integers numbers a, b and c
#that a**n + b**n == c**n for any number greater than 2

def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n and n > 2:
        print("Fermat was wrong!")
        print(f"result: {a ** n + b ** n == c ** n}")
    else:
        print("Femat was correct!")
        print(f"result: {a ** n + b ** n == c ** n}")

print("Chose 3 numbers and a exponent to check's the fermat last theorem")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
n = int(input("Exponent:"))

check_fermat(a, b, c, n)