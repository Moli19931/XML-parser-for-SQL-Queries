import re
moli=raw_input('Enter sql query')
moli1=moli.upper()
moli2=moli1.split()
'''print(moli1)'''
j=moli2[0]
#_____________________________________________________

def delet():
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    regex1 = r"DELETE(.*?)FROM"
    regex2 = r"FROM(.*?)WHERE"
    regex3 = r"WHERE(.*?);"
    regex4 = r"FROM(.*?);"
    
    exp1 = re.findall(regex1, moli1,re.DOTALL)
    exp2 = re.findall(regex2, moli1,re.DOTALL)
    exp3 = re.findall(regex3, moli1,re.DOTALL)
    exp4 = re.findall(regex4, moli1,re.DOTALL)
    print(exp1)
    t1=''.join(exp1)
    t1=t1.strip()
    print t1
    print(exp2)
    t2=''.join(exp2)
    t2=t2.strip()
    print t2
    print(exp3)
    t3=''.join(exp3)
    t3=t3.strip()
    print t3
    print(exp4)
    t4=''.join(exp4)
    t4=t4.strip()
    print t4
    #BETWEEN DELETE AND FROM
    if(t1 == "*" or t1== ""):
        flag1=1
    else:
        print "Incorrect entry between delete and from keywords"
    #BETWEEN FROM AND WHERE
    i2=re.search(r'(^[A-Z]+[A-Z0-9]*)',t2)  #table_name1
    if i2 is not None:
      flag2=1
    else:
      print 'Incorrect entry between from and where keywords'
    #BETWEEN WHERE AND ;
    i3=re.search(r'(^[A-Z]+[A-Z0-9]*)[=]([0-9]+)',t3) #COL1=NUMBER
    i4=re.search(r'(^[A-Z]+[A-Z0-9]*)[=]("[A-Z]+[A-Z0-9]*")',t3) #COL1="STRING"
    i5=re.search(r'(^[A-Z]+[A-Z0-9]*)[=]("[A-Z]+[A-Z0-9]*")(AND|OR)(^[A-Z]+[A-Z0-9]*)[=]("[A-Z]+[A-Z0-9]*")',t3) #COL1="STRING1 and/or col2="str2""
    i6=re.search(r'(^[A-Z]+[A-Z0-9]*)[=]([0-9]+)(AND|OR)(^[A-Z]+[A-Z0-9]*)[=]([0-9]+)',t3) #COL1=NUMBER and/or col2=num
    if i3 or i4 or i5 or i6 is not None:
      flag3=1
    else:
      print 'Incorrect entry between where and ; keywords'
    #BETWEEN FROM AND ;
    i7=re.search(r'(^[A-Z]+[A-Z0-9]*)',t4)  #table_name1
    if i7 is not None:
      flag4=1
    else:
      print 'Incorrect entry between from and ; keywords'
    if ((flag1==1 and flag2==1 and flag3==1) or (flag1==1 and flag4==1)):
        print "Correct select query"
    else:
        print "Incorrect select query"
      
    return;

# @@@@@@@@@@@@@@@@@@ DELETE QUERY @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if j=='DELETE':
    delet()
else:
    print "blah blah"

