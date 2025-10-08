"""Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd
 ki az 1-től a megadott számig terjedő egész számok összegét.
""" 
szam = int(input("adj meg egy egesz szamot"))
osszeg = 0
for i in range(1, szam + 1):
    osszeg += i
print(f"az 1 tol a {szam}ig osszesen {osszeg}")