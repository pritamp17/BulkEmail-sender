a_file = open("msg.txt")
lines = a_file. readlines()

ans = ""
for line in lines:
    ans = ans+line
print(ans)
a_file. close()
