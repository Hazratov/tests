class Solving:

    def close_with_zero(self, x: list) -> list:
        closest = x[0]
        for num in x:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest




    def find_duplicate(self, nums: list) -> bool:
        set_n = set(nums)

        if len(nums) == len(set_n) :
            return False
        return True




    def find_duplicate_2(self, nums: list) -> bool:
        result = []

        for num in nums:
            if not num in result:
                result.append(num)
        if len(nums) == len(result):
            return False
        return True

    def mergeAlternately(self, word1, word2):
        w_num1, w_num2 = len(word1), len(word2)
        n = max(w_num1, w_num2)
        result = ""
        for i in range(n):
            if i < w_num1:
                result += word1[i]
            if i < w_num2:
                result += word2[i]
        return result

    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if rev > (2 ** 31 - 1) // 10:
                return 0

            rev = rev * 10 + digit

        return rev * sign

    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            num_map[num] = i
        return []

obj = Solving()

print(obj.twoSum([3,2,4], 6))


