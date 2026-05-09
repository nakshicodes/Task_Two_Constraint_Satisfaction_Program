"""
Task 2(b): Constraint Satisfaction Problem - Nairobi Sub-Counties Colouring
Colour all 17 Nairobi sub-counties using the minimum number of colours
so that no two adjacent sub-counties share the same colour.

"""

import matplotlib.pyplot as plt # to draw charts, images, and graphs
import matplotlib.patches as mpatches # used to create the coloured legend boxes
from matplotlib.patches import FancyBboxPatch # draws a rounded rectangle centred at each sub-county's grid position, filled with its assigned colour


# Define the problem
# list of all the subcounties we need to colour
sub_counties = [
    'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 'Kibra',
    'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi North', 'Embakasi West',
    'Embakasi Central', 'Embakasi East', 'Embakasi South', 'Makadara',
    'Kamukunji', 'Starehe', 'Mathare'
]

# A dictionary in which each sub-county lists the other sub-counties it physically borders
adjacency = {
    'Westlands':        ['Roysambu', 'Kasarani', 'Starehe', 'Dagoretti North'],
    'Dagoretti North':  ['Westlands', 'Kibra', 'Dagoretti South', 'Starehe'],
    'Dagoretti South':  ['Dagoretti North', 'Kibra', 'Langata'],
    'Langata':          ['Dagoretti South', 'Kibra', 'Embakasi West', 'Embakasi South'],
    'Kibra':            ['Dagoretti North', 'Dagoretti South', 'Langata', 'Kamukunji', 'Makadara', 'Embakasi West'],
    'Roysambu':         ['Westlands', 'Kasarani', 'Mathare'],
    'Kasarani':         ['Westlands', 'Roysambu', 'Ruaraka', 'Embakasi North', 'Mathare'],
    'Ruaraka':          ['Kasarani', 'Embakasi North', 'Mathare', 'Makadara'],
    'Embakasi North':   ['Kasarani', 'Ruaraka', 'Embakasi Central', 'Embakasi East'],
    'Embakasi West':    ['Kibra', 'Langata', 'Embakasi Central', 'Embakasi South'],
    'Embakasi Central': ['Embakasi North', 'Embakasi West', 'Embakasi East', 'Embakasi South', 'Makadara'],
    'Embakasi East':    ['Embakasi North', 'Embakasi Central', 'Embakasi South'],
    'Embakasi South':   ['Langata', 'Embakasi West', 'Embakasi Central', 'Embakasi East'],
    'Makadara':         ['Kibra', 'Ruaraka', 'Kamukunji', 'Embakasi Central'],
    'Kamukunji':        ['Kibra', 'Makadara', 'Starehe'],
    'Starehe':          ['Westlands', 'Dagoretti North', 'Kamukunji', 'Mathare'],
    'Mathare':          ['Roysambu', 'Kasarani', 'Ruaraka', 'Starehe'],
}


# CSP Solver - Backtracking
# We start with 2, try to solve, and if it fails we try 3, then 4, stopping the moment a solution is found
# Checks whether assigning a colour to a region is safe. It loops through every neighbour of that region — if any neighbour already has the same colour, it returns False (conflict). If no conflicts, returns True
def is_valid(sc, colour, assignment):
    for neighbour in adjacency[sc]:
        if assignment.get(neighbour) == colour:
            return False
    return True

def solve(sub_counties, colours, assignment={}):
    if len(assignment) == len(sub_counties):
        return assignment
    unassigned = [sc for sc in sub_counties if sc not in assignment]
    sc = unassigned[0]
    for colour in colours:
        if is_valid(sc, colour, assignment):
            assignment[sc] = colour
            result = solve(sub_counties, colours, assignment)
            if result:
                return result
            del assignment[sc]
    return None

# Try increasing numbers of colours until a solution is found
print("Searching for minimum number of colours...")
solution = None
num_colours = 0

for k in range(2, 6):
    colours = ['Red', 'Blue', 'Green', 'Yellow'][:k]
    solution = solve(sub_counties, colours, {})
    if solution:
        num_colours = k
        print(f"  {k} colours: Solution found!")
        break
    else:
        print(f"  {k} colours: No solution.")


# Print the solution

print(f"\nMinimum colours needed: {num_colours}")

for sc, colour in solution.items():
    print(f"  {sc:<22}: {colour}")


# Draw the map

COLOUR_MAP = {
    'Red':    '#e74c3c',
    'Blue':   '#3498db',
    'Green':  '#2ecc71',
    'Yellow': '#f1c40f' # having colour options
}

positions = {
    'Roysambu':         (2, 8),   'Kasarani':         (3, 8),
    'Westlands':        (1, 7),   'Mathare':          (3, 7),   'Ruaraka':          (4, 7),
    'Dagoretti North':  (1, 6),   'Starehe':          (2, 6),   'Kamukunji':        (3, 6),   'Makadara':         (4, 6),   'Embakasi North':   (5, 7),
    'Dagoretti South':  (1, 5),   'Kibra':            (2, 5),   'Embakasi West':    (3, 5),   'Embakasi Central': (5, 6),   'Embakasi East':    (6, 6),
    'Langata':          (2, 4),   'Embakasi South':   (4, 4),
}

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_facecolor('#f0f0f0')

# Draw lines between adjacent sub-counties
drawn = set()
for sc, neighbours in adjacency.items():
    x1, y1 = positions[sc]
    for nb in neighbours:
        edge = tuple(sorted([sc, nb]))
        if edge not in drawn:
            x2, y2 = positions[nb]
            ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1, alpha=0.5)
            drawn.add(edge)

# Draw a coloured box for each sub-county
for sc, (cx, cy) in positions.items():
    colour = COLOUR_MAP[solution[sc]]
    box = FancyBboxPatch((cx - 0.45, cy - 0.35), 0.9, 0.7,
                         boxstyle="round,pad=0.05",
                         facecolor=colour, edgecolor='white', linewidth=2)
    ax.add_patch(box)
    label = sc.replace(' ', '\n') if len(sc) > 12 else sc
    ax.text(cx, cy, label, ha='center', va='center',
            fontsize=7, fontweight='bold', color='white')

used = list(dict.fromkeys(solution.values()))
handles = [mpatches.Patch(color=COLOUR_MAP[c], label=c) for c in used]
ax.legend(handles=handles, title=f'Colours used: {num_colours}', loc='lower right')
ax.set_title(f"Nairobi Sub-Counties - CSP Colouring Solution\n"
             f"17 sub-counties coloured with minimum {num_colours} colours")
ax.set_xlim(0, 7.5)
ax.set_ylim(3, 9.5)
ax.axis('off')

plt.tight_layout()
plt.savefig('nairobi_colouring.png')
plt.show()