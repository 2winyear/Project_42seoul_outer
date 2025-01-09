import time
import datetime

current_time = time.time()

# 구조체 반환
local_time = time.localtime()
# 문자열 반환
ctime = time.ctime()

print('Seconds since January 1, 1970: ' + format(current_time, ',.4f') + ' or %.2e in scientific notation'%(current_time))
print(time.strftime('%b %d %Y', local_time))