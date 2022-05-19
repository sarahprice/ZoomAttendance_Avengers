#activate myenv in terminal
#set path in order for relative paths to work

import glob
import pandas as pd

#path that holds all the saved Zoom Reports csv's downloaded from Zoom. 
path = /.#"C:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/Zoom_Attendance_pipeline/In_ZoomAttendance_rawCSVs/"
files = glob.glob(path + '\*.csv')

#Define empty list to store content
df = pd.DataFrame()
content = []

for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)

# convervting content into data_frame
df = pd.concat(content)
#print(df)

df.to_csv("C:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/Zoom_Attendance_pipeline/Out_ZoomAttendance_compiled/concat_ZoomAttendance.csv")

#insert path
#df = pd.read_csv("C:/Users/campb/OneDrive/Documents/Personal/RandomPythonScripts/Zoom_Attendance_pipeline/Out_ZoomAttendance_compiled/concat_ZoomAttendance.csv", index_col = False)#"User Name")

#Replace spaces in column names with an underscore (to remove spaces in the column so it's easier to split)
df.columns = df.columns.str.replace(' ', '_')

#split 'Join time' column into new columns named 'Date' and 'Join'
df[['Date','Join']]=df.Join_time.str.split(' ', n=1, expand= True)

##retains columns of interest
df_clean = df.loc[:,['User_Name','User_Email','Duration(Minutes)','Date']]


#Context: Some students joined Lecture more than once per lecture (e.g., if their internet kicked them off of zoom, they had to rejoin the meeting)
##Task: For each student (User_Name) and lecture (Date), sum the 'Duration(Minutes)'.
df_clean_SumDura = df_clean.groupby(["User_Name", "Date"])["Duration(Minutes)"].sum()
df = df_clean_SumDura.unstack()


#Calculate number of absences (i.e., number of "NaN") per student
#add column (i.e. ['Absences']) that calculates the number of NaN (is.null()) per row (for row use 'axis = 1')
df['Absences'] = df.isnull().sum(axis=1)

df.to_csv('C:/Users/campb/OneDrive/Documents/Cell_Bio/Spring22/1100am/LectureAttendance_concat/1100_concat_clean_WideTable.csv')
