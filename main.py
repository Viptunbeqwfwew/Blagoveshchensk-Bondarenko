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
    res = cursor.execute(f"SELECT DISTINCT model, type FROM Printer WHERE {input()} {input()} price > 280 ORDER by type desc, model").fetchall()
    for i in res:
        print(*i)


def DBcec():
    connect = sqlite3.connect(f"badData/{input()}")
    cursor = connect.cursor()
    gg, g = input().split()
    res = cursor.execute(f"""SELECT utQ.name, utV.name, utB.datetime, utB.vol FROM utB 
                                INNER JOIN utQ ON utB.q_id = utQ.id 
                                INNER JOIN utV ON utB.v_id = utV.id 
                                WHERE utV.color == '{gg}' and utB.vol > {g}
                                ORDER by utB.vol""").fetchall()
    for i in res:
        print(*i, sep=";")



def DBpir():
    connect = sqlite3.connect(f"ddd/{input()}")
    cursor = connect.cursor()
    gg = int(input())
    res = cursor.execute(f"""SELECT Robbers.name, Robbers.age, Injuries.title, Wounded.severity,
                                Injuries.level_of_severity * Wounded.severity * Wounded.amount_of_damage desc 
                                FROM Wounded 
                                INNER JOIN Robbers ON Wounded.name_id = Robbers.id 
                                INNER JOIN Injuries ON Wounded.injury_id = Injuries.id
                                ORDER by Injuries.level_of_severity * Wounded.severity * Wounded.amount_of_damage desc,
                                Robbers.name
                                """).fetchall()
    with open("badData/traffic.csv", encoding="utf8", mode='w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        for i in res[:gg]:
            writer.writerow(i)
            print(*i, sep=",")


def main():
    DBpir()


if __name__ == '__main__':
    main()


