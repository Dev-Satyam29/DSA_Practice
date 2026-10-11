class Solution {
    public int minRotations(String s) {
        int ans=0;
        int start=0;
        int m=10;
        for(int i=0;i<s.length();i++){
            int num = s.charAt(i) - '0';
            int clockwise=(num-start+m)%m;
            int anticlock=(start-num+m)%m;
            ans+=Math.min(clockwise,anticlock);
            start=num;
        }
        return ans;
    }
}