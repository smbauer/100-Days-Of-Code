import tkinter as tk


CONVERSION = 1.60934


def convert_m_to_km(miles=0):
    return round(miles * CONVERSION, 2)


def button_clicked():
    miles = int(input_miles.get())
    km = convert_m_to_km(miles=miles)
    label_result.config(text=km)


# setup the window
window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=75, pady=75)

# add a miles text input box
input_miles = tk.Entry(width=10)
input_miles.grid(column=1, row=0)

# add first text label
label_miles = tk.Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

# add second text label
label_equal = tk.Label(text="is equal to", font=("Arial", 12))
label_equal.grid(column=0, row=1)

# add km conversion label
label_result = tk.Label(text="0", font=("Arial", 12))
label_result.grid(column=1, row=1)

# add km text label
label_km = tk.Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

# add calculate button
button_calculate = tk.Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=2)

window.mainloop()
