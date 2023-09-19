"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    # base case: foo(0) = 0, foo(1) = 1
    if x <= 1:     
        return x
    #recursive case: sum previous two elements
    else:
        return foo(x-1)+foo(x-2)


def longest_run(mylist, key):
    current_sequence = 0
    longest_sequence = 0
    for i in mylist:
        # if current element = key, increase the value of the current sequence. If the current sequence is greater than the longest sequence, it is the new longest sequence
        if i == key:
            current_sequence += 1
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
        # if the current element does not match key, the sequence is broken. reset current sequence and don't change max sequence
        else: 
            current_sequence = 0
    return longest_sequence



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def longest_run_recursive(mylist, key):
        """
        base case is a list of size 1, the two possibilites are that the element matches the key or it doesn't, the return type is Result
        if the element matches the key, the longest run is 1 and the entire input does match the key, otherwise the longest run is 0
        and the input does not match key
        """
        if len(mylist) == 1:
            if mylist[0] == key:
                result = Result(1, 1, 1, True)
            else:
                result = Result(0,0,0, False)
        else:
            """
            For the recursive step, mylist is split into two halves and the longest_run_recursive function is called on them. 
            Depending on the conditions of the left and right side, the result is determined differently.
            If the entire input matches the key for both sides, the combined longest run is now equal to the sum of the left and right
            longest run and the entire input still matches.
            If only one of the lists had the entire input match the key, the longest run is equal to the longest run of that list plus
            the longest run of the half of the list it is merging with that is closest to it. 
            If both total inputs do not match, the longest run is equal to the longest run on the left or right side or the sum of the 
            longest run on the right side of the left list and the left side of the right list, whichever is largest.
            """
            left_side = longest_run_recursive(mylist[0:len(mylist)//2], key)
            right_side = longest_run_recursive(mylist[len(mylist)//2:], key)
            if ((left_side.is_entire_range == True) and (right_side.is_entire_range == True)):
                result = Result(left_side.longest_size, right_side.longest_size, left_side.longest_size + right_side.longest_size, True)
            elif (left_side.is_entire_range == True and right_side.is_entire_range == False):
                result = Result(left_side.longest_size + right_side.left_size, right_side.longest_size, left_side.longest_size + right_side.left_size, False)
            elif (left_side.is_entire_range == False and right_side.is_entire_range == True):
                result = Result(left_side.longest_size, right_side.longest_size + left_side.right_size, left_side.right_size + right_side.longest_size, False)
            else:
                result = Result(left_side.longest_size, right_side.longest_size, max(left_side.right_size + right_side.left_size, left_side.longest_size,  right_side.longest_size), False)
        return result
      
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([12,12, 12,12,12,12], 12) == 6
    assert longest_run([2,12,8,12,0,12,1], 12) == 1
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([12,12, 12,12,12,12], 12) == 6
    assert longest_run_recursive([2,12,8,12,0,12,1], 12) == 1
    

