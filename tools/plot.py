#!/usr/bin/env python


import click
from matplotlib import pyplot

__author__ = 'smore <smore@student.tugraz.at>'

'''
Plot cache template attack calibration histogram.

Tested with Python 2.7.

Usage:
    * ./calibration > data.txt
    * python ./plot.py --data data.txt --out plot.png
    * More options: ./plot.py --help

Install requirements:
    * pip install -r requirements.txt

Resources:
    * https://github.com/IAIK/cache_template_attacks
'''


def doPlot(bins, hit, miss, use_log, title, out_file):
    pyplot.figure()
    hitplot = pyplot.bar(bins, hit, log=use_log, color='g', edgecolor='g')
    missplot = pyplot.bar(bins, miss, log=use_log, color='r', edgecolor='r')
    pyplot.ylabel('frequency')
    pyplot.xlabel('access time')
    pyplot.legend([hitplot, missplot], ["hit", "miss"])
    pyplot.title(title)
    if out_file is None:
        pyplot.show()
    else:
        pyplot.savefig(out_file)


def parseHist(hist_file):
    bins = list()
    hit = list()
    miss = list()
    with open(hist_file) as f:
        data = f.readlines()
    data = filter(lambda l: l.strip()[0].isdigit(), data)
    data = map(lambda l: l.strip().split(), data)
    bins = map(lambda l: int(l[0][:-1]), data)
    hit = map(lambda l: int(l[1]), data)
    miss = map(lambda l: int(l[2]), data)
    return bins, hit, miss


@click.command()
@click.option('--log/--no-log', default=True, help='Plot in log scale?')
@click.option('--out', default=None, help='Output file for the plot.')
@click.option(
    '--data',
    required=True,
    help='Calibration hisogram data (output of calibration tool).')
@click.option(
    '--title',
    default='Cache hit/miss Histogram',
    help='Plot title.')
def main(data, log, title, out):
    bins, hit, miss = parseHist(data)
    doPlot(bins, hit, miss, log, title, out)

if __name__ == '__main__':
    main()
