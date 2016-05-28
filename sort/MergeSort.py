def merge(left, right):
    curL = curR = 0
    result = []
    while curL < len(left) and curR < len(right):
        if left[curL] < right[curR]:
            result.append(left[curL])
            curL += 1
        else:
            result.append(right[curR])
            curR += 1
    result += left[curL:] + right[curR:]
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data
    cur = int(len(data) / 2)
    return merge(merge_sort(data[:cur]),
                 merge_sort(data[cur:]))
