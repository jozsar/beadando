def birsag(ido,tav,hatar):
    km=tav/1000
    h=ido/3600
    if km/h>hatar:
        return True
    return False

def sebesseg(tav,ido):
    km=tav/1000
    h=ido/3600
    return km/h

try:
    bemenet=input("Adja meg a megtett távolságot és a sebességhatárt!(szóközzel elválasztva)")
    bemenetls=bemenet.split(" ")
    tav=int(bemenetls[0])
    hatar=int(bemenetls[1])
    trafi=""
    while trafi!="meres vege":
        trafi=input("Adja meg a traffipax által bemért adatokat!")
        trafils=trafi.split(" ")
        rendszam=trafils[0]
        ido=int(trafils[1])
        if birsag(ido,tav,hatar):
            seb=int(sebesseg(tav,ido))
            osszeg=int((((seb/hatar)*100)-100)*3000)
            fout=open(f"{rendszam}_birsag.txt","w")
            print(f"""BÍRSÁG!
A mai napon Önt a {rendszam} rendszámú gépjárművel a traffipax {seb} km/h sebességgel mérte be.
Ezért a következő bírság befizetésére kötelezzük: {osszeg}Ft""",file=fout)
            fout.close()
except ValueError:
    print("Nem megfelelően adta meg a bekért adatot!")
#példa bemenet:
#750 60
#GGA102 45
#VRE998 36
#AAD225 19
#meres vege