pass  # YOUR CODE HERE
def manhattan(a, b):
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    return d_x + d_y

import math

def euclidean(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)