Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

explanation
: Start with left at the beginning (0) and right at the end (len(s) - 1).
While Loop: Continue swapping as long as left < right.
Swap the characters at s[left] and s[right].
Move left forward and right backward.

code=
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the characters at left and right indices
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards each other
            left += 1
            right -= 1

       
        
 
