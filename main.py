import pandas as pd 

def getP(test,table,words):
    vals = [0,0,0,0]
    for word in range(len(words)):
        for i in test:
            if i.lower() == words[word]:
                vals[word] += 1
    p = table[0]*table[1]**vals[0]*table[2]**vals[1]*table[3]**vals[2]*table[4]**vals[3]
    return p

reviews = pd.read_csv('reviews.csv')
words = ["great","happy","bad","return"]
dataC = pd.DataFrame(columns=words,index=[0,1,2,3,4,5,6,7,8,9])
for i in range(10):
    line = reviews.loc[i]['REVIEW'].replace('.','')
    line = line.replace(',','')
    split = line.split()
    for word in words:
        count = 0
        for j in split:
            if j.lower() == word:
                count+=1
        if count != 0:
            dataC.iloc[i][word] = 1
        else:
            dataC.iloc[i][word] = 0
        
df_pos = dataC.iloc[:6,:]
df_neg = dataC.iloc[6:,:]
print(df_pos)
print(df_neg)
posKeyTotal = df_pos.shape[0]
negKeyTotal = df_neg.shape[0]


#setting up pos_table
pos_table = [0,0,0,0,0]
pos_table[0] = df_pos.shape[0]/dataC.shape[0]
pos_table[1] = df_pos["great"].sum()/posKeyTotal
pos_table[2] = df_pos["happy"].sum()/posKeyTotal
pos_table[3] = df_pos["bad"].sum()/posKeyTotal
pos_table[4] = df_pos["return"].sum()/posKeyTotal
print("P(C1) = %.3f P(great | C1) = %.3f P(happy | C1) = %.3f P(bad | C1) = %.3f P(return | C1) = %.3f" % (pos_table[0],pos_table[1],pos_table[2],pos_table[3],pos_table[4]))
#P(C1) = 0.600 P(great | C1) = 0.667 P(happy | C1) = 1.000 P(bad | C1) = 0.500 P(return | C1) = 0.167

#setting up neg_table
neg_table = [0,0,0,0,0]
neg_table[0] = df_neg.shape[0]/dataC.shape[0]
neg_table[1] = df_neg["great"].sum()/negKeyTotal
neg_table[2] = df_neg["happy"].sum()/negKeyTotal
neg_table[3] = df_neg["bad"].sum()/negKeyTotal
neg_table[4] = df_neg["return"].sum()/negKeyTotal
print("P(C2) = %.3f P(great | C2) = %.3f P(happy | C2) = %.3f P(bad | C2) = %.3f P(return | C2) = %.3f" % (neg_table[0],neg_table[1],neg_table[2],neg_table[3],neg_table[4]))
#P(C2) = 0.400 P(great | C2) = 0.500 P(happy | C2) = 0.250 P(bad | C2) = 0.750 P(return | C2) = 0.750

test1 = open('test1.txt','r').read()
test1 = test1.replace('.','')
test1 = test1.replace(',','')
test1 = test1.split()
pT1_C1 = getP(test1,pos_table,words)
pT1_C2 = getP(test1,neg_table,words)
if pT1_C1 > pT1_C2:
    print("Test 1 is a positive review")
else:
    print("Test 1 is a negative review")
#Test 1 is a negative review

test2 = open('test2.txt','r').read()
test2 = test2.replace('.','')
test2 = test2.replace(',','')
test2 = test2.split()
pT2_C1 = getP(test2,pos_table,words)
pT2_C2 = getP(test2,neg_table,words)
if pT2_C1 > pT2_C2:
    print("Test 2 is a positive review")
else:
    print("Test 2 is a negative review")
#Test 2 is a positive review