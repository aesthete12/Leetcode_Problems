class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        const int n = nums.size();
        int ans = 0;
        // dp[i][k] := the length of the longest arithmetic subsequence of
        // nums[0..i] with k = diff + 500
        unordered_map<int, unordered_map<int, int>> dp;

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j) {
                const int diff = nums[i] - nums[j];
                dp[i][diff] = max(2, dp[j].count(diff) ? dp[j][diff] + 1 : 2);
                ans = max(ans, dp[i][diff]);
            }

        return ans;
    }
};
