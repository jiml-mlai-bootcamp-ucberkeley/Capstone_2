# Capstone 2

## House Prices - Basic Regression Techniques

## Context
### Dataset source : https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset
### According to the source of the dataset provided:
#### This dataset contains Real Estate listings in the US broken by State and zip code.

## Business Understanding
### Objective
#### The objective is to find a model that will predict house prices.  This goal will change as the characteristics of the data provided are explored.

#### Many of the features in the dataset provided for this project are described in the "Data Understanding".  We can leverage and tweak them to find the best model.  The initial focus will be to build a codebase that can be leveraged with modifications afterwards.

## Data Understanding

### Data Descriptions
#### Here is the preliminary info about our dataset.
    RangeIndex: 1401066 entries, 0 to 1401065
    Data columns (total 10 columns):
    #   Column          Non-Null Count    Dtype  
    ---  ------          --------------    -----  
    0   status          1401066 non-null  object 
    1   bed             1184538 non-null  float64
    2   bath            1206853 non-null  float64
    3   acre_lot        1043599 non-null  float64
    4   city            1400875 non-null  object 
    5   state           1401066 non-null  object 
    6   zip_code        1400587 non-null  float64
    7   house_size      950954 non-null   float64
    8   prev_sold_date  714773 non-null   object 
    9   price           1400958 non-null  float64
    dtypes: float64(6), object(4)
    memory usage: 106.9+ MB

#### Here is the a list of descriptions for the features in the dataset.
    status (Housing status - a. ready for sale or b. ready to build)
    bed (# of beds)
    bath (# of bathrooms)
    acre_lot (Property / Land size in acres)
    city (city name)
    state (state name)
    zip_code (postal code of the area)
    house_size (house area/size/living space in square feet)
    prev_sold_date (Previously sold date)
    price (Housing price, it is either the current listing price or recently sold price if the house is sold recently)

#### For the purpose of this project a macro level analysis will be conducted at the state level for Connecticut, Massachusetts, NJ, NY, and Pennsylvania.
#### The initial count of houses in each state indicate a sufficient number to provide an adequate range.
#### However after removing duplicate entries this may prove to be a bigger challenge when we try micro level analysis.  But we will continue with this approach for Capstone 2.
<table>
<tr>
<th>Before removing duplicates</th>
<th>After removing duplicates</th>
</tr>
<tr>
<td>
state              Count<br/>
<b>Connecticut        98816</b><br/>
Delaware            2135<br/>
Georgia               50<br/>
Louisiana              3<br/>
Maine              36650<br/>
<b>Massachusetts     177170</b><br/>
New Hampshire      51394<br/>
<b>New Jersey        256551</b><br/>
<b>New York          653061</b><br/>
<b>Pennsylvania       20060</b><br/>
Puerto Rico        24679<br/>
Rhode Island       29610<br/>
South Carolina        25<br/>
Tennessee             20<br/>
Vermont            48230<br/>
Virgin Islands      2573<br/>
Virginia              31<br/>
West Virginia          5<br/>
Wyoming                3<br/>
</td>
<td>
state             Count<br/>
<b>Connecticut       13753</b><br/>
Delaware           1290<br/>
Georgia               5<br/>
Louisiana             1<br/>
Maine              4938<br/>
<b>Massachusetts     10051</b><br/>
New Hampshire      3431<br/>
<b>New Jersey        32601</b><br/>
<b>New York          67159</b><br/>
<b>Pennsylvania       9549</b><br/>
Puerto Rico        2645<br/>
Rhode Island       3332<br/>
South Carolina        1<br/>
Tennessee             1<br/>
Vermont            2544<br/>
Virgin Islands      730<br/>
Virginia              7<br/>
West Virginia         1<br/>
Wyoming               1<br/>
</td>
</tr>
</table>

#### Improving the Model

<ul>
<li>The range of values for the prev_sold_date feature is too wide and too far into the past for practical purposes.
<ul><ol>The rows for only the past few years will be used, generally after 2015.</ol></ul></li>
<li>The price feature also appears to be too wide and could use some attention.
    <ul>
        <ol>Whiskers and Zscore can help identify outliers.  After reviewing the results, Zscore appears to be the better option.
        </ol>
    </ul>
</li>
<li>Missing values for the bed, bath, acre_lot, and house_size have been replaced with mode().</li>
<li>Rows with other missing values will removed.</li>
<li>Normalizing the data was explored in this project.
    <ul>
        <ol>For consistency sake, all of the models we run using normlized data.</ol>
        <ol>Some of the models and feature selection techniques did not handle this well.</ol>
        <ol>Further exploration of this issue should prove to be intersting.</ol>
    </ul>
</li>
</ul>

#### Improving the Model

<ul>
<li>The range of values for the prev_sold_date feature is too wide and too far into the past for practical purposes.
<ul><ol>The rows for only the past few years will be used, generally after 2015.</ol></ul></li>
<li>The price feature also appears to be too wide and could use some attention.
<ul><ol>Whiskers and Zscore can help identify outliers.  After reviewing the results, Zscore appears to be the beter option.
</ol></ul></li>
<li>Missing values for the bed, bath, acre_lot, and house_size have been replaced with mode().</li>
<li>Rows with other missing values will removed.</li>
<li>Normalizing the data values will be explored for Capstone 2.</li>
</ul>

#### Here are samples of graphs for NJ.
#### House prices before ZScore
<img src="images/nj-prices-before-zscore.png">

#### House prices after ZScore
<img src="images/nj-prices-after-zscore.png">


#### Macro analysis (state level ) is provided in Notebooks that contain "Major" in the file name.
##### The five states selected worked well with the macro level analysis.
##### There was sufficient data to generate acceptable predictions and results.
##### Here is a sample of macro level analysis from NJ.
<table border="1">
  <thead>
    <tr>
      <th>model</th>
      <th>explained variance score</th>
      <th>mae score</th>
      <th>mse score</th>
      <th>r2 score</th>
      <th>mean fit time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ada Boost</th>
      <td>0.458110765</td>
      <td>0.598454</td>
      <td>0.632462</td>
      <td>0.361424</td>
      <td>0.074927</td>
    </tr>
    <tr>
      <th>Gradient Boosting</th>
      <td>0.610032567</td>
      <td>0.374979</td>
      <td>0.386768</td>
      <td>0.609493</td>
      <td>0.338895</td>
    </tr>
    <tr>
      <th>Hist Gradient Boosting</th>
      <td>0.696329826</td>
      <td>0.322916</td>
      <td>0.301281</td>
      <td>0.695806</td>
      <td>0.496136</td>
    </tr>
    <tr>
      <th>Random Forest</th>
      <td>0.639962410</td>
      <td>0.343331</td>
      <td>0.357106</td>
      <td>0.639442</td>
      <td>1.921009</td>
    </tr>
  </tbody>
</table>



#### File names with "Minor" provide micro level (zip code level) analysis for the location with the most houses.
##### This approach worked well for NJ and NY, but not Connecticut, Massachusetts, and Pennsylvania.
##### There weren't sufficient number of houses in the latter 3 states to generate acceptable predictions and results.
##### Here is a sample of micro level analysis from NY.
<table border="1">
  <thead>
    <tr>
      <th>model</th>
      <th>explained variance score</th>
      <th>mae score</th>
      <th>mse score</th>
      <th>r2 score</th>
      <th>mean fit time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ada Boost</th>
      <td>0.749018406</td>
      <td>0.361710</td>
      <td>0.233654</td>
      <td>0.726146</td>
      <td>0.003254</td>
    </tr>
    <tr>
      <th>Gradient Boosting</th>
      <td>0.794410909</td>
      <td>0.316163</td>
      <td>0.175412</td>
      <td>0.794408</td>
      <td>0.022038</td>
    </tr>
    <tr>
      <th>Hist Gradient Boosting</th>
      <td>0.721259049</td>
      <td>0.344220</td>
      <td>0.237900</td>
      <td>0.721169</td>
      <td>0.073810</td>
    </tr>
    <tr>
      <th>Random Forest</th>
      <td>0.794098279</td>
      <td>0.322214</td>
      <td>0.175852</td>
      <td>0.793892</td>
      <td>0.068906</td>
    </tr>
  </tbody>
</table>


## Model Comparisons
#### Different models were used with various feature selectors.
<table>
<tr><th>Models</th><th>Feature Selectors</th></tr>
<tr><td>Ada Boost AdaBoostRegressor</td><td></td></tr>
<tr><td>GradientBoostingRegressor</td><td></td></tr>
<tr><td>HistGradientBoostingRegressor</td><td></td></tr>
<tr><td>RandomForestRegressor</td><td></td></tr>
<tr><td>Decision Tree</td><td>Best Parameters</td></tr>
<tr><td></td><td>Recursive Feature Elimination</td></tr>
<tr><td></td><td>Sequential Feature Selector</td></tr>
<tr><td>K-Nearest Neighbors</td><td>Best Parameters</td></tr>
<tr><td></td><td>Sequential Feature Selector</td></tr>
<tr><td>Lasso</td><td>Best Parameters</td></tr>
<tr><td></td><td>Select From Model</td></tr>
<tr><td></td><td>Recursive Feature Elimination</td></tr>
<tr><td></td><td>Sequential Feature Selector</td></tr>
<tr><td>Linear and Polynomial</td><td>Best Parameters</td></tr>
<tr><td></td><td>Select From Model</td></tr>
<tr><td></td><td>Recursive Feature Elimination</td></tr>
<tr><td></td><td>Sequential Feature Selector</td></tr>
<tr><td>Ridge</td><td>Best Parameters</td></tr>
<tr><td></td><td>Select From Model</td></tr>
<tr><td></td><td>Recursive Feature Elimination</td></tr>
<tr><td></td><td>Sequential Feature Selector</td></tr>
</table>

#### In the majority of cases, using R2 score Gradient Boosting and Hist Gradient Boosting performed the best.
#### Other models and feature selections perormed well and could probably be tweaked to outperform the Boosting models.


## Insights
#### As initially described, working with this dataset is challenging.
#### The provider appears to be appending updates to the existing file instead of incremental updates.
#### The data for some states works well at a macro level, but insufficient for micro level analysis.
#### The latitude and longitude values that were added gave better results than using zip code or county.
#### A data source that provides the Latitude and Longitude for zip codes in the US was used for this purpose.
#### KMeans helped to cluster the houses and group them into geographic locations.
##### US zip codes with lat and long  https://www.kaggle.com/datasets/joeleichter/us-zip-codes-with-lat-and-long

## Next steps and recommendations
#### Pricing houses is very location specific.  Geocoding the data was helpful, but the general coordinates were almost equivalent to zip code.
#### The surrounding areas around each cluster can vary in the degree of desirability for home buyers.
#### The dataset used here does not provide specific addresses which would be needed for optimal micro level analysis.
#### Also, the other features bed, bath, acre lot, and house size can significantly impact the price.
#### Age of the house is missing from the data.  That is also very important.
#### I would also recommend additional techniques for data cleansing.  Outlier detection could be better too.

## Link to notebook
### https://github.com/jiml-mlai-bootcamp-ucberkeley/Capstone_2
