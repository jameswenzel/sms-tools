from A1Part1 import readAudio
from A1Part2 import minMaxAudio
from A1Part3 import hopSamples
from A1part4 import downsampleAudio
import numpy as np

assert readAudio('../sms-tools/sounds/piano.wav') == np.array([-0.06213569, -0.04541154, -0.02734458, -0.0093997 ,  0.00769066,	0.02319407,  0.03503525, 
0.04309214, 0.04626606,  0.0441908], dtype=float32)

