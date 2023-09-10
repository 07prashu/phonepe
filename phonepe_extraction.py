import os
import json
import pandas as pd

root_dir = (r'/content/pulse/data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, '/content/pulse/data/aggregated/transaction/country/india/state')):
    state_path = os.path.join(root_dir, '/content/pulse/data/aggregated/transaction/country/india/state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data we're interested in
                            for transaction_data in data['data']['transactionData']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'Transaction_Type': transaction_data['name'],
                                    'Transaction_Count': transaction_data['paymentInstruments'][0]['count'],
                                    'Transaction_Amount': transaction_data['paymentInstruments'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df1 = pd.DataFrame(data_list)
df1