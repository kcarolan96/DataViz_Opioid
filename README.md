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

**Final Visualisation**

My final visualisation was built as part of the presenting phase,  similar in design to my sketched data. 
I created the final chart using the Plotly library in python making use of the graph_objects modules.
Originally I looked at displaying all counties, however this was very cluttered and hard to read. Therefore by using head and tail for each year I visualised the top 10 and bottom 10
Animation
I constructed an interactive  horizontal barchart. This chart allowed the user to play through the time period from 2006-2019, or to select a year using the slider functionality at the bottom.
In my sketch I thought I would use checkboxes to select the year. This did not look as clean as using the slider. I also experimented with a dropdown menu to select the year, however it was less obvious the years were changing when you pressed play. 
This allowed me to create interaction by creating a moving bar chart. My solution was adapted from the Plotly animations documentation: https://plotly.com/python/animations/  and https://www.youtube.com/watch?v=lZNNmaWkiMI by Charming Data
By assigning each year to a different frame it allowed each year to have its own “frame” which means you can go through them similar to a slideshow. The slider was  placed at the bottom where you can select a year manually, or a play button to automatically cycle through each frame. When you change the Year, the title of the Chart changes to reflect the year.


Styling
Colour
I chose the colour palette of orange and blue. I am a previous user of ggplot2 in R and took the shades of orange and blue from here. Orange and light-blue were chosen as they are  colour-blind friendly as derivatives of Red and Blue, which are colour- blind friendly(Jeffrey Shaffer, 2016) This means that the chart should be accessible to most people. If I had been trying to show republican vs democrat I might have used red and blue, however I find orange and blue easier to look at. They are also complementary colours due to photoreceptor cells in our eyes, meaning the contrast acts in a balancing way (Smithsonian Magazine, 2012). The orange represents having coal mine, the blue was no coal mine
Annotations
Originally the percentage values were shown on the x axis as ticks.  However because there were 20 values it meant not all were showing depending on window size. To address this I placed the values after the bar. This made it immediately clear what per capita rate was attached to which county.
Legend
This part was particularly tricky to get right, as because I was using graph objects, if i tried to create a legend directly, it gave a marker for each year i.e coal mine yes/no 20006-2019, this broke the entire plot.
To get around this I created an empty trace and overlaid on the existing graph. This then had the correct information as shown in the example  graph screenshot above. However, this was a flawed fix as it removed the interactivity that usually exists with a plotly legend. In General I would be able to select a legend object and toggle it on and off.
Other Styling Points
I removed the graph lines from the graph and removed the X and Y axis markers. This was an effort to reduce the visual noise in the graph. As the percentages were added as annotations, it was not necessary to have graph lines going from data points to X axis. The Play button and Pause buttons were padded to make sure they were not obstructing county names, I also added the special characters for pause and play beside, to decrease cognitive load when finding them.




**Conclusion**
The datasets, cleaned data, jupyter notebook and python script have been stored in google drive  folder as part of preserving phase.
The visualisation presented here suggests that having a coal mine in a county correlates with higher rates of drug transactions. I think it effectively tells this story by showing it across the years, the counties in the top 10 were  mostly orange, the bottom 10 were almost always blue. It would be interesting to take another State such as Virginia and perform the same analysis or to take another state with large scale dangerous physical labour such as forestry or farming
 It is important to note that I have only shown the top and bottom 10 counties. I have not included the ratio of how many counties have coal mines versus how many don’t. 
It is also important to note that this chart does not take into account if buyers were travelling between counties, if a county with a high transaction volume was adjacent to a coalmining county but did not have coal itself. The values I present should be taken as a proxy or estimate rather than concrete per capita rates.
The data gathering and integration phases could be improved for future work. It might be useful to build a visualisation by loading the data in batches, or storing the data in a relational database in the cloud so that one could create a heatmap across the united states, or select different counties and compare them.


If I wanted to improve  this visualisation it would be useful to be able to select the Top N, i.e include a user input box, or drop down which allowed you to pick top 5, 10,25,50  or all counties, however I was not able to get this to work.
In addition the legend I included was a hack as I could not get a legend to work when using multiple frames that did not break the transition. To achieve the legend I had to include a dummy frame and disable the legend for the actual graph. This means you could’t just select coal mine counties or non coal mine counties.
I also would like to include smoother transitions between the frames
This chart does not suggest that drug companies intentionally targeted these communities, however in conjunction with other evidence it could be useful visualisation to further this argument. 



**References**
1. Paige Moody Steven Rich. 2023. How deeply did prescription opioid Pills Flood Your County? see here. (September 2023). Retrieved November 8, 2023 from https://www.washingtonpost.com/investigations/interactive/2023/opioid-epidemic-pain-pills-sold-oxycodone-hydrocodone/ 
2. US Census Bureau. 2021. County intercensal datasets: 2000-2010. (December 2021). Retrieved November 8, 2023 from https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-counties.html 
3. US Census Bureau. 2023. County population totals: 2010-2019. (March 2023). Retrieved November 30, 2023 from https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html 
4. Wikipedia. 2023. Coal mining in Kentucky. (April 2023). Retrieved November 8, 2023 from https://en.wikipedia.org/wiki/Coal_mining_in_Kentucky 
5. Ann K. Emery. 2017. When to use horizontal bar charts vs. Vertical Column Charts. (January 2017). Retrieved November 30, 2023 from https://depictdatastudio.com/when-to-use-horizontal-bar-charts-vs-vertical-column-charts/ 
6. Amy Esselman. 2022. Horizontal versus Vertical Bar Chart. (March 2022). Retrieved November 6, 2023 from https://www.storytellingwithdata.com/blog/2022/1/21/which-bar-orientation-should-i-use 
7. Jeffrey Shaffer, COO and VP of Information Technology and Analytics. 2016. 5 tips on designing colorblind-friendly visualizations. (April 2016). Retrieved November 10, 2023 from https://www.tableau.com/blog/examining-data-viz-rules-dont-use-red-green-together 
8. Smithsonian Magazine. 2012. The Scientific Reason Complementary Colors Look Good together. (November 2012). Retrieved November 30, 2023 from https://www.smithsonianmag.com/smart-news/the-scientific-reason-complementary-colors-look-good-together-114030051/

   
**Coding References**
1. Pandas - http://pandas.pydata.org/
2. Plotly - https://plotly.com/python/
3. Plotly traces - https://plotly.com/python/creating-and-updating-figures/#adding-traces
4. Plotly Animations - https://plotly.com/python/animations/ 
5. Create Racing Bar Graph - Python Plotly  https://www.youtube.com/watch?v=lZNNmaWkiMI 
6. Matplotlib https://matplotlib.org/
7. Notepad++ https://notepad-plus-plus.org/
