#!/usr/bin/env python3
# A class to set up Google Analytics API v4 queries and create Pandas dataframes

import pandas as pd
# import pygsheets
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from DimensionsAndMetrics import DimensionsAndMetrics

KEY_FILE_LOCATION = 'PutAPIKeyFileHere.json'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

class GAReport():
	"""docstring for GAReport"""
	def __init__(self, startdate, enddate, viewID, dimensions, metrics, filters):
		super(GAReport, self).__init__()
		self.VIEW_ID = viewID		
		self.startdate = startdate
		self.enddate = enddate
		
		# For the full list of dimensions & metrics, check https://developers.google.com/analytics/devguides/reporting/core/dimsmets
		columns = DimensionsAndMetrics()
		self.columnids = columns.ids
		self.columnnames = columns.names
		
		self.DIMENSIONS = self.setColumnIDs(dimensions)
		self.METRICS = self.setColumnIDs(metrics)
		self.FILTERS = filters
		
		self.analytics = self.initialize_analyticsreporting()
		response = self.get_report(self.analytics)
		self.df = self.convert_to_dataframe(response)
		self.setColumnNames()


	def initialize_analyticsreporting(self):
		credentials = ServiceAccountCredentials.from_json_keyfile_name(
			KEY_FILE_LOCATION, SCOPES)

		# Build the service object.
		analytics = build('analyticsreporting', 'v4', credentials=credentials)
		
		return analytics


	def get_report(self, analytics):
		return analytics.reports().batchGet(
			body={
				'reportRequests': [
				{
					'viewId': self.VIEW_ID,
					'dateRanges': [{'startDate': self.startdate, 'endDate': self.enddate}],
					'metrics': [{'expression':i} for i in self.METRICS],
					'dimensions': [{'name':j} for j in self.DIMENSIONS],
					"filtersExpression":self.FILTERS, 
				}]
			}
		).execute()


	def convert_to_dataframe(self, response):
	 
		for report in response.get('reports', []):
			columnHeader = report.get('columnHeader', {})
			dimensionHeaders = columnHeader.get('dimensions', [])
			metricHeaders = [i.get('name',{}) for i in columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])]
			finalRows = []

		for row in report.get('data', {}).get('rows', []):
			dimensions = row.get('dimensions', [])
			metrics = row.get('metrics', [])[0].get('values', {})
			rowObject = {}

			for header, dimension in zip(dimensionHeaders, dimensions):
				rowObject[header] = dimension
				
			for metricHeader, metric in zip(metricHeaders, metrics):
				rowObject[metricHeader] = metric

			finalRows.append(rowObject)
		
		
		dataFrameFormat = pd.DataFrame(finalRows)	
		return dataFrameFormat	


	def setColumnNames(self):
		"""docstring for setColumnNames"""
		keys = self.df.keys()
		for key in keys:
			self.df.rename(columns={key : self.columnids[key]}, inplace=True)


	def setColumnIDs(self, keynamess):
		"""docstring for setColumnIDs"""
		keyids = []
		for key in keynamess:
			keyids.append(self.columnnames[key])
		return keyids


	def export_to_sheets(self):
		 gc = pygsheets.authorize(service_file='client_secrets.json')
		 sht = gc.open_by_key(self.SHEET_ID)
		 wks = sht.worksheet_by_title('Sheet1')
		 wks.set_dataframe(self.df,'A1')

