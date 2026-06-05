class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        seen.reserve((int)nums.size());
        for (int i = 0; i < (int)nums.size(); i++) {
            // insert returns {iterator, new_val_bool}, so
            // new_val_bool is false -> duplicate found
            if (!seen.insert(nums[i]).second) {
                return true;
            }
        }
        return false;
    }
};