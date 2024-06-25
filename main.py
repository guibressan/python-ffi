#!/usr/bin/env python3

import ctypes
import time


class LibExamplePy:
    def iter(self, val: int):
        r = 0
        while val:
            r += val
            val -= 1
        return r


class LibExampleC:
    def __init__(self):
        self.lib = ctypes.CDLL("./libexample.so")

    def iter(self, val: int):
        self.lib.libexample_iter.argtypes = [ctypes.c_long]
        self.lib.libexample_iter.restype = ctypes.c_long
        return self.lib.libexample_iter(val)


def elapsed(func, label="default"):
    def wrap(*args, **kwargs):
        start = time.time()
        r1 = func(*args, **kwargs)
        elapsedms = (time.time() - start)*1000
        print(f"{label}: elapsed {elapsedms}ms")
        return r1
    return wrap


def test_wrapped(lib, val) -> int:
    return lib.iter(val)


def main():
    libex_c = LibExampleC()
    libex_py = LibExamplePy()
    val = 1_000_000_000
    exp = 500000000500000000

    r = elapsed(test_wrapped, label="C")(libex_c, val)
    if r != exp:
        print(f"exp: {exp}, got: {r}")

    r = elapsed(test_wrapped, label="Python")(libex_py, val)
    if r != exp:
        print(f"exp: {exp}, got: {r}")


if __name__ == "__main__":
    main()
