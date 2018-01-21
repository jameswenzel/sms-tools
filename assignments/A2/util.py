import numpy as np
from A2Part1 import genSine
from A2Part3 import DFT
from A2Part4 import IDFT
from A2Part5 import genMagSpec

are_close = lambda a, b: all(np.isclose(x, y) for x, y in zip(a, b))

print(genSine(1,2,0,8,1))
print(genMagSpec(genSine(1,2,0,8,1)))
print(IDFT(np.array([4,0,0,0])))