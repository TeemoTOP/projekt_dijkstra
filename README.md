# Projekt Dijkstra

## **Opis Projektu**

Celem projektu jest implementacja algorytmu Dijkstry w celu znalezienia najkrótszej ścieżki między wybranymi wierzchołkami w grafie oraz analiza wydajności algorytmu w różnych typach grafów (skierowane, nieskierowane).

## **Struktura Projektu**

```
projekt_dijkstra/
├── src/
│   ├── graph.py
│   ├── priority_queue.py
│   └── dijkstra.py
├── tests/
│   └── test_dijkstra.py
├── docs/
│   └── documentation.pdf
└── README.md
```
## **Zawartość Katalogów**

- `src/`: Zawiera źródłowy kod projektu.
  - `graph.py`: Klasa reprezentująca graf.
  - `priority_queue.py`: Implementacja kolejki priorytetowej opartej na kopcu binarnym.
  - `dijkstra.py`: Implementacja algorytmu Dijkstry oraz funkcji do rekonstrukcji ścieżki.

- `tests/`: Zawiera testy jednostkowe.
  - `test_dijkstra.py`: Testy dla algorytmu Dijkstry.

- `docs/`: Zawiera dokumentację projektu.
  - `documentation.pdf`: Dokumentacja techniczna projektu.

- `README.md`: Ten plik.

- `requirements.txt`: Lista zależności projektu.

## **Instalacja**

### **Wymagania**

- Python 3.8+
- Biblioteki:
  - `unittest` (wbudowana w Pythonie)
  - `matplotlib`

### **Kroki Instalacji**

1. **Klonowanie Repozytorium**

   ```bash
   git clone https://github.com/TeemoTOP/projekt_dijkstra.git
   cd projekt_dijkstra
2. **Instalacja Zależności**
```console
pip install -r requirements.txt
```

## **Uruchomienie Aplikacji**

Przejdź do katalogu src/ i uruchom skrypt dijkstra.py:

```console
cd src
python dijkstra.py

```
## **Uruchomienie Testów Jednostkowych**
Przejdź do katalogu głównego projektu i uruchom testy za pomocą unittest:

```
cd ..
python -m unittest discover -s tests
```

