# ZoomAttendance_Pipeline
Use Zoom Attendance Reports (CSVs) (from Canvas) to (1) calculate the number of absences and (2) convert into format used for visualizations (e.g., heatmap)

The goal here is to produce an attendance report for the whole semester, 
-calculating the number of minutes each student attends per lecture, 
-calculating the number of days absent throughout the entire semester

# Code takes the input csv's and produce 1 aggregated output

## Input-
Downloaded Zoom Reports (CSV) are automatically saved under the same name - there is no need to re-name these since this code will aggregate the CSV's. 

Important - all the CSV's should be saved in the same directory. The name of the directory name will be important to paste into this python aggregating script. 
I created the directory "RawCSV's" to store my Zoom Reports. 

## Output -
All zoom reports into 1 wide CSV with names in the rows and the dates of attendance as the columns. 
This output calculates the number of days absent.  

## Visualization -
The output can be used for data visualization purposes (e.g. Tableau). 
Since the aggregates data are relatively clean, you may not have to do much downstream cleaning. 

For my purposes here, I used the output CSV into Tableau to produce a heatmap (rows = student names, columns = lecture date, 'cells' show the time (minutes) students spent in each class).
I find this visualization easy to interpret as you can easily see which students are absent each day. 


