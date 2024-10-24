let Numero = 0
radio.onReceivedNumber(function (receivedNumber) {
    Numero = randint(1, 6)
    if (receivedNumber == Numero) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("STRING")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
basic.forever(function () {
    Numero = randint(1, 6)
    radio.sendNumber(Numero)
})
