#-----------------------------------------------
#Summary of the ETL project
#----------------------------------------------

The goals of this project were to:
- Extract data from two seperate sources
- Transorm the data
- Load the data into a database
- Use the database to display the data

#What I did for Extraction
- The two data sources that I used were FRED, and YCharts
- I pulled 6 seperate data sources from FRED for various economic time series
- I imported asset return data from an excel file with data exported from YCharts

#What I did for Transformation
- I created tables for each sperate economic serires from FRED due to incomsistent frequency and release timing.
- I created one table for the YCharts data as all infomration is provided annually.

#What I did for loading
- I loaded all the tables described above into an SQLite file.
- I experimented with using MYSQL, but decided against it when thinking about deployment options

#What I did for displaying the data
- One of the biggest requirements for data analysis in Finance is compliance review.
  You have to be able to show where every peice of data comes from.
- Given the need for compliance review, a dashboard for information I am making for work has a support file page.
- The link for the supprt file page is: http://127.0.0.1:5000/supportfilesecon

#--------------------------------------
#FILE KEY
#--------------------------------------
- econdatapull.py handles all of the ETL requirements
- app.py is the app that create the dashboard and displays the data for end user purposes. 
