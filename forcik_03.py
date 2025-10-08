"""Készíts egy programot, amely egy előre meghatározott jelszót vár el
 a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

jelszo = "meow"
lekertjelsz = input(" Írd be a jeszót! ")

while lekertjelsz != jelszo:
    print("NEM JÓ")
    lekertjelsz = input("Írd be újra a jelszót! ")

print("BEJUTOTTÁL")