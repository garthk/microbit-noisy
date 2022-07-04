# measure how fast we can measure sound level
# 24000 microseconds = 40 times per second
# measuring only the delay = same ahaaaa
# so yeah can't rely on that
# input.sound_level doesn't change outside forever?
# try https://www.youtube.com/watch?v=E3PklpEB6lU
# yeah nah
def on_button_pressed_a():
    global loud
    loud = 0
    pins.digital_write_pin(28, 1)
    for index in range(100):
        loud = pins.analog_read_pin(6)
        serial.write_value("loud", loud)
        control.wait_micros(80)
    pins.digital_write_pin(28, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(us)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

after = 0
us = 0
loud = 0
before = input.running_time_micros()

def on_forever():
    global after, us, before
    after = input.running_time_micros()
    us = after - before
    before = after
basic.forever(on_forever)
