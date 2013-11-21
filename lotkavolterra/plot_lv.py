import getopt
import numpy as np
import sys
from lotkavolterra import plot

def usage():
    '''Print usage information.'''
    print "View the results of a simulation of the evolution of a population of predators and prey using the Lotka-Volterra equations."
    print "This program expects to find three files - prey.csv, predator.csv and time_series.csv - holding the outputs of the simulation"
    print "Usage: python ploy_lv.py"
    print "Options:"
    print "  -h, --help              Print this message and exit."

flags = "h"
long_flags = ["help"]

try:
    options, arguments = getopt.getopt(sys.argv[1:], flags, long_flags)
except getopt.GetoptError as err:
    usage()
    sys.exit()
for option, argument in options:
    if option in ("-h", "--help"):
        usage()
        sys.exit()

prey = np.loadtxt("prey.csv", delimiter=",")
predator = np.loadtxt("predator.csv", delimiter=",")
time_series = np.loadtxt("time_series.csv", delimiter=",")

plot(time_series, prey, predator)
