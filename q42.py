"""
Date: 2018/9/18
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        punk = 0
        top_l = height[left]
        top_r = height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] <= top_l:
                    punk += top_l - height[left]
                else:
                    top_l = height[left]
                left += 1
            else:
                if height[right] < top_r:
                    punk += top_r - height[right]
                else:
                    top_r = height[right]
                right -= 1
        return punk

    def trap2(self, height):
        ans = 0
        cur = 0
        st = []
        while cur < len(height):
            while st and height[cur] > height[st[-1]]:
                top = st[-1]
                st.pop(-1)
                if not st:
                    break
                dist = cur - st[-1] - 1
                bound = min(height[cur], height[st[-1]]) - height[top]
                ans += dist * bound
            st.append(cur)
            cur += 1
        return ans


print(Solution().trap2([0,1,0,2,1,0,1,3,2,1,2,1]))

