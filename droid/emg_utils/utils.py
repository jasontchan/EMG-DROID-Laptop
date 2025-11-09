from .emg import EMG
from .emg_myo import EMGMyo
from droid.misc.parameters import *

def make_emg_streams():
    
    emg_streams = {}

    for i in range(num_bands):
        emg_streams[emg_names[i]] = EMGMyo(emg_mac[i], emg_tty[i], 
                                           position=emg_names[i].split("_")[-1], 
                                           window_length=emg_window_length, 
                                           mode=emg_mode_type)
    print(f"EMG streams created: {emg_streams}")
    return emg_streams