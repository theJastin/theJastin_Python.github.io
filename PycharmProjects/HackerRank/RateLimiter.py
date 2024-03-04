# i - second
# request - list of requests

request_list = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1"]
request_list1 = ["URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1", "URL2", "URL1", "URL2", "URL3", "URL1", "URL1", "URL8", "URL9", "URL1", "URL1"]
# i = 9
# limit = 2
# window = 5
def Verify(request_list, i, limit, window):
    URL = request_list[i]
    url_limit = 0
    if i >= limit:
        start = i-1
        end = max(0, i-window)-1
        # going backwards in window
        for j in range(start, end, -1):
            if request_list[j] == URL:
                url_limit += 1
    return url_limit < limit

def RateLimiter(request_list):
    result = []
    for i in range(len(request_list)):
        log = "good"
        if not Verify(request_list, i, 2, 5) or not Verify(request_list, i, 5, 30):
            log = "bad"
        result.append(log)
    return result

print(RateLimiter(request_list1))