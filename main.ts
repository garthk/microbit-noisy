//  measure how fast we can measure sound level
//  24000 microseconds = 40 times per second
//  measuring only the delay = same ahaaaa
//  so yeah can't rely on that
//  input.sound_level doesn't change outside forever?
//  try https://www.youtube.com/watch?v=E3PklpEB6lU
//  yeah nah
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    loud = 0
    pins.digitalWritePin(28, 1)
    for (let index = 0; index < 100; index++) {
        loud = pins.analogReadPin(6)
        serial.writeValue("loud", loud)
        control.waitMicros(80)
    }
    pins.digitalWritePin(28, 0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(us)
    basic.clearScreen()
})
let after = 0
let us = 0
let loud = 0
let before = input.runningTimeMicros()
basic.forever(function on_forever() {
    
    after = input.runningTimeMicros()
    us = after - before
    before = after
})
