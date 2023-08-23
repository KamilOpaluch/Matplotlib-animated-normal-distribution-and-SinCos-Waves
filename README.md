# Matplotlib-animated-normal-distribution-and-SinCos-Waves

Showcase oftwo animations in a single figure:

1. A histogram that updates its data in real-time. This histogram represents random data points.
2. Animated sine and cosine waves that shift over time

## View

![combined_animation_10_seconds](https://github.com/KamilOpaluch/Matplotlib-animated-normal-distribution-and-SinCos-Waves/assets/142261174/a1d45d3c-2a70-481d-a4b5-5df7336652c6)


## Code Structure

1. The figure contains two subplots.
2. The histogram is generated using random data points, and the animation refreshes these data points at regular intervals.
3. The sine and cosine animations shift the waves along the x-axis to give an animated effect.
4. The FuncAnimation class from matplotlib.animation is used to create both animations.
