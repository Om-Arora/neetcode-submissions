class Solution {
public:
    int findMin(vector<int> &nums) {
        int n = nums.size();
        int lo = 0;
        int hi = n - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            // key insight: compare mid with hi instead of lo
            // since mid can equal lo but mid != hi always true
            // -> gives more information always
            if (nums[mid] > nums[hi]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        return nums[lo];;
    }
};
