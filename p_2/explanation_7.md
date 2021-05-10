For this problem Trie and TrieNode are a better approach (same used before in the problem 5, with a few adjustments). It was important to clean the path.

The add method has the time and space complexity is O(n) where n is the number of directories and each part of the path needs to be iterated and a TrieNode is created multiple times.

The lookup method the time complexity is O(n) and space complexity is O(1) once that no additional memory is allocated.

