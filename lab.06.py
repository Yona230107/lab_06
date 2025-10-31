##part 3
#Question 1.
# By looking at the World demographic Indicators Extract we can ask and answer multiple question. 
#a. We can see relationship between the Internet use and the region. 
#b. We can explore the relationship between the region, the life expectancy of female and life expectancy of male. 
#c. we can explore the correlation between the region, the life expantancy of female and male, and the greenhouse gas emissions. 

#question 2
import pandas as pd 
import seaborn as sns
data=pd.read_csv("wdi_wide.csv")

# This code simply imports the modules we will be using for this lab and the dataset we will be working with.

#question 3
data["Physicians"].info()
data["Population"].info()
# This function gives us information about the data set, for instance the size of the dataset the datatype etc. 
# Each row represents a country 
# The 2 lines above allow us to answer the question: There are 207 non null in physicians so 10 null. Then in population there are zero null. 

#question 4
a=data.nunique()
print("This is the nunique")
print(a)
#This function simply counts how many different unique values are in a column.

#Question 5
b=data.describe()
print("This is describe")
print(b)
# This function describes more the data, for example, it gives the mean, standard deviation min and max of the GNI.

#Question #6
data["GNI per capita"] = (data["GNI"] / data ["Population"]).round(2)
print(data["GNI per capita"])
# This code adds a new collum and rounds it to 2 decimal places. 
#In order to find the GNI per capita, we simply divide the value of the GNI by the population. 

#Question# 7a 
print("This is the 7a")
print(data["Region"].value_counts())
#This code counts how many times each value appears in a column.
# Since each row represents a country, this code counts how many times each region are present, therefore it counts the amount countries are in each region. 

#Question 7b 
print("This is 7b")
print(data["High Income Economy"].value_counts())
#It will count how many rows have each value in the column "High Income Economy". Thus counting the amount of countries that have high economy.

#Question#8 
print("This is 8")
cross_tab_results = pd.crosstab(data["Region"],data["High Income Economy"])
print(cross_tab_results)
# This function allows to us to undertand the relationship betwen the income and the region, by simply crossing the rows. The output gives the amount of countries in ecah region with high income economy. 

# Question 9 

total_countries=0
filtered_data=data[data["Life expectancy, female"]>80]
for i in filtered_data["Country Name"]:
    print(i)
    total_countries+=1
print("the total amount of countries with female life expectancy higher than 80 is", total_countries)   
# The codes uses a loop and filtered data to make a list of the countries where women could expect to live for more then 80 yrs.   
        
         

## Part 4 
# Question 1.
# a) The relationship between GNI per capita and Female life expectancy 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female"
)
#b) The relationship between GNI per capita and male life expectancy 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male"
)
  

#Question 2
# a) Female
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region"
)
# This is the plot comparing GN1 per capita, female expectancy and the country. 
#b) Male 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region"
   
)
#This is the plot comparing GN1 per capita, male expectancy and the country.

#Question 3
#a) Female
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
    errorbar="sd",
    kind="line"
)
# This plot simply takes the plot a from question #2 and and turns them into lines by the "kind=line" statement and also adds errorbars having standard deviation as a value.
#b)Male
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    errorbar="sd",
    kind="line"
)

# Question#4
#a) Female
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
   
)
#b) Male 
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region"
)
#This plot, simply tranform the plot of the previous question in a linear regression  by using the lmplot funtion.

# Question#5
#list of 5 questions:
# 1. Is there a connection between life expectancy of female and male and the subregion they live in, per region ?
# 2. Is there a connection between life expectancy of female and male and the greehouse gas emmission,per region?
# 3. IS there a connection between life expectancy of female and male and the internet use, per region?
# 4. Is there a connection between life expectancy of male and female and the amount of physcians, per region?
# 5. Is there a connection between the life expectancy of female and male and the international tourisim, per regoin. 

#Answer to question 5
 
# 1. 
# a) Female
sns.relplot(
    data=data,
    x="Subregion",
    y="Life expectancy, female",
    col="Region"
)

# b) Male
sns.relplot(
    data=data,
    x="Subregion",
    y="Life expectancy, male",
    col="Region"
   
)
#This code makes separate scatter plots for each region to compare female and male life expectancy across different subregions.


# 2. 
# a) Female 
sns.relplot(
    data=data,
    y="Life expectancy, female", 
    x="Greenhouse gas emissions",
    col="Region"
)
# This code creates separate scatter plots for each region to show the relationship between female life expectancy and greenhouse gas emissions.
#b) Male
sns.relplot(
    data=data,
    y="Life expectancy, male", 
    x="Greenhouse gas emissions",
    col="Region"
)
# This code creates separate scatter plots for each region to show the relationship between male life expectancy and greenhouse gas emissions.


#3 
#a) female 
sns.relplot(
    data=data, 
    x="Internet use", 
    y="Life expectancy, female", 
    col="Region"
)
#b)
sns.relplot(
    data=data, 
    x="Internet use", 
    y="Life expectancy, male", 
    col="Region"
)
#This code creates separate scatter plots for each region to show the relationship between female  and male life expectancy and the internet use.
#a) female 
sns.relplot(
    data=data,
    x="Physicians",
    y="Life expectancy, female",   
   col ="Region",
)
#This code creates separate scatter plots for each region to show the relationship between female life expectancy and the amount of physicans.
#b) Male 
sns.relplot(
    data=data,
    x="Physicians",
    y="Life expectancy, male",   
   col ="Region",
)
#This code creates separate scatter plots for each region to show the relationship between male life expectancy and the amount of physicans.


#5. 
# a) Female
sns.relplot(
    data=data,
    y="Life expectancy, female",
    x="International tourism",
    col="Region"
)
#b) Male
sns.relplot(
    data=data,
    y="Life expectancy, male",
    x="International tourism",
    col="Region"
)
# This code creates separate scatter plots for each region to show how female  and male life expectancy relates to international tourism.

# Question 6

#a.   

data["Emissions per capita"] = (data["Greenhouse gas emissions"] / data ["Population"]) 
print(data["Emissions per capita"]) 

sns.relplot(
    data=data, 
    y="Emissions per capita", 
    x="Internet use",
)
# In this code, we first create a new column for emissions per capita. Then, we use this new column to help show the relationship between  emissions per capita, and internet use.

#b.

filtered_data = data[data["Emissions per capita"] > 0.03]
print("Hight emmisions Country are ",filtered_data[["Country Name","Emissions per capita"]])
# This code filters the dataset to only include countries with high emissions per capita (greater than 0.03), and then prints the names of those countries and the value of their emission. 

    
#c 

data["High_Emissions"] = data["Emissions per capita"] > 0.03
print(data["High_Emissions"])
sns.relplot(
    data=data,
    y="High_Emissions",
    x="Internet use",
   hue="Region"
   
   
   
)
#This code creates a new column to show which countries have high emissions and then makes a scatter plot comparing high-emission and low-emission countries in terms of internet use, while also showing their regions with different colors.
 
#d 

print("Do all high income economies have high emmission")
results=pd.crosstab(data["High Income Economy"], data["High_Emissions"])
print(results)
# This code first print a statement for us to better spot the output in the consol. 
# Then we used the function crosstab simply crooses the rows and see the amount that do have high income economy and high emission. 





