import re
from pathlib import Path
import multiprocessing
import tqdm
import os

def openfile(file_path):
    with open(file_path,'r') as file:
        data=file.readlines()
    return data

def extract_tm_score_by_average_length(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    # Extract TM-score normalized by average length
    tm_score_pattern = r'TM-score= (\d+\.\d+) \(if normalized by average length of two structures, i.e., LN= \d+\.\d+, d0= \d+\.\d+\)'
    tm_score_match = re.search(tm_score_pattern, data)
    tm_score_avg_length = float(tm_score_match.group(1))

    return tm_score_avg_length


def extract_text_between_lines(file,tmalign):
    name=file.split('/')[6].split('_')[3]

    with open(file,'r') as file,open('res.txt','a') as wf:
        data =file.readlines()
        data1 = ''.join(data[21:-1]).strip() 
        txt=f'TM-Align Score is:{tmalign}\n{name} >\n {data1}\n'
        wf.write(txt)
        return None


input_folder='/home/mt0/22CS60R49/MTP/tm_align_results'
tmfiles = [file for file in os.listdir(input_folder) if file.endswith(".tmalign")]

for i in range(len(tmfiles)-1):
    tmfile = os.path.join(input_folder, tmfiles[i])
    try:
        tm_score_avg_length = extract_tm_score_by_average_length(tmfile)
        if(tm_score_avg_length>=0.7):
            extract_text_between_lines(tmfile,tm_score_avg_length)
            #print(type(t))
            #print("TM-score normalized by average length:", tm_score_avg_length)
            # with open('output.txt','a') as file:
            #  file.write("TM-score normalized by average length:", tm_score_avg_length)
           
    except:
        pass