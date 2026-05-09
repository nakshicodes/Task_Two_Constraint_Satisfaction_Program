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

# Task 2(b) – Nairobi Sub-Counties Map Colouring (CSP)

A Constraint Satisfaction Problem (CSP) that colours all **17 Nairobi sub-counties** using the **minimum possible number of colours** so that no two adjacent sub-counties share the same colour.

---

## What It Does

Defines all 17 Nairobi sub-counties and their shared borders, then automatically finds the smallest number of colours needed to colour the map without any two neighbouring sub-counties sharing a colour. The solution is printed to the console and drawn as a schematic map.

---

## Requirements

```bash
pip install matplotlib
```

---

## How to Run

```bash
python Task_Two_Nairobi_SubCounties.py
```

> **Note:** Close the map window for the program to finish.

---

## Sub-Counties Covered

Westlands, Dagoretti North, Dagoretti South, Langata, Kibra, Roysambu, Kasarani, Ruaraka, Embakasi North, Embakasi West, Embakasi Central, Embakasi East, Embakasi South, Makadara, Kamukunji, Starehe, Mathare

---

## How the Algorithm Works

The program tries **2 colours first**, then **3**, then **4**, stopping as soon as a valid solution is found. For each attempt it uses **backtracking**:

1. Pick the first uncoloured sub-county
2. Try assigning it a colour
3. Check it doesn't match any already-coloured neighbour
4. If valid — move to the next sub-county
5. If no colour works — backtrack and change the previous assignment
6. Repeat until all 17 sub-counties are coloured

---

## Result

```
Searching for minimum number of colours...
  2 colours: No solution.
  3 colours: Solution found!

Minimum colours needed: 3
```

2 colours are not enough because the sub-county graph contains **odd-length cycles** (triangles of mutual neighbours). 3 colours are sufficient.

A map image `nairobi_colouring.png` is also saved in the same folder.
