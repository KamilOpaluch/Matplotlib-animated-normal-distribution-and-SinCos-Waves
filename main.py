import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# create an empty histogram on the right
n_bins = 30
x = np.random.randn(1000)
hist, bins, patches = ax1.hist(x, bins=n_bins, color='green', alpha=0.5)
ax1.set_xlim((np.min(bins), np.max(bins)))
ax1.set_ylim((0, np.max(hist)*1.1))

# define the update function for the histogram animation
def update_hist(frame):
    x = np.random.randn(1000)
    hist, bins = np.histogram(x, bins=n_bins)
    # Clear the subplot before updating it
    ax1.clear()
    hist, bins, patches = ax1.hist(x, bins=n_bins, color='green', alpha=0.5)
    ax1.set_xlim((np.min(bins), np.max(bins)))
    ax1.set_ylim((0, np.max(hist)*1.1))
    return patches

# create the histogram animation object
ani_hist = FuncAnimation(fig, update_hist, frames=100, interval=100, blit=True)

# Generate some initial data for the sine and cosine functions
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Set up the line plots for each subplot
line1, = ax2.plot(x, y1, color='blue')
line2, = ax2.plot(x, y2, color='orange')

# Define the update function for the sine and cosine animation
def update_sine_cosine(num):
    # Generate new data
    new_y1 = np.sin(x + num / 10)
    new_y2 = np.cos(x + num / 10)
    # Clear the subplot before updating it
    ax2.clear()
    # Update the plots
    line1, = ax2.plot(x, new_y1, color='blue')
    line2, = ax2.plot(x, new_y2, color='orange')
    # Set the titles for each subplot
    ax2.set_title("Sine and cosine waves")
    return line1, line2

# Create the sine and cosine animation
ani_sine_cosine = FuncAnimation(fig, update_sine_cosine, frames=100, interval=50, blit=True)

# Show the plot
plt.show()
