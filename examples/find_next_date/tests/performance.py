from memory_profiler import profile, memory_usage
from src.findNextDate import findNextDate
import random
import timeit


@profile
def profFindNextDate():
    findNextDate(
        random.randrange(1, 28), random.randrange(1, 12), random.randrange(0, 3000)
    )


if __name__ == "__main__":
    execution_time = timeit.timeit(profFindNextDate, number=1)
    print(f"Execution time: {execution_time}")
    # memory_usage_result = max(memory_usage((profFindNextDate)))
    # print(f"Memory usage: {memory_usage_result}")
