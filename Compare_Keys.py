import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)
df1 = pd.read_csv('Names1.csv')
df2 = pd.read_csv('Names2.csv')
s1 = set(df1['ConSecret1'])
s2 = set(df2['ConSecret2'])
set1 = s1.intersection(s2)
final_list1 = list(set1)
print("Common Consumer Secret is : ", final_list1)
s3 = set(df1['ConKey1'])
s4 = set(df2['ConKey2'])
set2 = s3.intersection(s4)
final_list2 = list(set2)
print("Common Consumer Key is :", final_list2)

if len(final_list1) > 0:
    for p in final_list1:
        dfA = pd.read_csv("Names1.csv", sep=",")
        dfB = pd.read_csv("Names2.csv", sep=',')
        print("The orgs with common secret in Landscape1 are: \n", dfA[dfA["ConSecret1"] == p])
        print("The orgs with common secret in Landscape2 are: \n", dfB[dfB["ConSecret2"] == p])
else:
    print("No common consumer secret found")


if len(final_list2) > 0:
    for q in final_list2:
        dfC = pd.read_csv("Names1.csv", sep=",")
        dfD = pd.read_csv("Names2.csv", sep=',')
        print("The orgs with common secret in Landscape1 are: \n", dfC[dfC["ConKey1"] == q])
        print("The orgs with common secret in Landscape2 are: \n", dfD[dfD["ConKey2"] == q])
else:
    print("No common consumer key found")
