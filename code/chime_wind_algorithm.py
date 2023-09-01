# SPDX-FileCopyrightText: Copyright (c) 2023 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT

"""
`chime_wind_algorithm`
===============================================================================
A test of a windchime wind speed algorithm.

* Author(s): JG for Cedar Grove Maker Studios

Implementation Notes
--------------------

**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

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
mixer.voice[0].level = 0.6

# Instantiate the chime synth with mostly default parameters
chime = Chime(mixer.voice[0], scale=Scale.HarryDavidPear)

# Play scale notes sequentially
for index, note in enumerate(chime.scale):
    chime.strike(note, 1)
    time.sleep(0.4)
time.sleep(1)

while True:
    # Play randomly; assume wind speed < 5MPH


    chime_index = []
    chime_index.append(random.randrange(len(chime.scale)))
    direction = random.choice((-1, 1))
    chime_index.append((chime_index[0] + direction) % len(chime.scale))
    chime_index.append((chime_index[1] + direction) % len(chime.scale))

    notes_to_play = random.randrange(len(chime_index) + 1)

    print(direction, chime_index, notes_to_play)

    #time.sleep(3)

    for count in range(notes_to_play):
        print(f"count {count}  index {chime_index[count]}")
        chime.strike(chime.scale[chime_index[count]], 1)
        time.sleep(random.randrange(1, 6) * 0.1)

    time.sleep(random.randrange(1, 8) * 0.5)
