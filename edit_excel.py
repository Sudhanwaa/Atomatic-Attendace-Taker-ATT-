############################################################################
############################################################################
                    # This is just a practice file 
############################################################################
############################################################################

import openpyxl
import pandas as pd

df= pd.read_csv("StudentDetails/studentdetails.csv")

print(df.head())

for i in range(0,df.shape[0]):
    print(type(df["Enrollment"][i]))
    if(df["Enrollment"][i]==10 and df["Name"][i]=="Hemang"):
        df=df.drop(i,axis=0)

df.to_csv("StudentDetails/studentdetails.csv",index=False)

print(df.head())