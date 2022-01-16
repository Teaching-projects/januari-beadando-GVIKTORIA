print("Hello ez a program kiírja egy megadott négyjegyű szám számjegyeit majd összeadja.")
szam=int(input("Adjon meg egy számot!"))
eredeti=szam
egyes=0
tizes=0
szazas=0
ezres=0
if(szam>999 and szam<10000):
    egyes=szam%10
    szam=szam-egyes
    szam=szam/10
    szam=round(szam)

    tizes=szam%10
    szam=szam-tizes
    szam=szam/10
    szam=round(szam)
    
    szazas=szam%10
    szam=szam-szazas
    szam=szam/10
    szam=round(szam)

    ezres=szam%10
    szam=szam-ezres
    szam=szam/10
    szam=round(szam)

    print ("eredeti:",eredeti, "ezres:",ezres,"szazas:",szazas,"tizes:",tizes,"egyes:",egyes)
    print("A szám megfelelő :)")
else:
    print("Ez a szám nem megfelelő,kérem adjon meg egy másikat!") 

print("A számjegyek összege", ezres+szazas+tizes+egyes)
print("Köszönöm hogy használtad a programomat:)")


