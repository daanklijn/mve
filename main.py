import pandas as pd 
import matplotlib.pyplot as plt

continents=['AF','AS','EU','NA','SA','OC']

# This file contains yearly global carbon dioxide emissions between 1964 - 2013 in ppm
co2 = pd.read_excel('CO2_mve.xlsx',index=False)

# This file contains continental surface measurements of monthly mean incoming solar 
# radiation between 1964 - 2013 in watts per meter squared
rad = pd.read_excel('Continentalrad_mve.xlsx') 
rad['WORLD']=rad[continents].mean(axis=1)

# This file contains monthly continental surface air temperature between 1964 - 2013 in degrees celcius
temp = pd.read_excel('Continentaltemp_mve.xlsx')
temp['WORLD']=temp[continents].mean(axis=1)

# This file contains yearly real GDP with constant 2010 prices of world and the United States in billions
gdp = pd.read_excel('GDP_mve.xlsx')

temp_world_plt = temp.plot.line(x='Date',y="WORLD") 
temp_world_plt.set_ylabel('Degrees celcius') 
temp_world_plt.set_title("Average temperature world over the years")

temp_continents_plt = temp.plot.line(x='Date',y=continents) 
temp_continents_plt.set_ylabel('Degrees celcius') 
temp_continents_plt.set_title("Temperature per continent")

temp_world_plt = rad.plot.line(x='Date',y="WORLD") 
temp_world_plt.set_ylabel('Watts per meter squared') 
temp_world_plt.set_title("Average solar radiation world over the years")

temp_continents_plt = rad.plot.line(x='Date',y=continents) 
temp_continents_plt.set_ylabel('Watts per meter squared') 
temp_continents_plt.set_title("Solar radiation per continent")

co2_plt = co2.plot.line(x='Date',y='CO2')
co2_plt.set_ylabel('PPM')
co2_plt.set_title('Global carbon dioxide emissions between 1964 - 2013')

gdp_plot = gdp.plot.line(x='Date')
gdp_plot.set_ylabel('Billions of dollars')
gdp_plot.set_title('Yearly real GDP with constant 2010 prices')

plt.show()