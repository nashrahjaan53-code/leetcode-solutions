class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)
        
        water = sorted(zip(waterStartTime, waterDuration))
        pref_min_dur = [0] * m
        pref_min_dur[0] = water[0][1]
        for i in range(1, m):
            pref_min_dur[i] = min(pref_min_dur[i-1], water[i][1])
        suff_min_finish = [0] * m
        suff_min_finish[m-1] = water[m-1][0] + water[m-1][1]
        for i in range(m-2, -1, -1):
            suff_min_finish[i] = min(suff_min_finish[i+1], water[i][0] + water[i][1])
        
        def best_after(t):
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) // 2
                if water[mid][0] <= t:
                    lo = mid + 1
                else:
                    hi = mid
            res = float('inf')
            if lo > 0:
                res = t + pref_min_dur[lo-1]
            if lo < m:
                res = min(res, suff_min_finish[lo])
            return res
        
        ans = float('inf')
        for i in range(n):
            finish_land = landStartTime[i] + landDuration[i]
            ans = min(ans, best_after(finish_land))
        
        land = sorted(zip(landStartTime, landDuration))
        pref_min_dur_l = [0] * n
        pref_min_dur_l[0] = land[0][1]
        for i in range(1, n):
            pref_min_dur_l[i] = min(pref_min_dur_l[i-1], land[i][1])
        suff_min_finish_l = [0] * n
        suff_min_finish_l[n-1] = land[n-1][0] + land[n-1][1]
        for i in range(n-2, -1, -1):
            suff_min_finish_l[i] = min(suff_min_finish_l[i+1], land[i][0] + land[i][1])
        
        def best_after_land(t):
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) // 2
                if land[mid][0] <= t:
                    lo = mid + 1
                else:
                    hi = mid
            res = float('inf')
            if lo > 0:
                res = t + pref_min_dur_l[lo-1]
            if lo < n:
                res = min(res, suff_min_finish_l[lo])
            return res
        
        for j in range(m):
            finish_water = waterStartTime[j] + waterDuration[j]
            ans = min(ans, best_after_land(finish_water))
        
        return ans





        


        