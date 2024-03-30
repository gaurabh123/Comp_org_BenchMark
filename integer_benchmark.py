# codes for colors in terminal
import time

COLOR_RED = "x1b[31m"
COLOR_GREEN = "x1b[32m"
COLOR_YELLOW = "x1b[33m"
COLOR_RESET = "x1b[0m"

def integer_bench():
    accumulated_time = 0
    test_value = 7
    calulation_result = 0

    #now doing 10 ^ 10 additions of integer constants

    beginnig_time = time.time()
    for _ in range(10000):
        for _ in range(10000):
            calulation_result = test_value + test_value
    completion_time = time.time()
    accumulated_time += completion_time - beginnig_time

    

