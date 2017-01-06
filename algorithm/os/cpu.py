import copy
import random


def log(msg):
    print(msg)
    with open('result.txt', 'a+', encoding='utf-8') as file:
        file.write(msg + '\n')


def run_process(process):
    process['time'] -= 1
    log('pid %s is running' % process['pid'])
    return process


def display_process(process_table):
    for p in process_table:
        log('pid %s is running which started at %s and uses time %s'
              % (p['pid'], p['started_at'], p['time']))


def first_in_first_out(process_table):
    process_table.sort(key=lambda x: x['started_at'])
    display_process(process_table)
    return process_table


def shortest_job_first(process_table):
    process_table.sort(key=lambda x: x['time'])
    display_process(process_table)
    return process_table


def priority_scheduling(process_table):
    if not process_table:
        return
    process_table.sort(key=lambda x: -x['priority'])
    run_process(process_table[0])
    process_table[0]['priority'] -= 1
    if process_table[0]['time'] == 0:
        del process_table[0]
    priority_scheduling(process_table)


def round_scheduling(process_table):
    cur_pid = 0
    end_pids = []
    while True:
        if len(end_pids) == len(process_table):
            break
        if cur_pid in end_pids:
            continue
        run_process(process_table[cur_pid])
        if process_table[cur_pid]['time'] == 0:
            end_pids.append(end_pids)
        cur_pid = cur_pid + 1 if cur_pid < (len(process_table) - 1) else 0


def init_process_table():
    _table = []
    for i in range(10):
        _table.append({
            'pid': i,
            'started_at': random.randint(1, 100),
            'time': random.randint(1, 3),
            'priority': random.randint(1, 10),
        })
    return _table


log('--------- 原始进程表 ---------')
PROCESS_TABLE = init_process_table()
log('-- pid -- started_at -- time -- priority')
for p in PROCESS_TABLE:
    log('--  %s  --    %s    --    %s    --   %s  ' % (p['pid'], p['started_at'], p['time'], p['priority']))
log('--------- 先进先出 ---------')
first_in_first_out(copy.deepcopy(PROCESS_TABLE))
log('--------- 最短作业优先 ---------')
shortest_job_first(copy.deepcopy(PROCESS_TABLE))
log('--------- 优先级调度 ---------')
priority_scheduling(copy.deepcopy(PROCESS_TABLE))
log('--------- 轮转调度 ---------')
round_scheduling(copy.deepcopy(PROCESS_TABLE))
