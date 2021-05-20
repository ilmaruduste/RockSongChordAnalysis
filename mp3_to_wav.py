import os
from pydub import AudioSegment
import ffmpeg
import glob

for filename in glob.glob('original_mp3/*.mp3'):
    print(f"Working on {filename}...")
    src = filename

    destination_filename = '_'.join(filename.split('/')[-1].split('.')[0:-1]) + '.wav'
    dst = 'ChordRecognitionMIDITrainedExtractor/Datas/audios_estimation/' + destination_filename

    # Song clips last for 1m 30s
    t1 = 30 * 1000 # 30 seconds
    t2 = 120 * 1000 # 120 seconds

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    newSound = sound[t1:t2]
    newSound.export(dst, format="wav")

print("Done!")