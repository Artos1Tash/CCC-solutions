# link - https://cccgrader.com/getproblem.php?fid=928107&authcode=1c164e9c05339bcb58835562edc30dc9

p = int(input())
c = int(input())
res = 0
if p > c:
    res += 500
res += p*50
res -= c*10

print(res)

# Time complexity - O(1)
# Space complexity - O(1)
