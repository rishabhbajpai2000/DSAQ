from datetime import datetime
# calculating the time difference
def time_diff(initial, final):
        time_i = datetime.strptime(initial, "%H:%M")
        time_f = datetime.strptime(final, "%H:%M")
        time_d = time_f - time_i
        return time_d.seconds
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        time_d = time_diff(current, correct)//60 ## the difference would be in mins
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