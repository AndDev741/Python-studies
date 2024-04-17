def countdown(n):
    if n < 0:
        print("The countdown is over")
    else:
        print(n)
        countdown(n)

countdown(10)