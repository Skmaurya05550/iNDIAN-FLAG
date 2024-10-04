import tkinter as tk
import math

# Create a new tkinter window
window = tk.Tk()
window.title("Indian Flag")

# Set the dimensions of the window (using proper proportions for the Indian flag 3:2 ratio)
window_width = 450
window_height = 300
window.geometry(f"{window_width}x{window_height}")

# Create a canvas to draw the flag
canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

# Define the colors
saffron_color = "#FF9933"  # Saffron
white_color = "#FFFFFF"
green_color = "#138808"  # Green
blue_color = "#000080"  # Navy Blue for Ashoka Chakra

# Draw the flag (3 horizontal stripes)
canvas.create_rectangle(0, 0, window_width, window_height/3, fill=saffron_color)  # Saffron at the top
canvas.create_rectangle(0, window_height/3, window_width, 2*window_height/3, fill=white_color)  # White in the middle
canvas.create_rectangle(0, 2*window_height/3, window_width, window_height, fill=green_color)  # Green at the bottom

# Draw the Ashoka Chakra (24-spoked wheel)
chakra_radius = 45  # Radius of the Chakra
chakra_x = window_width / 2  # Center of the Chakra (horizontally)
chakra_y = window_height / 2  # Center of the Chakra (vertically)

# Draw the outer circle of the Chakra
canvas.create_oval(chakra_x - chakra_radius, chakra_y - chakra_radius, chakra_x + chakra_radius, chakra_y + chakra_radius, outline=blue_color, width=2)

# Draw the 24 spokes of the Chakra
for i in range(24):
    angle = math.radians(i * 360 / 24)  # Angle for each spoke (24 spokes, equally spaced)
    x_end = chakra_x + chakra_radius * math.cos(angle)
    y_end = chakra_y + chakra_radius * math.sin(angle)
    canvas.create_line(chakra_x, chakra_y, x_end, y_end, fill=blue_color, width=2)

# Run the application
window.mainloop()
