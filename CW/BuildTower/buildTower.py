# Build Tower

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *

def tower_builder(n_floors):
    return [' '*((n_floors*2-n)//2)+'*' * n+' '*((n_floors*2-n)//2) for n in range(1, n_floors*2,2)]

