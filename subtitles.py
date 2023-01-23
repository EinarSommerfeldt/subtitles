import io
import pandas as pd

file = io.open("ichi.srt", mode="r", encoding="utf-8")
file_str = file.read()

file_list = file_str.split("\n")

time_format = "%H:%M:%S,%f" #00:01:55,281
padding = 0.5

for i, line in enumerate(file_list):
    if "-->" in line:
        timestamps = line.split("-->")
        timestamps[0] = timestamps[0].strip()
        timestamps[1] = timestamps[1].strip()
        t1 = pd.Timestamp(timestamps[0])
        t2 = pd.Timestamp(timestamps[1])
        t1 = t1 - pd.Timedelta(seconds=padding)
        t2 = t2 + pd.Timedelta(seconds=padding)
        file_list[i] = t1.strftime(time_format)[0:-3] + " --> " + t2.strftime(time_format)[0:-3] #Remove last 3 zeroes of microsecond

new_string = "\n".join(file_list)
output_file = io.open("output.srt", mode="w", encoding="utf-8")
output_file.write(new_string)

print("end of program")