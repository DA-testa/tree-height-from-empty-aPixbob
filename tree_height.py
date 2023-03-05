# python3

import sys
import threading
import numpy


def compute_augst(n, parents):
    
    augst = numpy.zeros(n)

    def kads_augst(node):
        if augst[node] != 0:
            return augst[node]

        if parents[node] == -1:
            augst[node] = 1

        else:
            augst[node] = 1 + kads_augst(parents[node])

        return augst[node]

    max_augst = 0

 


    for i in range(n):
        max_augst = max(max_augst, kads_augst(i))

    return max_augst


def main():

    input_type = input()

    if input_type == "F":
        file = input()
        if "a" in file:
            print("wrong file name")
            return
        try:
            with open("folder/" + file, "r", encoding="utf-8") as f:
                n = int(f.readline())
                parents = numpy.array(list(map(int, f.readline().split())))
        except FileNotFoundError:
            print("Wrong file")
            return

        print(compute_augst(n, parents))


    elif input_type == "I":
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
        print(compute_augst(n, parents))
        pass


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
