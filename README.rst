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
API documentation for this library can be found in `Cedargrove_Chime_API <https://github.com/CedarGroveStudios/CircuitPython_Chime/blob/main/media/pseudo_rtd_cedargrove_chime.pdf>`_.


.. image:: https://github.com/CedarGroveStudios/CircuitPython_Chime/blob/main/media/chime_api_page3.png

The CedarGrove Chimes class...


Planned updates:

...


