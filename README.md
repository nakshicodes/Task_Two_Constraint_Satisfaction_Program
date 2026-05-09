# Task 2(a) – Australia Map Colouring (CSP)

A Constraint Satisfaction Problem (CSP) that colours the regions of Australia using **3 colours** (Blue, Red, Green) so that no two adjacent regions share the same colour.

---

## What It Does

Defines the 5 Australian regions and which ones share a border, then uses a **backtracking algorithm** to find a valid colour assignment automatically. The solution is printed to the console and drawn as a map.

---

## Requirements

```bash
pip install matplotlib
```

---

## How to Run

```bash
python Task_Two_Map_of_Australia.py
```

> **Note:** Close the map window for the program to finish.

---

## Regions Covered

| Region | Full Name |
|---|---|
| WA | Western Australia |
| NT | Northern Territory |
| SA | South Australia |
| QLD | Queensland |
| NSW | New South Wales |

---

## How the Algorithm Works

**Backtracking** is a trial-and-error approach:

1. Pick the first uncoloured region
2. Try assigning it a colour
3. Check if that colour conflicts with any already-coloured neighbour
4. If no conflict — move on to the next region
5. If all colours cause a conflict — go back and change the previous region's colour
6. Repeat until all regions are coloured

---

## Output

```
Australia Map Colouring Solution:
------------------------------
  WA:  Blue
  NT:  Red
  SA:  Green
  QLD: Blue
  NSW: Red
```

A map image `australia_colouring.png` is also saved in the same folder.
