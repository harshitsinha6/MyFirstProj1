fn = input('First_Name = ')
ln = input('Last_Name = ')
pin = (input('PIN = '))
n = int(input('N = '))-1

fn1 = fn
ln1 = ln

LN = ''
SN = ''

fn = fn.lower()
ln = ln.lower()

if(len(fn) > len(ln)):
    LN = fn
    SN = ln
elif(len(fn) < len(ln)):
    LN = ln
    SN = fn
else:
    for i in range(len(fn)):
        if(ord(fn[i]) < ord(ln[i])):
            LN = ln
            SN = fn
            break
        elif(ord(fn[i]) > ord(ln[i])):
            LN = fn
            SN = ln
            break

LN = fn1
SN = ln1
#print('smaller name' , SN)
#print('longer name' , LN)
        
pin2 = pin[:: -1]

username = SN[0] + LN + pin[n]  + pin2[n]
print(username)
