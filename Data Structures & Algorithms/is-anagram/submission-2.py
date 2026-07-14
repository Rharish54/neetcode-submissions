class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # THIS SOLUTION IS O(nlgn), there is an O(n) SOLUTION!!!
        if len(s) != len(t):
            return False
        
        # lowk bs way of solving this problem
        # I sorted the two strings and then checked 
        # if they are equal
        new_s = sorted(s)
        # we use .join() here because all sorted()
        # does is it returns a list of the sorted characters
        # and then .join() brings them back into string format
        final_s = "".join(new_s)

        new_t = sorted(t)
        final_t = "".join(new_t)
        return final_s == final_t
