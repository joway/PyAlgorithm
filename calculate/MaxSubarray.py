def max_cros_mid_sub_array(data, low, mid, high):
    left = right = mid
    left_max = right_max = 0
    total = 0
    for i in range(mid, low - 1, -1):
        total += data[i]
        if total > left_max:
            left_max = total
            left = i
    total = 0
    for i in range(mid + 1, high + 1):
        total += data[i]
        if total > right_max:
            right_max = total
            right = i

    return left, right, left_max + right_max


def max_sub_array(data, low, high):
    if low == high:
        return low, high, data[low]
    mid = (high + low) // 2
    left_low, left_high, left_max = max_sub_array(data, low, mid)
    right_low, right_high, right_max = max_sub_array(data, mid + 1, high)
    mid_low, mid_high, mid_max = max_cros_mid_sub_array(data, low, mid, high)
    if left_max >= max(right_max, mid_max):
        return left_low, left_high, left_max
    elif right_max >= max(left_max, mid_max):
        return right_low, right_high, right_max
    else:
        return mid_low, mid_high, mid_max


print(max_sub_array([1, -2, -3, -1, -3, 1, 4], 0, 6))
