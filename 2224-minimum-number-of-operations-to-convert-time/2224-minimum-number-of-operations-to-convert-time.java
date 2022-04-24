class Solution {
    public int convertTime(String current, String correct) {
        int time_d = convertmin(correct) - convertmin(current);
        int rounds = 0;
        
        int r = 0;
        while(time_d != 0){
            if (time_d >= 60){
                r = time_d/60;
                rounds += r;
                time_d %= 60;
            }
            if (time_d >= 15){
                r = time_d/15;
                rounds += r;
                time_d %= 15;
            }
            if (time_d >= 5){
                r = time_d/5;
                rounds += r;
                time_d %= 5;
            }
            if (time_d >= 1){
                r = time_d/1;
                rounds += r;
                time_d %= 1;
            }
        }
        return rounds;
    }
    static int convertmin(String a){
        int ans = 0;
        String[] time = a.split(":");
        ans += Integer.parseInt(time[0])*60 + Integer.parseInt(time[1]);
        // System.out.println(Arrays.toString(time));
        // System.out.println(ans);
        return ans;
    }
}