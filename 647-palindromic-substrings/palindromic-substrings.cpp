class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        int count = 0;

        for (int i = 0; i < n; ++i) {
            count += countPalindromes(s, i, i); // Odd length palindromes with center at i
            count += countPalindromes(s, i, i + 1); // Even length palindromes with center between i and i+1
        }

        return count;
    }

private:
    int countPalindromes(const string& s, int left, int right) {
        int count = 0;

        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            ++count;
            --left;
            ++right;
        }

        return count;
    }
};
