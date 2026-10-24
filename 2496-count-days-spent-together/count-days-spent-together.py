from datetime import datetime as dt
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        current_yr = dt.now().year

        arriveAlice = f"{arriveAlice}-{current_yr}"
        leaveAlice = f"{leaveAlice}-{current_yr}"
        arriveBob = f"{arriveBob}-{current_yr}"
        leaveBob = f"{leaveBob}-{current_yr}"
        arriveAlice = dt.strptime(arriveAlice, "%m-%d-%Y")
        leaveAlice = dt.strptime(leaveAlice, "%m-%d-%Y")
        arriveBob = dt.strptime(arriveBob, "%m-%d-%Y")
        leaveBob = dt.strptime(leaveBob, "%m-%d-%Y")
    
        o_start = max(arriveAlice, arriveBob)
        o_end = min(leaveAlice, leaveBob)
    
        o_days = max(0, (o_end - o_start).days + 1)
        return o_days