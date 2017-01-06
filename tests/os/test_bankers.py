from algorithm.os.bankers import Bankers

PROCESSES = [
    [7, 5, 3],  # 0
    [3, 2, 2],  # 1
    [9, 0, 2],  # 2
    [2, 2, 2],  # 3
    [4, 3, 3],  # 4
]

RESOURCES = [10, 5, 7]

_status = [
    [0, 1, 0],  # 0
    [2, 0, 0],  # 1
    [3, 0, 2],  # 2
    [2, 1, 1],  # 3
    [0, 0, 2],  # 4
]

bankers = Bankers(processes=PROCESSES, resources=RESOURCES, status=_status)

# print('判断是否为安全序列: %s' % bankers.is_safe_status())
print('------------')
print('输出安全序列')

sequences = bankers.safe_sequences()
for row in sequences:
    print('安全序列为 : %s' % row)

print('------------')
request_1 = [1, 0, 1]
print('输入序列 %s' % bankers.request_res(1, request_1))
print(bankers.safe_sequences())
