/*
LeetCode - Easy 136. Single Number

Idea :
  1 - go through each elements in nums
  2 - do a xor between all the elements
  3 - only the unique element will remain

Runtime: 31 ms, faster than 57.36% of C++ online submissions for Single Number.
Memory Usage: 16.9 MB, less than 52.94% of C++ online submissions for Single Number.
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int tmp = 0;
        for(int i : nums){
            // copies the bit if it is set in one operand but not both.
            tmp ^= i;
        }
        return tmp;
    }
};
