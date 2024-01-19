class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")

        leap_year = list()
        for year in range(2020,1899,-4):
            leap_year.append(year)
        
        months = {'01': 31, 
                  '02': 28, 
                  '03': 31, 
                  '04': 30, 
                  '05': 31, 
                  '06': 30, 
                  '07': 31, 
                  '08': 31, 
                  '09': 30, 
                  '10': 31, 
                  '11': 30, 
                  '12': 31}

        # if it is a leap year, change Feb's days from 28 to 29
        if int(date[0]) in leap_year and int(date[0]) > 1900:
            months["02"] = 29
        
        ans = 0
        # add all months' days in that year
        for month in range(1, int(date[1])):
            month = f"0{str(month)}" if len(str(month)) == 1 else str(month)
            ans += months[month]
        
        return ans + int(date[2])