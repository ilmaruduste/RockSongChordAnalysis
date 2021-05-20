import audio_metadata
import pandas as pd
import glob

metadata_df_total = pd.DataFrame()

for filename in glob.glob('original_mp3/*.mp3'):

    metadata = audio_metadata.load(filename)
    
    metadata_df = pd.DataFrame(dict(metadata.tags))
    metadata_df['filename'] = '_'.join(filename.split('/')[-1].split('.')[0:-1])
    metadata_df_total = pd.concat([metadata_df_total, metadata_df])

print(metadata_df_total.head())

metadata_df_total.to_csv('processed_data/metadata_df_total.csv', sep = ';')