import time

# start a time in nanoseconds
start = time.time_ns()

# number that we are attempting to find the pythagorean triples that sum to
target = 1000

# variable for the base number to calculate the pythagorean triple off of.
x = 1
flag = True
# base pythagorean triple values
a = 0
b = 0
c = 0

while flag:
    # increment calculator base
    x += 1
    # calculate the base pythagorean triple values
    # Equation based on Plato's formula for finding Pythagorean triples:
    #  (2m)^2 + (m^2 - 1)^2 = (m^2 + 1)^2
    a = (2 * x)
    b = (x ** 2 - 1)
    c = (x ** 2 + 1)

    # if we found the value, stop the loop
    if a + b + c == target or c > target:
        break

    # set the mod value to 1, we will start at 2 inside the loop
    mod = 1
    # it can be assumed that if c * mod > target, we cannot sum a, b, and c to be equal to the target....
    # it will probably be safe to make this number lower, but this is guaranteed
    while mod * c < target:
        # increment the modifier
        mod += 1
        # test the modified values
        if a * mod + b * mod + c * mod == target:
            # set the flag to exit the outer loop
            flag = False
            # set the triple values to the modified state since they are the droids we were looking for
            a = a * mod
            b = b * mod
            c = c * mod
            # exit the loop
            break

# stop the timer
print(time.time_ns() - start)
# print the found values
print("a:", a, "  b:", b, "  c:", c, "  sum:", a + b + c, "  project euler answer:", a * b * c)
