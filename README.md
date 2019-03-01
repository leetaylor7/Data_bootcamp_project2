#-----------------------------------------------
#Summary of the ETL project
#----------------------------------------------#

#The goals of this project were to:
- Extract data from two seperate sources.
- Transorm the data.
- Load the data into a database.
- Use the database to display the data.

#What I did for Extraction
- The two data sources that I used were FRED, and YCharts.
- I pulled 6 seperate data sources from FRED using their API for several economic time series.
- I imported asset return data from an excel file with data exported from YCharts.

#What I did for Transformation
- I created tables for each sperate economic serires from FRED due to incomsistent frequency and release timing.
- I formatted the tables to have incremental IDs so that I can sort by most recent data normalize with sorting functions later.
- I created one table for the YCharts data as all infomration is provided annually.
- I set up all tables to be ordered first by date, then by values. This allows for data to be easily tracked and manipulted with for loops. 

#What I did for loading
- I loaded all the tables described above into an SQLite file.
- I experimented with using MYSQL, but decided against it when thinking about deployment options.
- SQLite is the easiest to transfer to other people as it does not require additional software to be installed.

#What I did for displaying the data
- One of the biggest requirements for data analysis in Finance is compliance review.
  You have to be able to show where every peice of data comes from.
- Given the need for compliance review, a dashboard for information I am making for work has a support file page.
- I did not make the data exportable to JSON format as no one in my office knows what JSON is except for me.
- The link for the supprt file page is: http://127.0.0.1:5000/supportfilesecon

#--------------------------------------
#FILE KEY
#--------------------------------------#
- econdatapull.py handles all of the ETL requirements
- app.py is the app that create the dashboard and displays the data for end user purposes. 
