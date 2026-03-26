import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))



def worker_tick(worker: Worker) -> None:
    if(worker.timer > 0):
        worker.timer -= 1
    elif(len(worker.source) > 0):
        fin_customer = worker.source.popleft()
        worker.dest.append(fin_customer)
        worker.timer = get_delay(worker.period, worker.spread_factor)


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"---------------Cycle {time/60}-------------")
    print(f"Time: {time}")
    for que in queues:
        print(f"Name: {que[0]}, State: {len(que[1])}")
    print("-----------------------------------------\n")


def create_worker(name:str, source:deque, dest:deque, period:int) -> Worker:
    return(Worker(name, source, dest, period, random.uniform(-10, 10)))


def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    gate_que = deque()
    vege_que = deque()
    cashier_que = deque()
    final_que = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe:list[tuple[str, deque]] = [
        ("Street", people_in_the_city),
        ("Gate", gate_que),
        ("Vege", vege_que),
        ("Cashier", cashier_que),
        ("Final", final_que)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 15s
    vege_m = 45  # Vážení zeleniny trvá 45s
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    street_worker = create_worker("Street worker", people_in_the_city, gate_que, day_m)
    gate_worker = create_worker("Gate worker", gate_que, vege_que, gate_m)
    vege_worker = create_worker("Vege worker", vege_que, cashier_que, vege_m)
    cashier_worker = create_worker("Cashier worker", cashier_que, final_que, final_m)

    workers:list[Worker]= [street_worker, gate_worker, vege_worker, cashier_worker]
    # 3. Hlavní smyčka simulace
    maxState = len(people_in_the_city)

    i = 0
    #for i in range(3600*2):
    while len(final_que) != maxState:
        i+=1
        for worker in workers:
            worker_tick(worker)
        if(i%60 == 0):
            print_snapshot(i, queues_to_observe)

    print_snapshot(i, queues_to_observe)

if __name__ == "__main__":
    main()
