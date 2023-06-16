import pandas as pd
import os.path

def Add_data_to_File(data_list):
    file_path = 'data.xlsx'

    if os.path.isfile(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=['Quote Text', 'Author Name', 'Tags List'])

    df = df._append({'Quote Text':data_list[0], 'Author Name':data_list[1], 'Tags List':data_list[2]}, ignore_index=True)
    df.to_excel(file_path, index=False)