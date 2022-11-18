import csv


def Da():
    fff, ffa = int(input()), int(input())
    with open("badData/traffic.csv", encoding="utf8", mode='r') as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        expensive = set(map(lambda x: x["name"], filter(lambda x: fff < int(x['volume']) < ffa and x['type'] == 'import', reader)))
    print(len(expensive))
    for i in expensive:
        print(i)


def main():
    Da()


if __name__ == '__main__':
    main()


