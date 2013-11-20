from lotkavolterra import plot
from lotkavolterra import simulate
from lotkavolterra import BIRTH
from lotkavolterra import DEATH
from lotkavolterra import POPULATION

import sys
import getopt

def usage():
    print "Usage: make [options] [target] ..."
    print "Options:"
    print "  -a N, --rabbit-birth=N  Natural growth rate of prey when there are no predators. Default: ", rabbit_birth
    print "  -b N, --rabbit-death=N  Natural death rate of prey due to predation. Default: ", rabbit_death
    print "  -c N, --fox-death=N     Natural death rate of predators when there are no prey. Default: ", fox_death
    print "  -d N, --fox-birth=N     How many prey have to be caught and eaten to produce a new predator. Default: ", fox_birth
    print "  -f N, --num-foxes=N     Initial fox population. Default: ", num_foxes
    print "  -r N, --num-rabbits=N   Initial rabbit population. Default: ", num_rabbits
    print "  -t N, --time=N          End time for simulation. Default: ", time
    print "  -n N, --time-steps=N    Number of time steps to run simulation for. Default: ", time_steps
    print "  -h, --help              Print this message and exit."

flags = "a:b:c:d:f:r:t:n:h"
long_flags = ["rabbit-birth=", "rabbit-death=", "fox-death=",
    "fox-birth=", "num-foxes=", "num-rabbits=",
    "time=", "time-steps=", "help"]

rabbit_birth = 1.0
rabbit_death = 0.1
fox_death = 1.5
fox_birth = 0.75
num_foxes = 4
num_rabbits = 20
time = 20
time_steps = 2000

try:
    options, arguments = getopt.getopt(sys.argv[1:], flags, long_flags)
except getopt.GetoptError as err:
    usage()
    sys.exit()
for option, argument in options:
    if option in ("-h", "--help"):
        usage()
        sys.exit()
    elif option in ("-a", "--rabbit-birth"):
        rabbit_birth = float(argument)
    elif option in ("-b", "--rabbit-death"):
        rabbit_death = float(argument)
    elif option in ("-c", "--fox-death"):
        fox_death = float(argument)
    elif option in ("-d", "--fox-birth"):
        fox_birth = float(argument)
    elif option in ("-f", "--num-foxes"):
        num_foxes = float(argument)
    elif option in ("-r", "--num-rabbits"):
        num_rabbits = float(argument)
    elif option in ("-t", "--time"):
        time = float(argument)
    elif option in ("-n", "--time-steps"):
        time_steps = float(argument)

predator_config = {}
predator_config[BIRTH] = fox_birth
predator_config[DEATH] = fox_death
predator_config[POPULATION] = num_foxes
prey_config = {}
prey_config[BIRTH] = rabbit_birth
prey_config[DEATH] = rabbit_death
prey_config[POPULATION] = num_rabbits

(time_series, prey, predator) = simulate(prey_config, predator_config, time, time_steps)
plot(time_series, prey, predator)
