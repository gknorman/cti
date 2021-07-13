# Given an unsorted integer array with max value n = length(integers), 
# find the first missing positive integer in O(n) time with constant space.
# Used partial sum formula from: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
def first_missing_positive_integer_unsorted_On(integers):
    n = len(integers)
    result = partial(n) - sum(integers)
    return n if result == 0 else result
   
def partial(n):
    sums = (n * (n+1))/2
    return sums
    n = len(integers)
    result = partial(n) - sum(integers)
    return n if result == 0 else result
   
def partial(n):
    sums = (n * (n+1))/2
    return sums
    
if __name__ == "__main__":
    print("Test 1: [0, 1,2] - should be: 3")
    print("RESULT:", first_missing_positive_integer_unsorted_On([0, 1,2]))
    
    print("\nTest 2: [1,0,3,4] - should be: 2")
    print("RESULT:", first_missing_positive_integer_unsorted_On([1,0,3,4]))
    
    print("\nTest 3: [8, 9, 1, 2, 3, 4, 5, 7, 0] \n- should be: 6")
    print("RESULT:", first_missing_positive_integer_unsorted_On([8, 9, 1, 2, 3, 4, 5, 7, 0]))
    
    print("\nTest 4: [11, 14, 2, 3, 12, 4, 1, 5, 6, 7, 8, 9, 10, 0, 15] \n- should be: 13")
    print("RESULT:", first_missing_positive_integer_unsorted_On([11, 14, 2, 3, 12, 4, 1, 5, 6, 7, 8, 9, 10, 0, 15]))
