n = int(input())
bus_shelter_i = list(map(int, input().split()))
ppl_market = list(map(int, input().split()))
umb_sale = list(map(int, input().split()))  

print(n)
print(bus_shelter_i)
print(ppl_market)
print(umb_sale)

summ = sum(umb_sale) + sum(bus_shelter_i)
sum_ppl = sum(ppl_market)
if sum_ppl > summ:
    print("NO")
else:
    print("YES")
    print(sum_ppl - sum(bus_shelter_i))
    out1 = bus_shelter_i[0] - ppl_market[0]
    out2 = ""
    out3 = bus_shelter_i[1] - ppl_market[0]

# I got stuck here