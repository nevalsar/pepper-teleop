import argparse
import qi
import sys
from time import sleep


class Pepper:
    session = None
    motion_service = None
    auton_service = None
    tts = None

    def __init__(self, ip, port):
        self.session = qi.Session()
        try:
            print("Connecting to Pepper at {ip}:{port}".format(ip=ip, port=port))
            self.session.connect("tcp://{ip}:{port}".format(ip=ip, port=str(port)))
            print("Connected!")
        except RuntimeError:
            print("Unable to connect to Pepper.")
            sys.exit(1)
        self.motion_service = self.session.service("ALMotion")
        self.auton_service = self.session.service("ALAutonomousMoves")
        self.tts = self.session.service("ALTextToSpeech")

    def move_forward(self, speed):
        print("Moving")
        self.motion_service.moveToward(speed, 0, 0)

    def turn_around(self, speed):
        print("Turning")
        self.motion_service.moveToward(0, 0, speed)

    def stop_moving(self):
        print("Stopping")
        self.motion_service.stopMove()

    def disable_collision_protection(self):
        print("Disabling collision protection")
        self.motion_service.setExternalCollisionProtectionEnabled("All", False)

    def sleep(self, duration):
        sleep(duration)
        self.stop_moving()

    def speak(self, text):
        self.tts.say(text)

    def enable_collision_protection(self):
        print("Enabling collision protection")
        self.auton_service.setBackgroundStrategy("backToNeutral")
        self.motion_service.setExternalCollisionProtectionEnabled("All", True)

    def on_keypress(self, key):
        try:
            print("alphanumeric key {0} pressed".format(key.char))
            if key == "w":
                self.move_forward(1)
                self.sleep(3)
            elif key == "s":
                self.move_forward(-1)
                self.sleep(3)
            elif key == "a":
                self.turn_around(1)
                self.sleep(1.3)
            elif key == "d":
                self.turn_around(-1)
                self.sleep(1.3)
            elif key == "1":
                self.speak("Hi")
            elif key == "2":
                self.speak("Bye")
        except AttributeError:
            print("special key {0} pressed".format(key))

    def start_teleop(self):
        print("Disabling collision protection and starting teleop.")
        print(
            "W: forward, S: backward, A: turn left, D: turn right, 1: say hi, 2: say bye"
        )
        print("Press Ctrl+C to exit.")
        self.disable_collision_protection()
        try:
            while True:
                key = input("Enter a key: ")
                self.on_keypress(key)
        except KeyboardInterrupt:
            self.enable_collision_protection()
            print("Enabling collision protection and exiting.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="teleop.py",
        description="Teleoperation script for Pepper Robot.",
    )
    parser.add_argument("--ip", type=str, required=True, help="Pepper's IP address")
    parser.add_argument(
        "-p", "--port", type=int, default=9559, help="Pepper's port number"
    )

    args = parser.parse_args()
    robot = Pepper(args.ip, args.port)
    robot.start_teleop()
