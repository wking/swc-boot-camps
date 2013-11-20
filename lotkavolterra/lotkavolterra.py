import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

PREY = 0
PREDATOR = 1
BIRTH = "birth"
DEATH = "death"
POPULATION = "population"

def update_population(population, time, prey, predator):
    '''
    Calculate the change in a population of predators and prey using
    the Lotka-Volterra equations at a single time-step.

    Parameters
    ----------

    population : array-like
        Current population of predators and prey as an array
        of form [current prey population, current predator
        population]. 
    time : float
        Time-step value.
    prey : dict
        Dictionary specifying prey behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for prey birth and death
        rate.
    predator : dict
        Dictionary specifying predator behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for predator birth and death
        rate.

    Returns
    -------

    output : array
        Array of form [new prey population, new predator population].
    '''
    return np.array([ 
        prey[BIRTH]*population[PREY] - 
            prey[DEATH]*population[PREY]*population[PREDATOR],
        -predator[DEATH]*population[PREDATOR] + 
            predator[BIRTH]*prey[DEATH]*population[PREY]*population[PREDATOR]])

def simulate(prey, predator, end_time = 20, time_steps = 2000):
    '''
    Simulate the evolution of a population of predators and prey
    using the Lotka-Volterra equations.

    Parameters
    ----------

    prey : dict
        Dictionary specifying prey behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for prey birth and death
        rate, and an integer indexed by key POPULATION for initial 
        population.
    predator : dict
        Dictionary specifying predator behavior. This must hold floats
        indexed by keys BIRTH and DEATH, for predator birth and death
        rate, and an integer indexed by key POPULATION for initial 
        population.
    end_time : scalar, optional
        End-time for simulation in seconds. Default 20.
    time_steps : int, optional
        Number of time-steps. Simulation values will be calculated
        from time==0 to time==end_time with time_steps - 1
        intermediate values. Default 2000.

    Returns
    -------
  
    output: tuple
        3-element tuple consisting of an array of length time_steps
        with the time-steps for the simulation, an array of the prey
        population at each time-step, and an array of the predator
        population at each time-step.
    '''
    time_series = np.linspace(0, end_time, time_steps)
    initial_population = np.array([prey[POPULATION], predator[POPULATION]])
    populations = integrate.odeint(
        update_population, 
        initial_population, 
        time_series, 
        args=(prey, predator))
    return (time_series, populations[:, PREY], populations[:, PREDATOR])

def plot(time_series, prey, predators):
    '''
    Plot the change in predator and prey populations over time at
    intervals specified by a given time-series.

    Parameters
    ----------

    time_series : array
        Time-series.
    prey : array
        An array of the prey at each time-step in time_series.
    predators : array
        An array of the predators at each time-step in time_series.
    '''
    fig = plt.figure()
    plt.plot(time_series, prey, 'r-', label='Prey')
    plt.plot(time_series, predators, 'b-', label='Predators')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.title('Evolution of predator and prey populations')
    plt.show()
