class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour_angle=(hour mod 12+minutes/60)×30°
        one_min_angle = 360 // 60
        one_hour_angle = 360 // 12
        mins_angle = one_min_angle * minutes
        hrs_angle = one_hour_angle * (hour % 12 + minutes / 60)
        diff = abs(hrs_angle - mins_angle)
        return min(diff, 360 - diff)