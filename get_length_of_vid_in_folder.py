import os 
import subprocess as sb 

def get_length(filename): 

    a = str(sb.check_output('ffprobe -i  "'+full_input_name+'" 2>&1 |findstr "Duration"',shell=True)) 
    a = a.split(",")[0].split("Duration:")[1].strip()
    h, m, s = a.split(':')
    duration_in_seconds = int(h) * 3600 + int(m) * 60 + float(s)
    return duration_in_seconds

#reference local test set location, these are unprocess videos 
local_test_set = "D:/Data_science/colaberry/video_audio_analysis/test_set/"
videos  = os.listdir(local_test_set)
sum_time =0 
for vid in (videos): 

    input_name = vid
    vid= vid.replace(".mp4", "")
    output_name = vid+"_output.mp4"
    
    full_input_name = local_test_set+input_name
    duration_seconds=get_length(full_input_name)
    
    sum_time += duration_seconds
    

print("total time of all videos in seconds -  {}".format(sum_time)  )
print("total time in hours is {}".format(sum_time/3600))

