import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from strategies.run_zipline import run_strategy
import zipline
import os
from zipline.api import set_benchmark, symbol


def main():
    zipline_dir = os.path.dirname(zipline.__file__)
    print("*** Zipline is installed @ {} ***".format(zipline_dir))
    perf = run_strategy("auto_correlation")
    #perf.to_csv("buy_and_hold.csv")
    perf.to_csv("auto_correlation.csv")


if __name__ == '__main__':
    main()
    

