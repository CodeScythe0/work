import pyfirmata2

# PWM demo on port 5. The default PWM frequency is 1kHz.

PORT = pyfirmata2.Arduino.AUTODETECT

# Creates a new board
board = pyfirmata2.Arduino(PORT)
print("Setting up the connection to the board ...")

# Setup the digital pin for PWM
pwm_3 = board.get_pin('d:11:p')

v = float(input("PWM duty cycle from 0 to 100: ")) / 100.0

# Set the duty cycle (0..1)
pwm_3.write(v)

# just idle here
input("Press enter to exit")

# pwm off
pwm_3.write(0)

# Close the serial connection to the Arduino
board.exit()