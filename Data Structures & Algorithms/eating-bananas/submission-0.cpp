class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // idea: binary search on the search space
        int lo = 1;
        int hi = 1e9;
        int mid = 0;
        while (lo < hi) {
            mid = lo + ((hi - lo) / 2);
            if (isValid(piles, mid, h)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

private:
    bool isValid(vector<int>& piles, int k, int h) {
        int count = 0;
        for (int i = 0; i < (int)piles.size(); i++) {
            count += (piles[i] + (k - 1)) / k;
        }
        return count <= h;
    }
};