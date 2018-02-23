##Making a basic Bokeh line graph
#
##importing Bokeh
#from bokeh.plotting import figure
#from bokeh.io import output_file, show
#
##prepare some data
#x=[3,7.6,10]
#y=[3,6,9]
#
##prepare the output file
#output_file("Line.html")
#
##Create figure object
#f=figure()
#
##create line plot
#f.triangle(x,y)
#
#show(f)
#------------------------------------------------------------------ READ CSV
#Making a basic Bokeh line graph

##importing Bokeh and pandas
#from bokeh.plotting import figure
#from bokeh.io import output_file, show
#import pandas
#
##prepare some data
#df=pandas.read_csv("bachelors.csv")
#x=df["Year"]
#y=df["Engineering"]
#
##prepare the output file
#output_file("Line_from_csv.html")
#
##Create figure object
#f=figure()
#
##create line plot
#f.line(x,y)
#
#show(f)
#------------------------------------------------------------------READ EXCEL
#importing Bokeh and pandas
#from bokeh.plotting import figure
#from bokeh.io import output_file, show
#import pandas
#
##prepare some data
#df=pandas.read_excel("verlegenhuken.xlsx")
#x=df["Temperature"]
#y=df["Pressure"]
#x=x/10
#y=y/10
#
##prepare the output file
#output_file("Line_from_csv.html")
#
##Create figure object
#f=figure()
#
#
#f.title.align="center"
#f.title.text="Temperature and Air Pressure"
#f.title.text_color="Gray"
#f.title.text_font="arial"
#f.title.text_font_style="bold"
#f.xaxis.axis_label="Temperature (°C)"
#f.yaxis.axis_label="Pressure (hPa)"
#
##create line plot
#f.circle(x,y, size=0.5)
#
#show(f)
##------------------------------------------------------------------ Parsed Datetime

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("D:\\Downloads\\Python\\Projects\\Bokeh Test\\adbe.csv", parse_dates=["Date"])

p=figure(width=500, height=250,x_axis_type="datetime", responsive=True)

p.line(df["Date"], df["Close"], color="Orange",alpha=0.5)

output_file("Timeseries.html")
show(p)