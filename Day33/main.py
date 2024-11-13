from tkinter import *
import requests

def get_quote():
    '''Retrieve a quote from the Kanye API and display it in the text box'''
    response = requests.get(url="https://api.kanye.rest/")
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])

# set up the screen
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# set up the background image
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day33/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye quotes", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

# set up the Kanye face button
kanye_img = PhotoImage(file="Day33/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, relief="flat")
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()