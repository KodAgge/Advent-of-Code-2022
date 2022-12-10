from time import perf_counter

def exec_stats(
    code: str,
    day: int,
    part: int,
    code_version: int,
    file_name: str = "input.txt"
) -> None:
    print("-"*60)
    print(f"Answer day {day} part {part} (version {code_version}):")
    start = perf_counter()
    exec(code)
    end = perf_counter()
    print(f"\nCode execution time: {1000*(end-start):.3f}ms")
    print(f"Number of characters in code: {len(code)}")
    print(f"Number of characters in code excluding file name: {len(code)-len(file_name)}")
    print("-"*60)

if __name__ == "__main__":
    code = "print('Hello World!')"
    exec_stats(code, 0, 0, 0)