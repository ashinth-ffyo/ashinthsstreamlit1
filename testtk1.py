from customtkinter import *

def light_living():
    pass

def sensor_living():
    pass

def living_window_open():#livingroom controls
    living_win = CTk()
    living_win.geometry("300x500")
    living_win.title("Livingroom Controls")

    btn_brightness = CTkButton(living_win,text="Brightness Controls",font=("Comic Sans Ms",25),width=200,height=50,command=brightness)
    btn_brightness.pack(pady=10)

    btn_led_livin = CTkButton(living_win,text="Light Controls", font=("Comic Sans Ms",25),width=200,height=50,command=light_living)
    btn_led_livin.pack(pady=10)

    btn_sensor_living = CTkButton(living_win, text="Sensor's ", font=("Comic Sans Ms",25),width=200,height=50,command=sensor_living)
    btn_sensor_living.pack()

    btn_destroy_br = CTkButton(living_win, text="Exit", fg_color=("#FF0000", "#FFFFFF"), command=living_win.destroy)
    btn_destroy_br.place(x=80, y=450)

    living_win.mainloop()
def brightness():#livingroom controls

    brightness_win = CTk()
    brightness_win.geometry("300x150")
    brightness_win.title("Brightness Of Living Room")

    def update_label(value):
        value_label.configure(text=f"Brightness Of Room Lights: {int(value)*10}%")

    # Create a slider and set its command to the update_label function
    slider = CTkSlider(brightness_win, from_=0, to=10, command=update_label,)
    slider.pack(pady=20)

    # Create a label to display the slider's value below it
    value_label = CTkLabel(brightness_win, text="Brightness Of Room Lights: 50%")
    value_label.pack()

    btn_destroy_br = CTkButton(brightness_win, text="Exit", fg_color=("#FF0000", "#FFFFFF"), command=brightness_win.destroy)
    btn_destroy_br.place(x=80, y=100)

    brightness_win.mainloop()

def bed_window_open():#bedroom controls
    pass

def dining_window_open():#diningroom controls
    pass

set_default_color_theme("dark-blue")

lobby = CTk()
lobby.geometry("400x370")
lobby.title("IOThome")

set_default_color_theme("dark-blue")

lbl_main_win = CTkLabel(lobby,text="IOThome",font=("Comic Sans Ms",60))
lbl_main_win.pack(pady=10)

btn_living_main = CTkButton(lobby, text="Livingroom", fg_color=("#4281A4","#D7DEDC"),width=200,height=50,font=("Comic Sans Ms",25), command=living_window_open)
btn_living_main.pack(padx=10,pady=10)

btn_dining_main = CTkButton(lobby, text="Diningroom", fg_color=("#EB8258", "#C04ABC"),width=200,height=50,font=("Comic Sans Ms",25), command=dining_window_open)
btn_dining_main.pack(padx=10,pady=10)

btn_bed_main = CTkButton(lobby, text="Bedroom", fg_color=("#1E91D6", "#0072BB"),width=200,height=50,font=("Comic Sans Ms",25), command=bed_window_open)
btn_bed_main.pack(padx=10,pady=10)

btn_destroy_main = CTkButton(lobby, text="Exit",fg_color=("#FF0000","#FFFFFF"),command=lobby.destroy)
btn_destroy_main.place(x=240,y=330)


lobby.mainloop()