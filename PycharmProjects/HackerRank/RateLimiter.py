# i - second
# request - list of requests

request = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1"]
request1 = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1"]
# i = 9
# limit = 2
# window = 5
def Verify(request, i, limit, window):
    URL = request[i]
    tmp_limit = 0
    start = 0
    end = 0
    if i < window:
        start = 0
        end = 0
    else:
        start = i-1
        end = i-window
    # going backwards in window
    for j in range(start, end, -1):
        if request[j] == URL:
            tmp_limit += 1
    if tmp_limit >= limit:
        return False
    else:
        return True

def RateLimiter(request):
    result = []
    good = 'OK'
    bad = 'NOT OK'
    for i in range(len(request)):
        if i != 0 and i % 30 == 0:
            if Verify(request, i, 5, 30):
                result.append("good30")
            else:
                result.append("bad30")
        else:
            if Verify(request, i, 2, 5):
                result.append(good)
            else:
                result.append(bad)
    return result

print(RateLimiter(request1))