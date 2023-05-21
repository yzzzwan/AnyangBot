import datetime

def five_days():
    today = datetime.date.today()
    # today = datetime.date(2023, 5, 26)

    # print(today)

    # 주말을 제외한 5일간의 날짜 구하기
    count = 0
    week_dates = []
    week_days=[]
    while count < 5:
        if today.weekday() < 5:  # 주말(토요일: 5, 일요일: 6)이 아닌 경우만 추가
            week_dates.append(str(today))
            if today.weekday() == 0:
                week_dates.append("월")
            elif today.weekday() == 1:
                week_dates.append("화")
            elif today.weekday() == 2:
                week_dates.append("수")
            elif today.weekday() == 3:
                week_dates.append("목")
            elif today.weekday() == 4:
                week_dates.append("금")
            count += 1
        today += datetime.timedelta(days=1)



    # print(week_dates)
    return week_dates


