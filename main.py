import csv
import sqlite3


def Da():
    fff, ffa = map(int, input().split())
    with open("badData/traffic.csv", encoding="utf8", mode='r') as csvFile:
        reader = csv.DictReader(csvFile, delimiter=";")
        expensive = set(map(lambda x: x["name"], filter(lambda x: fff < int(x['volume']) < ffa and x['type'] == 'import', reader)))
    print(len(expensive))
    for i in sorted(expensive):
        print(i)


def DBsec():
    connect = sqlite3.connect(f"badData/{input()}")
    cursor = connect.cursor()
    res = cursor.execute(f"SELECT model, type FROM Printer WHERE {input()} {input()} price > 280").fetchall()
    for i in res:
        print(*i)



def main():
    DBsec()


if __name__ == '__main__':
    main()


