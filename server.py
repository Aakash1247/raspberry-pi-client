# coding: utf-8
from socketIO_client import SocketIO
import pigpio

io_client = SocketIO('52.43.75.183', 8000)


def lock_control(pin_num, action):
    pi = pigpio.pi()
    avail_actions = {
        'unlock': 600,
        'lock': 2400,
    }
    pulsewidth = avail_actions.get(action, '')
    if not pulsewidth:
        raise ValueError('Action not permitted')
    pi.set_servo_pulsewidth(pin_num, pulsewidth)
    pi.stop()
    return pi.get_servo_pulsewidth(pin_num)


io_client.on('unlock', lock_control('unlock'))
io_client.on('lock', lock_control('lock'))

io_client.wait()
