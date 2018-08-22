
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
city = pd.read_csv(city_data_to_load)
ride = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
pyber = pd.merge(ride, city, on="city", how="outer")
# Display the data table for preview
pyber.head()


# ## Bubble Plot of Ride Sharing Data

# In[10]:


# Obtain the x and y coordinates for each of the three city types
pyber_type = pyber.set_index("type")

# take out all the urban city data
urban_pyber = pyber_type.loc["Urban", :]

# group all the different city
urban_pyber_city = urban_pyber.groupby(["city"])

# do calculation on total ride and average fare
urban_total_ride = urban_pyber_city["ride_id"].count()
urban_avg_fare = urban_pyber_city["fare"].mean()
urban_driver = urban_pyber_city["driver_count"].mean()

# take out all the suburban city data
suburban_pyber = pyber_type.loc["Suburban", :]

# group all the different city
suburban_pyber_city = suburban_pyber.groupby(["city"])

# do calculation on total ride and average fare
suburban_total_ride = suburban_pyber_city["ride_id"].count()
suburban_avg_fare = suburban_pyber_city["fare"].mean()
suburban_driver = suburban_pyber_city["driver_count"].mean()

# take out all the rural city data
rural_pyber = pyber_type.loc["Rural", :]

# group all the different city
rural_pyber_city = rural_pyber.groupby(["city"])

# do calculation on total ride and average fare
rural_total_ride = rural_pyber_city["ride_id"].count()
rural_avg_fare = rural_pyber_city["fare"].mean()
rural_driver = rural_pyber_city["driver_count"].mean()

# Build the scatter plots for each city types
# enlarge the scalar of the size of each data point by 10 times so it is easier to read the scatter plot
urban_p = plt.scatter(urban_total_ride, urban_avg_fare, s=urban_driver*10, facecolors="coral", edgecolors="black", alpha=0.75, linewidths=1.5, label="Urban")
suburban_p = plt.scatter(suburban_total_ride, suburban_avg_fare, s=suburban_driver*10, facecolors="deepskyblue", edgecolors="black", alpha=0.75, linewidths=1.5, label="Suburban")
rural_p = plt.scatter(rural_total_ride, rural_avg_fare, s=rural_driver*10, facecolors="gold", edgecolors="black", alpha=0.75, linewidths=1.5, label="Rural")

# Create a legend
plt.grid()
lgnd = plt.legend(handles=[urban_p, suburban_p, rural_p], scatterpoints=1, fontsize=10, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [50]
lgnd.legendHandles[1]._sizes = [50]
lgnd.legendHandles[2]._sizes = [50]

plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")

# Incorporate a text label regarding circle size
plt.text(50, 40, "Note:\nCircel size correlates with driver count per city")

# Save Figure
plt.savefig("Ride_Sharing_Data.png")


# In[3]:


# Show plot
plt.show()


# ## Total Fares by City Type

# In[4]:


# Calculate Type Percents

# Build Pie Chart

# Save Figure


# In[5]:


# Show Figure
plt.show()


# ## Total Rides by City Type

# In[6]:


# Calculate Ride Percents

# Build Pie Chart

# Save Figure


# In[7]:


# Show Figure
plt.show()


# ## Total Drivers by City Type

# In[8]:


# Calculate Driver Percents

# Build Pie Charts

# Save Figure


# In[9]:


# Show Figure
plt.show()

