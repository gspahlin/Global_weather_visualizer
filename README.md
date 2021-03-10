# Global Weather Visualizer
A project to use API data to visualize weather around the world. 
Data was obtained from OpenWeatherMap API from around 500 cities which were randomly selected by citipy.
The data was collected in lists, which were made into a dataframe and written to a .csv. 
In a second notebook the analysis and plotting tasks were implemented on this data. This included 
plotting latitude against temperature, humidity cloudiness and windspeed and doing linear regression analysis,
filtering data to find ideal conditions for a dogsledding vacation, and eventually plotting geographic data using 
Jupyter gmaps and google maps javascript API. Google Places API was called to find hotels near the cities with optimal
weather conditions. Finally humidity and the locations of hotels were plotted on a google map. 

Files:

Weather_api_caller_final.ipynb - This notebook is designed to loop calls to the OpenWeatherMap API, organize the data, and
write the results out to a .csv file

City_weather_analysis.ipynb - This contains all the analysis tasks and plotting. This notebook is also the one that interfaces with 
the google maps APIs 


city_weather_1_5_21_try2.csv  - this is an output file from the first notebook, which is analyzed in the second. It contains data from OpenWeatherMap API
collected on 1/5/21

Global_Weather_Survey.py - I decided to modify Weather_api_caller_final.ipynb into a script so that I could run it on the command line and easily get a 
survey of weather data from across the planet. The script tests to see if it can call London, and shuts down if the api cant be reached on that call. It also asks
for imput so that you can name the file without editing the code, and reports the number of cities called, and the number of rows of data collected. 


Temp_map_plotter4.ipynb  - An interactive weather map which uses a .csv imput, and allows temperatures to be visualized in ranges. Button controls from the 
ipywidgets library allow each range to be turned on and off. 
