class Solution:
    def countLargestGroup(self, n: int) -> int:

        ans = {}    # { sum of digits: [numbers] }
                    # e.i. { 1: [ 1,10 ] } because both 1 and 10 sum to 1

        for i in range(1,n+1):
            string_i = str(i)   # convert to string so that we can iterate through each stringed number
            sum_of_digits = 0

            for j in string_i: 
                sum_of_digits += int(j)

            # add sum group(key), and add numbers(value) to the sum group
            if sum_of_digits in ans:
                ans[sum_of_digits].append(i)
            else:
                ans[sum_of_digits] = [i]

        max_size = 0    
        for k,v in ans.items():
            max_size = max(max_size, len(v))    # get the largest size of the value

        count = 0
        for k,v in ans.items():
            if len(v) == max_size:
                count += 1  # count up if key with the largest sized value is found

        return count