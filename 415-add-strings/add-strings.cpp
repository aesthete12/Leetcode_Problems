class Solution {
 public:
  string addStrings(string num1, string num2) {
    string ans;
    int carry = 0;
    int i = num1.length() - 1;
    int j = num2.length() - 1;

    while (i >= 0 || j >= 0 || carry) {
      int sum = carry;
      if (i >= 0) {
        sum += num1[i] - '0';
        i--;
      }
      if (j >= 0) {
        sum += num2[j] - '0';
        j--;
      }
      carry = sum / 10;
      ans = to_string(sum % 10) + ans;
    }

    return ans;
  }
};
