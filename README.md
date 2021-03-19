# HalwarsingRandom
My own random algorithm

To use random, you need two python libraries: \n
pip install time \n
pip install sys \n

To install my project, you need to write to the console: \n
pip install halran \n

Usage example:\n
```python
from HalRan import *
print(random.randint(0,10,0.1))
print(random.randelem(['hi','hello','bye']))
```
\n

Functions: \n
random.randint(from (float or integer),to (float or integer),step (float or integer), additional difficult (random execution time, the longer the better the random; integer)) \n
out: random number; \n

random.randelem(array (array)) \n
out: random element of array; \n

Algorithm: \n
The program first takes the beginning of the execution time, then calculates the options for steps and gives the processor the task to list from 100000, so that the time passes, and then takes the end time and checks that it is not more than the number of options for steps and until it is less, it will not stop. This random can be considered real, since it is impossible to guess how long it will take the processor to complete this task.
