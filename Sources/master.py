import os
import glob
import pandas as pd
import re
main_directory = os.getcwd()+'/Sources/'

# Iterate through all folders and sub-folders
for root, dirs, files in os.walk(main_directory):
    if 'variables/' in root:
        csv_files = glob.glob(root+'/*.csv')
        dfs= []
        for csv in csv_files:
            month = re.findall(r'\d{4}_\d{2}', csv)[0]
            df = pd.read_csv(csv)
            df['month'] = month
            dfs.append(df)

        master_df = pd.concat(dfs)
        master_df.to_csv(main_directory+'master/{}.csv'.format(csv_files[0].split('/')[-1][:-12]),
                         index=False)

    else:
        pass
    
            

exit()
#IMD
path = os.getcwd()+'/Sources/IMD/data/rain/csv/'
csvs = glob.glob(path+'*.csv')
dfs= []
for csv in csvs:
    month = re.findall(r'\d{4}_\d{2}', csv)[0]
    df = pd.read_csv(csv)
    df['month'] = month
    dfs.append(df)

master_df = pd.concat(dfs)
master_df = master_df.rename(columns={'max': 'max_rain', 'mean':'mean_rain', 'sum':'sum_rain'})
master_df.to_csv(os.getcwd()+'/Sources/archive/rainfall.csv', index=False)

exit()
#BHUVAN
path = os.getcwd()+'/Sources/BHUVAN/data/inundation_pct/'
csvs = glob.glob(path+'*.csv')
dfs= []
for csv in csvs:
    month = re.findall(r'\d{4}_\d{2}', csv)[0]
    df = pd.read_csv(csv)
    df['month'] = month
    dfs.append(df)

master_df = pd.concat(dfs)

master_df.to_csv(os.getcwd()+'/Sources/archive/inundation.csv', index=False)