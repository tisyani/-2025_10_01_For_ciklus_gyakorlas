"""Számold ki egy adott szám faktoriálisát! A számot a felhasználótól kérd be!

Pl. Ha az adott szám 5, a faktoriálisa: 5! = 5 × 4 × 3 × 2 × 1 = 120
Itt elegendő csak az eredményt megadnod!
"""

szam = int(input("Adj meg egy számot: "))

faktorialis = 1
for i in range(1, szam + 1):
    faktorialis *= i

print(f"A(z) {szam}! faktoriálisa: {faktorialis}")