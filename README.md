# GAReport
A simple way to call the Google Analytics (v4) API

##  Why

Looking around the web, one can find a bunch of code based on Google's initial 2016 sample for v4 of the Google Analytics API.
While it all works, pulling multiple reports or changing things on the fly is a pain.
A high-level abstraction makes the process easier.
Getting the results in a Pandas dataframe makes running calculations, creating visualizations or even exporting to a database a breeze.

So, borrowing the excellent code base from [RitwikGA/GoogleAnalytics-Pandas-Sheet](https://github.com/RitwikGA/GoogleAnalytics-Pandas-Sheet/blob/master/gaExport.py "GoogleAnalytics-Pandas-Sheet/gaExport.py at master · RitwikGA/GoogleAnalytics-Pandas-Sheet · GitHub") this project wraps it into a class, adds a class for API calls and human readable labels.

##  Getting Started

To get started with this code, follow the instructions at [Hello Analytics Reporting API v4; Python quickstart for service accounts](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py "Hello Analytics Reporting API v4; Python quickstart for service accounts").
Especially, steps
1. [Enable the API](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py#1_enable_the_api "Hello Analytics Reporting API v4; Python quickstart for service accounts")

2. [Install the client library](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py#2_install_the_client_library "Hello Analytics Reporting API v4; Python quickstart for service accounts")

3. Setup the code
	1. Copy or download the following source code to where it will run.
	1. Move the previously downloaded client_secrets.json to the same directory as the code.
	1. In `GAReport` replace the value of the `KEY_FILE_LOCATION` with the appropriate path to the downloaded client_secrets.json.
	1. In `GAPullTest.py`  replace the value of `VIEW_ID`. You can use the Account Explorer to find a View ID.


##  Create a Report

`GAPullTest.py` is a sample report but this code can easily run from a Jupyter notebook.

1. Start by importing the GAReport class

```python
from GAReport import GAReport
```

2. Set the dimension(s). These are the first column(s) of the returned table. 
	(Example: Dimension is Page.
	The metrics, such as Pageviews, then display for each page.) 

```python
DIMENSIONS = ["Page", ]
```

3. Set the metric(s) (i.e. what you want to know about the dimension(s)).

```python
METRICS = ["Pageviews", "Unique Pageviews", "Avg. Time on Page", "Entrances", "Bounce Rate", "% Exit", "Page Value"]
```

4. Create the report.
	Access the report via `GAReport.df`.

```python
report = GAReport(startdate="yesterday", 
	enddate="yesterday", 
	viewID=VIEW_ID, 
	dimensions=DIMENSIONS, 
	metrics=METRICS, 
	filters=FILTERS)
print(report.df.head(3))
```

The output:

|     | Page                                                                                                                  | Pageviews | Unique Pageviews | Avg. Time on Page | Entrances | Bounce Rate |  % Exit | Page Value |
| ---:|:--------------------------------------------------------------------------------------------------------------------- | ---------:| ----------------:| -----------------:| ---------:| -----------:| -------:| ----------:|
|   0 | /news                                                                                                  |        25 |               23 |             11.05 |         0 |           0 |      20 |    33.6957 |
|   1 | /news/2021/new-food-services-partner                                                            |        15 |               15 |           50.3077 |         1 |         100 | 13.3333 |          0 |
|   2 | /news/2021/what-to-expect-for-fall-2021                                                                |        88 |               67 |           76.6923 |         5 |         100 | 26.1364 |    11.5672 |
