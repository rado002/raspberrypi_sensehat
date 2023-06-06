from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyian = (0,255,255)
white = (255,255,255)
darkblue = (0,0,128)
darkgrey = (169,169,169)
black = (0,0,0)

while True:
    sense.show_message("Raspberrypi is Awesome!", text_colour=white, back_colour=black, scroll_speed=0.03)