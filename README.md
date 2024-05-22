# Project 2: HDB Resale Trends: Predicting Home Values for New and Expecting Families


### Goals

The number of unique first-timer family applicants has increased significantly from over 19,000 in 2018 to about 34,000 in 2021. [Source: hdb.gov.sg]

To assist clients who are in urgent need of a resale HDB near a preferred primary school.

As a team of data scientists with PropNex, our goal is to create a value-added product that our agents can bring to their clients - a data backed predictive model for family applicants to predict HDB resale values, based on their family-centric needs.

This heavily reduces the guess-work needed by our agents and improves the overall transaction experience for our clients.

### Dataset

|Feature|Type|Dataset|Description|
|---|---|---|---|
|pri_sch_tier_1|int64|hdb_pri_sch_clean.csv|Top one third of schools that are most over-subscribed|
|pri_sch_tier_2|int64|hdb_pri_sch_clean.csv|Second one third of schools that are most over-subscribed|
|dist_from_city_centre|float64|hdb_pri_sch_clean.csv|Distance from CBD (lat 1.2831° N and lon 103.8511° E, Raffles Place|
|dist_to_3_psch_avg|float64|hdb_pri_sch_clean.csv|average distance from property to 3 nearest primary schools|
|transact_date|object|hdb_pri_sch_clean.csv|Date of resale transaction|
|floor_area_sqm|float64|hdb_pri_sch_clean.csv|Floor area of resale HDB in square metres|
|resale_price|float64|hdb_pri_sch_clean.csv|Resale price of resale HDB in Singapore dollars|
|storey|int64|hdb_pri_sch_clean.csv|Median value of storey range|
|age|int64|hdb_pri_sch_clean.csv|Age of resale flat|
|lat|float64|hdb_pri_sch_clean.csv|Latitude based on postal code|
|lon|float64|hdb_pri_sch_clean.csv|Longitude based on postal code|
|mall_dist|float64|hdb_pri_sch_clean.csv|Distance from flat to nearest mall|
|hawker_dist|float64|hdb_pri_sch_clean.csv|Distance from flat to nearest hawker|
|mrt_dist|float64|hdb_pri_sch_clean.csv|Distance from flat to nearest mrt station|
|bus_interchange|int64|hdb_pri_sch_clean.csv|boolean value if the nearest MRT station is also a bus interchange|
|bus_stop_dist|float64|hdb_pri_sch_clean.csv|distance (in metres) to the nearest bus stop|
|pri_sch|object|hdb_pri_sch_clean.csv|name of the nearest primary school|
|pri_sch_lat|float64|hdb_pri_sch_clean.csv|latitude (in decimal degrees) of the the nearest primary school|
|pri_sch_lon|float64|hdb_pri_sch_clean.csv|longitude (in decimal degrees) of the the nearest primary school|
|urban_prox_x_age|float64|hdb_pri_sch_clean.csv|Product of dist_from_city_centre and age|
|years_left|int64|hdb_pri_sch_clean.csv|Total lease (99) minus age|
|age_x_floor_area|float64|hdb_pri_sch_clean.csv|product of age & floor_area_sqm|
|age_x_storey|int64|hdb_pri_sch_clean.csv|product of age & storey|
|amen_dist|float64|hdb_pri_sch_clean.csv|mean of distance to closet mall, bus-stop, hawker and mrt|

The dataset can be found [here](../datasets/hdb_pri_sch_clean.csv)

    
##### Conclusion

Based on the **analysis** we've conducted of HDB Resale Price & Primary School Ballot data, we've observed that there are instances where guess work can have inaccuracies, in which a data-backed model can aim to reduce:
1. Out of all features, floor area has the strongest correlation with resale price, followed by distance to CBD, storey and age.
    * A deep dive into floor area however suggests that the price variance can be very high, especially for 4 and 5 room flats which offers affordability to budget conscious buyers who prioritise a larger home space
    * While number of rooms mostly increase with floor area, there are outliers of 3 room HDB units that exceed 150sqm. Despite the age, the last transaction price is still of the higher end
2. Price decreases as age increases, however a closer look shows that after 20 years price can increase gradually
3. Mature estates such as Bedok, Ang Mo Kio and Geylang also offer affordable housing options as compared to non-mature estates
    * These areas are also experiencing urban redevelopment to improve their accessibility

**Modelling**
<br> Based on our evaluation, our R^2 score comparison between the 3 regression models showed that a L2 regularization penalty that reduces the effect of multi-collinearity optimises our model the most. As there were features included in the model that could have been collinear (flat type vs floor area, distance to CBD vs town), in comparison to our R^2 score on L1 regularization that potentially overpenalises certain features, ridge was the best model to go with. 

Most importantly, our model focuses on helping families 
1. Get their kids to their desired schools
2. Convenience to work areas

This suggests that the distance to CBD feature, for instance, has to remain a strong feature in the model. 

**Predictive pricing**
<br>The predictor model will improve the overall transaction experience for PropNex clients by:
1. greatly reducing the learning curve for new property agents 
2. avoid misestimation of HDB prices by agents
3. enhance efficiency of buyer-seller price negotiations
10:54
##### Recommendations

As more transaction data is collected over time, the model will be trained to be even more accurate. In the meantime, the model is a working prototype whereby enhancement features are planned for:

**New features to be included**
* Renovation status
* Floor level
* View quality
* Amenities
* Primary schools within 2KM radius

**External data integration**
* Current market trends
* Interest rates/Consumer Price Index
* Government policy changes

**UI Enhancements**
* Map feature to select town
* Autofill parameters
* Town selection dropdown
* Charts to show predicted vs historical prices
* Save and compare predictions
