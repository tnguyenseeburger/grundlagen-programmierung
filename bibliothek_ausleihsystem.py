# =====================================
# Bibliotheks- und Ausleihsystem
# =====================================

aktueller_tag = 20

# -----------------------------
# Startdaten
# -----------------------------

buecher = [
    {"id": 101, "titel": "Python Basics", "kategorie": "Informatik", "verfuegbar": True, "ausleihen": 8},
    {"id": 102, "titel": "Algorithmen", "kategorie": "Informatik", "verfuegbar": False, "ausleihen": 12},
    {"id": 103, "titel": "Datenanalyse", "kategorie": "Data Science", "verfuegbar": False, "ausleihen": 10},
    {"id": 104, "titel": "Maschinelles Lernen", "kategorie": "Data Science", "verfuegbar": False, "ausleihen": 5},
    {"id": 105, "titel": "Künstliche Intelligenz", "kategorie": "Data Science", "verfuegbar": True, "ausleihen": 7},
]

nutzer = [
    {   "id": 12,
        "name": "Anna",
        "ausgeliehen": [
            {"buch_id": 102, "start": 7},
            {"buch_id": 103, "start": 7}
        ],
        "vormerkungen": []
    },

    {   "id": 13,
        "name": "Max",
        "ausgeliehen": [
            {"buch_id": 104, "start": 5}
        ],
        "vormerkungen": []
    },

    {   "id": 14,
        "name": "Lisa",
        "ausgeliehen": [],
        "vormerkungen": [
            102, 104
        ]
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


def suche_buecher_text(suchtext):
    suchtext = suchtext.lower()
    treffer = []

    for buch in buecher:
        if (suchtext in buch["titel"].lower()
                or suchtext in buch["kategorie"].lower()):
            treffer.append(buch)

    return treffer


def suche_buecher():
    print("\nSuchart:")
    print("1 Buch-ID")
    print("2 Titel oder Kategorie")
    suchart = input("Auswahl: ")

    if suchart == "1":
        try:
            buch_id = int(input("Buch-ID: "))
            buch = suche_buch(buch_id)

            if buch:
                print(
                    f"\nBuch gefunden: {buch['titel']} "
                    f"(Kategorie: {buch['kategorie']}) - ID: {buch['id']}"
                    f"\nVerfügbar: {'Ja' if buch['verfuegbar'] else 'Nein'}"
                )
            else:
                print("Buch nicht gefunden.")

        except ValueError:
            print("Ungültige Eingabe.")

    elif suchart == "2":
        suchtext = input("Suchtext: ")
        treffer = suche_buecher_text(suchtext)

        if treffer:
            print("\nGefundene Bücher:")
            for buch in treffer:
                print(
                    f"Buch: {buch['titel']} "
                    f"(Kategorie: {buch['kategorie']}) - ID: {buch['id']} - "
                    f"Verfügbar: {'Ja' if buch['verfuegbar'] else 'Nein'}"
                )
        else:
            print("Keine Bücher gefunden.")

    else:
        print("Ungültige Auswahl.")


def suche_nutzer(nutzer_id):
    for person in nutzer:
        if person["id"] == nutzer_id:
            return person
    return None


def suche_nutzer_name(name):
    name = name.lower()
    treffer = []

    for person in nutzer:
        if name in person["name"].lower():
            treffer.append(person)

    return treffer


def suche_nutzer_auswahl():
    print("\nSuchart:")
    print("1 Nutzer-ID")
    print("2 Name")
    suchart = input("Auswahl: ")

    if suchart == "1":
        try:
            nutzer_id = int(input("Nutzer-ID: "))
            person = suche_nutzer(nutzer_id)

            if person:
                ausgelieheneIDs = ""
                for ausleihe in person["ausgeliehen"]:
                    if ausgelieheneIDs:
                        ausgelieheneIDs += ", "
                    ausgelieheneIDs += str(ausleihe["buch_id"])
                vorgemerkteIDs = ""
                for vorgemerkt in person["vormerkungen"]:
                    if vorgemerkteIDs:
                        vorgemerkteIDs += ", "
                    vorgemerkteIDs += str(vorgemerkt)
                print(
                    f"\nNutzer gefunden: {person['name']} "
                    f"(ID: {person['id']})"
                    f"\nAusgeliehene Bücher: {len(person['ausgeliehen']) if len(person['ausgeliehen']) > 0 else ""} {"Stück mit folgenden IDs: " if ausgelieheneIDs else ""}"
                    f"{ausgelieheneIDs if ausgelieheneIDs else 'Keine'}"
                    f"\nVorgemerkte Bücher: {len(person['vormerkungen']) if len(person['vormerkungen']) > 0 else ""} {"Stück mit folgenden IDs: " if vorgemerkteIDs else ""}"
                    f"{vorgemerkteIDs if vorgemerkteIDs else 'Keine'}"
                )
            else:
                print("Nutzer nicht gefunden.")

        except ValueError:
            print("Ungültige Eingabe.")

    elif suchart == "2":
        name = input("Name: ")
        treffer = suche_nutzer_name(name)

        if treffer:
            print("\nGefundene Nutzer:")
            for person in treffer:
                vorgemerkteIDs = ""
                for vorgemerkt in person["vormerkungen"]:
                    if vorgemerkteIDs:
                        vorgemerkteIDs += ", "
                    vorgemerkteIDs += str(vorgemerkt)
                ausgelieheneIDs = ""
                for ausleihe in person["ausgeliehen"]:
                    if ausgelieheneIDs:
                        ausgelieheneIDs += ", "
                    ausgelieheneIDs += str(ausleihe["buch_id"])
                print(
                    f"--- Nutzer: {person['name']} "
                    f"(ID: {person['id']}) ---"
                    f"\nAusgeliehene Bücher: {len(person['ausgeliehen']) if len(person['ausgeliehen']) > 0 else ''} {"Stück mit folgenden IDs: " if ausgelieheneIDs else ""}"
                    f"{ausgelieheneIDs if ausgelieheneIDs else 'Keine'}"
                    f"\nVorgemerkte Bücher: {len(person['vormerkungen']) if len(person['vormerkungen']) > 0 else ''} {"Stück mit folgenden IDs: " if vorgemerkteIDs else ""}"
                    f"{vorgemerkteIDs if vorgemerkteIDs else 'Keine'}"
                )
        else:
            print("Keine Nutzer gefunden.")

    else:
        print("Ungültige Auswahl.")


# -----------------------------
# Anzeigen
# -----------------------------

def zeige_buecher():
    print("\nBücher:")
    for buch in buecher:
        print(f"Buch: {buch['titel']} (Kategorie: {buch['kategorie']}) - ID: {buch['id']} - Verfügbar: {'Ja' if buch['verfuegbar'] else 'Nein'} - Ausleihen: {buch['ausleihen']}")

def zeige_nutzer():
    print("\nNutzer:")
    for person in nutzer:
        print(f"Nutzer: {person['name']} - ID: {person['id']} - Ausgeliehene Bücher: {len(person['ausgeliehen'])} - Vormerkungen: {len(person['vormerkungen'])}")

# -----------------------------
# Hinzufügen
# -----------------------------

def fuege_buch_hinzu():
    try:
        buch_id = int(input("Buch-ID: "))

        if buch_id < 0:
            raise ValueError("Buch-ID darf nicht negativ sein.")
        if suche_buch(buch_id):
            raise ValueError("Diese Buch-ID existiert bereits.")

        titel = input("Titel: ").strip()

        if not titel:
            raise ValueError("Titel darf nicht leer sein.")

        kategorie = input("Kategorie: ").strip()

        if not kategorie:
            raise ValueError("Kategorie darf nicht leer sein.")

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
        if nutzer_id < 0:
            raise ValueError("Nutzer-ID darf nicht negativ sein.")
        if suche_nutzer(nutzer_id):
            raise ValueError("Diese Nutzer-ID existiert bereits.")

        name = input("Name: ").strip()
        if not name:
            raise ValueError("Name darf nicht leer sein.")

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

    platz = 1
    while platz <= len(sortierte_liste[:3]):
        buch = sortierte_liste[platz - 1]
        print(
            platz,
            ".",
            buch["titel"],
            "-",
            buch["ausleihen"],
            "Ausleihen"
        )
        platz += 1


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
# Datenprüfung beim Start
# -----------------------------

def pruefe_datenbestand():
    fehler = []
    buch_ids = set()
    nutzer_ids = set()
    ausgeliehene_buecher = {}

    # Zuerst wird geprüft, ob beide Datensammlungen grundsätzlich Listen sind.
    if not isinstance(buecher, list):
        fehler.append("Die Bücherdaten müssen als Liste vorliegen.")
    if not isinstance(nutzer, list):
        fehler.append("Die Nutzerdaten müssen als Liste vorliegen.")

    if fehler:
        for meldung in fehler:
            print("Datenfehler:", meldung)
        return False

    # Bei jedem Buch werden Pflichtfelder, IDs und Inhaltswerte geprüft.
    erforderliche_buchfelder = {
        "id", "titel", "kategorie", "verfuegbar", "ausleihen"
    }

    position = 1
    while position <= len(buecher):
        buch = buecher[position - 1]
        bezeichnung = f"Buch an Position {position}"

        if not isinstance(buch, dict):
            fehler.append(f"{bezeichnung} muss ein Datensatz sein.")
            position += 1
            continue

        fehlende_felder = erforderliche_buchfelder - buch.keys()
        if fehlende_felder:
            fehler.append(
                f"{bezeichnung} enthält nicht alle Pflichtfelder: "
                f"{', '.join(sorted(fehlende_felder))}."
            )
            position += 1
            continue

        buch_id = buch["id"]
        if not isinstance(buch_id, int) or isinstance(buch_id, bool):
            fehler.append(f"{bezeichnung} hat eine ungültige ID.")
        elif buch_id in buch_ids:
            fehler.append(f"Die Buch-ID {buch_id} ist doppelt vorhanden.")
        else:
            buch_ids.add(buch_id)

        #prüfen, ob Titel und Kategoie leer sind oder keine Strings sind
        if not isinstance(buch["titel"], str) or not buch["titel"].strip():
            fehler.append(f"{bezeichnung} hat keinen gültigen Titel.")
        if (not isinstance(buch["kategorie"], str)
                or not buch["kategorie"].strip()):
            fehler.append(f"{bezeichnung} hat keine gültige Kategorie.")
        #prüfen, ob verfügbar ein bool ist und ausleihen eine positive Zahl
        if not isinstance(buch["verfuegbar"], bool):
            fehler.append(
                f"{bezeichnung} muss bei 'verfuegbar' True oder False enthalten."
            )
        if (not isinstance(buch["ausleihen"], int)
                or isinstance(buch["ausleihen"], bool)
                or buch["ausleihen"] < 0):
            fehler.append(
                f"{bezeichnung} hat eine ungültige Anzahl an Ausleihen."
            )
        position += 1


    # Bei jedem Nutzer werden Pflichtfelder, IDs und Inhaltswerte geprüft.
    erforderliche_nutzerfelder = {
        "id", "name", "ausgeliehen", "vormerkungen"
    }

    position = 1
    while position <= len(nutzer):
        person = nutzer[position - 1]
        bezeichnung = f"Nutzer an Position {position}"

        if not isinstance(person, dict):
            fehler.append(f"{bezeichnung} muss ein Datensatz sein.")
            position += 1
            continue

        #prüfen, ob alle Pflichtfelder vorhanden sind
        fehlende_felder = erforderliche_nutzerfelder - person.keys()
        if fehlende_felder:
            fehler.append(
                f"{bezeichnung} enthält nicht alle Pflichtfelder: "
                f"{', '.join(sorted(fehlende_felder))}."
            )
            position += 1
            continue

        #prüfen, ob die ID ein Integer ist und nicht doppelt vorhanden
        nutzer_id = person["id"]
        if not isinstance(nutzer_id, int) or isinstance(nutzer_id, bool):
            fehler.append(f"{bezeichnung} hat eine ungültige ID.")
        elif nutzer_id in nutzer_ids:
            fehler.append(f"Die Nutzer-ID {nutzer_id} ist doppelt vorhanden.")
        else:
            nutzer_ids.add(nutzer_id)

        # Prüfen, ob Name und Vornamen leer sind oder keine Strings sind.
        if not isinstance(person["name"], str) or not person["name"].strip():
            fehler.append(f"{bezeichnung} hat keinen gültigen Namen.")
        if not isinstance(person["ausgeliehen"], list):
            fehler.append(f"{bezeichnung} hat keine gültige Ausleihliste.")
        if not isinstance(person["vormerkungen"], list):
            fehler.append(f"{bezeichnung} hat keine gültige Vormerkliste.")

        # Prüfen, ob die Ausleihen und Vormerkungen gültige Listen sind.
        if not isinstance(person["ausgeliehen"], list):
            ausgeliehen = []
        else:
            ausgeliehen = person["ausgeliehen"]

        if not isinstance(person["vormerkungen"], list):
            vormerkungen = []
        else:
            vormerkungen = person["vormerkungen"]

        bekannte_vormerkungen = []

        #prüfen, ob die Ausleihen gültige Datensätze sind
        ausleihe_position = 0
        while ausleihe_position < len(ausgeliehen):
            ausleihe = ausgeliehen[ausleihe_position]
            if not isinstance(ausleihe, dict):
                fehler.append(
                    f"{bezeichnung} enthält einen ungültigen Ausleihdatensatz."
                )
                ausleihe_position += 1
                continue

            #prüfen, ob die Ausleihe die Pflichtfelder enthält
            if "buch_id" not in ausleihe or "start" not in ausleihe:
                fehler.append(
                    f"{bezeichnung} enthält eine Ausleihe ohne Pflichtfelder."
                )
                ausleihe_position += 1
                continue

            #prüfen, ob die Buch-ID gültig ist und der Startwert eine positive Zahl ist
            buch_id = ausleihe["buch_id"]
            start = ausleihe["start"]
            if not isinstance(buch_id, int) or isinstance(buch_id, bool):
                fehler.append(
                    f"{bezeichnung} enthält eine ungültige Buch-ID."
                )
                ausleihe_position += 1
                continue
            if buch_id not in buch_ids:
                fehler.append(
                    f"{bezeichnung} verweist auf das unbekannte Buch "
                    f"{buch_id}."
                )
            if (not isinstance(start, int) or isinstance(start, bool)
                    or start < 1):
                fehler.append(
                    f"{bezeichnung} enthält einen ungültigen Ausleihbeginn."
                )

            #prüfen, ob das Buch mehreren Nutzern zugeordnet ist
            if buch_id in ausgeliehene_buecher:
                fehler.append(
                    f"Das Buch {buch_id} ist mehreren Nutzern zugeordnet."
                )
            else:
                ausgeliehene_buecher[buch_id] = nutzer_id
            ausleihe_position += 1

        # Eine Vormerkung darf nur auf ein vorhandenes Buch verweisen.
        vormerkung_position = 0
        while vormerkung_position < len(vormerkungen):
            buch_id = vormerkungen[vormerkung_position]
            if not isinstance(buch_id, int) or isinstance(buch_id, bool):
                fehler.append(
                    f"{bezeichnung} enthält eine Vormerkung mit ungültiger "
                    "Buch-ID."
                )
                vormerkung_position += 1
                continue
            if buch_id in bekannte_vormerkungen:
                fehler.append(
                    f"{bezeichnung} enthält doppelte Vormerkungen."
                )
            bekannte_vormerkungen.append(buch_id)
            if buch_id not in buch_ids:
                fehler.append(
                    f"{bezeichnung} hat eine Vormerkung für das unbekannte "
                    f"Buch {buch_id}."
                )
            vormerkung_position += 1
        position += 1

    # Zum Schluss wird der Verfügbarkeitsstatus mit den aktiven Ausleihen
    # abgeglichen: Ein ausgeliehenes Buch darf nicht verfügbar sein.
    buch_position = 0
    while buch_position < len(buecher):
        buch = buecher[buch_position]
        if not isinstance(buch, dict) or "id" not in buch:
            buch_position += 1
            continue

        buch_id = buch["id"]
        # prüfen, ob die Buch-ID gültig ist
        if not isinstance(buch_id, int) or isinstance(buch_id, bool):
            buch_position += 1
            continue
        ist_ausgeliehen = buch_id in ausgeliehene_buecher
        if ("verfuegbar" in buch
                and buch["verfuegbar"] == ist_ausgeliehen):
            fehler.append(
                f"Buch {buch_id} ist bei 'verfuegbar' widersprüchlich "
                f"zur Ausleihliste."
            )
        buch_position += 1

    if fehler:
        print("\n===== DATENPRÜFUNG FEHLGESCHLAGEN =====")
        for meldung in fehler:
            print("-", meldung)
        print("Das Programm wird wegen fehlerhafter Startdaten beendet.")
        return False

    print("Datenprüfung erfolgreich: Alle Startdaten sind konsistent.")
    return True


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

# der Datenbestand wird beim Start geprüft, um Inkonsistenzen zu erkennen
startDataCorrect = pruefe_datenbestand()

#der Hauptmenü-Loop wird nur gestartet, wenn die Startdaten korrekt sind
while startDataCorrect:

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
    print("10 Nutzer suchen")
    print("11 Leihfristen prüfen")
    print("0 Beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        suche_buecher()

    elif auswahl == "2":
        leihe_buch_aus()

    elif auswahl == "3":
        gib_buch_zurueck()

    elif auswahl == "4":
        merke_buch_vor()

    elif auswahl == "5":
        zeige_buecher()
        zeige_nutzer()

    elif auswahl == "6":
        aendere_tag()

    elif auswahl == "7":
        erstelle_bibliotheksbericht()

    elif auswahl == "8":
        fuege_buch_hinzu()

    elif auswahl == "9":
        fuege_nutzer_hinzu()

    elif auswahl == "10":
        suche_nutzer_auswahl()

    elif auswahl == "11":
        pruefe_leihfrist()

    elif auswahl == "0":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")