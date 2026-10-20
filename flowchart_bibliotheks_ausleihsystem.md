# Flowchart: Bibliotheks- und Ausleihsystem

Das folgende Flowchart bildet den Ablauf des Programms
`bibliothek_ausleihsystem.py` ab.

```mermaid
flowchart TD
    A([Programmstart]) --> B[Datenbestand prüfen]
    B --> C{Startdaten korrekt?}
    C -- Nein --> D[Fehlermeldungen ausgeben]
    D --> E([Programm beendet])
    C -- Ja --> F[Hauptmenü anzeigen]

    F --> G{Auswahl}
    G -- "1: Buch suchen" --> H[Buchsuche]
    G -- "2: Buch ausleihen" --> I[Ausleihe]
    G -- "3: Buch zurückgeben" --> J[Rückgabe]
    G -- "4: Buch vormerken" --> K[Vormerkung]
    G -- "5: Bücher/Nutzer anzeigen" --> L[Bestände anzeigen]
    G -- "6: Aktuellen Tag ändern" --> M[Tag ändern]
    G -- "7: Statistik und Bericht" --> N[Bericht erstellen]
    G -- "8: Buch hinzufügen" --> O[Buch hinzufügen]
    G -- "9: Nutzer hinzufügen" --> P[Nutzer hinzufügen]
    G -- "10: Nutzer suchen" --> Q[Nutzersuche]
    G -- "11: Leihfristen prüfen" --> R[Überfällige Ausleihen anzeigen]
    G -- "0: Beenden" --> S[Programm beendet]
    G -- Sonstige Eingabe --> T[Ungültige Auswahl melden]

    H --> F
    L --> F
    M --> F
    N --> F
    O --> F
    P --> F
    Q --> F
    R --> F
    T --> F

    I --> I1[Nutzer-ID und Buch-ID einlesen]
    I1 --> I2{Nutzer und Buch vorhanden?}
    I2 -- Nein --> I3[Fehler melden]
    I2 -- Ja --> I4{Buch verfügbar?}
    I4 -- Nein --> I3
    I4 -- Ja --> I5{Weniger als 5 Ausleihen?}
    I5 -- Nein --> I3
    I5 -- Ja --> I6[Ausleihe speichern]
    I6 --> I7[Buch als nicht verfügbar markieren]
    I7 --> I8[Ausleihzähler erhöhen]
    I8 --> I9[Vormerkung des Nutzers entfernen]
    I9 --> I10[Erfolg und Rückgabefrist ausgeben]
    I3 --> F
    I10 --> F

    J --> J1[Nutzer-ID und Buch-ID einlesen]
    J1 --> J2{Nutzer und Buch vorhanden?}
    J2 -- Nein --> J3[Fehler melden]
    J2 -- Ja --> J4{Nutzer hat dieses Buch ausgeliehen?}
    J4 -- Nein --> J3
    J4 -- Ja --> J5[Ausleihe aus Nutzerliste entfernen]
    J5 --> J6[Buch als verfügbar markieren]
    J6 --> J7[Erfolg melden]
    J3 --> F
    J7 --> F

    K --> K1[Nutzer-ID und Buch-ID einlesen]
    K1 --> K2{Nutzer und Buch vorhanden?}
    K2 -- Nein --> K3[Fehler melden]
    K2 -- Ja --> K4{Buch ist verfügbar?}
    K4 -- Ja --> K3
    K4 -- Nein --> K5{Bereits vorgemerkt?}
    K5 -- Ja --> K3
    K5 -- Nein --> K6[Vormerkung speichern]
    K6 --> K7[Erfolg melden]
    K3 --> F
    K7 --> F

    S --> E

    subgraph SUCHE_BUCH["Buchsuche"]
        H1{Suchart}
        H2[Buch-ID eingeben und Buch suchen]
        H3[Titel/Kategorie eingeben und Treffer suchen]
        H4[Suchergebnis oder Fehlermeldung ausgeben]
        H1 -- ID --> H2
        H1 -- Titel/Kategorie --> H3
        H2 --> H4
        H3 --> H4
    end
    H -.-> H1

    subgraph DATENPRUEFUNG["Datenprüfung beim Start"]
        V1[Bücher- und Nutzerdaten als Listen prüfen]
        V2[Bücher: Pflichtfelder, IDs und Werte prüfen]
        V3[Nutzer: Pflichtfelder, IDs und Listen prüfen]
        V4[Ausleihen und Vormerkungen prüfen]
        V5[Verfügbarkeit mit aktiven Ausleihen abgleichen]
        V1 --> V2 --> V3 --> V4 --> V5
    end
    B -.-> V1
```

## Legende

- **Abgerundete Knoten**: Start oder Ende des Programms
- **Rechteckige Knoten**: Verarbeitung oder Ausgabe
- **Rauten**: Entscheidungen bzw. Bedingungen
- **Graue Abschnitte**: genauerer Ablauf in einem verarbeitenden Knoten
- **Pfeil zurück zum Hauptmenü**: Die Funktion ist abgeschlossen und der
  Menüzyklus wird fortgesetzt
