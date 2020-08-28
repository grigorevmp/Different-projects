# Sort the odd

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
#
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
#
# Example
#
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    x = sorted([i for i in source_array if i % 2], reverse=False)
    y = [i for i in source_array if not i % 2]
    source_array = [1 if i % 2 else 0 for i in source_array]
    return [x.pop(0) if source_array[i] else y.pop(0) for i in range(len(source_array))]
