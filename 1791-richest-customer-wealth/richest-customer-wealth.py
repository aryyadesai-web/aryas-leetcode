class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealths=[]
        for i in accounts:
            wealth=0
            for j in i:
                wealth=wealth+j
            wealths.append(wealth)
        return max(wealths)