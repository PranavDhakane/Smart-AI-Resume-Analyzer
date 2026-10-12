/* 
LeetCode 2897: Apply Operations on Array to Maximize Sum of Squares
Easy problem statement
You are given an integer array nums and a number k.
You can choose any two different elements from the array and perform two operations:
- AND (&): Keeps only the bits that are 1 in both numbers.
- OR (|): Keeps the bits that are 1 in either number.
Update the first element with the AND result and the second element with the OR result at the same time.
You can repeat this operation as many times as you want.
Your task is to choose exactly k elements from the final array so that the sum of their squares is as large as possible.
Return the maximum sum modulo \(10^9+7\).
Example
Input:
nums = [2, 6, 5, 8]
k = 2


Output:
261


Explanation:
After applying the operations, we can get:
nums = [0, 6, 0, 15]


Choose the two elements 15 and 6.
Calculate their squares:
\[
15^2 + 6^2 = 225 + 36 = 261
\]

Therefore, the answer is 261.
What do you need to understand?
1. You can perform the operation any number of times.
2. You must choose exactly k elements.
3. Square each chosen element and add the results.
4. Make this sum as large as possible.
In one sentence: Rearrange the bits of the array elements using AND and OR operations to maximize the sum of squares of k selected elements.

*/



import java.util.*;

class Solution {
    public int maxSum(List<Integer> nums, int k) {
        int MOD = 1_000_000_007;
        int[] bitCount = new int[31];

        // Count set bits at each position
        for (int num : nums) {
            for (int bit = 0; bit < 31; bit++) {
                if ((num & (1 << bit)) != 0) {
                    bitCount[bit]++;
                }
            }
        }

        long ans = 0;

        // Build k maximum numbers
        for (int i = 0; i < k; i++) {
            long num = 0;

            for (int bit = 0; bit < 31; bit++) {
                if (bitCount[bit] > 0) {
                    num |= (1L << bit);
                    bitCount[bit]--;
                }
            }

            ans = (ans + num * num) % MOD;
        }

        return (int) ans;
    }
}
