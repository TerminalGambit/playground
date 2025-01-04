import json
import matplotlib.pyplot as plt

# Load the JSON file into a variable called 'conversations'
with open('data/data.json', 'r') as f:
    conversations = json.load(f)

# Create an empty list to store the data points for the graph
data_points = []

# Iterate through each conversation in the JSON file
for conversation in conversations:
    # Extract the sender, message, and timestamp values from the conversation
    sender = conversation['sender']
    message = conversation['message']
    timestamp = conversation['timestamp']

    # Add a tuple containing these values to the list of data points
    data_points.append((sender, message, timestamp))

# Plot the data points on a graph using Matplotlib
plt.plot(data_points)
plt.xlabel('Time')
plt.ylabel('Conversation')
plt.show()

import tkinter as tk
from matplotlib.backends.tkagg import FigureCanvasTkAgg

# Create a window for the GUI
root = tk.Tk()

# Create a figure and axis object to plot onto
fig, ax = plt.subplots(1)

# Create a canvas to display the graph
canvas = FigureCanvasTkAgg(fig=fig, master=root)
canvas.get_tk_widget().pack()

# Start the GUI event loop
root.mainloop()
