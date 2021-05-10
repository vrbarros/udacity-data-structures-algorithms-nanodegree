I decided to use the binary chop, where I compare the target number with middle element. The solution is to test 3 different hypotheses of results (using floor division with the number), keeping the execution until the exact number is found.

In the worst case, we can consider that the time complexity O(logn), and the space complexity is O(1). No additional space is needed to run this algorithm.

Reference:
- Binary Search Algorithm (https://en.wikipedia.org/wiki/Binary_search_algorithm)