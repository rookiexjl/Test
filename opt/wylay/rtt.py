# coding:utf-8
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
xalpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  
#key=[2,8,15,7,4,17]  
key=[0,11,8,24,20,13]
keylen=len(key)#取密钥长度是因为要考虑原文的长度是否比密钥长度大  
  
def encrypt(rawstring):  
    'ENCRYPT FUNCTION'  
    rawlist=list(rawstring)#将原字符串分解为字母的列表，变量记为rawlist  
    rawlistnum=[0 for i in range (len(rawstring))]#原字符串对应数字的列表，变量记为rawlistnum  
    rawlen=len(rawlist)  
    k=0  
    for item in rawlist:  
        for j in range(len(alpha)):  
            if item == alpha[j]:  
                rawlistnum[k] = j  
                k=k+1  
    resultnum=[0 for i in range (len(rawstring))]#加密后各字母所对应的数字的列表，变量记为resultnum  
    for i in range(len(rawlistnum)):  
        resultnum[i]=(rawlistnum[i]+key[i%keylen])%26  
    resultchar=[0 for i in range (len(rawstring))]#加密后的各字母的列表，变量记为resultchar  
    a=0  
    for index in resultnum:  
        resultchar[a]=xalpha[index]  
        a=a+1  
    result = ''.join(resultchar)  
    return result  
  
def decrypt(rawstring):  
    'DECRYPT FUNCTION'  
    rawlist=list(rawstring)  
    rawlistnum=[0 for i in range (len(rawstring))]  
    rawlen=len(rawlist)  
    k=0  
    for item in rawlist:  
        for j in range(len(xalpha)):  
            if item == xalpha[j]:  
                rawlistnum[k] = j  
                k=k+1  
    resultnum=[0 for i in range (len(rawstring))]  
    for i in range(len(rawlistnum)):  
        resultnum[i]=(rawlistnum[i]-key[i%keylen])%26#解密函数，此处为减法  
    resultchar=[0 for i in range (len(rawstring))]  
    a=0  
    for index in resultnum:  
        resultchar[a]=alpha[index]#注意为alpha，非xalpha  
        a=a+1  
    result = ''.join(resultchar)  
    return result  
  
def main():  
    'MAIN FUNCTION'  
    print 'Please Choose the Function:(E)ncrypt,(D)ecrypt'  
    choice = raw_input('>')  
    if choice == 'E':  
        print 'Please Input the Plaintext:'  
        plainstring = raw_input('>')  
        cipherresult = encrypt(plainstring)  
        print 'Encrypt Result:',cipherresult  
    elif choice == 'D':  
        print 'Please Input the Ciphertext:'  
        cipherstring = raw_input('>').upper()  
        plainresult = decrypt(cipherstring)  
        print 'Decrypt Result:',plainresult  
    else:  
        print 'Invalid Command'  
      
      
  
if __name__=="__main__":  
    main()  
