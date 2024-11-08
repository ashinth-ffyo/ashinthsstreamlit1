import customtkinter as ctk

# Initialize the app
app = ctk.CTk()
app.geometry("300x200")

# Function to update the label with the current slider value
def update_label(value):
    value_label.configure(text=f"Value: {int(value)}")

# Create a slider and set its command to the update_label function
slider = ctk.CTkSlider(app, from_=0, to=100, command=update_label)
slider.pack(pady=20)

# Create a label to display the slider's value below it
value_label = ctk.CTkLabel(app, text="Value: 0")
value_label.pack()

app.mainloop()
