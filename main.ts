// measure how fast we can measure sound level
// 24000 microseconds = 40 times per second
input.onButtonPressed(Button.A, function () {
    basic.showNumber(loud)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(us)
    basic.clearScreen()
})
let after = 0
let us = 0
let loud = 0
loud = input.soundLevel()
let before = input.runningTimeMicros()
basic.forever(function () {
    after = input.runningTimeMicros()
    us = after - before
    before = after
    loud = input.soundLevel()
})
