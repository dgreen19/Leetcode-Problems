class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ans = []
        
        for num in range (1, n+1):
            
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
               print("That is not the answer you're looking for.")
               ans.append(str(num))
        return ans
                           