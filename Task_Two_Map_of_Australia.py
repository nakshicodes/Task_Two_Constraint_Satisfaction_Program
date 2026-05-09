"""
Task 2(a): Constraint Satisfaction Problem - Map Colouring
Write a colouring constraint program to colour the five regions of Australia using 3 colours (Blue, Red, Green)
so that no two adjacent regions share the same colour.

"""

import matplotlib.pyplot as plt # to draw charts, images, and graphs
import matplotlib.patches as mpatches # used to create the coloured legend boxes


# Define the problem
#A list of all 7 Australian regions we need to colour
regions = ['WA', 'NT', 'SA', 'QLD', 'NSW']

#A dictionary that defines which regions share a border.
adjacency = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'QLD'],
    'SA':  ['WA', 'NT', 'QLD', 'NSW'],
    'QLD': ['NT', 'SA', 'NSW'],
    'NSW': ['QLD', 'SA'],
}

colours = ['Blue', 'Red', 'Green']


# CSP Solver - Backtracking
# Checks whether assigning a colour to a region is safe. It loops through every neighbour of that region — if any neighbour already has the same colour, it returns False (conflict). If no conflicts, returns True
def is_valid(region, colour, assignment):
    for neighbour in adjacency[region]:
        if assignment.get(neighbour) == colour:
            return False
    return True

def solve(regions, assignment={}):
    if len(assignment) == len(regions):
        return assignment
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]
    for colour in colours:
        if is_valid(region, colour, assignment):
            assignment[region] = colour
            result = solve(regions, assignment)
            if result:
                return result
            del assignment[region]
    return None

#Starts the algorithm with an empty assignment and stores the final solution.
solution = solve(regions, {})


# Print the solution

print("Australia Map Colouring Solution:")

for region, colour in solution.items():
    print(f"  {region}: {colour}")


# Draw the map

COLOUR_MAP = {'Blue': '#3498db', 'Red': '#e74c3c', 'Green': '#2ecc71'}

region_polygons = {
    'WA':  [(113,-14),(129,-14),(129,-35),(113,-35)],
    'NT':  [(129,-14),(138,-14),(138,-26),(129,-26)],
    'SA':  [(129,-26),(141,-26),(141,-38),(129,-38)],
    'QLD': [(138,-14),(154,-14),(154,-29),(141,-29),(141,-26),(138,-26)],
    'NSW': [(141,-29),(154,-29),(154,-37),(141,-37)],
}

region_labels = {
    'WA':(121,-26), 'NT':(133,-20), 'SA':(135,-32),
    'QLD':(146,-22), 'NSW':(147,-33),
}

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_facecolor('#d6eaf8')

for region, poly in region_polygons.items():
    xs = [p[0] for p in poly] + [poly[0][0]]
    ys = [p[1] for p in poly] + [poly[0][1]]
    ax.fill(xs, ys, color=COLOUR_MAP[solution[region]], alpha=0.85)
    ax.plot(xs, ys, color='white', linewidth=1.5)
    lx, ly = region_labels[region]
    ax.text(lx, ly, f"{region}\n({solution[region]})",
            ha='center', va='center', fontsize=10, fontweight='bold', color='white')

handles = [mpatches.Patch(color=COLOUR_MAP[c], label=c) for c in colours]
ax.legend(handles=handles, loc='lower left')
ax.set_title("Australia Map Colouring - CSP Solution (5 Regions)\nNo two adjacent regions share a colour")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

plt.tight_layout()
plt.savefig('australia_colouring.png')
plt.show()