import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Polygon

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Remove axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Set border color and width
for spine in ax.spines.values():
    spine.set_edgecolor('white')
    spine.set_linewidth(4)

# Create a gradient background by using multiple color polygons
ax.set_facecolor('midnightblue')
bg_colors = ['darkblue', 'midnightblue', 'navy', 'royalblue']
for i, color in enumerate(bg_colors):
    ax.fill_between([0, 10], 2*i, 2*(i+1), color=color)

# Draw the supermoon
moon = Circle((5, 7), 1.5, color='lightyellow', ec='gold', lw=2)
ax.add_patch(moon)

# Draw the mountains (triangles)
mountain1 = Polygon([[1, 1], [4, 5], [7, 1]], closed=True, color='darkslategray')
mountain2 = Polygon([[6, 1], [8, 4], [10, 1]], closed=True, color='slategrey')
ax.add_patch(mountain1)
ax.add_patch(mountain2)

# Create stars randomly
num_stars = 100
stars_x = np.random.rand(num_stars) * 10
stars_y = np.random.rand(num_stars) * 8 + 2  # Ensure stars are above the mountains
stars = ax.scatter(stars_x, stars_y, color='white', s=2)

# Draw trees as small triangles at the bottom of the scene
tree_positions = np.array([[2, 1], [3, 1], [5, 1], [6.5, 1], [8, 1]])
tree_heights = np.array([0.6, 0.8, 0.7, 0.5, 0.9])
trees = [Polygon([[x-0.1, y], [x+0.1, y], [x, y+h]], closed=True, color='green') 
         for (x, y), h in zip(tree_positions, tree_heights)]
for tree in trees:
    ax.add_patch(tree)

# Draw clouds (animated)
clouds = [
    Circle((2, 8), 0.5, color='lightgray', alpha=0.7),
    Circle((3, 8), 0.8, color='lightgray', alpha=0.7),
    Circle((7, 6), 0.6, color='lightgray', alpha=0.7),
    Circle((4, 9), 0.6, color='lightgray', alpha=0.7),
    Circle((8, 9), 0.8, color='lightgray', alpha=0.7)
]
for cloud in clouds:
    ax.add_patch(cloud)

# Shooting star initial position
shooting_star, = ax.plot([], [], marker='o', color='white', markersize=5)

# Title and text
plt.title("Supermoon Night", fontsize=18, color='lightyellow', pad=20)
ax.text(7, 1.5, "Peaceful Mountains", fontsize=12, color='lightyellow')

# Function to update elements for animation
def update(frame):
    # Animate the clouds to move from left to right
    for i, cloud in enumerate(clouds):
        cloud.set_center(((cloud.center[0] + 0.01 * (i+1)) % 10, cloud.center[1]))
    
    # Make the stars twinkle by changing their size
    star_sizes = np.random.rand(num_stars) * 10
    stars.set_sizes(star_sizes)

    # Move the shooting star diagonally
    shooting_star_x = np.linspace(8, 1, 50)
    shooting_star_y = np.linspace(9, 4, 50)
    if frame < 50:
        shooting_star.set_data(shooting_star_x[frame], shooting_star_y[frame])
    else:
        shooting_star.set_data([], [])  # Hide shooting star after it passes

    # Make the moon slightly "pulse" (grow and shrink)
    moon_radius = 1.5 + 0.05 * np.sin(frame * 0.1)
    moon.set_radius(moon_radius)
    
    # Sway the trees (simulate wind)
    sway = 0.01 * np.sin(frame * 0.2)
    for i, tree in enumerate(trees):
        x_shift = tree.xy[:, 0] + sway * (i+1)
        tree.xy[:, 0] = x_shift

    return clouds + [stars, shooting_star] + trees + [moon]

# Animate
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the plot with animation
plt.show()
