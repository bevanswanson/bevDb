import argparse

def main():
    file_path = "../../datasets/AD.txt"

    parser = argparse.ArgumentParser()
    parser.add_argument("term", help="the term to search the file for", type=str)
    parser.add_argument("times", help="the number of times to search the file", type=int)
    term = parser.parse_args().term
    times = parser.parse_args().times

    print(f"Searching file for '{term}' {times} number of times")

    search_results = []
    with open(file_path) as file:
        for num, line in enumerate(file, 1):
            if len(search_results) < times and term in line:
                search_results.append(num)

    print(f"Your search term appears on lines: {search_results}")

if __name__ == '__main__':
    main()