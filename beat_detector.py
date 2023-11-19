import librosa
import sys
import os

# file_path = "/Users/aalobaid/Downloads/StarWars3.wav"
# file_path = "/Users/aalobaid/Downloads/BabyElephantWalk60.wav"
#
# if len(sys.argv) == 2:
#     file_path = sys.argv[1]
# # y, sr = librosa.load(librosa.ex('choice'), duration=10)
# y, sr = librosa.load(file_path, duration=10)
# tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
# print(f"Beats: {beats}")
# print(f"Arguments: {sys.argv}")


# # Case 1
# file_path = "/Users/aalobaid/Downloads/BabyElephantWalk60.wav"
# y, sr = librosa.load(file_path, duration=10)
# tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
# print(f"Beats: {beats}")
#



# Case 2
# This line is just to show use the arguments. It does not do anything else
# print(f"Args: {sys.argv}")

def detect_beats(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The provided file does not exist. <{file_path}>")
        return
    y, sr = librosa.load(file_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    print(f"Beats: {beats}")
    for b in beats:
        print(f"{b}")
    write_beats_to_file(beats)
    time_stamps = librosa.frames_to_time(beats, sr=sr)
    print(f"Time Stamps: {time_stamps}")
    for t in time_stamps:
        print(f"{t}")
    write_time_stamps_to_file(time_stamps)


def write_beats_to_file(beats, fname="beats.csv"):
    with open(fname, "w") as f:
        for b in beats:
            f.write(f"{b}\n")


def write_time_stamps_to_file(beats, fname="timestamps.csv"):
    with open(fname, "w") as f:
        for b in beats:
            f.write(f"{b}\n")


if len(sys.argv) == 2:
    file_path = sys.argv[1]
    print(f"Analysing {file_path}")
    detect_beats(file_path)
else:
    print(f"Error: Expects the audio file")


