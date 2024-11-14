import odrive
from odrive.enums import *
import keyboard

class WheelController:
    def __init__(self, odrv_left_serial, odrv_right_serial):
        # Initialize the ODrive devices with their serial numbers
        self.odrv_left = odrive.find_any(serial_number=odrv_left_serial)
        self.odrv_right = odrive.find_any(serial_number=odrv_right_serial)
        self.speed = 1.0

    def arm_wheels(self):
        # Set wheels to closed loop control
        self.odrv_right.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.odrv_left.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        print("Wheels armed")

    def disarm_wheels(self):
        # Set wheels to idle
        self.odrv_right.axis0.requested_state = AXIS_STATE_IDLE
        self.odrv_left.axis0.requested_state = AXIS_STATE_IDLE
        print("Wheels disarmed")

    def set_wheel_speed(self, right_speed, left_speed):
        # Set the input velocity for each wheel
        self.odrv_right.axis0.controller.input_vel = right_speed
        self.odrv_left.axis0.controller.input_vel = left_speed

    def control_loop(self):
        # Arm the wheels
        self.arm_wheels()
        
        try:
            while True:
                if keyboard.is_pressed('w'):
                    if keyboard.is_pressed('d'):
                        self.set_wheel_speed(self.speed / 2, self.speed)
                    elif keyboard.is_pressed('a'):
                        self.set_wheel_speed(self.speed, self.speed / 2)
                    else:
                        self.set_wheel_speed(self.speed, self.speed)
                
                elif keyboard.is_pressed('s'):
                    if keyboard.is_pressed('d'):
                        self.set_wheel_speed(-self.speed / 2, -self.speed)
                    elif keyboard.is_pressed('a'):
                        self.set_wheel_speed(-self.speed, -self.speed / 2)
                    else:
                        self.set_wheel_speed(-self.speed, -self.speed)
                
                elif keyboard.is_pressed('a'):
                    self.set_wheel_speed(self.speed, self.speed / 2)
                
                elif keyboard.is_pressed('d'):
                    self.set_wheel_speed(self.speed / 2, self.speed)
                
                else:
                    # Stop the wheels when no keys are pressed
                    self.set_wheel_speed(0, 0)
        
        except KeyboardInterrupt:
            # Disarm wheels on interruption
            self.disarm_wheels()

# Example usage
if __name__ == "__main__":
    # Replace with actual serial numbers for the ODrive devices
    wheel_controller = WheelController("3946354F3231", "397135683231")
    wheel_controller.control_loop()
