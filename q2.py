import math
from functools import wraps
import time
from multiprocessing import Pool
import multiprocessing

from operator import add
from functools import reduce

BASE = 0

def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}は{elapsed_time}秒かかりました")
        return result
    return wrapper


def int2str(i: int, base: int) -> str:
    int2str_table: str = '0123456789ABCDEF'
    if not 2 <= base <= 16:
        raise ValueError('base must be 2 <= base < 16')

    result = []

    temp: int = abs(i)
    if temp == 0:
        result.append('0')
    else:
        while temp > 0:
            result.append(int2str_table[temp % base])
            temp = math.floor(temp / base)

    if i < 0:
        result.append('-')

    return ''.join(reversed(result))


def calc_enclosed_num(str: str) -> int:
    enclose_dict = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1,
                    'A': 1, 'B': 2, 'C': 0, 'D': 1, 'E': 0, 'F': 0}
    count = 0
    for s in list(str):
        count = count + enclose_dict[s]

    return count


def f(base, num) -> int:
    return calc_enclosed_num(int2str(num, base))


def f_wrap(num):
    return f(BASE, num)

@stop_watch
def calc(k, l, h):
    count = 0
    for i in range(l, h+1):
        count += f(k, i)

    print(count)


@stop_watch
def multi_calc(k, l, h):
    global BASE
    BASE = k
    p = Pool(multiprocessing.cpu_count() - 1)
    print('start multi')
    print(reduce(add, p.map(f_wrap, range(l, h+1))))


def main():
    # 標準入力から読み込み
    input_num_arr = input()
    (k, l, h) = input_num_arr.split(' ')
    (k, l, h) = (int(k), int(l), int(h))
    multi_calc(k, l, h)


if __name__ == '__main__':
    main()
