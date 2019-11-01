#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.random.random((2,3,5))


#4. Print a.
print(a)


#5. Create a 5x3x2 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.ones((5,3,2))


#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print(b.size==a.size)



#8. Are you able to add a and b? Why or why not?

#No, because they have different shape.


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c=b.T


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d=np.add(a,c)
#Because they have the same shape.

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
#print(d)



#12. Multiply a and c. Assign the result to e.
e = np.multiply(a,c)


#13. Does e equal to a? Why or why not?
print(e==a)
#Yes, because you are multiplying by one.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2,3,5))
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
def values(x):
    if x == d_min:
        x = 0
    elif x == d_max:
        x = 100
    elif 0 < x < d_mean:
        x = 25
    elif x == d_mean:
        x = 50
    elif d_mean < x < d_max:
        x = 75
    return x


for t in range(2):
    for e in range(3):
        f[t][e] = [values(x) for x in d[t][e]]
"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
