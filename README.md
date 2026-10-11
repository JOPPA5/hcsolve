# hcsolve

Repo na lúštenie historických šifier dvojicou AI agentov:

- **Solver** – hlavný agent, predvolene **GPT**. Zoženie šifru a kontext, lúšti a na konci vyrobí PDF správu.
- **Reviewer** – druhý agent od iného poskytovateľa, predvolene **Claude**. Nezávisle preverí, čo solver tvrdí.

Solver po review svoje riešenie opraví a až potom ho uzavrie.

> **Ak si agent a práve si načítal toto repo:** tento súbor je tvoje zadanie. Najprv si urči rolu (nižšie), potom zisti stav šifry a pokračuj presne od neho.

## Ktorá rola som

1. Ak ti rolu určil prompt, ktorým ťa spustili (`solver` / `reviewer`), platí prompt.
2. Inak platí predvolená rola zo súboru, ktorý si tvoj nástroj načítal pri štarte: `AGENTS.md` → **solver**, `CLAUDE.md` → **reviewer**.
3. Ak si nenačítal ani jeden, rolu neháď a opýtaj sa.

Rola musí sedieť so stavom šifry (tabuľka nižšie). Ak nie si na ťahu, nič nerob a povedz to.

Ak nevieš, na ktorej šifre robiť, a prompt to nehovorí, opýtaj sa. Nevyberaj si sám.

## Štruktúra

Každá šifra má vlastný priečinok `ciphers/<slug>/` (slug malými písmenami s pomlčkami, napr. `ciphers/copiale/`):

```
ciphers/<slug>/
  source/        pôvodná šifra a kontext – po stiahnutí sa nemení
  SOURCES.md     odkiaľ pochádza každý súbor v source/ (URL, dátum, čo to je)
  work/          skripty, pokusy, medzivýsledky
  NOTES.md       priebežný denník: hypotézy, čo sa skúšalo, čo zlyhalo a prečo
  SOLUTION.md    aktuálne tvrdenie solvera
  review/        REVIEW1.md, REVIEW2.md … – píše sem iba reviewer
  report/        report.pdf a jeho zdroj
  DONE1, REVIEWED1, FINAL …   značky stavu (pozri nižšie)
```

## Protokol: značky stavu

Agenti si odovzdávajú prácu **prázdnymi súbormi-značkami** v priečinku šifry. Na ich vznik počúva externý watcher a zobudí druhého agenta. Značka je teda signál aj záznam stavu.

| Značka | Kto ju vytvorí | Čo znamená | Koho zobudí |
|---|---|---|---|
| `DONEn` | solver | „myslím si, že mám hotovo, kolo *n*" | reviewera |
| `REVIEWEDn` | reviewer | „`review/REVIEWn.md` je dopísané" | solvera |
| `FINAL` | solver | pripomienky zapracované, `report/report.pdf` existuje | nikoho – koniec |

Pravidlá pre značky:

- **Značka sa vytvára ako úplne posledný krok.** Najprv dopíš všetky súbory, až potom značku. Watcher zobudí druhého agenta okamžite a ten nesmie nájsť rozpísanú prácu.
- Do značky napíš jeden riadok: čas v UTC a svoj model (napr. `2026-10-11T19:20Z claude-opus-5-5`).
- Po vytvorení značky **skonči ťah a nič ďalšie v priečinku nemeň**. Nečakaj v slučke, nespúšťaj druhého agenta sám – zobudí ťa watcher.
- Značky sa nemažú ani neprepisujú. Ďalšie kolo má ďalšie číslo.

### Ako zistiť stav po načítaní repa

Pozri sa, ktoré značky v `ciphers/<slug>/` existujú:

| Stav | Na ťahu | Čo robiť |
|---|---|---|
| priečinok neexistuje alebo je bez značiek | solver | lúštiť |
| najvyššie je `DONEn`, chýba `REVIEWEDn` | reviewer | spraviť review kola *n* |
| najvyššie je `REVIEWEDn` | solver | zapracovať review, potom `FINAL` alebo `DONEn+1` |
| existuje `FINAL` | nikto | hotovo, nič nemeň bez pokynu človeka |

## Inštrukcie pre solvera

**1. Príprava.** Ak `ciphers/<slug>/source/` neexistuje alebo je prázdny, stiahni šifru (prepis aj skeny, ak sú) a historický kontext: kto, kedy, komu, v akom jazyku, aké šifry sa vtedy a tam používali. Každý súbor zapíš do `SOURCES.md`. Súbory v `source/` potom už neupravuj – pracovné kópie patria do `work/`.

**2. Lúštenie.** Priebežne píš `NOTES.md`, vrátane slepých uličiek – reviewer aj ty po prebudení z nich vychádzate. Všetko, čo sa dá, rob skriptom vo `work/`, nie ručne.

**3. Čestnosť voči zdrojom.** Ak pri hľadaní kontextu narazíš na už publikované riešenie, zapíš to do `SOURCES.md` a `SOLUTION.md` a nevydávaj ho za vlastné. Čiastočné riešenie označ ako čiastočné.

**4. Odovzdanie (`DONEn`).** Keď si myslíš, že si hotový, napíš `SOLUTION.md`:

- typ šifry a kľúč (tabuľka substitúcie, nomenklátor, kľúčové slovo…)
- plaintext v pôvodnom jazyku a jeho preklad
- **jeden príkaz**, ktorý zo súboru v `source/` a kľúča vyrobí celý plaintext
- čo ostáva neisté: nerozlúštené znaky, hádané slová, alternatívne čítania
- prečo si myslíš, že je to správne (pokrytie textu, zmysluplnosť, zhoda s kontextom)

Až potom vytvor `DONEn` a skonči.

**5. Po prebudení (`REVIEWEDn`).** Prečítaj `review/REVIEWn.md` a pridaj do `SOLUTION.md` sekciu `## Odpoveď na review n`, kde ku každej pripomienke uvedieš, čo si opravil, alebo prečo s ňou nesúhlasíš (s dôkazom). Potom:

- verdikt `ACCEPT`, alebo `REVISE` a pripomienky si zapracoval → vyrob PDF a vytvor `FINAL`
- verdikt `REJECT`, alebo si riešenie podstatne zmenil → vytvor `DONEn+1` a nechaj to preveriť znova

**6. PDF správa.** `report/report.pdf` (zdroj nechaj vedľa, napr. `report/report.md`) obsahuje: pôvod a kontext šifry, postup, kľúč, plaintext a preklad, čo ostalo neisté, zhrnutie review a čo sa po ňom zmenilo. Píš ju pre človeka, ktorý nevidel nič z `work/`.

## Inštrukcie pre reviewera

Tvoja úloha je **pokúsiť sa riešenie vyvrátiť**, nie ho potvrdiť. Solverovým tvrdeniam never, kým si ich sám neoveríš.

- Zapisuješ **iba** do `review/`. Solverove súbory ani `source/` nemeň; vlastné overovacie skripty daj do `review/work/`.
- Spusti príkaz zo `SOLUTION.md` a porovnaj výstup s tvrdeným plaintextom. Ak sa dá, dešifruj aj vlastným nezávislým skriptom.
- Over, že kľúč je konzistentný a pokrýva **celý** šifrový text, nie len vybrané pasáže.
- Over prepis proti skenom v `source/`, ak sú.
- Posúď plaintext: je to skutočný jazyk danej doby, alebo náhodné slová natlačené na šum? Sedia mená, dátumy a miesta s kontextom?
- Skontroluj, či solver priznal všetky neistoty a či nepoužil publikované riešenie bez uvedenia.

Výsledok napíš do `review/REVIEWn.md`:

- **Verdikt** na prvom riadku: `ACCEPT`, `REVISE` alebo `REJECT`
- čo si overil a ako (príkazy, výstupy)
- číslované pripomienky, každá s dôkazom a závažnosťou (`blocker` / `major` / `minor`)
- čo si overiť nevedel

Až potom vytvor `REVIEWEDn` a skonči. Riešenie neopravuj sám – to je práca solvera.

## Pre človeka: watcher

Repo watcher neobsahuje. Stačí čokoľvek, čo sleduje `ciphers/*/` a pri vzniku `DONE*` spustí reviewera, pri vzniku `REVIEWED*` solvera – s promptom, ktorý uvedie rolu a cestu k šifre.
