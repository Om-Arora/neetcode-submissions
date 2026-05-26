class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        """
        pre[i] contains the product of everything up to, 
        but excluding, position i
        """
        pre = [1 for _ in range(n)]
        product = 1
        for i in range(1, n):
            product *= nums[i - 1]
            pre[i] = product

        """
        post[i] contains the product of everything after,
        and excluding, position i
        """
        post = [1 for _ in range(n)]
        product = 1
        for i in range(n - 1, 0, -1):
            product *= nums[i]
            post[i - 1] = product

        answer = [pre[i] * post[i] for i in range(n)]
        return answer

        