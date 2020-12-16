import os
import datetime

def diary():
    
    listfiles = os.listdir("../../Diary/")
    dt = datetime.datetime.today() 
    day_num = []

    for onefile in listfiles:
        day_num.append(int(onefile[3]))
    day_num.sort()

    #Day ?
    num_file = day_num[-1] + 1
    year = str(dt.year)[2:4]

    #create file
    filename = 'Day' + str(num_file) + '-' + str(dt.month) + '-' + str(dt.day) + '-' + str(year) + '.txt'
    
    with open(r"../../Diary/" + filename, 'w') as file:
        pass

if __name__ == '__main__':
    diary()
