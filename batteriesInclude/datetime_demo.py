from datetime import datetime, timedelta, timezone

now = datetime.now()

if __name__ == "__main__":
    print(now)
    print(type(now))
    # 特定时间的datetime
    my_time = datetime(2016, 6, 29, 12, 00)
    print(my_time)
    # 获得时间戳
    print(my_time.timestamp())
    print(now.timestamp() * 1000)
    # 时间戳转datetime
    print(datetime.fromtimestamp(1467172800))
    # 字符串转datetime
    print(datetime.strptime('201801-011200:12', '%Y%m-%d%H%M:%S'))
    # datetime转字符串
    print(my_time.strftime('%Y%m-%d%H%M:%S'))
    # datetime计算
    print(my_time + timedelta(days=1, hours=12))
    print(my_time - timedelta(days=1, hours=12))
    # 时区转换
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    # 不同时区的时间，时间戳是一致的
    print(utc_dt.timestamp(), bj_dt.timestamp())
