class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        
        int a_ar = date_to_i(arriveAlice);
        int a_l = date_to_i(leaveAlice);
        int b_ar = date_to_i(arriveBob);
        int b_l = date_to_i(leaveBob);
        
        int[] year = new int[366];
        for (int i = a_ar; i <= a_l; i++) 
            year[i] = 1;
        

        for (int i = b_ar; i <= b_l; i++) 
            if (year[i] == 1) year[i]++;
        

        int count = 0;
        for (int i : year)
            if (i == 2) count++;
        
        return count;
    } 
    
    int date_to_i(String date_string){
        int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30,31,30,31};
        int sum = 0;
        for (int i = 0; i<days.length;i++){
            sum += days[i];
            days[i] = sum;
        }
        int month = Integer.parseInt(date_string.substring(0,2));
        int date =  Integer.parseInt(date_string.substring(3,5));
        
        return days[month-1] + date;
        
    }
}