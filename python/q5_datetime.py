import sys
import operator
import time
import datetime
import calendar

def calc_time(start, stop, pattern):
	start_date = time.mktime(time.strptime(start, pattern))
	stop_date = time.mktime(time.strptime(stop, pattern))
	total = stop_date - start_date
	total_days = str(datetime.timedelta(seconds=total))
	return total_days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

print calc_time(date_start, date_stop, '%m-%d-%Y')

# 936 days, 23:00:00


####b)  
date_start = '12312013'  
date_stop = '05282015' 

print calc_time(date_start, date_stop, '%m%d%Y')

# 512 days, 23:00:00


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

print calc_time(date_start, date_stop, '%d-%b-%Y')

# 7849 days, 23:00:00