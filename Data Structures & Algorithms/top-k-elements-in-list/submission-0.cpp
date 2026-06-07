class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // create a frequency map
        // O(n)
        unordered_map<int, int> count;
        for (int& num : nums) {
            count[num] += 1;
        }

        // freq_t is of type (number, frequency)
        using freq_t = pair<int, int>;
        // using < for max-heap
        auto freq_comparator = [](freq_t a, freq_t b) {
            return a.second < b.second;
        };

        priority_queue<freq_t, vector<freq_t>, decltype(freq_comparator)> max_heap(freq_comparator);

        // do a heap-sort by putting pairs into heap
        // O(n log n)
        for (auto& [num, freq] : count) {
            max_heap.emplace(num, freq);
        }
        
        // now, find the top k
        vector<int> top_k;
        for (int i = 0; i < k; i++) {
            // given that heap has at least 1 element left
            top_k.push_back(max_heap.top().first);
            max_heap.pop();
        }

        return top_k;

    }
};