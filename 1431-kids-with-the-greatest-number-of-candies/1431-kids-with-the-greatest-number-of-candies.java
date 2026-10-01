class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int highest_num=candies[0];
        for(int n:candies){
            highest_num=Math.max(highest_num,n);
        }
        ArrayList<Boolean> res=new ArrayList<>();
        for(int i=0;i<candies.length;i++){
            int temp=candies[i]+extraCandies;
            if(temp>=highest_num){
                res.add(true);
            }else{
                res.add(false);
            }
        }
        return res;
    }
}