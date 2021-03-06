#!/usr/bin/env python
"""
Example of receive processing for PiRadar waveform

./receive.py input/code-l10000-b10-000000.bin output/rx-sim.bin
"""
import numpy as np
from matplotlib.pyplot import show

#
from piradar import estimate_range


def range_example(fntx, fnrx, fs, verbose=True):

    tx = np.fromfile(fntx, np.complex64)
    rx = np.fromfile(fnrx, np.complex64)

    if verbose:
        print(f"TX samples {tx.size}   RX samples {rx.size}")

    distest_m = estimate_range(tx, rx, fs, not verbose)

    return distest_m


if __name__ == "__main__":
    from argparse import ArgumentParser

    p = ArgumentParser()
    p.add_argument("fntx", help="file containing samples of transmit waveform")
    p.add_argument("fnrx", help="file containing samples of receive waveform")
    p.add_argument("--fs", help="sample rate [Hz]", default=100000)
    p = p.parse_args()

    distest_m = range_example(p.fntx, p.fnrx, p.fs)

    print(f"estimated one-way distance  {distest_m/1e3:.1f} km")

    show()
