# Good Programming Practice

Yesterday, we finished with a script that simulated predator-prey behavior via an implementation of the Lotka-Volterra equations using NumPy, SciPy and matplotlib. Today we'll clean up that script into a program, exploring aspects of good programming practice along the way.

## Get rid of the globals

The difficult bit is, so we'll do this first

def dX_dt(X, t, a, b, c, d):
   return np.array([ a*X[0] - b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1] ])

X = integrate.odeint(dX_dt, X_initial, t, args=(a, b, c, d))

python predators.py

## Refactor into functions





Now partition the rest into two functions:

def plot(t, predators, prey)

and

def simulate(a, b, c, d)

...which calls plot

and our only non-function code is

a=...
b=...
c=...
d=...
simulate(a,b,c,d)
---

python predators.py


Now return tuple (pr, pr, t) from simulate so program is
 
...
(pre,pre,t) = simulate(a,b,c,d)
plot(pre, pre, t)


## Rename variables

## Comment

What versus why

## Save data as a file


## Add command-line - optional

Did a lot of changes there tomorrow we'll see how we can test this
Here's one I prepared earlier - further to bundle b,d,pop into a class (like a C struct)

python script.py a b c d cats mice

## Outputs

Output data file
Output mean hares and pumas

Now we have a configurable program of reusable components!
