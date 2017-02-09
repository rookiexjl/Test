# coding:utf-8
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
xalpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  
key="aliyun"#密钥，定义为全局变量  
  
def modadd(a,b):  
    return (a+b)%26  
  
def modmin(a,b):  
    return (a-b)%26  
  
def chartonum(charx):  
    'turn the char into num like a->0'  
    for index,char in enumerate(alpha):  
        if char == charx:  
            return index  
  
def numtochar(numx):  
    'turn the number into char like 0->a'  
    return alpha[numx]  
  
def charstonums(charstring):#输入一个字符串，返回相应的数字列表  
    'turn the string into numstring'  
    numlist = []  
    for char in charstring:  
        numlist.append(chartonum(char))#chr函数将数字型转换成字符型  
    return numlist  
  
def numstochars(numstring):#输入一个以数字为成员的列表，返回相应的字符串  
    charlist = []  
    for member in numstring:  
        charlist.append(alpha[member])  
    resultstring = ''.join(charlist)  
    return resultstring  
      
def encrypt(plaintext):  
    plainlist = charstonums(plaintext)#将明文字符串变成相应的数字串  
    keylist = charstonums(key)  
    resultlist = []  
    #print plainlist#debug  
    #print keylist#debug  
      
    if len(plainlist) > len(keylist):#用长值作为循环控制，小值作为模数  
        listlength = len(plainlist)  
        listmod = len(keylist)  
        for index in range(listlength):  
            resultlist.append(modadd(plainlist[index],keylist[index%listmod]))  
    elif len(plainlist) <= len(keylist):  
        for index in range(len(plainlist)):  
            resultlist.append(modadd(plainlist[index],keylist[index]))  
    #print resultlist#debug  
    return numstochars(resultlist)  
      
def decrypt(ciphertext):  
    cipherlist = charstonums(ciphertext)#将密文字符串变成相应的数字串  
    keylist = charstonums(key)  
    resultlist = []  
    #print cipherlist#debug  
    #print keylist#debug  
      
    if len(cipherlist) > len(keylist):  
        listlength = len(cipherlist)  
        listmod = len(keylist)  
        for index in range(listlength):  
            resultlist.append(modmin(cipherlist[index],keylist[index%listmod]))  
    elif len(cipherlist) <= len(keylist):  
        for index in range(len(cipherlist)):  
            resultlist.append(modmin(cipherlist[index],keylist[index]))  
    #print resultlist#debug  
    return numstochars(resultlist)  
  
def main():  
    print "Choice:(E)ncrypt,(D)ecrypt"  
    choice = raw_input("$")  
    if choice=='E':  
        plaintext = raw_input(">")  
        result=encrypt(plaintext)  
        print "ciphertext:",result  
    elif choice=='D':  
        ciphertext = raw_input(">")  
        result=decrypt(ciphertext)  
        print "plaintext:",result  
  
if __name__=="__main__":  
    main()

