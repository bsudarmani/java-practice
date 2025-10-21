import tkinter as tk 
from tkinter import ttk 
root = tk.Tk() 
root.title("Login Form Example with Grid") 
root.geometry("450x500") 
# --- Frame --- 
frame = tk.Frame(root, padx=10, pady=10, bd=2, relief="groove") 
frame.pack(pady=10) 
# --- Labels and Entry --- 
tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="w", padx=5, pady=5) 
username = tk.Entry(frame) 
username.grid(row=0, column=1, padx=5, pady=5) 
tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="w", padx=5, pady=5) 
password = tk.Entry(frame, show="*") 
password.grid(row=1, column=1, padx=5, pady=5) 
# --- Radiobutton --- 
tk.Label(frame, text="Gender:").grid(row=2, column=0, sticky="w", padx=5, pady=5) 
gender = tk.StringVar() 
tk.Radiobutton(frame, text="Male", variable=gender, value="Male").grid(row=2, column=1, 
sticky="w") 
tk.Radiobutton(frame, text="Female", variable=gender, value="Female").grid(row=2, 
column=2, sticky="w") 
# --- Spinbox --- 
tk.Label(frame, text="Age:").grid(row=3, column=0, sticky="w", padx=5, pady=5) 
age = tk.Spinbox(frame, from_=18, to=60) 
age.grid(row=3, column=1, padx=5, pady=5) 
# --- Checkbutton --- 
remember = tk.IntVar() 
tk.Checkbutton(frame, text="Remember Me", variable=remember).grid(row=4, columnspan=3, 
pady=5) 
# --- Submit Button --- 
def submit():
    tree.insert("", tk.END, values=(username.get(), gender.get(), age.get())) 
tk.Button(frame, text="Login", command=submit).grid(row=5, columnspan=3, pady=10) 
# --- Treeview Table --- 
tree = ttk.Treeview(root, columns=("Username", "Gender", "Age"), show="headings") 
tree.heading("Username", text="Username") 
tree.heading("Gender", text="Gender") 
tree.heading("Age", text="Age") 
tree.pack(pady=10) 
# --- Menu --- 
menu = tk.Menu(root) 
root.config(menu=menu) 
file_menu = tk.Menu(menu, tearoff=0) 
menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="Exit", command=root.quit) 
root.mainloop() 
