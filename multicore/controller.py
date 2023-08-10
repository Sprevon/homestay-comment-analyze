import multiprocessing
from multiprocessing import Process

from multicore.ida.ida_multicore import compute_mul

if __name__ == '__main__':
    start = 0
    end = 1000
    compute_mul(start, end)

