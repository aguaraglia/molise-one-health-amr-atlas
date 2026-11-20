# Molise One Health AMR Atlas

Edizione regionale `molise_amr_atlas`, pubblicata da Codex Vitae ETS sulla stessa
base delle edizioni Abruzzo e Lazio.

## Stato

La letteratura pubblicata con collegamento territoriale esplicito al Molise
è un corpus piccolo e quasi tutto ospedaliero. Ne restano 11 inclusi
(20 novembre 2026): 1 di struttura, 3 di comune e 7 a scala regionale.

Una sola struttura nominata, georiferita con Nominatim (© OpenStreetMap
contributors, ODbL):

- Ospedale A. Cardarelli (Campobasso): 1 studio (PPS ECDC).

Gli articoli dei sette studi regionali non nominano l'ospedale: parlano di
un ospedale del Molise, dell'ospedale hub o di due ospedali. Nessuna
struttura è stata dedotta e gli studi stanno sul contorno della regione.

Studi con provincia: Campobasso 3 (carni al dettaglio a Campobasso; Cardarelli;
depuratori di Termoli e Campobasso), Isernia 1 (abbeveratoi di Frosolone,
Carpinone e Civitanova del Sannio).

L'IZS dell'Abruzzo e del Molise copre entrambe le regioni: sono inclusi solo
gli studi che separano i dati molisani.

L'edizione pubblica AR-ISS 2024 (copertura 67,0%, tre laboratori: Veneziale
di Isernia, San Timoteo di Termoli e Cardarelli di Campobasso, numerosità
molto piccole, 21-132 isolati, CC BY 4.0; attribuzione Istituto Superiore di
Sanità) e AIFA Open Data 2024, antibatterici J01 (CC BY 4.0; attribuzione
Agenzia Italiana del Farmaco). Non è stato trovato un rapporto ISTISAN o ISS
regionale sul Molise.

Sei layer (AMR umana, veterinaria, alimentare, ambientale, fauna selvatica,
contorno regionale):

- AMR umana: 1 elemento, 1 studio (punto del Cardarelli);
- AMR veterinaria: nessun elemento, nessuna evidenza pubblicata;
- AMR alimentare: 1 elemento (Campobasso), 1 studio;
- AMR ambientale: 2 elementi, 2 studi (Termoli e Campobasso; Frosolone, Carpinone e Civitanova del Sannio);
- AMR nella fauna selvatica: nessun elemento, nessuna evidenza pubblicata;
- studi a scala regionale: 1 elemento, 7 studi umani sul contorno.

I layer vuoti e le aree senza segnaposto sono nessuna evidenza pubblicata,
non resistenza zero. Ogni popup cita lo studio e il DOI (o il record PubMed
se il DOI non è assegnato) e ricorda che il segnaposto è il luogo dello
studio, non una prevalenza.

Confini ISTAT 2026 (136 comuni, 2 province, regione 14), letti in UTF-8.
Regione Molise, open data regionali, ASReM, ARPA Molise, IZSAM e il PDF
OsMed sono esclusi: vedi `metadata/EXCLUDED_SOURCES.md`.

Il conteggio in homepage e in pubblicazioni legge
`public/data/literature-catalog.json` (11).

## Pagine

Sorgente su `main`. Il sito statico è pubblicato dal branch `gh-pages`
(GitHub Pages, cartella `/`). Nessun file `CNAME`. Analitica: GoatCounter
`https://atlanteamr.goatcounter.com/count`, come le edizioni Abruzzo e Lazio.

## Build locale

```bash
python3 -m http.server 8000
```

Aprire `http://localhost:8000/`.

Per rigenerare i dati pubblici servono gli input in `raw/` e, per i confini,
l'archivio ISTAT indicato in `metadata/SNAPSHOTS.tsv`. I DBF ISTAT si leggono
in UTF-8:

```bash
pip install -r requirements-geodata.txt
python3 scripts/build_istat_geography.py --source-root <Limiti01012026_g> --output-root public/geography
python3 scripts/build_literature_catalog.py
python3 scripts/build_study_evidence_layers.py
```

## Directory

- `public/`: dati e asset approvati per il sito;
- `metadata/`: fonti, snapshot, ambito pubblico e fonti escluse;
- `raw/`: curatela, esummary e risposte Nominatim;
- `scripts/`: ricostruzione del catalogo e dei layer;
- `private/`: nessun dato riservato in questa edizione.
