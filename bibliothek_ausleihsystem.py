# =====================================
# Bibliotheks- und Ausleihsystem
# =====================================

aktueller_tag = 20

# -----------------------------
# Startdaten
# -----------------------------

buecher = [
    {"id": 101, "titel": "Python Basics", "kategorie": "Informatik",
     "verfuegbar": True, "ausleihen": 8},

    {"id": 102, "titel": "Algorithmen", "kategorie": "Informatik",
     "verfuegbar": False, "ausleihen": 12},

    {"id": 103, "titel": "Datenanalyse", "kategorie": "Data Science",
     "verfuegbar": True, "ausleihen": 10}
]

nutzer = [
    {
        "id": 12,
        "name": "Anna",
        "ausgeliehen": [
            {"buch_id": 102, "start": 7}
        ],
        "vormerkungen": []
    },

    {
        "id": 13,
        "name": "Max",
        "ausgeliehen": [],
        "vormerkungen": []
    }
]


# -----------------------------
# Suchfunktionen
# -----------------------------

def suche_buch(buch_id):
    for buch in buecher:
        if buch["id"] == buch_id:
            return buch
    return None


def suche_nutzer(nutzer_id):
    for person in nutzer:
        if person["id"] == nutzer_id:
            return person
    return None


# -----------------------------
# Hinzufügen
# -----------------------------

def fuege_buch_hinzu():
    try:
        buch_id = int(input("Buch-ID: "))

        if suche_buch(buch_id):
            raise ValueError("Diese Buch-ID existiert bereits.")

        titel = input("Titel: ")
        kategorie = input("Kategorie: ")

        neues_buch = {
            "id": buch_id,
            "titel": titel,
            "kategorie": kategorie,
            "verfuegbar": True,
            "ausleihen": 0
        }

        buecher.append(neues_buch)
        print("Buch erfolgreich hinzugefügt.")

    except ValueError as fehler:
        print("Fehler:", fehler)


def fuege_nutzer_hinzu():
    try:
        nutzer_id = int(input("Nutzer-ID: "))

        if suche_nutzer(nutzer_id):
            raise ValueError("Diese Nutzer-ID existiert bereits.")

        name = input("Name: ")

        neuer_nutzer = {
            "id": nutzer_id,
            "name": name,
            "ausgeliehen": [],
            "vormerkungen": []
        }

        nutzer.append(neuer_nutzer)

        print("Nutzer erfolgreich hinzugefügt.")

    except ValueError as fehler:
        print("Fehler:", fehler)


# -----------------------------
# Ausleihen
# -----------------------------

def leihe_buch_aus():
    try:
        nutzer_id = int(input("Nutzer-ID: "))
        buch_id = int(input("Buch-ID: "))

        person = suche_nutzer(nutzer_id)
        buch = suche_buch(buch_id)

        if person is None:
            raise ValueError("Nutzer nicht gefunden.")

        if buch is None:
            raise ValueError("Buch nicht gefunden.")

        if not buch["verfuegbar"]:
            raise ValueError("Buch ist bereits ausgeliehen.")

        if len(person["ausgeliehen"]) >= 5:
            raise ValueError("Ausleihlimit erreicht.")

        person["ausgeliehen"].append({
            "buch_id": buch_id,
            "start": aktueller_tag
        })

        buch["verfuegbar"] = False
        buch["ausleihen"] += 1

        if buch_id in person["vormerkungen"]:
            person["vormerkungen"].remove(buch_id)

        print("Ausleihe erfolgreich.")
        print("Rückgabe spätestens an Tag", aktueller_tag + 14)
    
    except ValueError as fehler:
        print("Fehler:", fehler)


# -----------------------------
# Rückgabe
# -----------------------------

def gib_buch_zurueck():
    try:
        nutzer_id = int(input("Nutzer-ID: "))
        buch_id = int(input("Buch-ID: "))

        person = suche_nutzer(nutzer_id)
        buch = suche_buch(buch_id)

        if person is None:
            raise ValueError("Nutzer nicht gefunden.")

        if buch is None:
            raise ValueError("Buch nicht gefunden.")

        gefunden = False

        for ausleihe in person["ausgeliehen"]:
            if ausleihe["buch_id"] == buch_id:
                person["ausgeliehen"].remove(ausleihe)
                gefunden = True
                break

        if not gefunden:
            raise ValueError(
                "Dieses Buch wurde von diesem Nutzer nicht ausgeliehen."
            )

        buch["verfuegbar"] = True

        print("Buch erfolgreich zurückgegeben.")

    except ValueError as fehler:
        print("Fehler:", fehler)


# -----------------------------
# Leihfrist prüfen
# -----------------------------

def pruefe_leihfrist():
    print("\nÜberfällige Ausleihen:")

    for person in nutzer:
        for ausleihe in person["ausgeliehen"]:

            if aktueller_tag > ausleihe["start"] + 14:

                buch = suche_buch(ausleihe["buch_id"])

                print(
                    person["name"],
                    "-",
                    buch["titel"],
                    "(überfällig)"
                )


# -----------------------------
# Vormerken
# -----------------------------

def merke_buch_vor():
    try:
        nutzer_id = int(input("Nutzer-ID: "))
        buch_id = int(input("Buch-ID: "))

        person = suche_nutzer(nutzer_id)
        buch = suche_buch(buch_id)

        if person is None:
            raise ValueError("Nutzer nicht gefunden.")

        if buch is None:
            raise ValueError("Buch nicht gefunden.")

        if buch["verfuegbar"]:
            raise ValueError(
                "Verfügbare Bücher dürfen nicht vorgemerkt werden."
            )

        if buch_id in person["vormerkungen"]:
            raise ValueError("Doppelte Vormerkung nicht erlaubt.")

        person["vormerkungen"].append(buch_id)

        print("Vormerkung erfolgreich.")

    except ValueError as fehler:
        print("Fehler:", fehler)


# -----------------------------
# Statistik
# -----------------------------

def zaehle_buecher_pro_kategorie():
    statistik = {}

    for buch in buecher:

        kat = buch["kategorie"]

        if kat not in statistik:
            statistik[kat] = 0

        statistik[kat] += 1

    print("\nBücher pro Kategorie:")

    for kat in statistik:
        print(kat, ":", statistik[kat])


def finde_top3_buecher():

    sortierte_liste = sorted(
        buecher,
        key=lambda x: x["ausleihen"],
        reverse=True
    )

    print("\nTop 3 Bücher:")

    for platz, buch in enumerate(sortierte_liste[:3], start=1):
        print(
            platz,
            ".",
            buch["titel"],
            "-",
            buch["ausleihen"],
            "Ausleihen"
        )


def erstelle_bibliotheksbericht():

    gesamt = len(buecher)

    verfuegbar = 0

    for buch in buecher:
        if buch["verfuegbar"]:
            verfuegbar += 1

    ausgeliehen = gesamt - verfuegbar

    print("\n===== BIBLIOTHEKSBERICHT =====")
    print("Bücher gesamt:", gesamt)
    print("Verfügbar:", verfuegbar)
    print("Ausgeliehen:", ausgeliehen)

    zaehle_buecher_pro_kategorie()
    finde_top3_buecher()


# -----------------------------
# Tag ändern
# -----------------------------

def aendere_tag():
    global aktueller_tag

    try:
        neuer_tag = int(input("Neuer Tag: "))

        if neuer_tag < 1:
            raise ValueError(
                "Nur ganze Zahlen ab 1 erlaubt."
            )

        aktueller_tag = neuer_tag

    except ValueError as fehler:
        print("Fehler:", fehler)


# -----------------------------
# Hauptprogramm
# -----------------------------

while True:

    print("\n===== HAUPTMENÜ =====")
    print("1 Buch suchen")
    print("2 Buch ausleihen")
    print("3 Buch zurückgeben")
    print("4 Buch vormerken")
    print("5 Bücher / Nutzer anzeigen")
    print("6 Aktuellen Tag ändern")
    print("7 Statistik und Bericht")
    print("8 Buch hinzufügen")
    print("9 Nutzer hinzufügen")
    print("10 Leihfrist prüfen")
    print("0 Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        try:
            buch_id = int(input("Buch-ID: "))
            buch = suche_buch(buch_id)

            if buch:
                print(buch)
            else:
                print("Nicht gefunden.")

        except ValueError:
            print("Ungültige Eingabe.")

    elif auswahl == "2":
        leihe_buch_aus()

    elif auswahl == "3":
        gib_buch_zurueck()

    elif auswahl == "4":
        merke_buch_vor()

    elif auswahl == "5":
        print("\nBücher:")
        for buch in buecher:
            print(buch)

        print("\nNutzer:")
        for person in nutzer:
            print(person)

    elif auswahl == "6":
        aendere_tag()

    elif auswahl == "7":
        erstelle_bibliotheksbericht()

    elif auswahl == "8":
        fuege_buch_hinzu()

    elif auswahl == "9":
        fuege_nutzer_hinzu()

    elif auswahl == "10":
        pruefe_leihfrist()

    elif auswahl == "0":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")