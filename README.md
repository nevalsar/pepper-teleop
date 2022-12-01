# Pepper Teleop

Simple teleoperation script for the [Pepper Robot][1] using Python.

## Instructions

- Turn on the Pepper robot. Make a note of the robot IP once boot is complete.
- Connect to same network as Pepper.
- Run the teleop script:
``` sh
python3 teleop.py --ip <robot_ip>
```

- Move forward and backward using 'w' and 's'. Turn left and right using 'a' and 'd'. Speak voice lines using '1' and '2' keys.
- Modify/extend teleop.py as needed.

## Usage

``` sh
teleop.py [-h] --ip IP [-p PORT]

Teleoperation script for Pepper Robot.

optional arguments:
  -h, --help            show this help message and exit
  --ip IP               Pepper's IP address
  -p PORT, --port PORT  Pepper's port number
```

## Dependencies

- Python 3.5.10
- [qi][2]
- [pynput][3]

[1]: https://www.aldebaran.com/en/pepper
[2]: https://pypi.org/project/qi/
[3]: https://pypi.org/project/pynput/
