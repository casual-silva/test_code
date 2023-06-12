## Q1
# >  Rearrange an array of integers so that the calculated value U is maximized. Among the arrangements that satisfy that test,
# choose the array with minimal ordering. The value of U for an array with n elements is calculated as :
# U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×arr[n-1] × (1÷arr[n]) if n is odd or
# U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×(1÷arr[n-1]) × arr[n] if n is even The sequence of operations is the same in either case,
# but the length of the array, n, determines whether the calculation ends on arr[n] or (1÷arr[n]). Arrange the elements to maximize U and the items are in the numerically smallest possible order.
# > **Note: **其中  itertools.permutations 数组全排列如果自己实现可以用 递归回溯实现

import itertools


def rearrange_array(arr):
    # 获取所有可能的排列
    permutations = list(itertools.permutations(arr))
    max_U = float('-inf')  # 负无穷大
    max_arr = None  # 最大计算值数组

    for perm in permutations:
        n = len(perm)
        U = 1

        if n % 2 == 0:
            # 偶数
            for i in range(0, n, 2):
                U *= perm[i]
                U /= perm[i + 1]
        else:
            # 奇数
            for i in range(0, n - 1, 2):
                U *= perm[i]
                U /= perm[i + 1]
            U *= perm[n - 1]

        if U > max_U:
            max_U = U
            max_arr = perm
    return max_arr


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 10]
    result = rearrange_array(arr)
    print(result)


## Q2
# >  The number of goals achieved by two football teams in matches in a league is given in the form of two lists. For each match of team B,
# compute the total number of matches of team A where team A has scored less than or equal to the number of goals scored by team B in that match.
# Example: teamA = [1, 2, 3] teamB = [2, 4] Team A has played three matches and has scored teamA = [1, 2, 3] goals in each match respectively.
# Team B has played two matches and has scored teamB = [2, 4] goals in each match respectively. For 2 goals scored by team B in its first match,
# team A has 2 matches with scores 1 and 2. For 4 goals scored by team B in its second match, team A has 3 matches with scores 1, 2 and 3. Hence, the answer is [2, 3].

def find_matches(A, B):
    matches = []
    for b_goals in B:
        count = 0
        for a_goals in A:
            if a_goals <= b_goals:
                count += 1
        matches.append(count)
    return matches


if __name__ == '__main__':
    # 示例数据
    team_A = [1, 2, 3]
    team_B = [2, 4]
    result = find_matches(team_A, team_B)
    print(result)


## Q3
# > Version:0.9 StartHTML:0000000105 EndHTML:0000001298 StartFragment:0000000141 EndFragment:0000001258
# > Implement a stack that accepts the following commands and performs the operations
# > described:
# > push v: Push integer v onto the top of the stack
# > pop: Pop the top element from the stack
# > inc i v: Add v to each of the bottom i elements of the stack
# > After each operation, print the value at the top of the stack. If the stack is empty, print the
# > string 'EMPTY'.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        self.print_top()

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        self.print_top()

    def inc(self, i, v):
        if not self.is_empty():
            for j in range(min(i, len(self.stack))):
                self.stack[j] += v
        self.print_top()

    def print_top(self):
        if self.is_empty():
            print("EMPTY")
        else:
            print(self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0


def process_commands(stack, cmd):
    if cmd.startswith("push"):
        value = int(cmd.split()[1])
        stack.push(value)
    elif cmd == "pop":
        stack.pop()
    elif cmd.startswith("inc"):
        i, v = map(int, cmd.split()[1:])
        stack.inc(i, v)


if __name__ == '__main__':

    # 示例命令
    commands = ["push 5", "push 3", "pop", "push 2", "inc 3 1", "pop", "pop", "pop", "pop", "pop", "pop"]
    stack = Stack()
    for cms in commands:
        process_commands(stack, cms)
