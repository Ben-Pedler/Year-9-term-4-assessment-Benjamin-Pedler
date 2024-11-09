For my IT project this term, I made a device with micro python and a Pico pi w board. This device consists of two actuators, a potentiometer and a button. This device also consists of two outputs, a buzzer and an LED light.  

When the button is being held down, it allows the function 'adjust_light_and_buzzer' to run. This function allows the potentiometer's value to be read. When the potentiometer is turned, the LED light will dim / get brighter. When the potentiometer value is greater than 65,534, the buzzer will sound. The reason I chose this value is because it is one less thean the greatest value. When the buzzer sounds, stop turning the potentiometer because it is at its max. 

The components for this device include: 
- Raspberry Pi Pico W 
- Bread board 
- Button 
- potentiometer 
- Buzzer 
- LED Light 
- USBC - Micro USB Cable (For Mac) 
- 10 Wires 
- Resistor 

Connecting the components 

The LED light is connected to the GPIO Pin 15 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 15 is at the end of the Pico Pi W meaning it is easy to wire. 

The Buzzer is connected to the GPIO Pin 14 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 14 is near the end of the Pico Pi W meaning it is easy to wire. 

The Button is connected to the GPIO Pin 17 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 17 is near the end of the Pico Pi W meaning it is easy to wire. 

The potentiometer is connected to the GPIO Pin 26, a GND Pin and the 3V3(OUT) Pin. The significance with Pin 26 is that the GPIO can double as an analog and digital pin, allowing the potentiometer to have different values from 0 - 65,535. The 3V3(OUT) Pin provides 3.3 volts into the potentiometer. The ground pin provides a low resistance pathway back to the power source. 

Pulse width modulation (PWN) 
I am using h 

The code for this is: 

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
