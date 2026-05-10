# code for cleaning data for the project
import pandas as pd

# Load CSV file
dfArray = [
    pd.read_csv("Brent Oil.csv"),
    pd.read_csv("Gold 100years.csv"),
    pd.read_csv("silver 100 years.csv"),
    pd.read_csv("swift_currency_tracker_all_reports.csv")
]

# -----------------------------
# BASIC DATA INSPECTION
# -----------------------------
for df in dfArray:
    for dataFrame in dfArray:
        print("\n")
        print("# -----------------------------")
        # percent of missing fields in each column
        missing_percent = (df.isnull().sum() / len(df)) * 100
        print(missing_percent)

        # duplicates
        duplicates = df.duplicated().sum()
        print("Duplicate rows:", duplicates)

        # general info for every col
        print("\nInfo: \n", df.info())
        print("\nDescription: \n", df.describe())

        # check if all fields are NOT null
        print("\nAll fields are NOT null:\n", (dataFrame.isnull().sum() <= 0).values)
        print("# -----------------------------")
        
        
        
# After inspection of all the datasets, I found that all the tables except the swift_currency_tracker_all_reports.csv have no missing values, and no duplicates. 
# this is a report for the swift_currency_tracker_all_reports.csv:

# code:
# missing_percent = (df.isnull().sum() / len(df)) * 100
# print(missing_percent)

# output:
# report_month            0.000000
# data_month              0.000000
# source_report_name      0.000000
# metric                  0.000000
# category                0.000000
# currency_or_economy     0.000000
# value                  12.727273
# unit                   12.727273
# rmb_global_rank        84.848485
# notes                   7.272727


# == Code i used to drop the rmb_global_rank column == 
# df = df.drop(columns=['rmb_global_rank'])
# df.to_csv("swift_currency_tracker_all_reports.csv", index=False)

#  for value and unit rows I decided to delete rows with nulls
#  because without those 2 fields all the data is not useful

# code:
# df = df.dropna(subset=['value', 'unit'])
# df.to_csv("swift_currency_tracker_all_reports.csv", index=False)


# ONE MORE ISSUE:
# in swift_currency_tracker_all_reports there still is one more issue
# the minimal value is less than zero, which is not possible
# so i just deleted the '-' sign from the walue