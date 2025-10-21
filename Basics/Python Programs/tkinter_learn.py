import tkinter as tk

root = tk.Tk()
root.title("Simple Menu")

# Create a menu object
simple_menu = tk.Menu(root, tearoff=0)

# Add commands directly
simple_menu.add_command(label="Open", command=lambda: print("Open clicked"))
simple_menu.add_command(label="Save", command=lambda: print("Save clicked"))
simple_menu.add_command(label="Exit", command=root.quit)

# Attach the menu to a right-click event
def show_menu(event):
    simple_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_menu)  # Right-click to show menu

root.mainloop()
