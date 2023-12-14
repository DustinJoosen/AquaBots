import tkinter
from Components.MoistureSensor import get_moisture as get_moisture_from_sensor

root = tkinter.Tk()
root.title("AquaBots control panel")

servo_switch_state = False


# Button callbacks.
def get_moisture():
    pin = moisture_pin_num_entry.get()

    moisture = get_moisture_from_sensor(pin, verbose=True)
    moisture_output_lbl.config(text=moisture)


def get_distance():
    distance_output_lbl.config(text="Value: 55 km")


def get_gps():
    gps_output_lbl.config(text="Value: 55w 22n")


def get_compass():
    compass_output_lbl.config(text="North")


# Switch control
def switch():
    global servo_switch_state
     
    # Determine is on or off
    if servo_switch_state:
        servo_measure_btn.config(image = servo_switch_img_off)
        servo_switch_state = False
        print("servo now off")
    else:
        servo_measure_btn.config(image = servo_switch_img_on)
        servo_switch_state = True
        print("servo now on")


# Moisture
moisture_group = tkinter.LabelFrame(root, text="Moisture sensor")

moisture_button_border = tkinter.Frame(moisture_group, highlightbackground="black", highlightthickness=1, bd=0)
moisture_measure_btn = tkinter.Button(moisture_button_border, text="Measure humidity", width=20)
moisture_measure_btn["command"] = get_moisture
moisture_measure_btn.grid(row=0)

moisture_button_border.grid(row=0, pady=10, padx=10, columnspan=2)

moisture_pin_num_lbl = tkinter.Label(moisture_group, text="Pin: ")
moisture_pin_num_lbl.grid(row=1, column=0)

moisture_pin_num_entry = tkinter.Entry(moisture_group, width=10)
moisture_pin_num_entry.insert(0, "2")
moisture_pin_num_entry.grid(row=1, column=1)

moisture_output_lbl = tkinter.Label(moisture_group, text="Result: ", )
moisture_output_lbl.grid(row=2, pady=10, padx=10, columnspan=2)

moisture_group.grid(row=0, column=0, padx=10, pady=10)

# Distance
distance_group = tkinter.LabelFrame(root, text="Distance sensor")

distance_button_border = tkinter.Frame(distance_group, highlightbackground="black", highlightthickness=1, bd=0)
distance_measure_btn = tkinter.Button(distance_button_border, text="Measure distance", width=20)
distance_measure_btn["command"] = get_distance
distance_measure_btn.grid(row=0)

distance_button_border.grid(row=0, pady=10, padx=10, columnspan=2)

distance_pin_num_lbl = tkinter.Label(distance_group, text="Pin: ")
distance_pin_num_lbl.grid(row=1, column=0)

distance_pin_num_entry = tkinter.Entry(distance_group, width=10)
distance_pin_num_entry.insert(0, "0")
distance_pin_num_entry.grid(row=1, column=1)

distance_output_lbl = tkinter.Label(distance_group, text="Result: ", )
distance_output_lbl.grid(row=2, pady=10, padx=10, columnspan=2)

distance_group.grid(row=0, column=1, padx=10, pady=10)

# GPS
gps_group = tkinter.LabelFrame(root, text="GPS sensor")

gps_button_border = tkinter.Frame(gps_group, highlightbackground="black", highlightthickness=1, bd=0)
gps_measure_btn = tkinter.Button(gps_button_border, text="Locate current position", width=20)
gps_measure_btn["command"] = get_gps
gps_measure_btn.grid(row=0)

gps_button_border.grid(row=0, pady=10, padx=10, columnspan=2)

gps_pin_num_lbl = tkinter.Label(gps_group, text="Pin: ")
gps_pin_num_lbl.grid(row=1, column=0)

gps_pin_num_entry = tkinter.Entry(gps_group, width=10)
gps_pin_num_entry.insert(0, "0")
gps_pin_num_entry.grid(row=1, column=1)

gps_output_lbl = tkinter.Label(gps_group, text="Result: ", )
gps_output_lbl.grid(row=2, pady=10, padx=10, columnspan=2)

gps_group.grid(row=0, column=2, padx=10, pady=10)

# Compass
compass_group = tkinter.LabelFrame(root, text="Compass")

compass_button_border = tkinter.Frame(compass_group, highlightbackground="black", highlightthickness=1, bd=0)
compass_measure_btn = tkinter.Button(compass_button_border, text="Get compass direction", width=20)
compass_measure_btn["command"] = get_compass
compass_measure_btn.grid(row=0)

compass_button_border.grid(row=0, pady=10, padx=10, columnspan=2)

compass_pin_num_lbl = tkinter.Label(compass_group, text="Pin: ")
compass_pin_num_lbl.grid(row=1, column=0)

compass_pin_num_entry = tkinter.Entry(compass_group, width=10)
compass_pin_num_entry.insert(0, "0")
compass_pin_num_entry.grid(row=1, column=1)

compass_output_lbl = tkinter.Label(compass_group, text="Result: ", )
compass_output_lbl.grid(row=2, pady=10, padx=10, columnspan=2)

compass_group.grid(row=1, column=0, padx=10, pady=10)

# Servo
servo_group = tkinter.LabelFrame(root, text="Servo")

servo_switch_img_on = tkinter.PhotoImage(file = "lib/switch_on.png")
servo_switch_img_off = tkinter.PhotoImage(file = "lib/switch_off.png")

servo_button_border = tkinter.Frame(servo_group, highlightbackground="black", highlightthickness=1, bd=0)
servo_measure_btn = tkinter.Button(servo_button_border, image=servo_switch_img_off, text="Get compass direction")
servo_measure_btn["command"] = switch
servo_measure_btn.grid(row=0)

servo_button_border.grid(row=0, pady=10, padx=10)
servo_group.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()
