# measure how fast we can measure sound level
# 24000 microseconds = 40 times per second

def on_button_pressed_a():
    basic.show_number(loud)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(us)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

after = 0
us = 0
loud = 0
loud = input.sound_level()
before = input.running_time_micros()

def on_forever():
    global after, us, before, loud
    after = input.running_time_micros()
    us = after - before
    before = after
    loud = input.sound_level()
basic.forever(on_forever)
