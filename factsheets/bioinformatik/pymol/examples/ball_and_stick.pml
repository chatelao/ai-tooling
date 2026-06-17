# Ball and Stick Model
load protein.pdb
hide all

# Show as stick and ball
show sticks
show spheres
set sphere_scale, 0.25

# Enable double bonds
set valence, 1

# Colors: red for O, blue for N
color red, elem o
color blue, elem n

# Default color for carbon (green in the user's image for some, pink for others)
color green, elem c

# Center the view
zoom
