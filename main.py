z = 0
y = 0
x = 0
music.set_volume(200)
serial.redirect_to_usb()
serial.write_line("")
serial.write_line("")
serial.write_line("Hello Bug")

def on_every_interval():
    serial.write_line("x:" + str(x) + "; y:" + str(y) + "; z:" + str(z))
loops.every_interval(500, on_every_interval)

def on_forever():
    global x, y, z
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    if x < -100:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . # # #
                        . # . . .
                        . . # . .
        """)
    elif x > 100:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # . #
                        . . . # .
                        . . # . .
        """)
    elif y < -100:
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
    elif y > 100:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # . # .
                        . . # . .
        """)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)
    if z > 300:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.IN_BACKGROUND)
    else:
        music.stop_all_sounds()
basic.forever(on_forever)
