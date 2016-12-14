# 银行家算法  多个资源
import copy

from utils.calc import matrix_col_sum


class Bankers(object):
    def __init__(self, processes, resources, status=None):
        """
            :param processes: [pid][res] 进程所需最大资源表
            :param resources: [res] 现有资源
            :param status: [pid][res_now] 进程占用资源状态
        """
        self.processes = processes
        self.resources = resources
        self.res_num = len(self.resources)
        self.pid_num = len(self.processes)
        self.status = status if status else [[0] * len(resources) * len(processes)]

    def is_all_stopped(self, status=None):
        if status is None:
            status = self.status
        result = sum(sum(status, []))
        if result == 0:
            return True
        return False

    def res_available(self, status=None):
        if status is None:
            status = self.status
        res_available = []
        for i in range(self.res_num):
            res_available.append(self.resources[i] - matrix_col_sum(status, i))
        return res_available

    def select_available_pid(self, status):
        if status is None:
            status = self.status
        selected_pid = None
        res_available = self.res_available(status)
        for i in range(self.pid_num):
            if sum(status[i]) == 0:
                continue
            pid = i
            for j in range(self.res_num):
                if self.processes[i][j] - status[i][j] > res_available[j]:
                    pid = None
                    break
            if pid is not None:
                selected_pid = pid
                break
        return selected_pid

    def select_available_pids(self, status):
        if status is None:
            status = self.status
        selected_pids = []
        res_available = self.res_available(status)
        for i in range(self.pid_num):
            if sum(status[i]) == 0:
                continue
            pid = i
            for j in range(self.res_num):
                if self.processes[i][j] - status[i][j] > res_available[j]:
                    pid = None
                    break
            if pid is not None:
                selected_pids.append(pid)
        return selected_pids

    def run_pid(self, pid, status=None):
        if status is None:
            status = self.status
        status[pid] = [0] * self.res_num
        return status

    # 得到当前 status 下的全部安全序列
    def safe_sequences(self, status=None):
        if status is None:
            status = self.status
        post_sequences = []
        # 0. 判断是否所有进程结束
        if self.is_all_stopped(status):
            return []
        # 1. 查找所有可用进程, 若不存在, 则死锁
        selected_pids = self.select_available_pids(status)
        if not selected_pids:
            return []
        for selected_pid in selected_pids:
            # 2. 运行该进程并标记为终止, 结束后释放资源, 更新 status
            # print('pid %s is running' % selected_pid)
            _status = self.run_pid(selected_pid, copy.deepcopy(status))
            # 3. 重新调度
            _posts = self.safe_sequences(_status)
            if _posts:
                post_sequences += [[selected_pid] + p for p in _posts]
            else:
                post_sequences.append([selected_pid])
        return post_sequences

    def is_safe_status(self, status=None):
        if status is None:
            status = self.status
        # 0. 判断是否所有进程结束
        if self.is_all_stopped(status):
            return True
        # 1. 查找是否存在一个可以被分配资源的进程, 若不存在, 则死锁
        selected_pid = self.select_available_pid(status)
        if selected_pid is None:
            return False
        # 2. 运行该进程并标记为终止, 结束后释放资源, 更新 status
        # print('pid %s is running' % selected_pid)
        status = self.run_pid(selected_pid, copy.deepcopy(status))
        # 3. 重新调度
        return self.is_safe_status(status)

    def is_approved_request(self, pid, req_res):
        res_available = self.res_available()
        for r in range(len(req_res)):
            if req_res[r] > res_available[r]:
                return False
        _status = copy.deepcopy(self.status)
        for r in range(len(req_res)):
            _status[pid][r] += req_res[r]
        return self.is_safe_status(_status)

    def request_res(self, pid, req_res):
        if self.is_approved_request(pid, req_res):
            for r in range(len(req_res)):
                self.status[pid][r] += req_res[r]
            self.run_pid(pid, status=self.status)
            return True
        return False
