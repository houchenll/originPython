import time

def get_time():
    return time.strftime("%Y_%m_%d_%H%M%S")

def get_min():
    return time.strftime("%Y_%m_%d_%H%M")

def print_log(msg):
    file_name = get_min() + ".txt"
    fo = open(file_name, 'a')
    fo.write(get_time() + " " + msg + "\n")
    fo.close()

print_log("异常日志")
time.sleep(3)
print_log("异常")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)
print_log("异常日志")
time.sleep(3)