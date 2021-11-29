file = open(r"/magyar/magyar_fixed.txt", 'r')
f = open("/magyar/magyar/magyar_train.txt", 'w')
i=0
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    next_line = file.readline()
    i=i+1
    relation=""
    if not next_line:
        break;
    correctsentence = ""
    split1 = next_line.split('"relation":')
    #print(split1[1] ,", " ,i)
    if(i < 631):
        relation='"relation": "P177"}'
        list[0]=list[0]+1
    elif(i<1216):
        relation='"relation": "P364"}'
        list[1]=list[1]+1
    elif(i<1687):
        relation = '"relation": "P2094"}'
        list[2]=list[2]+1

    elif(i<2182):
        relation = '"relation": "P361"}'
        list[3]=list[3]+1

    elif(i<2410):
        relation = '"relation": "P641"}'
        list[4]=list[4]+1

    elif(i<3050):
        relation = '"relation": "P59"}'
        list[5]=list[5]+1

    elif(i<3395):
        relation = '"relation": "P413"}'
        list[6]=list[6]+1

    elif(i<3940):
        relation = '"relation": "P206"}'
        list[7]=list[7]+1

    elif(i<4454):
        relation = '"relation": "P412"}'
        list[8]=list[8]+1

    elif(i<5027):
        relation = '"relation": "P155"}'
        list[9]=list[9]+1

    elif(i<5656):
        relation = '"relation": "P26"}'
        list[10]=list[10]+1

    elif(i<5888):
        relation = '"relation": "P410"}'
        list[11]=list[11]+1

    elif(i<6498):
        relation = '"relation": "P25"}'
        list[12]=list[12]+1

    elif(i<7099):
        relation = '"relation": "P463"}'
        list[13]=list[13]+1

    elif(i<7722):
        relation = '"relation": "P40"}'
        list[14]=list[14]+1

    else:
        relation = '"relation": "P921"}'
        list[15]=list[15]+1



    correctsentence=split1[0] + relation
    f.write(correctsentence + '\n')

file.close()
f.close()
print(list)
