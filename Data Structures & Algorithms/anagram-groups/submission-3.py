class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary where keys are default type lists (hashmap)
        res = defaultdict(list)

        # iterate through the list of strings
        for s in strs:
            # set up an array for every string in strs (this will be defaulted for every s)
            # it has a size of 26 so that each index can keep track of the number of characters 
            # of the alphabet that the string s contains
            # ex: ate -> [1, 0, 0, 0, 1, 0, ..., 1, ..., 0]
            #             a, b, c, d, e, f, ..., t, ..., z
            counter = [0] * 26

            # iterate thru each character in the respective string
            for c in s:
                # have to account for 0 indexing, so we take the ascii value using ord() of the 
                # character and then we substract it by the ascii value of 'a' to serve as a base
                counter[ord(c) - ord("a")] += 1

                # after the line of code above we know have a unique list that is only similar for
                # strings that have the same number and type of characters in them
            # the array is our key and then the values are the different strings
            # NOTE: we convert from a list to a tuple here bc python does not allow for lists to be keys
            res[tuple(counter)].append(s)
        # return the values. keep in mind that they want a list of lists, so by using list() function
        # it creates a list and every entry will be every value of our hashmap!
        return list(res.values())