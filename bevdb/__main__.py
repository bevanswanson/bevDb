import argparse
import time


def main():
    file_path = "../../datasets/AD.txt"

    parser = argparse.ArgumentParser()
    parser.add_argument("--term", help="the term to search the file for", type=str)
    parser.add_argument("--times", help="the number of times to search the file", type=int, default=1)
    term = parser.parse_args().term
    times = parser.parse_args().times

    print(f"Searching file for '{term}' {times} number of times")
    start_time = time.time()
    for x in range(times):
        with open(file_path) as file:
            search_results = []
            for num, line in enumerate(file, 1):
                if term in line:
                    search_results.append(num)
            print(f"Your search term appears on lines: {search_results}")
    print(f"This search took {time.time() - start_time} seconds to run")

if __name__ == '__main__':
    main()