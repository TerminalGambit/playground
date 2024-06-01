import java.util.List;
class Solution {
    public void moveZeroes(List<Integer> nums) {
        int p=0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) != 0) {
                swap(nums, p++, i);
            }
        }
    }
    
    private void swap(List<Integer> nums, int i, int j) {
        int temp = nums.get(i);
        nums.set(i, nums.get(j));
        nums.set(j, temp);
        }
}