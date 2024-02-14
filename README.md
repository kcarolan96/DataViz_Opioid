# DataViz_Opioid
Data Visualization Project:  Opioid transaction versus coal mining in Kentucky

**How to use**

• **DataVisualisation_CleaningNotebook.ipynb** contains a jupyter style notebook wit data exploration\
• **cleanedData.csv** Contains the cleaned data set to be used with DataVIsualisation_VisualisationScript.py\
• **DataVIsualisation_VisualisationScript.py** contains an executable script to create my interactive barchart

Below is an edited form of report written for Msc In Computing at Dublin City Universisty. This project achieved a mark of 95%

**Abstract**

Dopesick is a 2021 TV Series concerning the opioid crisis in America during the 2000s and its connection to the prescription medicine OxyContin. The series follows many characters in the state of Virginia. One storyline involved a young woman working in a coal mine who hurts her back and ends up addicted to opioids.

By using the generic analytical pipeline introduced in DCU course CA682i; this analysis looks  at the per capita drug transaction rates for the state of Kentucky between 2006 and 2019. This analysis aims to investigate whether there is a relationship between opioid sales and the presence of coal mines. The analysis is on Washington Post Data, US  Census and Population estimates, and Coalfield data for the state of Kentucky. By comparing the top and bottom 10 counties by transaction. The graph suggests that counties in the top 10 most likely have a coalmine, with the converse being true for the bottom ranked.This serves as a good starting point to perform a more detailed analytic project on whether the number of opioid sales could predict the presence of a coalmine or other primary sector work, however such analytic work is outside the scope of this work

**Data Sets**

The data gathered for analysis came from the drug enforcement administration data collated by The Washington Post (Steven Rich, 2023). Their interface allows you to select a state and download the raw data for that state. This was a zipped CSV file (arcos-ky-statewide-itemized.csv) which was 2.13GB in size with 7,222,079 rows. I originally looked at using the entire dataset. This was approximately 80gb in size, as such I did not have the computing power to analyse a dataset of this size. It did not fit  in ram and I did not have access to a cloud service that I could distribute this over.
Instead I took just Kentucky, chosen somewhat arbitrarily due to the fact that Kentucky is famous for having many coal mines.

Secondary data sources of this analysis were population metrics for the usa by county and whether a county has a coalmine.
There were 2 datasets coming from 2019: PEP Population Estimates and County Intercensal and Datasets: 2000-2010 (US Census Bureau, 2023) and  (US GOV, 2021).  These were collected by Querying www.census.gov website. Both datasets were USA wide and not restricted to Kentucky
The Coalmine data was taken by scraping the wikipedia page Coal_mining_in_Kentucky (Wikipedia, 2023) for the Eastern and Western coalfields using pandas html reading function. 

My data exhibits both aspects of volume and variety. Volume as the main dataset is 2.13gb’s of data ~7 million rows. This is too big to analyse using a spreadsheet application like Excel. Excel can only open 1,048,576 rows. Additionally, I combine data from 4 distinct data sources which demonstrates variety.


**Data Exploration, Processing, Cleaning and/or Integration**
During the processing phase, Python 3.12.0 in a Jupyter Notebook was used to perform the data cleaning and integration. 
Opioid Data (arcos-ky-statewide-itemized.csv)
Pandas library was used to read the CSV and store it as a dataframe. By checking the column names and first 5 rows, using dataframe.head(), two columns were identified as interesting to explore as part of the visualisation, ‘Buyer County’ and ‘Transaction Date’. From this, I created a new dataframe where each county had the total counts by county for each year. This involved the following steps :
1. Set “TRANSACTION_DATE” to a datetime stamp,
2. Getting just the year e.g. 2006-03-28 becomes 2006
3. Grouping the data frame by BUYER_COUNTY and Year, getting the size and setting it to Transaction count
4. Utilising the Pivot function of pandas to get a new dataframe which gets transaction counts by county for each year.\

Population Data\

Cleaning process for pop file 2000-2010: I got the error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 211963: invalid continuation byte. By examining this position in Notepad++ I was able to see non-utf-8 characters however this line was for new-mexico so I removed this.
Once both files were loaded to dataframes the following steps were performed.\
• Both data frames were filtered to only include Kentucky data.\
• County names were made uppercase and the words Kentucky, County and the whitespace were removed.This ensured a uniform representation of the county names\
• Column names were changed to contain just the year e.g 4/1/2010 Census population!!Population became 2010.\
• All Columns except Years 2006-2010 and County Names were removed \
• The data frames were merged by inner join on country names\
• Where years had both census and estimated populations, only census data was retained.\
• String values in certain years were cast to integers, as identified by commas in the .head() output.\

Coal mine Data

Coalmine data was processed by merging the 2 Wikipedia tables. I also prepared the County[8] column by removing the word county, whitespace, and converting it to uppercase.

Final Dataset - per_capita_df

• The final dataset was derived as part of a limited analysing phase. dividing the population data and drug data years columns in a for loop e.g. drugByYear_dF[year] / kentuckypop2000_2019_df2[year].  I then created a new column with Yes/No values by using a lambda function which compares the main dataset with the coalmine dataset, if they matched it was yes, if no match no./
• Missing data was identified for Roberston; there were no transactions in this county. However, according to Google,  the county does not have a pharmacy. This was set as 0 Finally, the new dataframe was saved to a CSV  “usecleanedData.csv”. This was so it could be used as a Python script but also so it could be used later as part of the preserving phase.

![Alt text](relative%20path/to/vizsketch.jpg?raw=true "Title")

