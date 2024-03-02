# Student Zoom Attendence

Purpose of this analysis: Calculate student attendence recorded for an entire semester. Once processed, this data can be visualized in a BI tool (e.g., Tableau).

The analysis will calculate the:
* time (minutes) in attendance per lecture
* total absences per semester


## Input
Raw data

To obtain the Zoom Attendance Reports, having access to the API would streamline the export. However, the API was not accessable due to the permissions set by my organization. As a workaround, I downloaded reports directly from Zoom. 

* When Zoom attendance reports are downloaded (as CSV's), they are automatically saved under the Meeting ID. This analysis aggregates the csv's into a single entity, so there's no need to re-name the csv's.
* Important note on privacy: student names in the raw data were replaced with character names from the Avengers. 

Architecture 

* All CSV's must be saved in the same directory. Paste this path in the appropriate section in the jupyter notebook.

E.g., in my case, I saved my csv's in the directory "RawCSVs". 

## Extract/Transform/Load
Extract: 
* All csv's are pulled from the directory specified above.
  
Transform:
* The Zoom reports are then aggregated into a single dataframe.
* Attendance for each student is collapsed, having 1 student entry per day. If a student has multiple records in a single day, the time per session is summed to report the total minutes in attendance per day. If a student is not present during the day, the reported time is 0. 
* To calculate total absences, the number of sessions with 0 minutes is considered an absence.
* To measure the total number of absences for the entire semester, the number of absences is counted. The structure of this dataframe has student names (rows) and dates of attendance (columns). 

Load:
* The dataframe is saved as a csv, which allows for downstream visualizations.

## Visualization
For my purposes, I used the output csv for Tableau to produce a heatmap (rows = student names, columns = lecture date, 'cells' show the time (minutes) students spent in each class).
I find this visualization easy to interpret as you can easily see which students are absent each day throughout the entire semester.

