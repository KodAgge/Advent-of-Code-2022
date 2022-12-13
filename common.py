from time import perf_counter
import inspect

def load_file(test = False):
    day = inspect.getmodule(inspect.stack()[1][0]).__file__.split("\\")[-1].split(".")[0]
    with open(f"inputs/{day}.{'test' if test else 'in'}") as file:
        return file.readlines()

def exec_stats(
    code: str,
    day: int,
    part: int,
    code_version: int,
    file_name: str = "input.txt"
) -> None:
    print(f"Answer day {day} part {part} (version {code_version}):")
    start = perf_counter()
    exec(code)
    end = perf_counter()
    print(f"\nCode execution time: {1000*(end-start):.3f}ms")
    print(f"Number of characters in code: {len(code)}")
    print(f"Number of characters in code excluding file name: {len(code)-len(file_name)+2}")
    print("-"*60)


def exec_stats_multi(
    code_list, 
    day: int, 
    part: int,
    file_name: str
) -> None:
    for i, code in enumerate(code_list):
        exec_stats(code=code, day=day, part=part, code_version=i+1, file_name=file_name)


if __name__ == "__main__":
    code = "print('Hello World!')"
    exec_stats(code, 0, 0, 0)