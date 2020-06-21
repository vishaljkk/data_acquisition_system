import myModule
import random
from oscilloscope import Osc


# adjust window_sec and intensity to improve visibility
osc = Osc(window_sec=10, intensity=1)


@osc.signal
def increasing_signal(state):
    delta = 1

    while True:
        state.draw(random.randint(-delta, delta))
        delta += 5
        print(myModule.fib(3)) # CHANGE THE CODE HERE AYUSH

osc.start()
