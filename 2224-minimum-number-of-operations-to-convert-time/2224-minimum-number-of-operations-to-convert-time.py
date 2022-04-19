
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = 60 * int(current[0:2]) + int(current[3:5]) # Current time in minutes
        target_time = 60 * int(correct[0:2]) + int(correct[3:5]) # Current time in minutes
        time_d = target_time - current_time # Difference b/w current and target times in minutes

        rounds = 0
        while(time_d != 0):
            if (time_d >= 60):
                r = time_d//60
                rounds += r
                time_d %= 60
            if (time_d >= 15):
                r = time_d//15
                rounds += r
                time_d %= 15
            if (time_d >= 5):
                r = time_d//5
                rounds += r
                time_d %= 5
            if (time_d >= 1):
                r = time_d//1
                rounds += r
                time_d %= 1
        return rounds