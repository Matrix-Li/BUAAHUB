from JsonWrap import jsonwrap

thread1 = {"ID": 0, "info": "This is the content", "likeCnt": 99, "time": 1590930911,
           "latestUID": 456, "latestTime": 1590930916}  # 帖子详情应该包括点赞数、发帖时间、最新回帖人、最新回复时间等，注意这里时间以时间戳格式返回
thread2 = {"ID": 1, "info": "This is the content", "likeCnt": 99,
           "time": 1590930911, "latestUID": 456, "latestTime": 1590930916}
thread3 = {"ID": 2, "info": "This is the content", "likeCnt": 99,
           "time": 1590930911, "latestUID": 456, "latestTime": 1590930916}

allthreadsfromDB = [thread1, thread2, thread3]

res = []
for thread in allthreadsfromDB:
    res.append(thread)


def test_array():
    return jsonwrap(0, "ok", res)
