class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min rate is total_banana // hours +1
        # max rate is the max(bananas of pile)
        total_bananas = sum(piles)
        if total_bananas % h != 0:
            min_rate = total_bananas // h + 1
        else:
            min_rate = total_bananas // h 
        max_rate = max(piles)
        
        # then use the binary to find the good time
        def find_hours(piles: List[int], r: int) -> int:
            h = 0
            for p in piles:
                if p%r ==0:
                    h += p // r
                else:
                    h += p // r + 1
            return h
        
        while min_rate <= max_rate:
            middle_rate = min_rate + (max_rate - min_rate) // 2
            if find_hours(piles, middle_rate) > h:
                # too slow
                min_rate = middle_rate + 1
            elif find_hours(piles, middle_rate) <= h:
                # if do not catch here, the next slow one may catch as result
                res = middle_rate
                # fast, want to find slower rate
                max_rate = middle_rate - 1
            
        return res
        



        