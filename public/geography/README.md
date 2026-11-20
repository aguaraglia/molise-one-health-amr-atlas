# Geografia pubblica - edizione Molise

La cartografia pubblica dell'edizione Molise comprende:

- `atlas_region.geojson`: confine regionale ISTAT 2026 (codice 14);
- `atlas_provinces.geojson`: 2 province ISTAT 2026: Campobasso (CB 070) e Isernia (IS 094);
- `atlas_municipalities.geojson`: 136 comuni ISTAT al 1/1/2026.

Fonte: ISTAT, «Confini delle unità amministrative a fini statistici al 1° gennaio 2026», versione generalizzata (Limiti01012026_g.zip, SHA-256 in `metadata/SNAPSHOTS.tsv`), CC BY 4.0. Gli attributi dei DBF sono letti in UTF-8 e le coordinate sono convertite da EPSG:32632 a WGS84 da `scripts/build_istat_geography.py`.

Gli studi della letteratura curata stanno in layer distinti sotto `public/data/`. L'unica struttura nominata (Ospedale A. Cardarelli, Campobasso) è geocodificata tramite OSM Nominatim (1 richiesta al secondo, 2026-11-20; risposte grezze in `raw/nominatim/`). Gli ospedali non nominati negli studi restano sul contorno regionale.
