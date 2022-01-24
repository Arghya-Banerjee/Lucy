import datetime

EtaTime = str(input("Enter time in format HH:MM:SS : "))
EtaDate = str(input("Enter date in format DD:MM:YYYY : "))

EtaTime_str = EtaTime.split(":")
EtaDate_str = EtaDate.split(":")

User_Hour = EtaTime_str[0]
User_Min = EtaTime_str[1]
User_Sec = EtaTime_str[2]

User_Date = EtaDate_str[0]
User_Month = EtaDate_str[1]
User_Year = EtaDate_str[2]


UserTime = f"{User_Year}-{User_Month}-{User_Date} {User_Hour}:{User_Min}:{User_Sec}"
UserTime = str(UserTime)

NowTime = datetime.datetime.now()
NowTime = str(NowTime)

TimeDiff = datetime.timedelta(UserTime - NowTime)

print(TimeDiff)

print(NowTime)
print(UserTime)





# # Present Time Splitting

# TimeNow = datetime.datetime.now()
# TimeNow = str(TimeNow)
# TimeNow_str_date_time_split = TimeNow.split(" ")

# TimeNow_Date = TimeNow_str_date_time_split[0]
# TimeNow_Time = TimeNow_str_date_time_split[1]

# TimeNow_Time_split = TimeNow_Time.split(":")

# TimeNow_Time_Hour = TimeNow_Time_split[0]
# TimeNow_Time_Min = TimeNow_Time_split[1]
# TimeNow_Time_Sec = TimeNow_Time_split[2]

# TimeNow_Date_split = TimeNow_Date.split("-")

# TimeNow_Date_Day = TimeNow_Date_split[0]
# TimeNow_Date_Month = TimeNow_Date_split[1]
# TimeNow_Date_Year = TimeNow_Date_split[1]


# print(TimeNow)
# print(TimeNow_str_date_time_split)

# print(EtaTime_str)