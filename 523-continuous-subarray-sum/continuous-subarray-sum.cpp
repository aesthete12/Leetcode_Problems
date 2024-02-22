class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int prefix = 0;
        unordered_set<int> prefixSet;
        int runningSum = 0; // To track the running sum of the prefix

        for (int i = 0; i < nums.size(); ++i) {
            prefix += nums[i];
            if (k != 0)
                prefix %= k; // Apply modulus operation only when k is non-zero
            
            if (prefixSet.count(prefix)) {
                return true;
            }
            
            // Add the running sum to the set before checking for the next index
            prefixSet.insert(runningSum);
            runningSum = prefix;
        }

        return false;
    }
};
