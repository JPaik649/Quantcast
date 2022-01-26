import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="filename of the cookie log file", type=str)
parser.add_argument("-d", "--date", help="specified date", type=str)

def sortFunc(n):
    return n[1]

def parsefile(filename):
    f = open(filename, "rt")
    lines = f.readlines()
    toReturn = {}
    for i in range(1, len(lines)):
        toParse = lines[i].split(",")
        cookie = toParse[0]
        date = toParse[1].split("T")[0].split("-")
        #index 0 = year; index 1 = month; index 2 = day
        year = toReturn.get(date[0])
        if year is None:
            toReturn.update({date[0]: {}})
            year = toReturn.get(date[0])
        month = year.get(date[1])
        if month is None:
            year.update({date[1]: {}})
            month = year.get(date[1])
        day = month.get(date[2])
        if day is None:
            month.update({date[2]: [(cookie, 1)]})
            continue
        #First we must check if cookie is already listed
        found = False
        for i in range(0, len(day)):
            if day[i][0] == cookie:
                temp = list(day[i])
                temp[1] += 1
                day[i] = tuple(temp)
                found = True
                break
        if not found:
            day.append((cookie, 1))
        day.sort(key = sortFunc, reverse = True)
    f.close()
    return toReturn

def findCookie(cookieMap, date):
    year = cookieMap.get(date[0])
    if year is None:
        return None
    month = year.get(date[1])
    if month is None:
        return None
    day = month.get(date[2])
    if day is None:
        return None
    largest = day[0][1]
    toReturn = []
    x = 0
    while largest == day[x][1]:
        toReturn.append(day[x][0])
        x += 1
        if x >= len(day):
            break
    return toReturn
    

def cookie(args):
    if args.date is None:
        print("Date mode expected")
        quit()
    if os.path.exists(args.filename) is False:
        print("File: \"" + args.filename + "\" does not exist")
        quit()
    cookieMap = parsefile(args.filename)
    date = str(args.date).split("-")
    cookies = findCookie(cookieMap, date)
    if cookies is None:
        print("No cookies active on this day")
    else:
        for x in cookies:
            print(x)

if __name__ == "__main__":
    args = parser.parse_args()
    cookie(args)