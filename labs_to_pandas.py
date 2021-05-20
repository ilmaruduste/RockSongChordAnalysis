import pandas as pd
import glob

complete_df = pd.DataFrame()

labs_path = 'ChordRecognitionMIDITrainedExtractor/Datas/labs_estimated/'

for filename in glob.glob(str(labs_path + '*.lab')):
    print(f"Working on {filename.split('/')[-1]}...")
    # temp_df = pd.read_csv('001.Led Zeppelin-1971-Led Zeppelin IV-04-Stairway To Heaven short.wav.lab', sep = ' ', header = None)
    temp_df = pd.read_csv(filename, sep = ' ', header = None)
    temp_df['song_name'] = ''.join(filename.split('/')[-1].split('.')[0:-2])

    complete_df = pd.concat([complete_df, temp_df])
    # df.head()
    
complete_df.columns = ['start_timestamp', 'end_timestamp', 'chord', 'song_name']
complete_df.head()

# complete_df.to_csv('250_wav_90s.csv', sep = ';')
complete_df.to_csv('processed_data/750_songs_complete_chords.csv', sep = ';')