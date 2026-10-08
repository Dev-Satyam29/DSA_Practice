class Solution {
    public int firstMissingPositive(int[] nums) {
        int n =nums.length;
        int[] freq=new int[n+1];
        for(int i:nums){
            if(1<=i && i<=n){
                freq[i]=1;
            }
        }
        for(int i=1;i<freq.length;i++){
            if(freq[i]==0){
                return i;
            }
        }
        return n+1;
    }
}