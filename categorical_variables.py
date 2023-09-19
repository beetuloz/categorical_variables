# Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exporting the dataset 'titanic'
df = sns.load_dataset('titanic')
df.head()

# Finding columns that has the following data types: "category", "object" or "bool" to get to the categorical variables
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

# Some variables might look like numerical but essentially categorical.
num_but_cat = [col for col in df.columns if df[col].dtypes in ["int","float"] and df[col].nunique() < 10]

# Some variables might have many number of unique classes, which are called "cardinal"
cat_but_car = [col for col in df.columns if str(df[col].dtypes) in ["category","object"] and df[col].nunique() > 20]

# Merging the categorical variables together and removing the cardinal variables
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

# The visualisation method for categorical variables are usually barplot or countplot. An example:
df["sex"].value_counts().plot(kind="bar")
plt.show

# Function that summarizes all the categorical variables and visualises instead of running everything one by one
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts()}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

# Running the function in all categorical columns of the dataframe
for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df,col, plot=True)

