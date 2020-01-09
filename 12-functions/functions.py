def sum(x,y):
    result = x + y
    return result

def cube(x):
    return x * x * x

def calculate_steps(distance,step_length):
    return distance / step_length

def absolute_diff(x,y):
    if(x > y):
        return x - y
    else:
        return y - x

def absolute_diff2(x,y):
    return abs(x-y)