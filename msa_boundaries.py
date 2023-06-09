# This file should write Python code to determine the bounding boxes of MSAs
# The first step will be to read in the msas_cleaned.csv file and the zipcodes.csv file

import pandas as pd

# a function that reads the csv file and returns pandas dataframe


def read_csv(filename):
    """Reads the csv file and returns a list of lists of the data"""
    df = pd.read_csv(filename, header=None)
    return df

# a function that joins the data between the two dataframes on the zip column


def join_data(df1, df2):
    """Joins the data between the two dataframes on the zip column"""
    df = pd.merge(df1, df2, left_on=0, right_on=8)
    header_row = 0
    df.columns = df.iloc[header_row]
    df = df.drop(df.index[header_row])
    df['xmin'] = df['xmin'].astype(float)
    df['xmax'] = df['xmax'].astype(float)
    df['ymin'] = df['ymin'].astype(float)
    df['ymax'] = df['ymax'].astype(float)

    return df

# a function that returns the bounding box of the MSA. Compare each row's bounding box to calculate the min and max of the whole MSA. Each bounding box is defined by xmin, ymin, xmax, ymax
# the function also gets the center of the MSA and the distance from the center to the furthest point in the MSA
def get_msa_bounding_box(df, msa):
    """Returns the bounding box of the MSA"""
    # get the rows for the MSA
    rows = df[df['msa_code'] == msa]
    msa_title = rows.iloc[0]['msa_title']
    msa_state = rows.iloc[0]['STATE_NAME']

    # get the min and max values for longitude and latitude
    min_long = rows['xmin'].min()
    max_long = rows['xmax'].max()
    min_lat = rows['ymin'].min()
    max_lat = rows['ymax'].max()
    # get the center of the MSA
    center_long = (float(min_long) + float(max_long)) / 2
    center_lat = (float(min_lat) + float(max_lat)) / 2
    # get the distance from the center to the furthest point in the MSA
    radius = int(max(abs(center_long - min_long)*50, abs(center_lat - min_lat)*70)*1.15*1609) # lat/long to nautical miles to miles
    # return the bounding box
    return [msa, msa_title, msa_state, min_long, min_lat, max_long, max_lat, center_long, center_lat, radius]



# def get_msa_bounding_box(df, msa):
#     """Returns the bounding box of the MSA"""
#     # get the rows for the MSA
#     rows = df[df['msa_code'] == msa]

#     msa_title = rows.iloc[0]['msa_title']
#     # get the min and max values for longitude and latitude
#     min_long = rows['xmin'].max()
#     max_long = rows['xmax'].min()
#     min_lat = rows['ymin'].min()
#     max_lat = rows['ymax'].max()

#     # return the bounding box
#     return [msa, msa_title, min_long, min_lat, max_long, max_lat]

# a function that writes a csv file


def write_csv(df, filename):
    """Writes a csv file"""
    df.to_csv(filename, index=False)


# a function that iterates through the MSAs and writes them to a csv file
def write_msa_bounding_boxes(df, filename):
    """Iterates through the MSAs and writes them to a csv file"""
    # get the unique MSAs
    msas = df['msa_code'].unique()
    # create a list to hold the bounding boxes
    bounding_boxes = []
    # iterate through the MSAs
    for msa in msas:
        # get the bounding box
        bounding_box = get_msa_bounding_box(df, msa)
        # add the bounding box to the list
        bounding_boxes.append(bounding_box)
    # create a dataframe from the bounding boxes
    df = pd.DataFrame(bounding_boxes, columns=[
                      'msa_code', 'msa_title', 'state', 'min_long', 'min_lat', 'max_long', 'max_lat', 'center_long', 'center_lat', 'radius'])
    # write the csv file
    write_csv(df, filename)

# a function that runs the program


def main():
    """Runs the program"""
    # read in the MSAs.csv file
    df1 = read_csv('msas_cleaned.csv')
    # read in the zipcodes.csv file
    df2 = read_csv('county_bounding_boxes.csv')
    # join the dataframes
    df = join_data(df1, df2)
    print(df.head())
    # write the msa bounding boxes to a csv file
    write_msa_bounding_boxes(df, 'msa_bounding_boxes.csv')


# call the main function
main()
