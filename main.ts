let z = 0
let y = 0
let x = 0
music.setVolume(200)
serial.redirectToUSB()
serial.writeLine("")
serial.writeLine("")
serial.writeLine("Hello Bug")
loops.everyInterval(500, function () {
    serial.writeLine("x:" + x + "; y:" + y + "; z:" + z)
})
basic.forever(function () {
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    if (x < -100) {
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
    } else if (x > 100) {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
    } else if (y < -100) {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else if (y > 100) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
            `)
    } else {
        basic.showIcon(IconNames.SmallSquare)
    }
    if (z > 300 && Math.abs(y) < 500) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.InBackground)
    } else {
        music.stopAllSounds()
    }
})
