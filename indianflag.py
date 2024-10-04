import tkinter as tk
import math

window = tk.Tk()
window.title("Indian Flag")

window_width = 450
window_height = 300
window.geometry(f"{window_width}x{window_height}")

canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

saffron_color = "#FF9933"  # Saffron
white_color = "#FFFFFF"
green_color = "#138808"  # Green
blue_color = "#000080"  # Navy Blue for Ashoka Chakra

canvas.create_rectangle(0, 0, window_width, window_height/3, fill=saffron_color)  
canvas.create_rectangle(0, window_height/3, window_width, 2*window_height/3, fill=white_color)
canvas.create_rectangle(0, 2*window_height/3, window_width, window_height, fill=green_color)  

chakra_radius = 45  
chakra_x = window_width / 2 
chakra_y = window_height / 2  

canvas.create_oval(chakra_x - chakra_radius, chakra_y - chakra_radius, chakra_x + chakra_radius, chakra_y + chakra_radius, outline=blue_color, width=2)


for i in range(24):
    angle = math.radians(i * 360 / 24)  
    x_end = chakra_x + chakra_radius * math.cos(angle)
    y_end = chakra_y + chakra_radius * math.sin(angle)
    canvas.create_line(chakra_x, chakra_y, x_end, y_end, fill=blue_color, width=2)

window.mainloop()
