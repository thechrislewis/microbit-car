from microbit import *

# First we create a Motor class to control a single motor
class Motor:
    def __init__(self, motor_pin): # initialize motor with given pin
        
        self.pin = motor_pin
        self.pin.set_analog_period(20) # set PWM period to 20ms for motor control
        
    def run(self, speed): # run motor at given speed
        ''' run(speed) - value between 0 and 1023
        run(512)
        '''
        
        speed = max(0, min(1023, speed))  # constrain speed between 0 and 1023
        self.pin.write_analog(speed) # set motor speed
            
    def stop(self): # stop the motor by running motor at speed 0
        ''' stop motor'''
        self.run(0)

# code to test class code
if __name__ == "main":
    motor = Motor(pin1)

    motor.run(1)
    sleep(1000)

    motor.stop()



    