#!/usr/bin/env python3

from GAReport import GAReport

VIEW_ID = 'PutViewIDHere'

DIMENSIONS = ["Page", ]
METRICS = ["Pageviews", "Unique Pageviews", "Avg. Time on Page", "Entrances", "Bounce Rate", "% Exit", "Page Value"]
	# Use these instructions for creating single and multiple filters: https://developers.google.com/analytics/devguides/reporting/core/v3/reference#filters
FILTERS= "ga:pagePath=~news" 

report = GAReport(startdate="yesterday", enddate="yesterday", viewID=VIEW_ID, dimensions=DIMENSIONS, metrics=METRICS, filters=FILTERS)
print(report.df.head(3))