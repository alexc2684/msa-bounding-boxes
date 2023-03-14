# MSA Bounding Box Calculator

### tl;dr msa_bounding_boxes.csv contains the bounding boxes for all MSAs in the US

How to run the code:

1. Clone the repo
2. Install the requirements: `pip install -r requirements.txt`
3. Run the code: `python3 msa_bounding_boxes.py`

The code finds bounding boxes based on the join of the county bounding box data and the associated MSA for each county. The code then finds the bounding box for each MSA by finding the minimum and maximum latitude and longitude for each MSA. The code then outputs the bounding boxes for each MSA to a csv file.

![](example.png?raw=true)
