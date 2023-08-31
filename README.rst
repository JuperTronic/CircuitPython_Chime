Introduction
============


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_Chime/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircuitPython class for generating wind chime and bell sounds using synthio.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Usage Example
=============

.. code-block:: python

    import time
    import board
    import random
    import audiobusio
    import audiomixer
    from cedargrove_chime import Chime, Scale, Voice, Material, Striker

    # Instantiate I2S output and mixer buffer for synthesizer
    audio_output = audiobusio.I2SOut(
        bit_clock=board.D12, word_select=board.D9, data=board.D6
    )
    mixer = audiomixer.Mixer(
        sample_rate=11020, buffer_size=4096, voice_count=1, channel_count=1
    )
    audio_output.play(mixer)
    mixer.voice[0].level = 1.0

    # Instantiate the chime synth with mostly default parameters
    chime = Chime(mixer.voice[0], scale=Scale.HavaNegila)

    # Play scale notes sequentially
    for index, note in enumerate(chime.scale):
        chime.strike(note, 1)
        time.sleep(0.4)
    time.sleep(1)

    while True:
        # Play randomly
        for count in range(random.randrange(10)):
            chime.strike(random.choice(chime.scale), 1)
            time.sleep(random.randrange(1, 3) * 0.6)

        time.sleep(random.randrange(1, 10) * 0.5)


Documentation
=============
API documentation for this library can be found in `PunkConsole_API <https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/pseudo_readthedocs_cedargrove_punkconsole.pdf>`_.


.. image:: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/Stereo_Punk_Console_test.png

The CedarGrove PunkConsole emulates an astable square-wave oscillator and
synchronized non-retriggerable one-shot monostable multivibrator to create
the classic stepped-tone generator sound of the Atari Punk Console. As with
the original circuit, the oscillator frequency and one-shot pulse width are
the input parameters. Instantiation of the Punk Console class will start the
output waveform based on the input parameters and enable the output signal
if `mute=False`. If no input parameters are provided, the output signal
will be disabled regardless of the mute value. Once instantiated, the class
is controlled by the `frequency`, `pulse_width_ms`, and `mute` properties.

This version of the emulator works only with PWM-capable output pins.

Depending on the timer and PWM capabilities of the host MPU board, the
emulator can easily outperform the original analog circuit. Oscillator
frequency is only limited by the MPU's PWM duty cycle and frequency
parameters, which may create output signals well above the practical audio
hearing range. Therefore, it is recommended that one-shot pulse width input
be limited to the range of 0.5ms and 5ms and that the oscillator frequency
input range be between 3Hz and 3kHz -- although experimentation is
encouraged!

The repo contains three examples, a simple single-channel console, an
annoying stereo noisemaker, and a note table driven sequencer. For the first
two examples, input is provided by potentiometers attached to
two analog input pins. The sequencer is controlled by an internal list of
notes that select the oscillator frequency; pulse width is potentiometer
controlled.

- Minimum and maximum input ranges (may be further limited by the MPU):
    - pulse_width: 0.05ms to  5000ms
    - frequency:      1Hz to >4MHz

- Practical input ranges for audio (empirically determined):
    - pulse_width:  0.5ms to 5ms
    - frequency:      3Hz to 3kHz

The CedarGrove Punk Console algorithm uses PWM frequency and duty cycle
parameters to build the output waveform. The PWM output frequency is an
integer multiple of the oscillator frequency input compared to the one-shot
pulse width input:

``pwm_freq = freq_in / (int((pulse_width) * freq_in) + 1)``

The PWM output duty cycle is calculated after the PWM output frequency is
determined. The PWM output duty cycle is the ratio of the one-shot pulse
width and the wavelength of the PWM output frequency:

``pwm_duty_cycle = pulse_width * pwm_freq``


Planned updates:

For non-PWM analog output, use ``audiocore`` with a waveform sample in the
``RawSample`` binary array, similar to the ``simpleio.tone()`` helper. The output
waveform's duty cycle will be adjusted by altering the contents of the array,
perhaps with `ulab` to improve code execution time. The
``audiocore.RawSample.sample_rate`` frequency is expected to be directly
proportional to the original algorithm's PWM frequency output value, calculated
from the ``sample_rate`` divided by the length of the ``audiocore.RawSample`` array
(number of samples).

MIDI control: A version that uses USB and/or UART MIDI is in the queue. Note
that the ``PunkConsole.mute`` property could be used for note-on and note-off.
``note_in_example.py`` shows how muting can be used for individual notes.

CV control: A Eurorack version was discussed, it's just a bit lower on the
to-do list, that's all. But you know, the first two examples use analog inputs
(0 to +3.3 volts) for frequency and pulse width control. Just sayin'.


.. image:: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/CG_PunkConsole_04.jpeg

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/CG_PunkConsole_01.jpeg

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/CG_PunkConsole_02.jpeg

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PunkConsole/blob/main/media/CG_PunkConsole_03.jpeg


For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_PunkConsole/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
