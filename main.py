import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

root = tk.Tk()

# Icon image file
icon = tk.PhotoImage(file="img.png")
# setting icon of root window
root.iconphoto(False, icon)
root.geometry("800x500")
root.resizable(height=False, width=False)
root.title("Formula Calculator")
font1 = Font(size=15, weight="bold")


# Velocity page
def velocity_page():
    velocity_frame = tk.Frame(main_frame)
    velocity0()
    velocity_frame.pack()


def hide_indicator():
    velocity_indicator.config(bg="#0002A1")


def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicator()
    lb.config(bg="#158aff")
    delete_page()
    page()


# Create option frame
option_canvas = tk.Canvas(root, bg="#001253")
option_frame = tk.Frame(option_canvas, bg="#001253")
option_scrollbar = tk.Scrollbar(root, orient="vertical", command=option_canvas.yview)
option_canvas.configure(yscrollcommand=option_scrollbar.set)

option_scrollbar.pack(side="right", fill="y")
option_canvas.pack(side="left", fill="both", expand=True)
option_canvas.create_window((0, 0), window=option_frame, anchor="nw")

option_frame.bind("<Configure>", lambda event, canvas=option_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

label2 = tk.Label(option_frame, text="MECHANICS", font=font1, bg="grey", padx=50, pady=5)
label2.place(x=10, y=0)

# Velocity button
velocity_btn = tk.Button(option_frame, text="velocity           ", font=font1, bd=0, fg="#3A98B9", bg="#121212",
                         command=lambda: indicate(velocity_indicator, velocity_page))
velocity_btn.place(x=10, y=50)
velocity_indicator = tk.Label(option_frame, text="", bg="#c3c3c3")
velocity_indicator.place(x=3, y=50, width=5, height=40)

# Create main frame
main_frame1 = tk.Frame(root, highlightthickness=2)
main_frame1.pack(side=tk.LEFT)
main_frame1.pack_propagate(False)
main_frame = tk.Frame(root, highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=500, width=1000)


# Velocity
def calculate_velocity(displacement_entry, time_entry, velocity_label):
    try:
        displacement = float(displacement_entry.get())
        time = float(time_entry.get())
        velocity = displacement / time
        velocity_label.config(text="Velocity: {:.2f} m/s".format(velocity))
    except ValueError:
        velocity_label.config(text="Please enter valid input.")


# Velocity
def clear(displacement_entry, time_entry):
    displacement_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


# Create velocity layout
def velocity0():
    # Create a label for Velocity.
    label1 = tk.Label(main_frame, text="VELOCITY", font=font1, bg="grey", padx=5, pady=5)
    label1.grid(row=0, column=0, padx=5, pady=5)
    # Create labels and entries for displacement and time.
    displacement_label = tk.Label(main_frame, text=""Displacement (m): ")
    displacement_label.grid(row=1, column=0, padx=5, pady=5)
    displacement_entry = tk.Entry(main_frame, width=12)
    displacement_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(main_frame, text="Time (s): ")
    time_label.grid(row=2, column=0, padx=5, pady=5)
    time_entry = tk.Entry(main_frame, width=12)
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a button to calculate velocity and clear.
    calculate_button = tk.Button(main_frame, text="Calculate",
                                 command=lambda: calculate_velocity(displacement_entry, time_entry, velocity_label))
    calculate_button.grid(row=3, column=1, padx=5, pady=5)

    # Create a label to display the velocity.
    velocity_label = tk.Label(main_frame, fg="blue")
    velocity_label.grid(row=4, column=1, padx=5, pady=5)

    clear_button = tk.Button(main_frame, text="Clear", command=lambda: clear(displacement_entry, time_entry))
    clear_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()


