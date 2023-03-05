# 221RDB216 Roberts Kārlis Kaudze grupa 4
import sys
import threading
import numpy


def compute_height(n, vecaks):
    # tree creation
    bern = [[] for _ in range(n)]
    for i in range(n):
        vecaks1 = vecaks[i]
        if vecaks1 == -1:
            sakn = i
        else:
            bern[vecaks1].append(i)

    # augst for tree
    def compute_depth(node):
        if not bern[node]:
            return 1
        max_depth = 0
        for bern0 in bern[node]:
            depth = compute_depth(bern0)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(sakn)


def main():
    input_type = input()

    if "I" in input_type:
        n = int(input())
        vecaks = list(map(int, input().split()))
        height = compute_height(n, vecaks)
        print(height)
    elif "F" in input_type:
        filename = input()
        with open("test/" + filename, "r") as f:
            n = int(f.readline())
            vecaks = list(map(int, f.readline().split()))
            height = compute_height(n, vecaks)
            print(height)
    else:
        print("incorrecto!")
        exit()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
