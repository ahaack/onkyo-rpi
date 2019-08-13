import time
import pigpio


class OnkyoCommand():

    def __init__(self, pi, gpio):
        self.pi = pi
        self.gpio = gpio
        pi.set_mode(gpio, pigpio.OUTPUT)

    def _create_header_wave(self):
        wf = []
        wf.append(pigpio.pulse(1 << self.gpio, 0, 3000))
        wf.append(pigpio.pulse(0, 1 << self.gpio, 1000))
        return wf

    def _create_trailer_wave(self):
        wf = []
        wf.append(pigpio.pulse(1 << self.gpio, 0, 1000))
        wf.append(pigpio.pulse(0, 1 << self.gpio, 40000))
        return wf

    def _create_command_wave(self, command):
        wf = []
        for x in range(0, 12):
            gap = 2000 if command & 2048 != 0 else 1000
            wf.append(pigpio.pulse(1 << self.gpio, 0, 1000))
            wf.append(pigpio.pulse(0, 1 << self.gpio, gap))
            command = command << 1
        return wf

    def send(self, command):

        self.pi.wave_clear()

        wave_elements = self._create_header_wave() + \
            self._create_command_wave(command) + \
            self._create_trailer_wave()

        self.pi.wave_add_generic(wave_elements)
        self.pi.wave_send_once(self.pi.wave_create())

        while self.pi.wave_tx_busy():
            time.sleep(0.1)
