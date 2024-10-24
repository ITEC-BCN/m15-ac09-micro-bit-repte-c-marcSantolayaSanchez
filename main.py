Numero = 0

def on_received_number(receivedNumber):
    global Numero
    Numero = randint(1, 6)
    if receivedNumber == Numero:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("STRING")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_forever():
    global Numero
    Numero = randint(1, 6)
    radio.send_number(Numero)
basic.forever(on_forever)
