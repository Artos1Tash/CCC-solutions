# link - https://cccgrader.com/getproblem.php?fid=928112&authcode=b826b0953d93cbcc681cd62581ebd270

people = int(input())
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0

ddict = {}
for i in range(people):
    days = str(input())
    ddict[i] = days

val = list(ddict.values())

for j in val:
    for i in j:
        if i == "Y":
            day1 += 1
        # if i[1] == "Y":
        #     day2 += 1
        # if i[2] == "Y":
        #     day3 += 1
        # if i[3] == "Y":
        #     day4 += 1
        # if i[4] == "Y":
        #     day5 += 1

print(day1, day2, day3, day4, day5)
print(ddict)
print(list(ddict.values()))