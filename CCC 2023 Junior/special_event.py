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

for j in range(len(val)):
    if val[j][0] == "Y":
            day1 += 1
    if val[j][1] == "Y":
            day2 += 1
    if val[j][2] == "Y":
            day3 += 1
    if val[j][3] == "Y":
            day4 += 1
    if val[j][4] == "Y":
            day5 += 1

res = {1: day1, 2: day2, 3: day3, 4: day4, 5: day5}
print(max(res, key=res.get))


# n=int(input(""))
# grid=[]
# for a in range(n):
#     row=list(input(""))
#     grid.append(row)
# columns=list(zip(*grid))
# counts=[]

# for col in enumerate(columns):
#     count=col[1].count("Y")
#     counts.append((col[0],count))

# maxValue=max(counts,key=lambda x:x[1])[1]
# printing=""
# for col in enumerate(columns):
#     if col[1].count("Y")==maxValue and printing=="":
#         printing+=str(col[0]+1)
#     elif col[1].count("Y")==maxValue:
#         printing+=","+str(col[0]+1)
# print(printing)
