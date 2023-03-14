# code that converts the first column of a csv file to formatted zip codes
import pandas as pd
# a function that reads in the csv file as a pandas dataframe


def read_csv(filename):
    """Reads the csv file and returns a pandas dataframe"""
    df = pd.read_csv(filename, header=None)
    return df

# a function that converts strings into formatted zip codes. For example, "100" becomes "00100", and "1,001" becomes "01001"


def convert_zip_codes(df):
    """Converts strings into formatted zip codes"""
    # create a list to store the zip codes
    zip_codes = []
    # loop through each zip code
    for zip_code in df[0]:
        # convert the zip code to a string
        zip_code = str(zip_code)
        # remove the commas
        zip_code = zip_code.replace(",", "")
        # add leading zeros
        zip_code = zip_code.zfill(5)
        # add the zip code to the list
        zip_codes.append(zip_code)
    # add the zip codes to the dataframe
    df[0] = zip_codes
    # return the dataframe
    return df


# a function that writes the dataframe to a csv file
def write_csv(df):
    """Writes the dataframe to a csv file"""
    df.to_csv("msa_cleaned.csv", header=False, index=False)


# read in the csv file
df = read_csv("MSAs.csv")
# convert the zip codes
df = convert_zip_codes(df)
# write the dataframe to a csv file
write_csv(df)
