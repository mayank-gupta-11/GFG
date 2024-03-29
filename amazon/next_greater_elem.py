"""
Input: [4, 2, 5, 7, 1, 8, 9, 3]
Output: {4: 5, 2: 5, 5: 7, 7: 8, 1: 8, 8: 9, 9: -1, 3: -1}

"""
def next_greater(arr):
  stack = []
  result = {}

  # Iterate through the list in reverse order
  for i in range(len(arr)-1, -1, -1):
    # Pop elements from the stack until we find an element that is
    # greater than or equal to the current element
    while stack and stack[-1] <= arr[i]:
      stack.pop()
    # If the stack is empty, there is no next greater element
    if not stack:
      result[arr[i]] = -1
    # Otherwise, the next greater element is the top element of the stack
    else:
      result[arr[i]] = stack[-1]
    # Push the current element onto the stack
    stack.append(arr[i])
