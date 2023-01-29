import io
import pandas as pd
import math

def read_config():
    config = {}
    config_file = io.open("config.txt", mode="r", encoding="utf-8")
    config_str = config_file.read()

    config_list = config_str.split("\n")
    for line in config_list:
        line_list = line.split("=")
        config[line_list[0].strip()] = line_list[1].strip()
    return config

def edit_subtitle(config):
    time_format = "%H:%M:%S,%f" #00:01:55,281000

    file = io.open(config["filename"], mode="r", encoding="utf-8")
    file_str = file.read()
    file_list = file_str.split("\n")
    
    padding = float(config["padding"])
    shift = float(config["shift"])

    progressive_shifting = bool(int(config["progressive_shifting"]))
    first_time = pd.Timestamp(config["first_time"])
    second_time = pd.Timestamp(config["second_time"])
    interval_shift = float(config["interval_shift"])

    difference = second_time-first_time
    desync_factor = interval_shift/difference.total_seconds()



    for i, line in enumerate(file_list):
        if "-->" in line:
            timestamps = line.split("-->")
            timestamps[0] = timestamps[0].strip()
            timestamps[1] = timestamps[1].strip()
            t1 = pd.Timestamp(timestamps[0])
            t2 = pd.Timestamp(timestamps[1])
            t1 = t1 - pd.Timedelta(seconds=padding) + pd.Timedelta(seconds=shift)
            t2 = t2 + pd.Timedelta(seconds=padding) + pd.Timedelta(seconds=shift)

            if progressive_shifting:
                delta = first_time-t1
                correction_seconds = math.floor(delta.total_seconds()*desync_factor)
                correction_mseconds = int(delta.microseconds/1000*desync_factor)
                t1 = t1 + pd.Timedelta(seconds=correction_seconds, milliseconds=correction_mseconds)
                t2 = t2 + pd.Timedelta(seconds=correction_seconds, milliseconds=correction_mseconds)

            file_list[i] = t1.strftime(time_format)[0:-3] + " --> " + t2.strftime(time_format)[0:-3] #Remove last 3 zeroes of microsecond

    new_string = "\n".join(file_list)
    output_file = io.open("output.srt", mode="w", encoding="utf-8")
    output_file.write(new_string)


config = read_config()
edit_subtitle(config)
print("end of program")