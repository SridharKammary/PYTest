from datetime import datetime
import pandas as pd

date=datetime.now()
print(f"Date with time: {date}")
onlyDate=datetime.date(date)
print(f"Only Date : {onlyDate}")

#prepare the date from values

preparedDate=datetime(year=2023,month=12,day=30)
print(f"Prepared Date: {preparedDate}")

#Get the Year, Get the Month and get the Day, date ==> is date with time value
print(f"Year={datetime.strftime(date,'%Y')},Month={datetime.strftime(date,'%m')},Day={datetime.strftime(date,'%d')}")

#get the date in MM-DD-YYYY format
print(f" Formatedd Date={datetime.strftime(date,'%m-%d-%Y')}")

#Add months, Days, Years
#Get last day of the Months and first daye of the month, we use pandas for addition and subtraction
#print(pd.DateOffset(month=2)), observe we have taken params: month and years (not Month and Year)
d=date + pd.DateOffset(month=2)
print(f"Adding 2 months to current Date = {d}")
d=date + pd.DateOffset(years=2)
print(f"Adding 2 Years  = {d}")
d=date - pd.DateOffset(years=4)
print(f"Subtract 4 Years = {d}")
#Lets play with pandas Classes, Methods
print(f"Time Stamp: {pd.Timestamp(d)}")