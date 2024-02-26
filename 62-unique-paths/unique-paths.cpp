class Solution {
public:
    int uniquePaths(int m, int n) {
        // Ensure m is less than or equal to n for optimized space usage
        if (m > n) return uniquePaths(n, m);

        vector<int> dp(m, 1); // Store the number of unique paths for each column

        for (int j = 1; j < n; ++j) {
            for (int i = 1; i < m; ++i) {
                // The number of unique paths to reach (i, j) is the sum of the paths
                // from above (i-1, j) and left (i, j-1)
                dp[i] += dp[i - 1];
            }
        }

        return dp[m - 1];
    }
};
