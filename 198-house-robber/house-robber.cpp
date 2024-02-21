class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];

        int prevMax = nums[0];
        int currMax = max(nums[0], nums[1]);

        for (int i = 2; i < nums.size(); ++i) {
            int temp = currMax;
            currMax = max(currMax, prevMax + nums[i]);
            prevMax = temp;
        }

        return currMax;
    }
};
