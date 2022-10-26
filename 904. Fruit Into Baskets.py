class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        maxNum = 0

        start = 0
        end = 0

        baskets = {}

        while end < len(fruits):
            baskets[fruits[end]
                    ] = 1 if fruits[end] not in baskets else baskets[fruits[end]]+1
            while start < end and len(baskets) > 2:
                baskets[fruits[start]] -= 1
                if baskets[fruits[start]] == 0:
                    del baskets[fruits[start]]
                start += 1

            maxNum = max(maxNum, end - start + 1)
            end += 1

        return maxNum
