import datetime 

def solution_station_2(date: str) -> str:

    weekdays_en_to_jp = {
    'Monday': '月曜日', 
    'Tuesday': '火曜日', 
    'Wednesday': '水曜日', 
    'Thursday': '木曜日', 
    'Friday': '金曜日', 
    'Saturday': '土曜日', 
    'Sunday': '日曜日'}

    day = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')

    return weekdays_en_to_jp[day]

