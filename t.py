import csv


def a():
    with open('map/static/data.csv') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in rows:
            data = row[0].replace('POLYGON ((','').replace('))','').split(', ')
            print(data, row[1])

if __name__=="__main__":
    a()