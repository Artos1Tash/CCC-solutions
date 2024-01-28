# link - https://cccgrader.com/getproblem.php?fid=928110&authcode=e9abed4cbbf2dd73b7ed0dc55825f33b

peppers = {
            "Poblano": 1500,
            "Mirasol": 6000,
            "Serrano": 15500,
            "Cayenne": 40000,
            "Thai": 75000,
            "Habanero": 125000,
            }

res = 0

number_of_peppers = int(input())

for i in range(number_of_peppers):
    pepper = input()
    res += peppers[pepper]

print(res)

# Time complexity - O(n)
# Space complexity - O(1)