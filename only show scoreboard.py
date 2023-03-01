import tkinter as tk

# Open the file and read the data
with open("scores.txt", "r") as file:
    data = [line.strip().split(",") for line in file]

# Sort the data by the number in descending order
data.sort(key=lambda x: int(x[1]), reverse=True)

# Create a Tkinter window
window = tk.Tk()
window.title("Sorted Data")

# Set the window size to full screen
window.geometry("1920x1080+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

# Set the font and size of the labels
label_font = ("Arial", 20)

# Set the width of each label to a fixed size
label_width = 20

# Create a label for each name and number in reverse order
for i, (name, number) in enumerate(data):
    label = tk.Label(window, text=f"{i+1}. {number}: {name}", font=label_font, width=label_width)
    label.config(anchor=tk.CENTER, padx=10, pady=3)
    label.pack(fill=tk.X)

# Run the Tkinter event loop
window.mainloop()