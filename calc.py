num1 = "42"
num2 = "1234"
def add(num1,num2):
    ans = 0
    while(len(num1) < len(num2)):
        num1 = "0" + num1
    while(len(num2) < len(num1)):
        num2 = "0" + num2
    n = len(num1)
    for i in range(n-1, -1, -1):
        ans = (((int(num1[i])) + (int(num2[i])))*(pow(10,n-i-1)) + ans)
        final = str(ans)
    print (num1 + " + " + num2 + " = " + final)
add(num1,num2)