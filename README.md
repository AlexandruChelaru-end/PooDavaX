Această aplicație este un microserviciu de tip CLI (Command Line Interface) implementat în Python, care oferă operații matematice de bază:
- Ridicarea la putere (`pow`)
- Calculul numărului Fibonacci de ordin `n`
- Calculul factorialului unui număr
Toate cererile sunt validate cu Pydantic și persistate într-o bază de date locală SQLite, conform cerințelor temei.

- `click` – CLI framework pentru parsingul de argumente
- `pydantic` – validare input (modelare tipuri)
- `sqlite3` – bază de date locală
- `flake8` – pentru stil și linting

Arhitectură și organizare
Proiectul este structurat pe module separate:
- cli.py # Interfața CLI
- logic.py # Implementarea funcțiilor matematice
- models.py # Modele Pydantic pentru validarea inputului
- storage.py # Salvare în baza de date SQLite
- requirements.txt # Librării necesare
- .flake8 # Configurare linting

Rulează comenzi din CLI
python cli.py pow --base 2 --exp 5
Output: Rezultat: 32
python cli.py fib --n 10
Output: Rezultat: 55
python cli.py fact --n 6
Output: Rezultat: 720

Aplicația creează automat fișierul requests.db în care salvează:
-numele operației
-inputul primit
-rezultatul returnat
