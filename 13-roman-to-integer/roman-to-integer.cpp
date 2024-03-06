class Solution {
public:
    int romanToInt(const string& s) {
        unordered_map<char, int> roman = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int ans = 0;
        int prevValue = 0; // Store the value of previous numeral

        for (int i = s.length() - 1; i >= 0; --i) {
            int currentValue = roman[s[i]];
            if (currentValue < prevValue) {
                ans -= currentValue;
            } else {
                ans += currentValue;
            }
            prevValue = currentValue; // Update the previous value
        }

        return ans;
    }
};
