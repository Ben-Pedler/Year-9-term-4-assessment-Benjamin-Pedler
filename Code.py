import machine
import time

# Pin setup
potentiometer_pin = machine.ADC(26)  # ADC pin connected to the potentiometer (GP26)
led_pin = machine.Pin(15, machine.Pin.OUT)  # PWM pin connected to LED (GP15)
buzzer_pin = machine.Pin(14, machine.Pin.OUT)  # Pin connected to buzzer (GP14)
button = machine.Pin(17,machine.Pin.IN, machine.Pin.PULL_UP)

# Set up PWM for the LED
led_pwm = machine.PWM(led_pin)
led_pwm.freq(1000)  # Frequency for PWM (adjustable, 1 kHz here)

# Threshold for buzzer activation
threshold = 65534

# Function to read potentiometer and adjust LED brightness
def adjust_light_and_buzzer():
    # Read potentiometer value (0-65535)
    potentiometer_value = potentiometer_pin.read_u16()
    print("Potentiometer Value:", potentiometer_value)

    # Map potentiometer value (0-65535) to PWM duty cycle (0-1023 for the Pico)
    pwm_duty = int(potentiometer_value / 65535 * 1023)
    led_pwm.duty_u16(pwm_duty)

    # If the potentiometer value exceeds the threshold, activate buzzer
    if potentiometer_value > threshold:
        buzzer_pin.on()  # Turn on buzzer
    else:
        buzzer_pin.off()  # Turn off buzzer

# Main loop
while True:
    if button.value() ==0:  # Check if button is pressed (active low)
        adjust_light_and_buzzer()
    else:
        buzzer_pin.off()  # Ensure buzzer is off when button is not pressed
    time.sleep(0.1)  # Delay to avoid excessive CPU usage
