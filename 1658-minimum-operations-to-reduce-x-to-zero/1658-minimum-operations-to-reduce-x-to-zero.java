class Solution {
    public int minOperations(int[] nums, int x) {
        int sum=0;
        int n=nums.length;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        int target=sum-x;
        if(target==0){
            return n;
        }
        if(target<0){
            return -1;
        }
        int left=0;
        int curr=0;
        int best=-1;
        for(int r=0;r<n;r++){
            curr+=nums[r];
            while(curr>target){
                curr-=nums[left];
                left+=1;
            }
            if(curr==target){
                best=Math.max(best,r-left+1);
            }
        }
        if(best==-1){
            return -1;
        }else{
            return n-best;
        }
    }
}