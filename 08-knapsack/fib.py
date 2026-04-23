import functools

from utils import measure_time


count = 0

def fib(n: int) -> int:
    if n <= 1:
        return n
    global  count
    count += 1
    fib1 = fib(n - 1)
    fib2 = fib(n - 2)
    return fib1 + fib2

@functools.cache
def fib_cache(n: int) -> int:
    # TODO implementujte s functools.cache.
    return 0

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    # TODO implementujte s explicitní pamětí.
    return 0


def fib_ultra_list(n):
    if(n<=1):
        return(n)

    fibonachi = [0, 1]

    for _ in range(1, n):
        fibonachi.append(fibonachi[-1] + fibonachi[-2])

    return(fibonachi[-1])

def fib_ultra_num(n):
    if(n<=1):
        return(n)

    fib1 = 0
    fib2 = 1

    for _ in range(1, n):
        fib1, fib2 = fib2, fib1+fib2

    return(fib2)


def main() -> None:
    lookup: dict[int, int] = {}

    a = 200 # to je hned
    #a = 30 # to už chvilku trvá
    #a = 40 # za jak dlouho se asi dočkáme?

    measure_time(lambda: fib_cache(a), 1)
    measure_time(lambda: fib_mem(a, {}), 100)
    measure_time(lambda: fib_ultra_list(a), 100)
    measure_time(lambda: fib_ultra_num(a), 100)
    #measure_time(lambda: fib(a))

    print(f"{fib_cache(a)/fib_cache(a-1)}, {fib_ultra_list(a)/fib_ultra_list(a-1)}, {fib_ultra_num(a)/fib_ultra_num(a-1)}")

def hello():
    print("Hello")

if __name__ == "__main__":
    main()
