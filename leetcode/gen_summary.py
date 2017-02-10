import os
import re


def get_all_filenames(path):
    ret = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                ret.append(os.path.join(root, file))

    return ret


if __name__ == '__main__':

    filenames = get_all_filenames('array')
    summaries = []
    for filename in filenames:
        with open(filename, mode='r', encoding='utf-8') as file:
            _result = re.findall(r"\"\"\" Summary\n(.+?)\n\"\"\"", file.read(), re.DOTALL)
            summary = _result[0] if _result else None
            if summary and summary.replace(' ', ''):
                summaries.append(summary.replace(' ', '').replace('\n', ''))

    num = 1
    for s in summaries:
        print('%s. %s' % (num, s))
        num += 1
