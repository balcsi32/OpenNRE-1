file = open(r"magyar/split/merge.txt", 'r')
f = open("magyar/magyar.txt", 'w')
while True:
    next_line = file.readline()

    if not next_line:
        break;

    correctsentence=""
    split1=next_line.split('"h":')
    split2 = split1[1].split('"')
    h1=''
    h2=""
    h3=""
    t1=""
    t2 = ""
    t3 = ""
    i = 1
    #print("split:" ,split1)

    while split2[i] != '],' :
        h1=h1+split2[i]
        i=i+1
    i = i + 1
    h2 =h2 +split2[i]
    i=i+1
    h3=h3 +split2[i]
    h1 = h1.replace(',', ' ')
    h3=h3.replace(']','')
    h3=h3.replace('[','')
    i = i + 3

    while split2[i] != '],' :
        t1=t1+split2[i]
        i=i+1
    i = i + 1
    t1 = t1.replace(',', ' ')
    t2 =t2 +split2[i]
    i=i+1

    t3=t3 +split2[i]
    t3 = t3.replace(']', '')
    t3 = t3.replace('[', '')


    print(t1)
    #print(t1, " + ", t2, " + ", t3)

    correctsentence=correctsentence + split1[0]+' "h": {"name": "'+h1 + '", "id": "'+h2 + '", "pos": [' + h3[1:-1]+']'+'}, "t": {"name": "'+t1 + '", "id": "'+t2 + '", "pos": [' + t3[1:-2]+']},"relation": ""}'
    print(correctsentence,"")
    f.write(correctsentence + '\n')

file.close()
f.close()
