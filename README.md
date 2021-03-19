# HalwarsingRandom  
My own random algorithm  

To use random, you need two python libraries:  
pip install time  
pip install sys  

To install my project, you need to write to the console:  
pip install halran  

Usage example:  
```python
from halran import *
print(random.randint(0,10,0.1))
print(random.randelem(['hi','hello','bye']))
```
  

Functions:   
random.randint(from (float or integer),to (float or integer),step (float or integer), additional difficult (random execution time, the longer the better the random; integer)) \n
out: random number;   

random.randelem(array (array))  
out: random element of array;  

Algorithm:  
The program first takes the beginning of the execution time, then calculates the options for steps and gives the processor the task to list from 100000, so that the time passes, and then takes the end time and checks that it is not more than the number of options for steps and until it is less, it will not stop. This random can be considered real, since it is impossible to guess how long it will take the processor to complete this task.
