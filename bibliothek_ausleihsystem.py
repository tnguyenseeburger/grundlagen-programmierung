# =====================================
# Bibliotheks- und Ausleihsystem
# =====================================

aktueller_tag = 20

ausleihfrist = 14

# -----------------------------
# Startdaten
# -----------------------------

# 55 Buecher und 18 Nutzer.
# 18 Buecher sind aktuell ausgeliehen; Starttage sind gespeichert.
# Vormerkungen beziehen sich nur auf aktuell ausgeliehene Buecher.

buecher = [{'id': 101,
  'titel': 'Python Basics',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 3},
 {'id': 102,
  'titel': 'Algorithmen',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 10},
 {'id': 103,
  'titel': 'Datenanalyse',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 17},
 {'id': 104,
  'titel': 'Mathematik I',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 24},
 {'id': 105,
  'titel': 'Mathematik II',
  'kategorie': 'Mathematik',
  'verfuegbar': False,
  'ausleihen': 7},
 {'id': 106,
  'titel': 'Statistik kompakt',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 14},
 {'id': 107,
  'titel': 'Physik im Alltag',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 21},
 {'id': 108,
  'titel': 'Grundlagen Chemie',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 4},
 {'id': 109,
  'titel': 'Biologie verstehen',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': False,
  'ausleihen': 11},
 {'id': 110,
  'titel': 'Technik und Gesellschaft',
  'kategorie': 'Technik',
  'verfuegbar': True,
  'ausleihen': 18},
 {'id': 111,
  'titel': 'Projektmanagement',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 25},
 {'id': 112,
  'titel': 'BWL Grundlagen',
  'kategorie': 'Wirtschaft',
  'verfuegbar': False,
  'ausleihen': 8},
 {'id': 113,
  'titel': 'Mikrooekonomie',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 15},
 {'id': 114,
  'titel': 'Kommunikation',
  'kategorie': 'Soft Skills',
  'verfuegbar': True,
  'ausleihen': 22},
 {'id': 115,
  'titel': 'Praesentation',
  'kategorie': 'Soft Skills',
  'verfuegbar': True,
  'ausleihen': 5},
 {'id': 116,
  'titel': 'Python Basics 2',
  'kategorie': 'Informatik',
  'verfuegbar': False,
  'ausleihen': 12},
 {'id': 117,
  'titel': 'Algorithmen 2',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 19},
 {'id': 118,
  'titel': 'Datenanalyse 2',
  'kategorie': 'Informatik',
  'verfuegbar': False,
  'ausleihen': 26},
 {'id': 119,
  'titel': 'Mathematik I 2',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 9},
 {'id': 120,
  'titel': 'Mathematik II 2',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 16},
 {'id': 121,
  'titel': 'Statistik kompakt 2',
  'kategorie': 'Mathematik',
  'verfuegbar': False,
  'ausleihen': 23},
 {'id': 122,
  'titel': 'Physik im Alltag 2',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 6},
 {'id': 123,
  'titel': 'Grundlagen Chemie 2',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 13},
 {'id': 124,
  'titel': 'Biologie verstehen 2',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': False,
  'ausleihen': 20},
 {'id': 125,
  'titel': 'Technik und Gesellschaft 2',
  'kategorie': 'Technik',
  'verfuegbar': True,
  'ausleihen': 3},
 {'id': 126,
  'titel': 'Projektmanagement 2',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 10},
 {'id': 127,
  'titel': 'BWL Grundlagen 2',
  'kategorie': 'Wirtschaft',
  'verfuegbar': False,
  'ausleihen': 17},
 {'id': 128,
  'titel': 'Mikrooekonomie 2',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 24},
 {'id': 129,
  'titel': 'Kommunikation 2',
  'kategorie': 'Soft Skills',
  'verfuegbar': True,
  'ausleihen': 7},
 {'id': 130,
  'titel': 'Praesentation 2',
  'kategorie': 'Soft Skills',
  'verfuegbar': False,
  'ausleihen': 14},
 {'id': 131,
  'titel': 'Python Basics 3',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 21},
 {'id': 132,
  'titel': 'Algorithmen 3',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 4},
 {'id': 133,
  'titel': 'Datenanalyse 3',
  'kategorie': 'Informatik',
  'verfuegbar': False,
  'ausleihen': 11},
 {'id': 134,
  'titel': 'Mathematik I 3',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 18},
 {'id': 135,
  'titel': 'Mathematik II 3',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 25},
 {'id': 136,
  'titel': 'Statistik kompakt 3',
  'kategorie': 'Mathematik',
  'verfuegbar': False,
  'ausleihen': 8},
 {'id': 137,
  'titel': 'Physik im Alltag 3',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 15},
 {'id': 138,
  'titel': 'Grundlagen Chemie 3',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 22},
 {'id': 139,
  'titel': 'Biologie verstehen 3',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': False,
  'ausleihen': 5},
 {'id': 140,
  'titel': 'Technik und Gesellschaft 3',
  'kategorie': 'Technik',
  'verfuegbar': True,
  'ausleihen': 12},
 {'id': 141,
  'titel': 'Projektmanagement 3',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 19},
 {'id': 142,
  'titel': 'BWL Grundlagen 3',
  'kategorie': 'Wirtschaft',
  'verfuegbar': False,
  'ausleihen': 26},
 {'id': 143,
  'titel': 'Mikrooekonomie 3',
  'kategorie': 'Wirtschaft',
  'verfuegbar': True,
  'ausleihen': 9},
 {'id': 144,
  'titel': 'Kommunikation 3',
  'kategorie': 'Soft Skills',
  'verfuegbar': True,
  'ausleihen': 16},
 {'id': 145,
  'titel': 'Praesentation 3',
  'kategorie': 'Soft Skills',
  'verfuegbar': False,
  'ausleihen': 23},
 {'id': 146,
  'titel': 'Python Basics 4',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 6},
 {'id': 147,
  'titel': 'Algorithmen 4',
  'kategorie': 'Informatik',
  'verfuegbar': True,
  'ausleihen': 13},
 {'id': 148,
  'titel': 'Datenanalyse 4',
  'kategorie': 'Informatik',
  'verfuegbar': False,
  'ausleihen': 20},
 {'id': 149,
  'titel': 'Mathematik I 4',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 3},
 {'id': 150,
  'titel': 'Mathematik II 4',
  'kategorie': 'Mathematik',
  'verfuegbar': True,
  'ausleihen': 10},
 {'id': 151,
  'titel': 'Statistik kompakt 4',
  'kategorie': 'Mathematik',
  'verfuegbar': False,
  'ausleihen': 17},
 {'id': 152,
  'titel': 'Physik im Alltag 4',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 24},
 {'id': 153,
  'titel': 'Grundlagen Chemie 4',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': False,
  'ausleihen': 7},
 {'id': 154,
  'titel': 'Biologie verstehen 4',
  'kategorie': 'Naturwissenschaft',
  'verfuegbar': True,
  'ausleihen': 14},
 {'id': 155,
  'titel': 'Technik und Gesellschaft 4',
  'kategorie': 'Technik',
  'verfuegbar': False,
  'ausleihen': 21}]

nutzer = [{'id': 1,
  'name': 'Anna',
  'ausgeliehen': [{'buch_id': 105, 'start': 2}, {'buch_id': 112, 'start': 7}],
  'vormerkungen': [109]},
 {'id': 2, 'name': 'David', 'ausgeliehen': [{'buch_id': 109, 'start': 3}], 'vormerkungen': [105]},
 {'id': 3, 'name': 'Sara', 'ausgeliehen': [], 'vormerkungen': [116]},
 {'id': 4, 'name': 'Max', 'ausgeliehen': [{'buch_id': 116, 'start': 6}], 'vormerkungen': [118]},
 {'id': 5, 'name': 'Lena', 'ausgeliehen': [{'buch_id': 118, 'start': 7}], 'vormerkungen': [121]},
 {'id': 6, 'name': 'Jonas', 'ausgeliehen': [{'buch_id': 121, 'start': 8}], 'vormerkungen': [124]},
 {'id': 7, 'name': 'Mira', 'ausgeliehen': [{'buch_id': 124, 'start': 10}], 'vormerkungen': [127]},
 {'id': 8, 'name': 'Leon', 'ausgeliehen': [{'buch_id': 127, 'start': 11}], 'vormerkungen': [130]},
 {'id': 9, 'name': 'Nora', 'ausgeliehen': [{'buch_id': 130, 'start': 12}], 'vormerkungen': []},
 {'id': 10, 'name': 'Emil', 'ausgeliehen': [{'buch_id': 133, 'start': 13}], 'vormerkungen': []},
 {'id': 11, 'name': 'Sofia', 'ausgeliehen': [{'buch_id': 136, 'start': 14}], 'vormerkungen': []},
 {'id': 12, 'name': 'Paul', 'ausgeliehen': [{'buch_id': 139, 'start': 15}], 'vormerkungen': []},
 {'id': 13, 'name': 'Maja', 'ausgeliehen': [{'buch_id': 142, 'start': 16}], 'vormerkungen': []},
 {'id': 14, 'name': 'Felix', 'ausgeliehen': [{'buch_id': 145, 'start': 17}], 'vormerkungen': []},
 {'id': 15, 'name': 'Clara', 'ausgeliehen': [{'buch_id': 148, 'start': 18}], 'vormerkungen': []},
 {'id': 16, 'name': 'Tim', 'ausgeliehen': [{'buch_id': 151, 'start': 4}], 'vormerkungen': []},
 {'id': 17, 'name': 'Laura', 'ausgeliehen': [{'buch_id': 153, 'start': 9}], 'vormerkungen': []},
 {'id': 18, 'name': 'Noah', 'ausgeliehen': [{'buch_id': 155, 'start': 19}], 'vormerkungen': []}]

aktueller_tag = 20



# -----------------------------
# Suchfunktionen
# -----------------------------

def suche_buch(buch_id):
    for buch in buecher:
        if buch["id"] == buch_id:
            return buch
    return None

def suche_buecher(suchart, suche):
    if suchart == "1":
        
        buch_id = int(suche)
        buch = suche_buch(buch_id)
        return [buch] if buch else []

        

    elif suchart == "2":
        suche = suche.lower()
        treffer = []     
        for buch in buecher:
            if (suche in buch["titel"].lower() or suche in buch["kategorie"].lower()):
                treffer.append(buch)
        return treffer

    else:
        return None


def suche_nutzer(nutzer_id):
    for person in nutzer:
        if person["id"] == nutzer_id:
            return person
    return None


def suche_nutzer_auswahl(suchart, suche):
    if suchart == "1":
        nutzer_id = int(suche)
        person = suche_nutzer(nutzer_id)
        return [person] if person else []

    elif suchart == "2":
        suche = suche.lower()
        treffer = []
        for person in nutzer:
            if suche in person["name"].lower():
                treffer.append(person)
        return treffer
    else:
        return None

# -----------------------------
# Hinzufügen
# -----------------------------

def fuege_buch_hinzu(buch_id, titel, kategorie):
    if buch_id < 0:
        raise ValueError("Buch-ID darf nicht negativ sein.")
    if suche_buch(buch_id):
        raise ValueError("Diese Buch-ID existiert bereits.")

    if not titel:
        raise ValueError("Titel darf nicht leer sein.")

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


def fuege_nutzer_hinzu(nutzer_id, name):
    if nutzer_id < 0:
        raise ValueError("Nutzer-ID darf nicht negativ sein.")
    if suche_nutzer(nutzer_id):
        raise ValueError("Diese Nutzer-ID existiert bereits.")

    if not name:
        raise ValueError("Name darf nicht leer sein.")

    neuer_nutzer = {
        "id": nutzer_id,
        "name": name,
        "ausgeliehen": [],
        "vormerkungen": []
    }

    nutzer.append(neuer_nutzer)


# -----------------------------
# Ausleihen
# -----------------------------

def leihe_buch_aus(nutzer_id, buch_id):
    
    person = suche_nutzer(nutzer_id)
    buch = suche_buch(buch_id)

    if person is None:
        raise ValueError("Nutzer nicht gefunden.")

    if buch is None:
        raise ValueError("Buch nicht gefunden.")

    if not buch["verfuegbar"]:       
        raise ValueError("Buch ist bereits ausgeliehen. Bitte vormerken.")

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

    return aktueller_tag + ausleihfrist
    
# -----------------------------
# Rückgabe
# -----------------------------

def gib_buch_zurueck(nutzer_id, buch_id):
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

    return



# -----------------------------
# Leihfrist prüfen
# -----------------------------

def pruefe_leihfrist():
    ueberfaellige_ausleihen = []

    for person in nutzer:
        for ausleihe in person["ausgeliehen"]:
            if aktueller_tag > ausleihe["start"] + ausleihfrist:
                buch = suche_buch(ausleihe["buch_id"])
                ueberfaellige_ausleihen.append(
                    (person["name"], buch["titel"])
                )

    return ueberfaellige_ausleihen


# -----------------------------
# Vormerken
# -----------------------------

def merke_buch_vor(nutzer_id, buch_id):
    person = suche_nutzer(nutzer_id)
    buch = suche_buch(buch_id)

    if person is None:
        raise ValueError("Nutzer nicht gefunden.")

    if buch is None:
        raise ValueError("Buch nicht gefunden.")

    if buch["verfuegbar"]:
        raise ValueError("Verfügbare Bücher dürfen nicht vorgemerkt werden.")

    if buch_id in person["vormerkungen"]:
        raise ValueError("Doppelte Vormerkung nicht erlaubt.")

    person["vormerkungen"].append(buch_id)

    return


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

    return statistik


def finde_top3_buecher():
    sortierte_liste = sorted(
        buecher,
        key=lambda x: x["ausleihen"],
        reverse=True
    )

    return sortierte_liste[:3]


def erstelle_bibliotheksbericht():
    gesamt = len(buecher)
    verfuegbar = 0
    for buch in buecher:
        if buch["verfuegbar"]:
            verfuegbar += 1

    ausgeliehen = gesamt - verfuegbar

    statistik = zaehle_buecher_pro_kategorie()
    top3 = finde_top3_buecher()

    return gesamt, verfuegbar, ausgeliehen, statistik, top3


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

def aendere_tag(neuer_tag):
    global aktueller_tag

    if not neuer_tag.isdigit():
        raise ValueError(
            "Eingabe keine ganze Zahl. Nur ganze Zahlen ab 1 erlaubt."
        )
    neuer_tag = int(neuer_tag)
    if neuer_tag < 1:
        raise ValueError(
            "Eingabe unter 1. Nur ganze Zahlen ab 1 erlaubt."
        )

    aktueller_tag = neuer_tag


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

    auswahl = input("\nAuswahl: ")

    if auswahl == "1":
        try:
            print("\nSuchart:")
            print("1 Buch-ID")
            print("2 Titel oder Kategorie")
            suchart = input("Auswahl: ")
            suche = input("Suchtext: ")
            treffer = suche_buecher(suchart, suche)
            if treffer:
                ausgeliehenVon = None
                ausgeliehenBis = None
                for buch in treffer:
                    if not buch["verfuegbar"]:
                        for person in nutzer:
                            for ausleihe in person["ausgeliehen"]:
                                if ausleihe["buch_id"] == buch["id"]:
                                    ausgeliehenVon = person["id"]
                                ausgeliehenBis = ausleihe["start"] + ausleihfrist
                                break
                    print(
                        f"\nBuch gefunden: {buch['titel']} "
                        f"(Kategorie: {buch['kategorie']}) - ID: {buch['id']}"
                        f"\nVerfügbar: {'Ja' if buch['verfuegbar'] else 'Nein, ausgeliehen von Nutzer-ID: ' + str(ausgeliehenVon) if ausgeliehenVon else ""}"
                        f"{'\nVoraussichtlich wieder verfügbar ab Tag: ' + str(ausgeliehenBis) if ausgeliehenBis else ''}"
                    )
            else:
                print("Keine Bücher gefunden.")
        except ValueError:
            print("Ungültige Eingabe.")

    elif auswahl == "2":
        try:
            nutzer_id = int(input("Nutzer-ID: "))
            buch_id = int(input("Buch-ID: "))
            ausgeliehenBis = leihe_buch_aus(nutzer_id, buch_id)
            print("Ausleihe erfolgreich.")
            print("Rückgabe spätestens an Tag", ausgeliehenBis)
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "3":
        try:
            nutzer_id = int(input("Nutzer-ID: "))
            buch_id = int(input("Buch-ID: "))
            gib_buch_zurueck(nutzer_id, buch_id)
            print("Buch erfolgreich zurückgegeben.")
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "4":
        try:
            nutzer_id = int(input("Nutzer-ID: "))
            buch_id = int(input("Buch-ID: "))
            merke_buch_vor(nutzer_id, buch_id)
            print("Vormerkung erfolgreich.")
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "5":
        print("\nBücher:")
        for buch in buecher:
            print(f"Buch: {buch['titel']} (Kategorie: {buch['kategorie']}) - ID: {buch['id']} - Verfügbar: {'Ja' if buch['verfuegbar'] else 'Nein'} - Ausleihen: {buch['ausleihen']}")

        print("\nNutzer:")
        for person in nutzer:
            print(f"Nutzer: {person['name']} - ID: {person['id']} - Ausgeliehene Bücher: {len(person['ausgeliehen'])} - Vormerkungen: {len(person['vormerkungen'])}")

    elif auswahl == "6":
        try:
            neuer_tag = input("Neuer Tag: ")
            aendere_tag(neuer_tag)
            print("Aktueller Tag erfolgreich geändert auf:", aktueller_tag)
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "7":
        gesamt, verfuegbar, ausgeliehen, statistik, top3 = (
            erstelle_bibliotheksbericht()
        )

        print("\n===== BIBLIOTHEKSBERICHT =====")
        print("Bücher gesamt:", gesamt)
        print("Verfügbar:", verfuegbar)
        print("Ausgeliehen:", ausgeliehen)

        print("\nBücher pro Kategorie:")
        for kat in statistik:
            print(kat, ":", statistik[kat])

        print("\nTop 3 Bücher:")
        platz = 1
        while platz <= len(top3):
            buch = top3[platz - 1]
            print(f"{platz}. {buch['titel']} - {buch['ausleihen']} Ausleihen")
            platz += 1

    elif auswahl == "8":
        try:
            buch_id = int(input("Buch-ID: "))
            titel = input("Titel: ").strip()
            kategorie = input("Kategorie: ").strip()
            fuege_buch_hinzu(buch_id, titel, kategorie)
            print("Buch erfolgreich hinzugefügt.")
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "9":
        try:
            nutzer_id = int(input("Nutzer-ID: "))
            name = input("Name: ").strip()
            fuege_nutzer_hinzu(nutzer_id, name)
            print("Nutzer erfolgreich hinzugefügt.")
        except ValueError as fehler:
            print("Fehler:", fehler)

    elif auswahl == "10":
        try:
            print("\nSuchart:")
            print("1 Nutzer-ID")
            print("2 Name")
            suchart = input("Auswahl: ")
            if suchart == "1":
                suche = input("Nutzer-ID: ")
            else:
                suche = input("Suchtext: ")
            treffer = suche_nutzer_auswahl(suchart, suche)

            if treffer:
                if suchart == "1":
                    meldung = "Nutzer gefunden:"
                else:
                    print("\nGefundene Nutzer:")

                for person in treffer:
                    ausgeliehene_ids = ", ".join(
                        str(ausleihe["buch_id"])
                        for ausleihe in person["ausgeliehen"]
                    )
                    vorgemerkte_ids = ", ".join(
                        str(buch_id) for buch_id in person["vormerkungen"]
                    )
                    anzahl_ausgeliehen = (
                        len(person["ausgeliehen"])
                        if person["ausgeliehen"] else ""
                    )
                    anzahl_vorgemerkt = (
                        len(person["vormerkungen"])
                        if person["vormerkungen"] else ""
                    )

                    if suchart == "1":
                        print(
                            f"\n{meldung} {person['name']} "
                            f"(ID: {person['id']})"
                        )
                    else:
                        print(
                            f"--- Nutzer: {person['name']} "
                            f"(ID: {person['id']}) ---"
                        )
                    print(
                        f"Ausgeliehene Bücher: {anzahl_ausgeliehen} "
                        f"{'Stück mit folgenden IDs: ' if ausgeliehene_ids else ''}"
                        f"{ausgeliehene_ids if ausgeliehene_ids else 'Keine'}"
                    )
                    print(
                        f"Vorgemerkte Bücher: {anzahl_vorgemerkt} "
                        f"{'Stück mit folgenden IDs: ' if vorgemerkte_ids else ''}"
                        f"{vorgemerkte_ids if vorgemerkte_ids else 'Keine'}"
                    )
            elif suchart == "1":
                print("Nutzer nicht gefunden.")
            elif suchart == "2":
                print("Keine Nutzer gefunden.")
            else:
                print("Ungültige Auswahl.")
        except ValueError:
            print("Ungültige Eingabe.")

    elif auswahl == "11":
        ueberfaellige_ausleihen = pruefe_leihfrist()
        print("\nÜberfällige Ausleihen:")
        for name, titel in ueberfaellige_ausleihen:
            print(name, "-", titel, "(überfällig)")

    elif auswahl == "0":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")