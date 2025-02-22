import hogyegyek

kerdesek = []


def intro():
    print("Hogy egyél, hogy jól legyél?")
    print(f"Töltsd kis ezt a {len(kerdesek)} kérdéses quizt és tudd meg hogy mennyire vagy egészséges!")

def olvas(path):
    f = open(path, "r", encoding="utf-8")
    for sor in f:
        kerdesek.append(hogyegyek.Hogyegyek(sor))
    f.close()

def kerdes():
    teljesPontszam = 0
    for kerdes in kerdesek:
        print(f"\nKérdés: {kerdes.question1}")
        print(f"a) {kerdes.answerA}")
        print(f"b) {kerdes.answerB}")
        print(f"c) {kerdes.answerC}")

        valasz = input("Válassz eggyet (a, b, c): ").strip().lower()
        while valasz not in ("a", "b", "c"):
            print("\nHiba kérem valassz ujra, a, b, c")
            valasz = input("Válassz eggyet (a, b, c): ").strip().lower()

        if valasz == "a":
            teljesPontszam += kerdes.scoreA
        elif valasz == "b":
            teljesPontszam += kerdes.scoreB
        elif valasz == "c":
            teljesPontszam += kerdes.scoreC
        else:
            print("Hiba. Nem kaptál pontokat:(")

    return teljesPontszam

def vege(pontszam):
    print(f"\nA teljes pontszámod: {pontszam} pont\n")
    if pontszam < 21:
        print("\033[1;32m c:")
        print(
            "Gratulálunk, te tudod, hogy kell igazán egészségesen élni. Ami nagyon fontos, hogy továbbra is figyelj oda a megfelelő hidratálásra és a rostbevitelre. Ha még nem próbáltad, akkor itt az ideje kipróbálni az alternatív fehérje megoldásokat is. Szuper egészséges és finom tud lenni. Egyre vigyázz, azért ne hajtsd túl magad. ;)")
    elif pontszam < 30:
        print("\033[1;33;40m (:")
        print(
            "Jó úton jársz, de még van mit javítani az étkezéseden. Figyelj a rost és a megfelelő fehérje bevitelre (hal, pulyka vagy csirke legyen a fő és a hüvelyes zöldségek). Nézz utána a mediterrán étrendnek, a tested meg fogja hálálni. A nassolást, amennyire lehet, mellőzd. A nyugodt alváshoz pedig elengedhetetlen a jó környezet, a sötét szoba. Nyugi, nincs szörny az ágy alatt. ;)")
    else:
        print("\033[1;31;40m ):")
        print(
            "Ajjaj, nagy a baj. Nem figyelsz az étkezésedre. Ha ezen nem változtatsz, komoly egészségügyi következményei is lehetnek (mint a cukorbetegség, a magas vérnyomás vagy a korai csontritkulás).")
        print(
            "Légy tudatos, egy életünk van. Javasoljuk, hogy a gyorsan felszívódó szénhidrátokat (vagy épp a szupergyorsan felszívódókat) -mint a nassok, sütemények, krumpli, rizs- cseréld lassan felszívódó szénhidrátokra – basmati rizs, hajdina, köles, kuszkusz- és fogyassz elég folyadékot. Minden nap legalább egy 4km-es távot sétálj le gyorssétával. Ha azt érzed, hogy nehézkes az alvás, akkor lefekvés előtt egy 30 perccel már ne nézz tv-t és ne használd a telefonodat sem. Így nyugodtabb lesz az alvásod és másnap nem kelsz fáradtan, ami miatt amúgy összezabálsz mindent.")

olvas("kerdesek.txt")

intro()

pontszam = kerdes()



vege(pontszam)

# :)
