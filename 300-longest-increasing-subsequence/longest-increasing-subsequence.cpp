class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty())
            return 0;

        std::vector<int> lisEndings;
        lisEndings.push_back(nums[0]);

        for (int i = 1; i < nums.size(); ++i) {
            auto it = std::lower_bound(lisEndings.begin(), lisEndings.end(), nums[i]);
            if (it == lisEndings.end())
                lisEndings.push_back(nums[i]);
            else
                *it = nums[i];
        }

        return lisEndings.size();
    }
};
