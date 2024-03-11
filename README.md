<h1> Data Science Capstone Project IBM - Space X Falcon 9 landing predictions </h1>


The commercial space industry has become more accessible with companies like SpaceX offering cost-effective launches. SpaceX's Falcon 9 launch costs $62 million, significantly cheaper than competitors at $165 million. This cost-effectiveness is due to reusability, notably with the first stage of Falcon 9 rockets. However, there are instances of unsuccessful landings, prompting the need for accurate prediction of first stage reusability. As part of Space Y, a new rocket company competing with SpaceX, our task is to determine launch prices and predict first stage reusability using machine learning and public data.

### Objective###
SpaceX's cost-effective launches, notably with the Falcon 9 rocket, have revolutionized the commercial space industry. In response, Space Y seeks to compete by predicting first-stage reusability using machine learning and public data. Our objective was to identify factors influencing rocket landing success, assess feature contributions to success rates, and determine the most effective prediction algorithm.

### Questions We Want To Answer###
* What factors determine the success of a rocket landing?
* How do various features contribute to the success rate of rocket landings?
* Which algorithm is most effective for predicting the success of rocket landings?

### Methodology Approach ###
We utilized SpaceX REST API and web scraping from Wikipedia, performed standardized, filtered, and encoded data for analysis and machine learning. Employed various Exploratory Data Analysis (EDA) techniques such as scatter plots, bar graphs, and SQL queries to analyze relationships and gain insights. Utilized Folium and Plotly Dash for interactive visualizations and dashboards. Implemented classification models and grid search for algorithm selection and hyperparameter tuning.

* Data collected from Space X API 
* Additional information collected through Web scraping [Link here](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2010%E2%80%932019)). 
* Data Wrangling and processing
* Exploratory analysis using SQL magic and Python visualization tools.
* Data analytics using Folium Interactive maps and Plotly Dshboards
* Predictive analysis using Machine Learning Classification algorithms.
  
### Key Outcomes ###
Identified various factors contributing to rocket landing success, including booster version, orbit type, payload weight, launch site, and landing type. Orbits like ES-L1, GEO, HEO, SSO, and VLEO exhibit high success rates, while lower-weighted payloads tend to perform better. Drone Ship considered is observed to be the most used and successful landing type landed among all.
Launch sites with larger flight volumes show higher success rates. Booster versions like FT, B4, and B5 dominate successful launches. Kennedy Space Center Launch Complex has the highest success rate of launches.  Determined Decision Tree Classifier as the most effective for predicting rocket landing success.

### Recommendation ###

These findings provide valuable insights for optimizing rocket launch operations and improving success rates in the commercial space industry. Space Y should prioritize launching payloads into orbits with higher success rates, strategically select launch sites based on safety and operational efficiency, carefully plan payload distribution, and optimize booster version selection. Leveraging machine learning models like Decision Trees can aid in predictive analysis and informed decision-making for maximizing success rates.

### Dependencies ###
* Data collection Libraries
    * Requests
    * Beasutiful Soup
* Data Wrangling and processing Libraries
    * Pandas
    * Numpy
    * SQLAlchemy
* Visualization Libraries
    * Matplotlib
    * Seaborn
    * Folium
    * Plotly
    * Dash
* Machine Learning Libraries
    * Scikit Learn

### Deliverables ###
* Comprehensive businees report in form of a power point presentation. [Link here]([https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2010%E2%80%932019](https://github.com/NimraZeeshan/Capstone-Project-Falcon-9-Spaace-X/blob/main/Week%205/ds-capstone-final%20(11-03-24).pdf))) 
* Jupyter notebooks containing codes and results [Link here]([https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2010%E2%80%932019](https://github.com/NimraZeeshan/Capstone-Project-Falcon-9-Spaace-X/blob/main/Week%205/ds-capstone-final%20(11-03-24).pdf](https://github.com/NimraZeeshan/Capstone-Project-Falcon-9-Spaace-X/tree/main)https://github.com/NimraZeeshan/Capstone-Project-Falcon-9-Spaace-X/tree/main))) 
