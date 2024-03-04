# i - second
# request - list of requests

request_list = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1"]
request_list1 = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1"]
# i = 9
# limit = 2
# window = 5
def Verify(request_list, i, limit, window):
    URL = request_list[i]
    tmp_limit = 0
    if i < window:
        start = 0
        end = 0
    else:
        start = i-1
        end = i-window
    # going backwards in window
    for j in range(start, end, -1):
        if request_list[j] == URL:
            tmp_limit += 1
    if tmp_limit >= limit:
        return False
    else:
        return True

def RateLimiter(request_list):
    result = []
    for i in range(len(request_list)):
        # isGood = verify 1
        # if not isGood return "bad"
        # isGood = verify 2
        log = "good"
        if not Verify(request_list, i, 2, 5) or not Verify(request_list, i, 5, 30):
            log = "bad"
        result.append(log)
    return result

print(RateLimiter(request_list))