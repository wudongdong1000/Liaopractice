#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
#以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(ddt_str,tz_str):
    m=re.match(r'^UTC(\+|-)(0[0-9]|[0-9]):00',tz_str)
    UTC=int(m.group(1)+m.group(2))
    cday=datetime.strptime(ddt_str,'%Y-%m-%d %H:%M:%S')
    utc_dt=cday.replace(tzinfo=timezone(timedelta(hours=UTC)))
    timestp=utc_dt.timestamp()
    return timestp

print(to_timestamp('2015-5-31 16:10:30', 'UTC-09:00'))
    
