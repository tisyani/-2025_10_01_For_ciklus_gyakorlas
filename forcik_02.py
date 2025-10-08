"""Kérj be két számot a felhasználótól (a és b). Írasd ki az összes
 számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.
"""

a = int(input("Adj meg egy számot!"))
b = int(input("Adj meg egy számot!"))

if b> a:
    for i in range(b - 1, a, - 1):
        print(i)

else:
    for i in range (b, a , +1):
        print(i)

    
        