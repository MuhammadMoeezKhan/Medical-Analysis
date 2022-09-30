"""
Created on Thu Sep  8 15:05:07 2022

@author: moeezkhan
"""

'''
https://archive.ics.uci.edu/ml/datasets/Thyroid+Disease
Thyroid Disease Data Set
sick.names:
sick.data
'''

import pandas as pd
import numpy as np

# If you want to read in just a few rows, for testing, specify that value with 
# numRows. Otherwise, use the default value (None) to read in all rows.
def readSickData(numRows = None):
    colNames = ["age", 
                "sex", 
                "on thyroxine", 
                "query on thyroxine", 
                "on antithyroid medication",
                "sick", 
                "pregnant", 
                "thyroid surgery",
                "I131 treatment", 
                "query hypothyroid", 
                "query hyperthyroid", 
                "lithium", 
                "goitre", 
                "tumor", 
                "hypopituitary", 
                "psych", 
                "TSH measured", 
                "TSH", 
                "T3 measured", 
                "T3", 
                "TT4 measured", 
                "TT4", 
                "T4U measured", 
                "T4U", 
                "FTI measured", 
                "FTI", 
                "TBG measured", 
                "TBG", 
                "referral source",
                "output"]
    df = pd.read_csv("data/sick.data", index_col=False, na_values="?", delimiter = ",", header=None, names=colNames, engine='python', nrows=numRows)
    df = df.loc[:, 'age':'referral source']
    return df


# Of course, all of these problems should be solved completely programmatically.
# Don't hardcode anything. That is, don't figure out part or all of the 
# answer by-hand and just type it in.


def sectionA(first):
    print("\n=================================================================")
    print("=================================================================")
    print("=================================================================")
    print("Section A: Series Access")
    # first is a Series object corresponding to the first patient
    # in the dataset. Use it with various operations to work out the problems below.
    
    
    print("\nA1 -----------------------------------------------------------------")
    # Show the value of the column at position 17 (using iloc).
    valForColAtPosition2 = first.iloc[17]
    print("Val for col at position 17:", valForColAtPosition2)


    print("\nA2 -----------------------------------------------------------------")
    # Show the value of the FTI column (using loc).
    valForFTI = first.loc['FTI']
    print("Val for FTI:", valForFTI)
    
    
    print("\nA3 -----------------------------------------------------------------")
    # Show the name of the column at position 13
    nameOfCol13 = first.index[13]
    print("Name of col at position 13:", nameOfCol13)
    

    print("\nA4 -----------------------------------------------------------------")
    # Show the values for the columns from the beginning, up to and including "psych".
    begToPsych = first.loc[:'psych']
    print("Beginning to 'psych':\n", begToPsych, sep='')
    
    
    print("\nA5 -----------------------------------------------------------------")
    # Show the values for the columns at positions 1 up to and including 5
    col1Through5 = first.iloc[1:6]
    print("Col 1 up to and including 5:\n", col1Through5, sep='')
    
    
    print("\nA6 -----------------------------------------------------------------")
    # Show the values for the columns at positions 2 and 5 only
    col2And5 = first.iloc[[2,5]]
    print("Col 2 and 5:\n", col2And5, sep='')
    
    
    print("\nA7 -----------------------------------------------------------------")
    # Show the values for the "TSH" and "T3" values
    tshAndT3 = first.loc[['TSH','T3']]
    print("TSH and T3:\n", tshAndT3, sep='')
    
    #A COMPLETED
    
    
def sectionB(sickDF):
    print("\n=================================================================")
    print("=================================================================")
    print("=================================================================")
    print("Section B: DataFrame Access")
    # Note, for sickDF, that the patient label is the same as the integer position.
    # The first patient has label and position 0, etc.
    
    
    print("\nB1 -----------------------------------------------------------------")
    # Show the Series corresponding to the second patient in the dataset.
    secondPatient = sickDF.iloc[1,:]
    print("Second patient:\n", secondPatient, sep='')
    
    
    print("\nB2 -----------------------------------------------------------------")
    # Show the Series corresponding to all values of the "pregnant" column.
    preg = sickDF.loc[:,'pregnant']
    print("Pregnant:\n", preg, sep='')
    
    
    print("\nB3 -----------------------------------------------------------------")
    # Show patients 2 and 4, all columns.
    allCol24 = sickDF.iloc[[2,4],:]
    print("Patients 2 and 4, all cols:\n", allCol24, sep='')
    
    
    print("\nB4 -----------------------------------------------------------------")
    # Show patients 2 and 4, the columns from "TSH measured" through "TBG", inclusive.
    
    someCol24 = sickDF.loc[[2,4], 'TSH measured' : 'TBG']
    print("Patients 2 and 4, some cols:\n", someCol24, sep="")

    #B COMPLETED



def sectionC(sickDF):
    print("\n=================================================================")
    print("=================================================================")
    print("=================================================================")
    print("Section C: DataFrame Processing")
    # Some of these may require multiple lines of code.
    # Declare additional local variables as you see fit.
    
    
    print("\nC1 -----------------------------------------------------------------")
    # What is the average age of a paticleent in this dataset?
    
    
    avgAge = sickDF.loc[ : , "age"].mean()
    print("Average age:", avgAge)
    
    
    print("\nC2 -----------------------------------------------------------------")
    # What is the most common sex in this dataset?
    commonSex = sickDF.loc[ : , "sex"].mode().iloc[0]
    print("Common sex:", commonSex)
    
    
    print("\nC3 -----------------------------------------------------------------")
    # Show the age of the oldest patient in the dataset.
    oldest = sickDF.loc[ : , "age"].max()
    print("Oldest age:", oldest)
    # The oldest patient is listed as 455, which is clearly a mistake. We'll fix it soon.
    
    
    print("\nC4 -----------------------------------------------------------------")
    # Show the indices and ages of the 3 oldest patients in the dataset.
    oldest3Ages = sickDF.loc[ : , "age"].nlargest(3)
    print("Oldest 3 IDs and ages:\n", oldest3Ages, sep="")
   
    
    print("\nC5 -----------------------------------------------------------------")
    # Show *all data* for the 3 oldest patients in the dataset.
    oldest3 = sickDF.loc[oldest3Ages.index]
    print("Oldest 3 all data:\n", oldest3, sep="")
    
    
    print("\nC6 -----------------------------------------------------------------")
    # Show all patients with age less than 20
    ageUnder20 = sickDF.loc[sickDF.loc[ : , "age"] < 20]
    print("Patients under age 20:\n", ageUnder20, sep="")
    
    
    #C COMPLETED
 
    
def hw03():
    # Ensure that enough columns print when we print a dataframe
    pd.set_option('display.max_columns', 20)
    
    sickDF = readSickData()
    print("The first 5 rows of the dataset:\n", sickDF.head(5), sep='')
    
    first = sickDF.loc[0, :]
    print("Series object corresponding to the first patient:\n", first, sep='')
    
    sectionA(first)
    sectionB(sickDF)
    sectionC(sickDF)
    
    
    # We'll keep section D (below) in the hw03 function, because
    # we're mutating sickDF in the problems below. (Otherwise we'll get a warning message
    # about the mutation not taking effect in the way we might intend.)
    
    print("\n=================================================================")
    print("=================================================================")
    print("=================================================================")
    print("Section D: Deeper DataFrame Processing")
    
    # Note that some of these problems mutate sickDF. So if you do these problems 
    # out of order, your answers might vary in some ways until you've completed
    # them all.
    
    print("\nD1 -----------------------------------------------------------------")
    # Change sickDF so that any patient with age over 120 is dropped (erroneous data).
    # Then print the oldest age again to show that it has been updated.
    newSeries = sickDF.loc[:, "age"] 
    sickDF.loc[: , "age"] = newSeries.loc[newSeries < 120]
    oldest = sickDF.loc[: ,"age"].max()
    print("Oldest age after dropping erroneous row:", oldest)
    
    
    print("\nD2 -----------------------------------------------------------------")
    # Show the average age of women in the dataset.
	# Note: Your answer here depends on doing D1 correctly first, since D1 changes sickDF!
    femaleDF = sickDF.loc[ (sickDF.loc[: , "sex"] == 'F')]
    avgFemaleAge = femaleDF.loc[:, "age"].mean()
    print("Average female age:", avgFemaleAge)
    
    
    print("\nD3 -----------------------------------------------------------------")
    # Show the standard deviation of TT4 scores for women 50 and older.
    femalesOver50 = femaleDF.loc[ femaleDF.loc[:, "age"] >= 50 ]
    stdTT4FemaleOver50 = femalesOver50.loc[:, "TT4"].std()
    print("Standard deviation of TT4 scores for women 50 and older:", stdTT4FemaleOver50)
    
    
    print("\nD4 -----------------------------------------------------------------")
    # Show the number of people that are either on antithyroid medication, 
    # or have had thyroid surgery, or both.
    selectDF = sickDF.loc[ (sickDF.loc[: , "on antithyroid medication"] == 't') | 
                           (sickDF.loc[: , "thyroid surgery"] == 't') ]
    countAntiOrSurg = selectDF.loc[: ,  "age"].count()
    print("Number of people on antithyroid med, or with thyroid surgery:", countAntiOrSurg)
    
    
    print("\nD5 -----------------------------------------------------------------")
    # Add a new column to sickDF labeled "measurement sum" that is
    # the sum of the following measurements:
    # TSH, T3, TT4, T4U, FTI, TBG
    # Treat any missing values as 0 in the sum.
    copySickDF = sickDF.loc[: , :].fillna(0)
    combinedSeries = copySickDF.loc[: , "TSH"] + copySickDF.loc[: , "T3"] + copySickDF.loc[: , "TT4"] + copySickDF.loc[: , "T4U"] + copySickDF.loc[: , "FTI"] + copySickDF.loc[: , "TBG"]      
    sickDF.loc[: , "measurement sum"] = combinedSeries.map(lambda value : 0 if(np.isnan(value)) else value)
    print("First 5 rows of sickDF after 'measurement sum' column added:\n", sickDF.head(5), sep='')
    
    
    print("\nD6 -----------------------------------------------------------------")
    # Fill in the missing values of the FTI column with whichever is greater: the TT4 value, or 110.
    # You may also find this useful:
    # https://datascience.stackexchange.com/questions/17769/how-to-fill-missing-value-based-on-other-columns-in-pandas-dataframe
    sickDF.loc[: , "FTI"] = sickDF.apply(lambda row : max(row.loc["TT4"], 110) if(np.isnan(row.loc["FTI"])) else row.loc["FTI"], axis = 1)
    print("First 5 rows of sickDF after FTI missing values filled in:\n", sickDF.head(5), sep='')


    print("\nD7 -----------------------------------------------------------------")
    # Replace the column named TT4 with a column called TT4Cat.
    # Any TT4 value < 100 should be marked 'low' in TT4Cat.
    # Any TT4 value >= 100 and <= 120 should be marked 'medium' in TT4Cat.
    # Any TT4 value >120 should be marked 'high' in TT4Cat.
    # rename method --> df.rename(columns = {'team':'team_name', 'points':'points_scored'}, inplace = True)
    newSeries = sickDF.loc[: , "TT4"].map(lambda TT4value : "low" if(TT4value < 100) else ( "medium" if(TT4value >= 100 and TT4value <= 120)  else "high" ))
    sickDF.loc[: , "TT4"] = newSeries
    sickDF.rename( columns = {'TT4':'TT4Cat'}, inplace = True )
    print("First 5 rows of sickDF after replacing TT4 with TT4Cat:\n", sickDF.head(5), sep='')


    print("\nD8 -----------------------------------------------------------------")
    # Determine whether there is any patient in the dataset that:
    # Is female
    # Is in her 30's
    # Is pregnant
    # Has not had thyroid surgery
    # Doctors did query whether or not she had hypothyroidism
    # If there are any patients who meet the above conditions, list their IDs (row labels).
    checkingSeries = (sickDF.loc[:, "sex"] == 'F') & ((sickDF.loc[: , "age"] >= 30) & (sickDF.loc[: , "age"] < 40)) & (sickDF.loc[: , "pregnant"] == "t") & (sickDF.loc[: , "thyroid surgery"] == "f") & (sickDF.loc[: , "query hypothyroid"] == "t")
    areThereAny = checkingSeries.any()
    print("Are there any such women:", areThereAny)
    
    whoAreThey = sickDF.loc[checkingSeries].index
    print("The following women meet those criteria:\n", whoAreThey)
    
    
    print("\nD9 -----------------------------------------------------------------")
    # The attribute "on thyroxine" is really bool, although its type is currently interpreted as a string (either "t" or "f").
    # Convert that column's type to the bool type.
    # (We could do this for many attributes, of course, but we'll stick with just that one for now.)
    convertSeries = sickDF.loc[: , "on thyroxine"]
    sickDF.loc[: , "on thyroxine"] = convertSeries.map(lambda boolVal : True if(boolVal == "t") else False)
    print("First 5 rows of sickDF after converting 'on thyroxine' to bool:\n", sickDF.head(5), sep='')

    #D COMPLETED
    
hw03()
