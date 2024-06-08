class Solution 
{
    public boolean checkSubarraySum(int[] nums, int k) 
    {
        Map<Integer, Integer> remainderIndexMap = new HashMap<>();
        remainderIndexMap.put(0, -1);
        int sum = 0;
        for (int i = 0; i < nums.length; ++i) 
        {
            sum += nums[i];
            int remainder = sum % k;
            if (remainderIndexMap.containsKey(remainder) && i - remainderIndexMap.get(remainder) >= 2) 
            {
                return true;
            }
            remainderIndexMap.putIfAbsent(remainder, i);
        }
        return false;
    }
}