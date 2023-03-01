import datetime
from functools import cmp_to_key
result_data = []
result_data.append({
    'id': 2,
    'create_time': '2012-10-8 11:09:22',
	})
result_data.append({
    'id': 3,
    'create_time': '2012-10-10 11:09:22',
    })
result_data.append({
    'id': 1,
    'create_time': '2012-10-1 11:09:22',
    })


def cmp_datetime(a, b):
    a_datetime = datetime.datetime.strptime(a.create_time, '%Y-%m-%d %H:%M:%S')
    b_datetime = datetime.datetime.strptime(b.create_time, '%Y-%m-%d %H:%M:%S')

    if a_datetime > b_datetime:
        return -1
    elif a_datetime < b_datetime:
        return 1
    else:
        return 0

print(result_data)
result_data.sort(key=cmp_to_key(cmp_datetime),reverse=True)
print(result_data)