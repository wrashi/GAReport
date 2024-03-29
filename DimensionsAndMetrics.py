#!/usr/bin/env python3
# Data from https://www.googleapis.com/analytics/v3/metadata/ga/columns

data = [
	 {
		"id": "ga:userType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "User Type",
		"description": "A boolean, either New Visitor or Returning Visitor, indicating if the users are new or returning.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitorType",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:userType",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "DEPRECATED",
		"uiName": "User Type",
		"description": "A boolean, either New Visitor or Returning Visitor, indicating if the users are new or returning.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionCount",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "Count of Sessions",
		"description": "The session index for a user. Each session from a unique user will get its own incremental index starting from 1 for the first session. Subsequent sessions do not change previous session indices. For example, if a user has 4 sessions to the website, sessionCount for that user will have 4 distinct values of '1' through '4'.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitCount",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:sessionCount",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "DEPRECATED",
		"uiName": "Count of Sessions",
		"description": "The session index for a user. Each session from a unique user will get its own incremental index starting from 1 for the first session. Subsequent sessions do not change previous session indices. For example, if a user has 4 sessions to the website, sessionCount for that user will have 4 distinct values of '1' through '4'.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:daysSinceLastSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "Days Since Last Session",
		"description": "The number of days elapsed since users last visited the property, used to calculate user loyalty.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userDefinedValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "User Defined Value",
		"description": "The value provided when defining custom user segments for the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userBucket",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "User Bucket",
		"description": "Randomly assigned users tag to allow A/B testing and splitting of remarketing lists. Ranges from 1-100.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:users",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "Users",
		"description": "The total number of users for the requested time period.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitors",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:users",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "DEPRECATED",
		"uiName": "Users",
		"description": "The total number of users for the requested time period.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:newUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "New Users",
		"description": "The number of sessions marked as a user's first sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:newVisits",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:newUsers",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "DEPRECATED",
		"uiName": "New Users",
		"description": "The number of sessions marked as a user's first sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:percentNewSessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "% New Sessions",
		"description": "The percentage of sessions by users who had never visited the property before.",
		"calculation": "ga:newUsers / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:percentNewVisits",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:percentNewSessions",
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "User",
		"status": "DEPRECATED",
		"uiName": "% New Sessions",
		"description": "The percentage of sessions by users who had never visited the property before.",
		"calculation": "ga:newUsers / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:1dayUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "1 Day Active Users",
		"description": "Total number of 1-day active users for each day in the requested time period. At least one of ga:nthDay, ga:date, or ga:day must be specified as a dimension to query this metric. For a given date, the returned value will be the total number of unique users for the 1-day period ending on the given date.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:7dayUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "7 Day Active Users",
		"description": "Total number of 7-day active users for each day in the requested time period. At least one of ga:nthDay, ga:date, or ga:day must be specified as a dimension to query this metric. For a given date, the returned value will be the total number of unique users for the 7-day period ending on the given date.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:14dayUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "14 Day Active Users",
		"description": "Total number of 14-day active users for each day in the requested time period. At least one of ga:nthDay, ga:date, or ga:day must be specified as a dimension to query this metric. For a given date, the returned value will be the total number of unique users for the 14-day period ending on the given date.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:28dayUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "28 Day Active Users",
		"description": "Total number of 28-day active users for each day in the requested time period. At least one of ga:nthDay, ga:date, or ga:day must be specified as a dimension to query this metric. For a given date, the returned value will be the total number of unique users for the 28-day period ending on the given date.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:30dayUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "30 Day Active Users",
		"description": "Total number of 30-day active users for each day in the requested time period. At least one of ga:nthDay, ga:date, or ga:day must be specified as a dimension to query this metric. For a given date, the returned value will be the total number of unique users for the 30-day period ending on the given date.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionDurationBucket",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Session Duration",
		"description": "The length (returned as a string) of a session measured in seconds and reported in second increments.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitLength",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:sessionDurationBucket",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Session",
		"status": "DEPRECATED",
		"uiName": "Session Duration",
		"description": "The length (returned as a string) of a session measured in seconds and reported in second increments.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Sessions",
		"description": "The total number of sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visits",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:sessions",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Session",
		"status": "DEPRECATED",
		"uiName": "Sessions",
		"description": "The total number of sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:bounces",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Bounces",
		"description": "The total number of single page (or single interaction hit) sessions for the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:bounceRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Bounce Rate",
		"description": "The percentage of single-page session (i.e., session in which the person left the property from the first page).",
		"calculation": "ga:bounces / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitBounceRate",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:bounceRate",
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Session",
		"status": "DEPRECATED",
		"uiName": "Bounce Rate",
		"description": "The percentage of single-page session (i.e., session in which the person left the property from the first page).",
		"calculation": "ga:bounces / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionDuration",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Session Duration",
		"description": "Total duration (in seconds) of users' sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgSessionDuration",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Avg. Session Duration",
		"description": "The average duration (in seconds) of users' sessions.",
		"calculation": "ga:sessionDuration / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:referralPath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Referral Path",
		"description": "The path of the referring URL (e.g., document.referrer). If someone places on their webpage a link to the property, this is the path of the page containing the referring link.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:fullReferrer",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Full Referrer",
		"description": "The full referring URL including the hostname and path.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:campaign",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Campaign",
		"description": "For manual campaign tracking, it is the value of the utm_campaign campaign tracking parameter. For AdWords autotagging, it is the name(s) of the online ad campaign(s) you use for the property. If you use neither, its value is (not set).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:source",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Source",
		"description": "The source of referrals. For manual campaign tracking, it is the value of the utm_source campaign tracking parameter. For AdWords autotagging, it is google. If you use neither, it is the domain of the source (e.g., document.referrer) referring the users. It may also contain a port address. If users arrived without a referrer, its value is (direct).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:medium",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Medium",
		"description": "The type of referrals. For manual campaign tracking, it is the value of the utm_medium campaign tracking parameter. For AdWords autotagging, it is cpc. If users came from a search engine detected by Google Analytics, it is organic. If the referrer is not a search engine, it is referral. If users came directly to the property and document.referrer is empty, its value is (none).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sourceMedium",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Source / Medium",
		"description": "Combined values of ga:source and ga:medium.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:keyword",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Keyword",
		"description": "For manual campaign tracking, it is the value of the utm_term campaign tracking parameter. For AdWords traffic, it contains the best matching targeting criteria. For the display network, where multiple targeting criteria could have caused the ad to show up, it returns the best matching targeting criteria as selected by Ads. This could be display_keyword, site placement, boomuserlist, user_interest, age, or gender. Otherwise its value is (not set).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adContent",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Ad Content",
		"description": "For manual campaign tracking, it is the value of the utm_content campaign tracking parameter. For AdWords autotagging, it is the first line of the text for the online Ad campaign. If you use mad libs for the AdWords content, it contains the keywords you provided for the mad libs keyword match. If you use none of the above, its value is (not set).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialNetwork",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Social Network",
		"description": "The social network name. This is related to the referring social network for traffic sources; e.g., Google+, Blogger.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:hasSocialSourceReferral",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Social Source Referral",
		"description": "A boolean, either Yes or No, indicates whether sessions to the property are from a social source.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:organicSearches",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Organic Searches",
		"description": "The number of organic searches happened in a session. This metric is search engine agnostic.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adGroup",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads: Ad Group",
		"description": "The name of the AdWords ad group.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adSlot",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads: Ad Slot",
		"description": "The location (Top, RHS, or not set) of the advertisement on the hosting page.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adDistributionNetwork",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Ad Distribution Network",
		"description": "The network (Content, Search, Search partners, etc.) used to deliver the ads.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adMatchType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Query Match Type",
		"description": "The match type (Phrase, Exact, Broad, etc.) applied for users' search term. Ads on the content network are identified as \"Content network\". For details, see https://support.google.com/adwords/answer/2472708?hl=en.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adKeywordMatchType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Keyword Match Type",
		"description": "The match type (Phrase, Exact, or Broad) applied to the keywords. For details, see https://support.google.com/adwords/answer/2472708.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adMatchedQuery",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Search Query",
		"description": "The search query that triggered impressions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adPlacementDomain",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Placement Domain",
		"description": "The domain where the ads on the content network were placed.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adPlacementUrl",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Placement URL",
		"description": "The URL where the ads were placed on the content network.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adFormat",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Ad Format",
		"description": "The AdWords ad format (Text, Image, Flash, Video, etc.).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adTargetingType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Targeting Type",
		"description": "This (keyword, placement, or vertical targeting) indicates how the AdWords ads were targeted.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adTargetingOption",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Placement Type",
		"description": "It is Automatic placements or Managed placements, indicating how the ads were managed on the content network.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adDisplayUrl",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Display URL",
		"description": "The URL the AdWords ads displayed.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adDestinationUrl",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Destination URL",
		"description": "The URL to which the AdWords ads referred traffic.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adwordsCustomerID",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads Customer ID",
		"description": "Customer's AdWords ID, corresponding to AdWords API AccountInfo.customerId.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adwordsCampaignID",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads Campaign ID",
		"description": "AdWords API Campaign.id.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adwordsAdGroupID",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads Ad Group ID",
		"description": "AdWords API AdGroup.id.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adwordsCreativeID",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads Creative ID",
		"description": "AdWords API Ad.id.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adwordsCriteriaID",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Google Ads Criteria ID",
		"description": "AdWords API Criterion.id. The geographical targeting Criteria IDs are listed at https://developers.google.com/analytics/devguides/collection/protocol/v1/geoid.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:impressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Impressions",
		"description": "Total number of campaign impressions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Clicks",
		"description": "Total number of times users have clicked on an ad to reach the property.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adCost",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Cost",
		"description": "Derived cost for the advertising campaign. Its currency is the one you set in the AdWords account.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:CPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "CPM",
		"description": "Cost per thousand impressions.",
		"calculation": "ga:adCost / (ga:impressions / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:CPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "CPC",
		"description": "Cost to advertiser per click.",
		"calculation": "ga:adCost / ga:adClicks",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:CTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "CTR",
		"description": "Click-through-rate for the ad. This is equal to the number of clicks divided by the number of impressions for the ad (e.g., how many times users clicked on one of the ads where that ad appeared).",
		"calculation": "ga:adClicks / ga:impressions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:costPerTransaction",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Cost per Transaction",
		"description": "The cost per transaction for the property.",
		"calculation": "(ga:adCost) / (ga:transactions)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:costPerGoalConversion",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Cost per Goal Conversion",
		"description": "The cost per goal conversion for the property.",
		"calculation": "(ga:adCost) / (ga:goalCompletionsAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:costPerConversion",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Cost per Conversion",
		"description": "The cost per conversion (including ecommerce and goal conversions) for the property.",
		"calculation": "(ga:adCost) / (ga:transactions+ga:goalCompletionsAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:RPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "RPC",
		"description": "RPC or revenue-per-click, the average revenue (from ecommerce sales and/or goal value) you received for each click on one of the search ads.",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll) / ga:adClicks",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:ROI",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adwords",
		"status": "DEPRECATED",
		"uiName": "ROI",
		"description": "This metric is deprecated and will be removed soon. Please use ga:ROAS instead.",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll - ga:adCost) / ga:adCost",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:margin",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adwords",
		"status": "DEPRECATED",
		"uiName": "Margin",
		"description": "This metric is deprecated and will be removed soon. Please use ga:ROAS instead.",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll - ga:adCost) / (ga:transactionRevenue + ga:goalValueAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:ROAS",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "ROAS",
		"description": "Return On Ad Spend (ROAS) is the total transaction revenue and goal value divided by derived advertising cost.",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll) / ga:adCost",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adQueryWordCount",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "Query Word Count",
		"description": "The number of words in the search query.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalCompletionLocation",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Completion Location",
		"description": "The page path or screen name that matched any destination type goal completion.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalPreviousStep1",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Previous Step - 1",
		"description": "The page path or screen name that matched any destination type goal, one step prior to the goal completion location.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalPreviousStep2",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Previous Step - 2",
		"description": "The page path or screen name that matched any destination type goal, two steps prior to the goal completion location.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalPreviousStep3",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Previous Step - 3",
		"description": "The page path or screen name that matched any destination type goal, three steps prior to the goal completion location.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXStarts",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Starts",
		"description": "The total number of starts for the requested goal number.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalStartsAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Starts",
		"description": "Total number of starts for all goals defined in the profile.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXCompletions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Completions",
		"description": "The total number of completions for the requested goal number.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalCompletionsAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Completions",
		"description": "Total number of completions for all goals defined in the profile.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Value",
		"description": "The total numeric value for the requested goal number.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalValueAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Value",
		"description": "Total numeric value for all goals defined in the profile.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalValuePerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Per Session Goal Value",
		"description": "The average goal value of a session.",
		"calculation": "ga:goalValueAll / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalValuePerVisit",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:goalValuePerSession",
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Goal Conversions",
		"status": "DEPRECATED",
		"uiName": "Per Session Goal Value",
		"description": "The average goal value of a session.",
		"calculation": "ga:goalValueAll / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXConversionRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Conversion Rate",
		"description": "Percentage of sessions resulting in a conversion to the requested goal number.",
		"calculation": "ga:goalXXCompletions / ga:sessions",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalConversionRateAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal Conversion Rate",
		"description": "The percentage of sessions which resulted in a conversion to at least one of the goals.",
		"calculation": "ga:goalCompletionsAll / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXAbandons",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Abandoned Funnels",
		"description": "The number of times users started conversion activity on the requested goal number without actually completing it.",
		"calculation": "(ga:goalXXStarts - ga:goalXXCompletions)",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalAbandonsAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Abandoned Funnels",
		"description": "The overall number of times users started goals without actually completing them.",
		"calculation": "(ga:goalStartsAll - ga:goalCompletionsAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalXXAbandonRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Goal XX Abandonment Rate",
		"description": "The rate at which the requested goal number was abandoned.",
		"calculation": "((ga:goalXXStarts - ga:goalXXCompletions)) / (ga:goalXXStarts)",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalAbandonRateAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Goal Conversions",
		"status": "PUBLIC",
		"uiName": "Total Abandonment Rate",
		"description": "Goal abandonment rate.",
		"calculation": "((ga:goalStartsAll - ga:goalCompletionsAll)) / (ga:goalStartsAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:browser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Browser",
		"description": "The name of users' browsers, for example, Internet Explorer or Firefox.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:browserVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Browser Version",
		"description": "The version of users' browsers, for example, 2.0.0.14.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:operatingSystem",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Operating System",
		"description": "Users' operating system, for example, Windows, Linux, Macintosh, or iOS.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:operatingSystemVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Operating System Version",
		"description": "The version of users' operating system, i.e., XP for Windows, PPC for Macintosh.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:mobileDeviceBranding",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Mobile Device Branding",
		"description": "Mobile manufacturer or branded name.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:mobileDeviceModel",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Mobile Device Model",
		"description": "Mobile device model.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:mobileInputSelector",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Mobile Input Selector",
		"description": "Selector (e.g., touchscreen, joystick, clickwheel, stylus) used on the mobile device.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:mobileDeviceInfo",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Mobile Device Info",
		"description": "The branding, model, and marketing name used to identify the mobile device.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:mobileDeviceMarketingName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Mobile Device Marketing Name",
		"description": "The marketing name used for the mobile device.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:deviceCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Device Category",
		"description": "The type of device: desktop, tablet, or mobile.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:continent",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Continent",
		"description": "Users' continent, derived from users' IP addresses or Geographical IDs.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:subContinent",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Sub Continent",
		"description": "Users' sub-continent, derived from their IP addresses or Geographical IDs. For example, Polynesia or Northern Europe.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:country",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Country",
		"description": "Users' country, derived from their IP addresses or Geographical IDs.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:region",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Region",
		"description": "Users' region, derived from their IP addresses or Geographical IDs. In U.S., a region is a state, New York, for example.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:metro",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Metro",
		"description": "The Designated Market Area (DMA) from where traffic arrived.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:city",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "City",
		"description": "Users' city, derived from their IP addresses or Geographical IDs.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:latitude",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Latitude",
		"description": "The approximate latitude of users' city, derived from their IP addresses or Geographical IDs. Locations north of the equator have positive latitudes and locations south of the equator have negative latitudes.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:longitude",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Longitude",
		"description": "The approximate longitude of users' city, derived from their IP addresses or Geographical IDs. Locations east of the prime meridian have positive longitudes and locations west of the prime meridian have negative longitudes.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:networkDomain",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Network Domain",
		"description": "The domain name of users' ISP, derived from the domain name registered to the ISP's IP address.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:networkLocation",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Service Provider",
		"description": "The names of the service providers used to reach the property. For example, if most users of the website come via the major cable internet service providers, its value will be these service providers' names.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:flashVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Flash Version",
		"description": "The version of Flash, including minor versions, supported by users' browsers.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:javaEnabled",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Java Support",
		"description": "A boolean, either Yes or No, indicating whether Java is enabled in users' browsers.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:language",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Language",
		"description": "The language, in ISO-639 code format (e.g., en-gb for British English), provided by the HTTP Request for the browser.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenColors",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Screen Colors",
		"description": "The color depth of users' monitors, retrieved from the DOM of users' browsers. For example, 4-bit, 8-bit, 24-bit, or undefined-bit.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sourcePropertyDisplayName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Source Property Display Name",
		"description": "Source property display name of roll-up properties. This is valid for only roll-up properties.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sourcePropertyTrackingId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Source Property Tracking ID",
		"description": "Source property tracking ID of roll-up properties. This is valid for only roll-up properties.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenResolution",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "System",
		"status": "PUBLIC",
		"uiName": "Screen Resolution",
		"description": "Resolution of users' screens, for example, 1024x738.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialActivityContentUrl",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Activities",
		"status": "DEPRECATED",
		"uiName": "Shared URL",
		"description": "For a social data hub activity, this is the URL shared by the associated social network users.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:hostname",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Hostname",
		"description": "The hostname from which the tracking request was made.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pagePath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page",
		"description": "A page on the website specified by path and/or query parameters. Use this with hostname to get the page's full URL.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pagePathLevel1",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page path level 1",
		"description": "This dimension rolls up all the page paths in the first hierarchical level in pagePath.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pagePathLevel2",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page path level 2",
		"description": "This dimension rolls up all the page paths in the second hierarchical level in pagePath.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pagePathLevel3",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page path level 3",
		"description": "This dimension rolls up all the page paths in the third hierarchical level in pagePath.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pagePathLevel4",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page path level 4",
		"description": "This dimension rolls up all the page paths into hierarchical levels. Up to 4 pagePath levels maybe specified. All additional levels in the pagePath hierarchy are also rolled up in this dimension.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageTitle",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page Title",
		"description": "The page's title. Multiple pages might have the same page title.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:landingPagePath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Landing Page",
		"description": "The first page in users' sessions, or the landing page.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:secondPagePath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Second Page",
		"description": "The second page in users' sessions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exitPagePath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Exit Page",
		"description": "The last page or exit page in users' sessions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:previousPagePath",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Previous Page Path",
		"description": "A page visited before another page on the same property, typically used with the pagePath dimension.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageDepth",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page Depth",
		"description": "The number of pages visited by users during a session. The value is a histogram that counts pageviews across a range of possible values. In this calculation, all sessions will have at least one pageview, and some percentage of sessions will have more.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Page Value",
		"description": "The average value of this page or set of pages, which is equal to (ga:transactionRevenue + ga:goalValueAll) / ga:uniquePageviews.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:entrances",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Entrances",
		"description": "The number of entrances to the property measured as the first pageview in a session, typically used with landingPagePath.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:entranceRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Entrances / Pageviews",
		"description": "The percentage of pageviews in which this page was the entrance.",
		"calculation": "ga:entrances / ga:pageviews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Pageviews",
		"description": "The total number of pageviews for the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageviewsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Pages / Session",
		"description": "The average number of pages viewed during a session, including repeated views of a single page.",
		"calculation": "ga:pageviews / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageviewsPerVisit",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:pageviewsPerSession",
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Page Tracking",
		"status": "DEPRECATED",
		"uiName": "Pages / Session",
		"description": "The average number of pages viewed during a session, including repeated views of a single page.",
		"calculation": "ga:pageviews / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:contentGroupUniqueViewsXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Content Grouping",
		"status": "PUBLIC",
		"uiName": "Unique Views XX",
		"description": "The number of unique content group views. Content group views in different sessions are counted as unique content group views. Both the pagePath and pageTitle are used to determine content group view uniqueness.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniquePageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Unique Pageviews",
		"description": "Unique Pageviews is the number of sessions during which the specified page was viewed at least once. A unique pageview is counted for each page URL + page title combination.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:timeOnPage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Time on Page",
		"description": "Time (in seconds) users spent on a particular page, calculated by subtracting the initial view time for a particular page from the initial view time for a subsequent page. This metric does not apply to exit pages of the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgTimeOnPage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Avg. Time on Page",
		"description": "The average time users spent viewing this page or a set of pages.",
		"calculation": "ga:timeOnPage / (ga:pageviews - ga:exits)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exits",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "Exits",
		"description": "The number of exits from the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exitRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Page Tracking",
		"status": "PUBLIC",
		"uiName": "% Exit",
		"description": "The percentage of exits from the property that occurred out of the total pageviews.",
		"calculation": "ga:exits / (ga:pageviews + ga:screenviews)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchUsed",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Site Search Status",
		"description": "A boolean, either Visits With Site Search or Visits Without Site Search, to distinguish whether internal search was used in a session.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchKeyword",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Search Term",
		"description": "Search term used within the property.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchKeywordRefinement",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Refined Keyword",
		"description": "Subsequent keyword search term or string entered by users after a given initial string search.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Site Search Category",
		"description": "The category used for the internal search if site search categories are enabled in the view. For example, the product category may be electronics, furniture, or clothing.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchStartPage",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Start Page",
		"description": "The page where users initiated an internal search.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchDestinationPage",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Destination Page",
		"description": "The page users immediately visited after performing an internal search on the site. This is usually the search results page.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchAfterDestinationPage",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Search Destination Page",
		"description": "The page that users visited after performing an internal search on the site.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchResultViews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Results Pageviews",
		"description": "The number of times a search result page was viewed.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchUniques",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Total Unique Searches",
		"description": "Total number of unique keywords from internal searches within a session. For example, if \"shoes\" was searched for 3 times in a session, it would be counted only once.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgSearchResultViews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Results Pageviews / Search",
		"description": "The average number of times people viewed a page as a result of a search.",
		"calculation": "ga:searchResultViews / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchSessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Sessions with Search",
		"description": "The total number of sessions that included an internal search.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchVisits",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:searchSessions",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "DEPRECATED",
		"uiName": "Sessions with Search",
		"description": "The total number of sessions that included an internal search.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:percentSessionsWithSearch",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "% Sessions with Search",
		"description": "The percentage of sessions with search.",
		"calculation": "ga:searchSessions / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:percentVisitsWithSearch",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:percentSessionsWithSearch",
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "DEPRECATED",
		"uiName": "% Sessions with Search",
		"description": "The percentage of sessions with search.",
		"calculation": "ga:searchSessions / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchDepth",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Search Depth",
		"description": "The total number of subsequent page views made after a use of the site's internal search feature.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgSearchDepth",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Avg. Search Depth",
		"description": "The average number of pages people viewed after performing a search.",
		"calculation": "ga:searchDepth / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchRefinements",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Search Refinements",
		"description": "The total number of times a refinement (transition) occurs between internal keywords search within a session. For example, if the sequence of keywords is \"shoes\", \"shoes\", \"pants\", \"pants\", this metric will be one because the transition between \"shoes\" and \"pants\" is different.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:percentSearchRefinements",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "% Search Refinements",
		"description": "The percentage of the number of times a refinement (i.e., transition) occurs between internal keywords search within a session.",
		"calculation": "ga:searchRefinements / ga:searchResultViews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchDuration",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Time after Search",
		"description": "The session duration when the site's internal search feature is used.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgSearchDuration",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Time after Search",
		"description": "The average time (in seconds) users, after searching, spent on the property.",
		"calculation": "ga:searchDuration / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchExits",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Search Exits",
		"description": "The number of exits on the site that occurred following a search result from the site's internal search feature.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchExitRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "% Search Exits",
		"description": "The percentage of searches that resulted in an immediate exit from the property.",
		"calculation": "ga:searchExits / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchGoalXXConversionRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Site Search Goal XX Conversion Rate",
		"description": "The percentage of search sessions (i.e., sessions that included at least one search) which resulted in a conversion to the requested goal number.",
		"calculation": "ga:goalXXCompletions / ga:searchUniques",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:searchGoalConversionRateAll",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Site Search Goal Conversion Rate",
		"description": "The percentage of search sessions (i.e., sessions that included at least one search) which resulted in a conversion to at least one of the goals.",
		"calculation": "ga:goalCompletionsAll / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:goalValueAllPerSearch",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Internal Search",
		"status": "PUBLIC",
		"uiName": "Per Search Goal Value",
		"description": "The average goal value of a search.",
		"calculation": "ga:goalValueAll / ga:searchUniques",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageLoadTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Page Load Time (ms)",
		"description": "Total time (in milliseconds), from pageview initiation (e.g., a click on a page link) to page load completion in the browser, the pages in the sample set take to load.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageLoadSample",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Page Load Sample",
		"description": "The sample set (or count) of pageviews used to calculate the average page load time.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgPageLoadTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Page Load Time (sec)",
		"description": "The average time (in seconds) pages from the sample set take to load, from initiation of the pageview (e.g., a click on a page link) to load completion in the browser.",
		"calculation": "(ga:pageLoadTime / ga:pageLoadSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:domainLookupTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Domain Lookup Time (ms)",
		"description": "The total time (in milliseconds) all samples spent in DNS lookup for this page.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgDomainLookupTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Domain Lookup Time (sec)",
		"description": "The average time (in seconds) spent in DNS lookup for this page.",
		"calculation": "(ga:domainLookupTime / ga:speedMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:pageDownloadTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Page Download Time (ms)",
		"description": "The total time (in milliseconds) to download this page among all samples.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgPageDownloadTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Page Download Time (sec)",
		"description": "The average time (in seconds) to download this page.",
		"calculation": "(ga:pageDownloadTime / ga:speedMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:redirectionTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Redirection Time (ms)",
		"description": "The total time (in milliseconds) all samples spent in redirects before fetching this page. If there are no redirects, this is 0.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgRedirectionTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Redirection Time (sec)",
		"description": "The average time (in seconds) spent in redirects before fetching this page. If there are no redirects, this is 0.",
		"calculation": "(ga:redirectionTime / ga:speedMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:serverConnectionTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Server Connection Time (ms)",
		"description": "Total time (in milliseconds) all samples spent in establishing a TCP connection to this page.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgServerConnectionTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Server Connection Time (sec)",
		"description": "The average time (in seconds) spent in establishing a TCP connection to this page.",
		"calculation": "(ga:serverConnectionTime / ga:speedMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:serverResponseTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Server Response Time (ms)",
		"description": "The total time (in milliseconds) the site's server takes to respond to users' requests among all samples; this includes the network time from users' locations to the server.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgServerResponseTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Server Response Time (sec)",
		"description": "The average time (in seconds) the site's server takes to respond to users' requests; this includes the network time from users' locations to the server.",
		"calculation": "(ga:serverResponseTime / ga:speedMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:speedMetricsSample",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Speed Metrics Sample",
		"description": "The sample set (or count) of pageviews used to calculate the averages of site speed metrics. This metric is used in all site speed average calculations, including avgDomainLookupTime, avgPageDownloadTime, avgRedirectionTime, avgServerConnectionTime, and avgServerResponseTime.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:domInteractiveTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Document Interactive Time (ms)",
		"description": "The time (in milliseconds), including the network time from users' locations to the site's server, the browser takes to parse the document (DOMInteractive). At this time, users can interact with the Document Object Model even though it is not fully loaded.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgDomInteractiveTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Document Interactive Time (sec)",
		"description": "The average time (in seconds), including the network time from users' locations to the site's server, the browser takes to parse the document and execute deferred and parser-inserted scripts.",
		"calculation": "(ga:domInteractiveTime / ga:domLatencyMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:domContentLoadedTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Document Content Loaded Time (ms)",
		"description": "The time (in milliseconds), including the network time from users' locations to the site's server, the browser takes to parse the document and execute deferred and parser-inserted scripts (DOMContentLoaded). When parsing of the document is finished, the Document Object Model (DOM) is ready, but the referenced style sheets, images, and subframes may not be finished loading. This is often the starting point of Javascript framework execution, e.g., JQuery's onready() callback.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgDomContentLoadedTime",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "Avg. Document Content Loaded Time (sec)",
		"description": "The average time (in seconds) the browser takes to parse the document.",
		"calculation": "(ga:domContentLoadedTime / ga:domLatencyMetricsSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:domLatencyMetricsSample",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Site Speed",
		"status": "PUBLIC",
		"uiName": "DOM Latency Metrics Sample",
		"description": "Sample set (or count) of pageviews used to calculate the averages for site speed DOM metrics. This metric is used to calculate ga:avgDomContentLoadedTime and ga:avgDomInteractiveTime.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:appInstallerId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "App Installer ID",
		"description": "The ID of the app installer (e.g., Google Play Store) from which the app was downloaded. By default, the app installer ID is set by the PackageManager#getInstallerPackageName method.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:appVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "App Version",
		"description": "The application version.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:appName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "App Name",
		"description": "The application name.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:appId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "App ID",
		"description": "The application ID.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Screen Name",
		"description": "The name of the screen.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenDepth",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Screen Depth",
		"description": "The number of screenviews (reported as a string) per session, useful for historgrams.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:landingScreenName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Landing Screen",
		"description": "The name of the first viewed screen.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exitScreenName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Exit Screen",
		"description": "The name of the screen where users exited the application.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Screen Views",
		"description": "The total number of screenviews.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniqueScreenviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Unique Screen Views",
		"description": "The number of unique screen views. Screen views in different sessions are counted as separate screen views.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniqueAppviews",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:uniqueScreenviews",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "App Tracking",
		"status": "DEPRECATED",
		"uiName": "Unique Screen Views",
		"description": "The number of unique screen views. Screen views in different sessions are counted as separate screen views.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:screenviewsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Screens / Session",
		"description": "The average number of screenviews per session.",
		"calculation": "ga:screenviews / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:timeOnScreen",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Time on Screen",
		"description": "The time spent viewing the current screen.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgScreenviewDuration",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "App Tracking",
		"status": "PUBLIC",
		"uiName": "Avg. Time on Screen",
		"description": "Average time (in seconds) users spent on a screen.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Event Category",
		"description": "The event category.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventAction",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Event Action",
		"description": "Event action.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventLabel",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Event Label",
		"description": "Event label.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalEvents",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Total Events",
		"description": "The total number of events for the profile, across all categories.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniqueDimensionCombinations",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Unique Dimension Combinations",
		"description": "Unique Dimension Combinations counts the number of unique dimension-value combinations for each dimension in a report. This lets you build combined (concatenated) dimensions post-processing, which allows for more flexible reporting without having to update your tracking implementation or use additional custom-dimension slots. For more information, see https://support.google.com/analytics/answer/7084499.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniqueEvents",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Unique Events",
		"description": "The number of unique events. Events in different sessions are counted as separate events.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Event Value",
		"description": "Total value of events for the profile.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgEventValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Avg. Value",
		"description": "The average value of an event.",
		"calculation": "ga:eventValue / ga:totalEvents",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionsWithEvent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Sessions with Event",
		"description": "The total number of sessions with events.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitsWithEvent",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:sessionsWithEvent",
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Event Tracking",
		"status": "DEPRECATED",
		"uiName": "Sessions with Event",
		"description": "The total number of sessions with events.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventsPerSessionWithEvent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Event Tracking",
		"status": "PUBLIC",
		"uiName": "Events / Session with Event",
		"description": "The average number of events per session with event.",
		"calculation": "ga:totalEvents / ga:sessionsWithEvent",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:eventsPerVisitWithEvent",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:eventsPerSessionWithEvent",
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Event Tracking",
		"status": "DEPRECATED",
		"uiName": "Events / Session with Event",
		"description": "The average number of events per session with event.",
		"calculation": "ga:totalEvents / ga:sessionsWithEvent",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Transaction ID",
		"description": "The transaction ID, supplied by the ecommerce tracking method, for the purchase in the shopping cart.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:affiliation",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Affiliation",
		"description": "A product affiliation to designate a supplying company or brick and mortar location.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionsToTransaction",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Sessions to Transaction",
		"description": "The number of sessions between users' purchases and the related campaigns that lead to the purchases.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitsToTransaction",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:sessionsToTransaction",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "DEPRECATED",
		"uiName": "Sessions to Transaction",
		"description": "The number of sessions between users' purchases and the related campaigns that lead to the purchases.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:daysToTransaction",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Days to Transaction",
		"description": "The number of days between users' purchases and the most recent campaign source prior to the purchase.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productSku",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product SKU",
		"description": "The product SKU, defined in the ecommerce tracking application, for purchased items.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product",
		"description": "The product name, supplied by the ecommerce tracking application, for purchased items.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Category",
		"description": "Any product variation (size, color) supplied by the ecommerce application for purchased items, not compatible with Enhanced Ecommerce.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:currencyCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Currency Code",
		"description": "The local currency code (based on ISO 4217 standard) of the transaction.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Transactions",
		"description": "The total number of transactions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Ecommerce Conversion Rate",
		"description": "The average number of transactions in a session.",
		"calculation": "ga:transactions / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionsPerVisit",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:transactionsPerSession",
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "DEPRECATED",
		"uiName": "Ecommerce Conversion Rate",
		"description": "The average number of transactions in a session.",
		"calculation": "ga:transactions / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Revenue",
		"description": "The total sale revenue (excluding shipping and tax) of the transaction.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:revenuePerTransaction",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Avg. Order Value",
		"description": "The average revenue of an ecommerce transaction.",
		"calculation": "ga:transactionRevenue / ga:transactions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionRevenuePerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Per Session Value",
		"description": "Average transaction revenue for a session.",
		"calculation": "ga:transactionRevenue / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionRevenuePerVisit",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:transactionRevenuePerSession",
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "DEPRECATED",
		"uiName": "Per Session Value",
		"description": "Average transaction revenue for a session.",
		"calculation": "ga:transactionRevenue / ga:sessions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionShipping",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Shipping",
		"description": "The total cost of shipping.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionTax",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Tax",
		"description": "Total tax for the transaction.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Total Value",
		"description": "Total value for the property (including total revenue and total goal value).",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:itemQuantity",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Quantity",
		"description": "Total number of items purchased. For example, if users purchase 2 frisbees and 5 tennis balls, this will be 7.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniquePurchases",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Unique Purchases",
		"description": "The number of product sets purchased. For example, if users purchase 2 frisbees and 5 tennis balls from the site, this will be 2.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:revenuePerItem",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Avg. Price",
		"description": "The average revenue per item.",
		"calculation": "ga:itemRevenue / ga:itemQuantity",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:itemRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Revenue",
		"description": "The total revenue from purchased product items.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:itemsPerPurchase",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Avg. QTY",
		"description": "The average quantity of this item (or group of items) sold per purchase.",
		"calculation": "ga:itemQuantity / ga:uniquePurchases",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localTransactionRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Revenue",
		"description": "Transaction revenue in local currency.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localTransactionShipping",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Shipping",
		"description": "Transaction shipping cost in local currency.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localTransactionTax",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Tax",
		"description": "Transaction tax in local currency.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localItemRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Product Revenue",
		"description": "Product revenue in local currency.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionNetwork",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Network",
		"description": "For social interactions, this represents the social network being tracked.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionAction",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Action",
		"description": "For social interactions, this is the social action (e.g., +1, bookmark) being tracked.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionNetworkAction",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Network and Action (Hit)",
		"description": "For social interactions, this is the concatenation of the socialInteractionNetwork and socialInteractionAction action (e.g., Google: +1) being tracked at this hit level.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionTarget",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Entity",
		"description": "For social interactions, this is the URL (or resource) which receives the social network action.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialEngagementType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Type",
		"description": "Engagement type, either \"Socially Engaged\" or \"Not Socially Engaged\".",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Social Actions",
		"description": "The total number of social interactions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:uniqueSocialInteractions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Unique Social Actions",
		"description": "The number of sessions during which the specified social action(s) occurred at least once. This is based on the the unique combination of socialInteractionNetwork, socialInteractionAction, and socialInteractionTarget.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Social Interactions",
		"status": "PUBLIC",
		"uiName": "Actions Per Social Session",
		"description": "The number of social interactions per session.",
		"calculation": "ga:socialInteractions / ga:uniqueSocialInteractions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:socialInteractionsPerVisit",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:socialInteractionsPerSession",
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Social Interactions",
		"status": "DEPRECATED",
		"uiName": "Actions Per Social Session",
		"description": "The number of social interactions per session.",
		"calculation": "ga:socialInteractions / ga:uniqueSocialInteractions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userTimingCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "Timing Category",
		"description": "For easier reporting purposes, this is used to categorize all user timing variables into logical groups.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userTimingLabel",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "Timing Label",
		"description": "The name of the resource's action being tracked.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userTimingVariable",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "Timing Variable",
		"description": "Used to add flexibility to visualize user timings in the reports.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userTimingValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "User Timing (ms)",
		"description": "Total number of milliseconds for user timing.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userTimingSample",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "User Timing Sample",
		"description": "The number of hits sent for a particular userTimingCategory, userTimingLabel, or userTimingVariable.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:avgUserTimingValue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "User Timings",
		"status": "PUBLIC",
		"uiName": "Avg. User Timing (sec)",
		"description": "The average elapsed time.",
		"calculation": "(ga:userTimingValue / ga:userTimingSample / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exceptionDescription",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Exceptions",
		"status": "PUBLIC",
		"uiName": "Exception Description",
		"description": "The description for the exception.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exceptions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Exceptions",
		"status": "PUBLIC",
		"uiName": "Exceptions",
		"description": "The number of exceptions sent to Google Analytics.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:exceptionsPerScreenview",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Exceptions",
		"status": "PUBLIC",
		"uiName": "Exceptions / Screen",
		"description": "The number of exceptions thrown divided by the number of screenviews.",
		"calculation": "ga:exceptions / ga:screenviews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:fatalExceptions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Exceptions",
		"status": "PUBLIC",
		"uiName": "Crashes",
		"description": "The number of exceptions where isFatal is set to true.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:fatalExceptionsPerScreenview",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Exceptions",
		"status": "PUBLIC",
		"uiName": "Crashes / Screen",
		"description": "The number of fatal exceptions thrown divided by the number of screenviews.",
		"calculation": "ga:fatalExceptions / ga:screenviews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:experimentId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Experiments",
		"status": "PUBLIC",
		"uiName": "Experiment ID",
		"description": "The user-scoped ID of the content experiment that users were exposed to when the metrics were reported.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:experimentVariant",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Experiments",
		"status": "PUBLIC",
		"uiName": "Variant",
		"description": "The user-scoped ID of the particular variant that users were exposed to during a content experiment.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dimensionXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Custom Variables or Columns",
		"status": "PUBLIC",
		"uiName": "Custom Dimension XX",
		"description": "The value of the requested custom dimension, where XX refers to the number or index of the custom dimension.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"premiumMinTemplateIndex": "1",
		"premiumMaxTemplateIndex": "200",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:customVarNameXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Custom Variables or Columns",
		"status": "PUBLIC",
		"uiName": "Custom Variable (Key XX)",
		"description": "The name for the requested custom variable.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"premiumMinTemplateIndex": "1",
		"premiumMaxTemplateIndex": "50",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:metricXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Custom Variables or Columns",
		"status": "PUBLIC",
		"uiName": "Custom Metric XX Value",
		"description": "The value of the requested custom metric, where XX refers to the number or index of the custom metric. Note that the data type of ga:metricXX can be INTEGER, CURRENCY, or TIME.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "20",
		"premiumMinTemplateIndex": "1",
		"premiumMaxTemplateIndex": "200",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:customVarValueXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Custom Variables or Columns",
		"status": "PUBLIC",
		"uiName": "Custom Variable (Value XX)",
		"description": "The value for the requested custom variable.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"premiumMinTemplateIndex": "1",
		"premiumMaxTemplateIndex": "50",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:date",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Date",
		"description": "The date of the session formatted as YYYYMMDD.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:year",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Year",
		"description": "The year of the session, a four-digit year from 2005 to the current year.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:month",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Month of the year",
		"description": "Month of the session, a two digit integer from 01 to 12.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:week",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Week of the Year",
		"description": "The week of the session, a two-digit number from 01 to 53. Each week starts on Sunday.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:day",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Day of the month",
		"description": "The day of the month, a two-digit number from 01 to 31.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:hour",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Hour",
		"description": "A two-digit hour of the day ranging from 00-23 in the timezone configured for the account. This value is also corrected for daylight savings time. If the timezone follows daylight savings time, there will be an apparent bump in the number of sessions during the changeover hour (e.g., between 1:00 and 2:00) for the day per year when that hour repeats. A corresponding hour with zero sessions will occur at the opposite changeover. (Google Analytics does not track user time more precisely than hours.)",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:minute",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Minute",
		"description": "Returns the minutes, between 00 and 59, in the hour.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:nthMonth",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Month Index",
		"description": "The index for a month in the specified date range. In the date range, the index for the first month is 0, for the second month 1, and so on.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:nthWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Week Index",
		"description": "The index for each week in the specified date range. The index for the first week in the date range is 0, for the second week 1, and so on. The index corresponds to week entries.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:nthDay",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Day Index",
		"description": "The index for each day in the specified date range. The index for the first day (i.e., start-date) in the date range is 0, for the second day 1, and so on.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:nthMinute",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Minute Index",
		"description": "The index for each minute in the specified date range. The index for the first minute of the first day (i.e., start-date) in the date range is 0, for the next minute 1, and so on.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dayOfWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Day of Week",
		"description": "Day of the week, a one-digit number from 0 (Sunday) to 6 (Saturday).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dayOfWeekName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Day of Week Name",
		"description": "Name (in English) of the day of the week.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dateHour",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Hour of Day",
		"description": "Combined values of ga:date and ga:hour formated as YYYYMMDDHH.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dateHourMinute",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Date Hour and Minute",
		"description": "Combined values of ga:date, ga:hour and ga:minute formated as YYYYMMDDHHMM.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:yearMonth",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Month of Year",
		"description": "Combined values of ga:year and ga:month.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:yearWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Week of Year",
		"description": "Combined values of ga:year and ga:week.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:isoWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "ISO Week of the Year",
		"description": "ISO week number, where each week starts on Monday. For details, see http://en.wikipedia.org/wiki/ISO_week_date. ga:isoWeek should only be used with ga:isoYear because ga:year represents Gregorian calendar.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:isoYear",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "ISO Year",
		"description": "The ISO year of the session. For details, see http://en.wikipedia.org/wiki/ISO_week_date. ga:isoYear should only be used with ga:isoWeek because ga:week represents Gregorian calendar.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:isoYearIsoWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "ISO Week of ISO Year",
		"description": "Combined values of ga:isoYear and ga:isoWeek.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAd",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad (GA Model)",
		"description": "DCM ad name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAdId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad ID (GA Model)",
		"description": "DCM ad ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAdType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad Type (GA Model)",
		"description": "DCM ad type name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAdTypeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad Type ID",
		"description": "DCM ad type ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAdvertiser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Advertiser (GA Model)",
		"description": "DCM advertiser name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Advertiser ID (GA Model)",
		"description": "DCM advertiser ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCampaign",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Campaign (GA Model)",
		"description": "DCM campaign name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCampaignId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Campaign ID (GA Model)",
		"description": "DCM campaign ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCreativeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative ID (GA Model)",
		"description": "DCM creative ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCreative",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative (GA Model)",
		"description": "DCM creative name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickRenderingId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Rendering ID (GA Model)",
		"description": "DCM rendering ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCreativeType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Type (GA Model)",
		"description": "DCM creative type name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCreativeTypeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Type ID (GA Model)",
		"description": "DCM creative type ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickCreativeVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Version (GA Model)",
		"description": "DCM creative version of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickSite",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Site (GA Model)",
		"description": "Site name where the DCM creative was shown and clicked on for the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickSiteId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Site ID (GA Model)",
		"description": "DCM site ID where the DCM creative was shown and clicked on for the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickSitePlacement",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Placement (GA Model)",
		"description": "DCM site placement name of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickSitePlacementId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Placement ID (GA Model)",
		"description": "DCM site placement ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClickSpotId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Floodlight Configuration ID (GA Model)",
		"description": "DCM Floodlight configuration ID of the DCM click matching the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightActivity",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Activity",
		"description": "DCM Floodlight activity name associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightActivityAndGroup",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Activity and Group",
		"description": "DCM Floodlight activity name and group name associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightActivityGroup",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Activity Group",
		"description": "DCM Floodlight activity group name associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightActivityGroupId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Activity Group ID",
		"description": "DCM Floodlight activity group ID associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightActivityId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Activity ID",
		"description": "DCM Floodlight activity ID associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Advertiser ID",
		"description": "DCM Floodlight advertiser ID associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightSpotId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Floodlight Configuration ID",
		"description": "DCM Floodlight configuration ID associated with the floodlight conversion (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAd",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad",
		"description": "DCM ad name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAdId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad ID (CM360 Model)",
		"description": "DCM ad ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAdType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad Type (CM360 Model)",
		"description": "DCM ad type name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAdTypeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Ad Type ID (CM360 Model)",
		"description": "DCM ad type ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAdvertiser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Advertiser (CM360 Model)",
		"description": "DCM advertiser name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Advertiser ID (CM360 Model)",
		"description": "DCM advertiser ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventAttributionType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Attribution Type (CM360 Model)",
		"description": "There are two possible values: ClickThrough and ViewThrough. If the last DCM event associated with the Google Analytics session was a click, then the value will be ClickThrough. If the last DCM event associated with the Google Analytics session was an ad impression, then the value will be ViewThrough (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCampaign",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Campaign (CM360 Model)",
		"description": "DCM campaign name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCampaignId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Campaign ID (CM360 Model)",
		"description": "DCM campaign ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCreativeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative ID (CM360 Model)",
		"description": "DCM creative ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCreative",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative (CM360 Model)",
		"description": "DCM creative name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventRenderingId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Rendering ID (CM360 Model)",
		"description": "DCM rendering ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCreativeType",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Type (CM360 Model)",
		"description": "DCM creative type name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCreativeTypeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Type ID (CM360 Model)",
		"description": "DCM creative type ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventCreativeVersion",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Creative Version (CM360 Model)",
		"description": "DCM creative version of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventSite",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Site (CM360 Model)",
		"description": "Site name where the DCM creative was shown and clicked on for the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventSiteId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Site ID (CM360 Model)",
		"description": "DCM site ID where the DCM creative was shown and clicked on for the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventSitePlacement",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Placement (CM360 Model)",
		"description": "DCM site placement name of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventSitePlacementId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Placement ID (CM360 Model)",
		"description": "DCM site placement ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmLastEventSpotId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM360 Floodlight Configuration ID (CM360 Model)",
		"description": "DCM Floodlight configuration ID of the last DCM event (impression or click within the DCM lookback window) associated with the Google Analytics session (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightQuantity",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM Conversions",
		"description": "The number of DCM Floodlight conversions (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmFloodlightRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM Revenue",
		"description": "DCM Floodlight revenue (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:landingContentGroupXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Grouping",
		"status": "PUBLIC",
		"uiName": "Landing Page Group XX",
		"description": "Content group of users' landing pages.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:previousContentGroupXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Grouping",
		"status": "PUBLIC",
		"uiName": "Previous Page Group XX",
		"description": "Refers to content group that was visited before another content group.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:contentGroupXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Grouping",
		"status": "PUBLIC",
		"uiName": "Page Group XX",
		"description": "The content group on a property. A content group is a collection of content providing a logical structure that can be determined by tracking code or page title/URL regex match, or predefined rules.",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userAgeBracket",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "PUBLIC",
		"uiName": "Age",
		"description": "Age bracket of users.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitorAgeBracket",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:userAgeBracket",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "DEPRECATED",
		"uiName": "Age",
		"description": "Age bracket of users.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:userGender",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "PUBLIC",
		"uiName": "Gender",
		"description": "Gender of users.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:visitorGender",
		"kind": "analytics#column",
		"attributes": {
		"replacedBy": "ga:userGender",
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "DEPRECATED",
		"uiName": "Gender",
		"description": "Gender of users.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:interestOtherCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "PUBLIC",
		"uiName": "Other Category",
		"description": "Indicates that users are more likely to be interested in learning about the specified category, and more likely to be ready to purchase.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:interestAffinityCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "PUBLIC",
		"uiName": "Affinity Category (reach)",
		"description": "Indicates that users are more likely to be interested in learning about the specified category.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:interestInMarketCategory",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Audience",
		"status": "PUBLIC",
		"uiName": "In-Market Segment",
		"description": "Indicates that users are more likely to be ready to purchase products or services in the specified category.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Revenue",
		"description": "The total revenue from AdSense ads.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseAdUnitsViewed",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Ad Units Viewed",
		"description": "The number of AdSense ad units viewed (requires integration with AdSense). An ad unit is a set of ads displayed as a result of one piece of the AdSense ad code. For details, see https://support.google.com/adsense/answer/32715?hl=en.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseAdsViewed",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Impressions",
		"description": "The number of AdSense ads viewed (requires integration with AdSense). Multiple ads can be displayed within an ad Unit.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseAdsClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Ads Clicked",
		"description": "The number of times AdSense ads on the site were clicked (requires integration with AdSense).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsensePageImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Page Impressions",
		"description": "The number of pageviews during which an AdSense ad was displayed (requires integration with AdSense). A page impression can have multiple ad Units.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense CTR",
		"description": "The percentage of page impressions resulted in a click on an AdSense ad (requires integration with AdSense).",
		"calculation": "ga:adsenseAdsClicks/ga:adsensePageImpressions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseECPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense eCPM",
		"description": "The estimated cost per thousand page impressions (requires integration with AdSense). It is the AdSense Revenue per 1,000 page impressions.",
		"calculation": "ga:adsenseRevenue/(ga:adsensePageImpressions/1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseExits",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Exits",
		"description": "The number of sessions ended due to a user clicking on an AdSense ad (requires integration with AdSense).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseViewableImpressionPercent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Viewable Impression %",
		"description": "The percentage of viewable impressions (requires integration with AdSense).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adsenseCoverage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Adsense",
		"status": "PUBLIC",
		"uiName": "AdSense Coverage",
		"description": "The percentage of ad requests that returned at least one ad (requires integration with AdSense).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Impressions",
		"description": "An ad impression is reported whenever an individual ad is displayed on the website. For example, if a page with two ad units is viewed once, we'll display two impressions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherCoverage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Coverage",
		"description": "Coverage is the percentage of ad requests that returned at least one ad. Generally, coverage can help you identify sites where the publisher account (AdSense, AdX, DFP) isn't able to provide targeted ads. (Ad Impressions / Total Ad Requests) * 100",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherMonetizedPageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Monetized Pageviews",
		"description": "This measures the total number of pageviews on the property that were shown with an ad from one of the linked publisher accounts (AdSense, AdX, DFP). Note that a single page can have multiple ad units.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherImpressionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Impressions / Session",
		"description": "The ratio of linked publisher account (AdSense, AdX, DFP) ad impressions to Analytics sessions (Ad Impressions / Analytics Sessions).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherViewableImpressionsPercent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Viewable Impressions %",
		"description": "The percentage of viewable ad impressions. An impression is considered a viewable impression when it has appeared within users' browsers and has the opportunity to be seen.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Clicks",
		"description": "The number of times ads from a linked publisher account (AdSense, AdX, DFP) were clicked on the site.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher CTR",
		"description": "The percentage of pageviews that resulted in a click on a linked publisher account (AdSense, AdX, DFP) ad.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Revenue",
		"description": "The total estimated revenue from all linked publisher account (AdSense, AdX, DFP) ads.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherRevenuePer1000Sessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher Revenue / 1000 Sessions",
		"description": "The total estimated revenue from all linked publisher accounts (AdSense, AdX, DFP) per 1,000 Analytics sessions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalPublisherECPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Publisher",
		"status": "PUBLIC",
		"uiName": "Publisher eCPM",
		"description": "The effective cost per thousand pageviews. It is the total estimated revenue from all linked publisher accounts (AdSense, AdX, DFP) per 1,000 pageviews.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Impressions",
		"description": "An Ad Exchange ad impression is reported whenever an individual ad is displayed on the website. For example, if a page with two ad units is viewed once, we'll display two impressions.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxCoverage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Coverage",
		"description": "Coverage is the percentage of ad requests that returned at least one ad. Generally, coverage can help identify sites where the Ad Exchange account isn't able to provide targeted ads. (Ad Impressions / Total Ad Requests) * 100",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxMonetizedPageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Monetized Pageviews",
		"description": "This measures the total number of pageviews on the property that were shown with an ad from the linked Ad Exchange account. Note that a single page can have multiple ad units.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxImpressionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Impressions / Session",
		"description": "The ratio of Ad Exchange ad impressions to Analytics sessions (Ad Impressions / Analytics Sessions).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxViewableImpressionsPercent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Viewable Impressions %",
		"description": "The percentage of viewable ad impressions. An impression is considered a viewable impression when it has appeared within users' browsers and has the opportunity to be seen.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Clicks",
		"description": "The number of times AdX ads were clicked on the site.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX CTR",
		"description": "The percentage of pageviews that resulted in a click on an Ad Exchange ad.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Revenue",
		"description": "The total estimated revenue from Ad Exchange ads.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxRevenuePer1000Sessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX Revenue / 1000 Sessions",
		"description": "The total estimated revenue from Ad Exchange ads per 1,000 Analytics sessions. Note that this metric is based on sessions to the site, not on ad impressions.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:adxECPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ad Exchange",
		"status": "PUBLIC",
		"uiName": "AdX eCPM",
		"description": "The effective cost per thousand pageviews. It is the Ad Exchange revenue per 1,000 pageviews.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpLineItemId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Line Item Id",
		"description": "The ID of the Google Ad Manager line item.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpLineItemName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Line Item Name",
		"description": "The name of the Google Ad Manager line item.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Impressions",
		"description": "A DFP ad impression is reported whenever an individual ad is displayed on the website. For example, if a page with two ad units is viewed once, we'll display two impressions (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpCoverage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Coverage",
		"description": "Coverage is the percentage of ad requests that returned at least one ad. Generally, coverage can help identify sites where the DFP account isn't able to provide targeted ads. (Ad Impressions / Total Ad Requests) * 100 (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpMonetizedPageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Monetized Pageviews",
		"description": "This measures the total number of pageviews on the property that were shown with an ad from the linked DFP account. Note that a single page can have multiple ad units (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpImpressionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Impressions / Session",
		"description": "The ratio of DFP ad impressions to Analytics sessions (Ad Impressions / Analytics Sessions) (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpViewableImpressionsPercent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Viewable Impressions %",
		"description": "The percentage of viewable ad impressions. An impression is considered a viewable impression when it has appeared within users' browsers and has the opportunity to be seen (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Clicks",
		"description": "The number of times DFP ads were clicked on the site (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM CTR",
		"description": "The percentage of pageviews that resulted in a click on an DFP ad (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Revenue",
		"description": "DFP revenue is an estimate of the total ad revenue based on served impressions (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpRevenuePer1000Sessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM Revenue / 1000 Sessions",
		"description": "The total estimated revenue from DFP ads per 1,000 Analytics sessions. Note that this metric is based on sessions to the site, not on ad impressions (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dfpECPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers",
		"status": "PUBLIC",
		"uiName": "GAM eCPM",
		"description": "The effective cost per thousand pageviews. It is the DFP revenue per 1,000 pageviews (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Impressions",
		"description": "Backfill Impressions is the sum of all AdSense or Ad Exchance ad impressions served as backfill through DFP. An ad impression is reported whenever an individual ad is displayed on the website. For example, if a page with two ad units is viewed once, we'll display two impressions (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillCoverage",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Coverage",
		"description": "Backfill Coverage is the percentage of backfill ad requests that returned at least one ad. Generally, coverage can help identify sites where the publisher account isn't able to provide targeted ads. (Ad Impressions / Total Ad Requests) * 100. If both AdSense and Ad Exchange are providing backfill ads, this metric is the weighted average of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillMonetizedPageviews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Monetized Pageviews",
		"description": "This measures the total number of pageviews on the property that were shown with at least one ad from the linked backfill account(s). Note that a single monetized pageview can include multiple ad impressions (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillImpressionsPerSession",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Impressions / Session",
		"description": "The ratio of backfill ad impressions to Analytics sessions (Ad Impressions / Analytics Sessions). If both AdSense and Ad Exchange are providing backfill ads, this metric is the sum of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillViewableImpressionsPercent",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Viewable Impressions %",
		"description": "The percentage of backfill ad impressions that were viewable. An impression is considered a viewable impression when it has appeared within the users' browsers and had the opportunity to be seen. If AdSense and Ad Exchange are both providing backfill ads, this metric is the weighted average of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Clicks",
		"description": "The number of times backfill ads were clicked on the site. If AdSense and Ad Exchange are both providing backfill ads, this metric is the sum of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill CTR",
		"description": "The percentage of backfill impressions that resulted in a click on an ad. If AdSense and Ad Exchange are both providing backfill ads, this metric is the weighted average of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillRevenue",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Revenue",
		"description": "The total estimated revenue from backfill ads. If AdSense and Ad Exchange are both providing backfill ads, this metric is the sum of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillRevenuePer1000Sessions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill Revenue / 1000 Sessions",
		"description": "The total estimated revenue from backfill ads per 1,000 Analytics sessions. Note that this metric is based on sessions to the site and not ad impressions. If both AdSense and Ad Exchange are providing backfill ads, this metric is the sum of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:backfillECPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick for Publishers Backfill",
		"status": "PUBLIC",
		"uiName": "GAM Backfill eCPM",
		"description": "The effective cost per thousand pageviews. It is the DFP Backfill Revenue per 1,000 pageviews. If both AdSense and Ad Exchange are providing backfill ads, this metric is the sum of the two backfill accounts (DFP linking enabled and Hide DFP Revenue not enabled).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:acquisitionCampaign",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Acquisition Campaign",
		"description": "The campaign through which users were acquired, derived from users' first session.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:acquisitionMedium",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Acquisition Medium",
		"description": "The medium through which users were acquired, derived from users' first session.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:acquisitionSource",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Acquisition Source",
		"description": "The source through which users were acquired, derived from users' first session.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:acquisitionSourceMedium",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Acquisition Source / Medium",
		"description": "The combined value of ga:userAcquisitionSource and ga:acquisitionMedium.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:acquisitionTrafficChannel",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Acquisition Channel",
		"description": "Traffic channel through which users were acquired. It is extracted from users' first session. Traffic channel is computed based on the default channel grouping rules (at view level if available) at the time of user acquisition.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:browserSize",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Browser Size",
		"description": "The viewport size of users' browsers. A session-scoped dimension, browser size captures the initial dimensions of the viewport in pixels and is formatted as width x height, for example, 1920x960.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:campaignCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Traffic Sources",
		"status": "PUBLIC",
		"uiName": "Campaign Code",
		"description": "For manual campaign tracking, it is the value of the utm_id campaign tracking parameter.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:channelGrouping",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Channel Grouping",
		"status": "PUBLIC",
		"uiName": "Default Channel Grouping",
		"description": "The Channel Group associated with an end user's session for this View (defined by the View's Channel Groupings).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:checkoutOptions",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Checkout Options",
		"description": "User options specified during the checkout process, e.g., FedEx, DHL, UPS for delivery options; Visa, MasterCard, AmEx for payment options. This dimension should be used with ga:shoppingStage (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:cityId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "City ID",
		"description": "Users' city ID, derived from their IP addresses or Geographical IDs. The city IDs are the same as the Criteria IDs found at https://developers.google.com/analytics/devguides/collection/protocol/v1/geoid.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:cohort",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Cohort",
		"description": "Name of the cohort to which a user belongs. Depending on how cohorts are defined, a user can belong to multiple cohorts, similar to how a user can belong to multiple segments.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortNthDay",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Day",
		"description": "Day offset relative to the cohort definition date. For example, if a cohort is defined with the first visit date as 2015-09-01, then for the date 2015-09-04, ga:cohortNthDay will be 3.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortNthMonth",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Month",
		"description": "Month offset relative to the cohort definition date. The semantics of this dimension differs based on whether lifetime value is requested or not. For a cohorts report not requesting lifetime value: This is the week offset from the cohort definition start date. For example, if cohort is defined as 2015-09-01 \u003c= first session date \u003c= 2015-09-30. Then, for 2015-09-01 \u003c= date \u003c= 2015-09-30, ga:cohortNthMonth = 0. 2015-10-01 \u003c= date \u003c= 2015-10-31, ga:cohortNthMonth = 2. and so on. For a cohorts request requesting lifetime value: ga:cohortNthMonth is calculated relative to the users acquisition date. It is not dependent on the cohort definition date. For example, if we define a cohort as 2015-10-01 \u003c= first session date \u003c= 2015-09-30. And a user was acquired on 2015-09-04. Then, for 2015-09-04 \u003c= date \u003c= 2015-10-04, ga:cohortNthMonth = 0 2015-10-04 \u003c= date \u003c= 2015-11-04, ga:cohortNthMonth = 1, and so on.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortNthWeek",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Week",
		"description": "Week offset relative to the cohort definition date. The semantics of this dimension differs based on whether lifetime value is requested or not. For a cohorts report not requesting lifetime value: This is the week offset from the cohort definition start date. For example, if cohort is defined as 2015-09-01 \u003c= first session date \u003c= 2015-09-07. Then, for 2015-09-01 \u003c= date \u003c= 2015-09-07, ga:cohortNthWeek = 0. 2015-09-08 \u003c= date \u003c= 2015-09-14, ga:cohortNthWeek = 1. etc. For a cohorts request requesting lifetime value: ga:cohortNthWeek is calculated relative to the users acquisition date. It is not dependent on the cohort definition date. For example, if we define a cohort as 2015-09-01 \u003c= first session date \u003c= 2015-09-07. And a user was acquired on 2015-09-04. Then, for 2015-09-04 \u003c= date\u003c= 2015-09-10, ga:cohortNthWeek = 0 2015-09-11 \u003c= date \u003c= 2015-09-17, ga:cohortNthWeek = 1",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:continentId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Continent ID",
		"description": "Users' continent ID, derived from users' IP addresses or Geographical IDs.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:countryIsoCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Country ISO Code",
		"description": "Users' country's ISO code (in ISO-3166-1 alpha-2 format), derived from their IP addresses or Geographical IDs. For example, BR for Brazil, CA for Canada.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dataSource",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Platform or Device",
		"status": "PUBLIC",
		"uiName": "Data Source",
		"description": "The data source of a hit. By default, hits sent from analytics.js are reported as \"web\" and hits sent from the mobile SDKs are reported as \"app\". These values can be overridden in the Measurement Protocol.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickAdvertiser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Advertiser (GA Model)",
		"description": "DBM advertiser name of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Advertiser ID (GA Model)",
		"description": "DBM advertiser ID of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickCreativeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Creative ID (GA Model)",
		"description": "DBM creative ID of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickExchange",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Exchange (GA Model)",
		"description": "DBM exchange name of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickExchangeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Exchange ID (GA Model)",
		"description": "DBM exchange ID of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickInsertionOrder",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Insertion Order (GA Model)",
		"description": "DBM insertion order name of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickInsertionOrderId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Insertion Order ID (GA Model)",
		"description": "DBM insertion order ID of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickLineItem",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Line Item NAME (GA Model)",
		"description": "DBM line item name of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickLineItemId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Line Item ID (GA Model)",
		"description": "DBM line item ID of the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickSite",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Site (GA Model)",
		"description": "DBM site name where the DBM creative was shown and clicked on for the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClickSiteId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Site ID (GA Model)",
		"description": "DBM site ID where the DBM creative was shown and clicked on for the DBM click matching the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventAdvertiser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Advertiser (CM360 Model)",
		"description": "DBM advertiser name of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Advertiser ID (CM360 Model)",
		"description": "DBM advertiser ID of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventCreativeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Creative ID (CM360 Model)",
		"description": "DBM creative ID of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventExchange",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Exchange (CM360 Model)",
		"description": "DBM exchange name of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventExchangeId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Exchange ID (CM360 Model)",
		"description": "DBM exchange ID of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventInsertionOrder",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Insertion Order (CM360 Model)",
		"description": "DBM insertion order name of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventInsertionOrderId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Insertion Order ID (CM360 Model)",
		"description": "DBM insertion order ID of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventLineItem",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Line Item (CM360 Model)",
		"description": "DBM line item name of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventLineItemId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Line Item ID (CM360 Model)",
		"description": "DBM line item ID of the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventSite",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Site (CM360 Model)",
		"description": "DBM site name where the DBM creative was shown and clicked on for the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmLastEventSiteId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Site ID (CM360 Model)",
		"description": "DBM site ID where the DBM creative was shown and clicked on for the last DBM event (impression or click within the DBM lookback window) associated with the Google Analytics session (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAdGroup",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Ad Group",
		"description": "DS Ad Group (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAdGroupId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Ad Group ID",
		"description": "DS Ad Group ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAdvertiser",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Advertiser",
		"description": "DS Advertiser (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAdvertiserId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Advertiser ID",
		"description": "DS Advertiser ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAgency",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Agency",
		"description": "DS Agency (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsAgencyId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Agency ID",
		"description": "DS Agency ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsCampaign",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Campaign",
		"description": "DS Campaign (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsCampaignId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Campaign ID",
		"description": "DS Campaign ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsEngineAccount",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Engine Account",
		"description": "DS Engine Account (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsEngineAccountId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Engine Account ID",
		"description": "DS Engine Account ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsKeyword",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Keyword",
		"description": "DS Keyword (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsKeywordId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Keyword ID",
		"description": "DS Keyword ID (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:experimentCombination",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Experiments",
		"status": "PUBLIC",
		"uiName": "Experiment ID with Variant",
		"description": "The user-scoped ID of the experiment and variant that users were exposed to during an experiment.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:experimentName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Content Experiments",
		"status": "PUBLIC",
		"uiName": "Experiment Name",
		"description": "The user-scoped name of the content experiment that users were exposed to when the metrics were reported.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionCreative",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion Creative",
		"description": "The creative content designed for a promotion (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion ID",
		"description": "The ID of the promotion (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion Name",
		"description": "The name of the promotion (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionPosition",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion Position",
		"description": "The position of the promotion on the web page or application screen (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:isTrueViewVideoAd",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Adwords",
		"status": "PUBLIC",
		"uiName": "TrueView Video Ad",
		"description": "A boolean, Yes or No, indicating whether the ad is an AdWords TrueView video ad.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:metroId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Metro Id",
		"description": "The three digit Designated Market Area (DMA) code from where traffic arrived, derived from users' IP addresses or Geographical IDs.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:nthHour",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Time",
		"status": "PUBLIC",
		"uiName": "Hour Index",
		"description": "The index for each hour in the specified date range. The index for the first hour of the first day (i.e., start-date) in the date range is 0, for the next hour 1, and so on.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:orderCouponCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Order Coupon Code",
		"description": "Code for the order-level coupon (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productBrand",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Brand",
		"description": "The brand name under which the product is sold (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productCategoryHierarchy",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Category (Enhanced Ecommerce)",
		"description": "The hierarchical category in which the product is classified (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productCategoryLevelXX",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Category Level XX",
		"description": "Level (1-5) in the product category hierarchy, starting from the top (Enhanced Ecommerce).",
		"minTemplateIndex": "1",
		"maxTemplateIndex": "5",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productCouponCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Coupon Code",
		"description": "Code for the product-level coupon (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productListName",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product List Name",
		"description": "The name of the product list in which the product appears (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productListPosition",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product List Position",
		"description": "The position of the product in the product list (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productVariant",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Variant",
		"description": "The specific variation of a product, e.g., XS, S, M, L for size; or Red, Blue, Green, Black for color (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:regionId",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Region ID",
		"description": "Users' region ID, derived from their IP addresses or Geographical IDs. In U.S., a region is a state, New York, for example. The region IDs are the same as the Criteria IDs listed at https://developers.google.com/analytics/devguides/collection/protocol/v1/geoid.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:regionIsoCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Region ISO Code",
		"description": "Users' region ISO code in ISO-3166-2 format, derived from their IP addresses or Geographical IDs.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:shoppingStage",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Shopping Stage",
		"description": "Various stages of the shopping experience that users completed in a session, e.g., PRODUCT_VIEW, ADD_TO_CART, CHECKOUT, etc. (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:subContinentCode",
		"kind": "analytics#column",
		"attributes": {
		"type": "DIMENSION",
		"dataType": "STRING",
		"group": "Geo Network",
		"status": "PUBLIC",
		"uiName": "Sub Continent Code",
		"description": "Users' sub-continent code in UN M.49 format, derived from their IP addresses or Geographical IDs. For example, 061 for Polynesia, 154 for Northern Europe.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:buyToDetailRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Buy-to-Detail Rate",
		"description": "Unique purchases divided by views of product detail pages (Enhanced Ecommerce).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:calcMetric_\u003cNAME\u003e",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Custom Variables or Columns",
		"status": "PUBLIC",
		"uiName": "Calculated Metric",
		"description": "The value of the requested calculated metric, where \u003cNAME\u003e refers to the user-defined name of the calculated metric. Note that the data type of ga:calcMetric_\u003cNAME\u003e can be FLOAT, INTEGER, CURRENCY, TIME, or PERCENT. For details, see https://support.google.com/analytics/answer/6121409.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:cartToDetailRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Cart-to-Detail Rate",
		"description": "Product adds divided by views of product details (Enhanced Ecommerce).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:cohortActiveUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Users",
		"description": "This metric is relevant in the context of ga:cohortNthDay/ga:cohortNthWeek/ga:cohortNthMonth. It indicates the number of users in the cohort who are active in the time window corresponding to the cohort nth day/week/month. For example, for ga:cohortNthWeek = 1, number of users (in the cohort) who are active in week 1. If a request doesn't have any of ga:cohortNthDay/ga:cohortNthWeek/ga:cohortNthMonth, this metric will have the same value as ga:cohortTotalUsers.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortAppviewsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Appviews per User",
		"description": "App views per user for a cohort.",
		"calculation": "ga:screenviews / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortAppviewsPerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Appviews Per User (LTV)",
		"description": "App views per user for the acquisition dimension for a cohort.",
		"calculation": "ga:screenviews / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortGoalCompletionsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Goal Completions per User",
		"description": "Goal completions per user for the acquisition dimension for a cohort.",
		"calculation": "ga:goalCompletionsAll / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortGoalCompletionsPerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Goal Completions Per User (LTV)",
		"description": "Goal completions per user for a cohort.",
		"calculation": "ga:goalCompletionsAll / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortPageviewsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Pageviews per User",
		"description": "Pageviews per user for a cohort.",
		"calculation": "ga:pageviews / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortPageviewsPerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Pageviews Per User (LTV)",
		"description": "Pageviews per user for the acquisition dimension for a cohort.",
		"calculation": "ga:pageviews / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortRetentionRate",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "User Retention",
		"description": "Cohort retention rate.",
		"calculation": "ga:cohortActiveUsers / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortRevenuePerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Revenue per User",
		"description": "Revenue per user for a cohort.",
		"calculation": "ga:transactions / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortRevenuePerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Revenue Per User (LTV)",
		"description": "Revenue per user for the acquisition dimension for a cohort.",
		"calculation": "ga:transactionRevenue / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortSessionDurationPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Session Duration per User",
		"description": "Session duration per user for a cohort.",
		"calculation": "ga:sessionDuration / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortSessionDurationPerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "TIME",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Session Duration Per User (LTV)",
		"description": "Session duration per user for the acquisition dimension for a cohort.",
		"calculation": "ga:sessionDuration / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortSessionsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Sessions per User",
		"description": "Sessions per user for a cohort.",
		"calculation": "ga:sessions / ga:cohortTotalUsers",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortSessionsPerUserWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Sessions Per User (LTV)",
		"description": "Sessions per user for the acquisition dimension for a cohort.",
		"calculation": "ga:sessions / ga:cohortTotalUsersWithLifetimeCriteria",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortTotalUsers",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Total Users",
		"description": "Number of users belonging to the cohort, also known as cohort size.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:cohortTotalUsersWithLifetimeCriteria",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Lifetime Value and Cohorts",
		"status": "PUBLIC",
		"uiName": "Users",
		"description": "This is relevant in the context of a request which has the dimensions ga:acquisitionTrafficChannel/ga:acquisitionSource/ga:acquisitionMedium/ga:acquisitionCampaign. It represents the number of users in the cohorts who are acquired through the current channel/source/medium/campaign. For example, for ga:acquisitionTrafficChannel=Direct, it represents the number users in the cohort, who were acquired directly. If none of these mentioned dimensions are present, then its value is equal to ga:cohortTotalUsers.",
		"addedInApiVersion": "4"
		}
	 },
	 {
		"id": "ga:dbmCPA",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 eCPA",
		"description": "DBM Revenue eCPA (Analytics 360 only, requires integration with DBM).",
		"calculation": "ga:dbmCost / ga:dbmConversions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmCPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 eCPC",
		"description": "DBM Revenue eCPC (Analytics 360 only, requires integration with DBM).",
		"calculation": "ga:dbmCost / ga:dbmClicks",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmCPM",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 eCPM",
		"description": "DBM Revenue eCPM (Analytics 360 only, requires integration with DBM).",
		"calculation": "ga:dbmCost / (ga:dbmImpressions / 1000)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 CTR",
		"description": "DBM CTR (Analytics 360 only, requires integration with DBM).",
		"calculation": "ga:dbmClicks / ga:dbmImpressions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Clicks",
		"description": "DBM Total Clicks (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmConversions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Conversions",
		"description": "DBM Total Conversions (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmCost",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Cost",
		"description": "DBM Cost (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 Impressions",
		"description": "DBM Total Impressions (Analytics 360 only, requires integration with DBM).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dbmROAS",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Bid Manager",
		"status": "PUBLIC",
		"uiName": "DV360 ROAS",
		"description": "DBM ROAS (Analytics 360 only, requires integration with DBM).",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll) / ga:dbmCost",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmCPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM CPC",
		"description": "DCM Cost Per Click (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM CTR",
		"description": "DCM Click Through Rate (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM Clicks",
		"description": "DCM Total Clicks (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmCost",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM Cost",
		"description": "DCM Total Cost (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM Impressions",
		"description": "DCM Total Impressions (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmMargin",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Campaign Manager",
		"status": "DEPRECATED",
		"uiName": "CM Margin",
		"description": "This metric is deprecated and will be removed soon. Please use ga:dcmROAS instead.",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmROAS",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM ROAS",
		"description": "DCM Return On Ad Spend (ROAS) (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dcmRPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Campaign Manager",
		"status": "PUBLIC",
		"uiName": "CM RPC",
		"description": "DCM Revenue Per Click (Analytics 360 only).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsCPC",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 CPC",
		"description": "DS Cost to advertiser per click (Analytics 360 only, requires integration with DS).",
		"calculation": "ga:dsCost/ga:dsClicks",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 CTR",
		"description": "DS Click Through Rate (Analytics 360 only, requires integration with DS).",
		"calculation": "ga:dsClicks/ga:dsImpressions",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Clicks",
		"description": "DS Clicks (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsCost",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Cost",
		"description": "DS Cost (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsImpressions",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Impressions",
		"description": "DS Impressions (Analytics 360 only, requires integration with DS).",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsProfit",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 Profit",
		"description": "DS Profit (Analytics 360 only, requires integration with DS).",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll - ga:dsCost)",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsReturnOnAdSpend",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 ROAS",
		"description": "DS Return On Ad Spend (Analytics 360 only, requires integration with DS).",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll) / ga:dsCost",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:dsRevenuePerClick",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "DoubleClick Search",
		"status": "PUBLIC",
		"uiName": "SA360 RPC",
		"description": "DS Revenue Per Click (Analytics 360 only, requires integration with DS).",
		"calculation": "(ga:transactionRevenue + ga:goalValueAll) / ga:dsClicks",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:hits",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Session",
		"status": "PUBLIC",
		"uiName": "Hits",
		"description": "Total number of hits for the view (profile). This metric sums all hit types, including pageview, custom event, ecommerce, and other types. Because this metric is based on the view (profile), not on the property, it is not the same as the property's hit volume.",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion CTR",
		"description": "The rate at which users clicked through to view the internal promotion (ga:internalPromotionClicks / ga:internalPromotionViews) - (Enhanced Ecommerce).",
		"calculation": "ga:internalPromotionClicks / ga:internalPromotionViews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion Clicks",
		"description": "The number of clicks on an internal promotion (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:internalPromotionViews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Internal Promotion Views",
		"description": "The number of views of an internal promotion (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localProductRefundAmount",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Product Refund Amount",
		"description": "Refund amount in local currency for a given product (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:localRefundAmount",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Local Refund Amount",
		"description": "Total refund amount in local currency for the transaction (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productAddsToCart",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Adds To Cart",
		"description": "Number of times the product was added to the shopping cart (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productCheckouts",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Checkouts",
		"description": "Number of times the product was included in the check-out process (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productDetailViews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Detail Views",
		"description": "Number of times users viewed the product-detail page (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productListCTR",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "PERCENT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product List CTR",
		"description": "The rate at which users clicked through on the product in a product list (ga:productListClicks / ga:productListViews) - (Enhanced Ecommerce).",
		"calculation": "ga:productListClicks / ga:productListViews",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productListClicks",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product List Clicks",
		"description": "Number of times users clicked the product when it appeared in the product list (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productListViews",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product List Views",
		"description": "Number of times the product appeared in a product list (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productRefundAmount",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Refund Amount",
		"description": "Total refund amount associated with the product (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productRefunds",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Refunds",
		"description": "Number of times a refund was issued for the product (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productRemovesFromCart",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Removes From Cart",
		"description": "Number of times the product was removed from the shopping cart (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:productRevenuePerPurchase",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Product Revenue per Purchase",
		"description": "Average product revenue per purchase (commonly used with Product Coupon Code) (ga:itemRevenue / ga:uniquePurchases) - (Enhanced Ecommerce).",
		"calculation": "ga:itemRevenue / ga:uniquePurchases",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:quantityAddedToCart",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Quantity Added To Cart",
		"description": "Number of product units added to the shopping cart (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:quantityCheckedOut",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Quantity Checked Out",
		"description": "Number of product units included in check out (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:quantityRefunded",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Quantity Refunded",
		"description": "Number of product units refunded (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:quantityRemovedFromCart",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Quantity Removed From Cart",
		"description": "Number of product units removed from a shopping cart (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:refundAmount",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Refund Amount",
		"description": "Currency amount refunded for a transaction (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:revenuePerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "CURRENCY",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Revenue per User",
		"description": "The total sale revenue (excluding shipping and tax) of the transaction divided by the total number of users.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:sessionsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "User",
		"status": "PUBLIC",
		"uiName": "Number of Sessions per User",
		"description": "The total number of sessions divided by the total number of users.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:totalRefunds",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "INTEGER",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Refunds",
		"description": "Number of refunds that have been issued (Enhanced Ecommerce).",
		"allowedInSegments": "true",
		"addedInApiVersion": "3"
		}
	 },
	 {
		"id": "ga:transactionsPerUser",
		"kind": "analytics#column",
		"attributes": {
		"type": "METRIC",
		"dataType": "FLOAT",
		"group": "Ecommerce",
		"status": "PUBLIC",
		"uiName": "Transactions per User",
		"description": "Total number of transactions divided by total number of users.",
		"allowedInSegments": "false",
		"addedInApiVersion": "3"
		}
	 }
]


class DimensionsAndMetrics():
	"""docstring for DimensionsAndMetrics"""
	def __init__(self):
		super(DimensionsAndMetrics, self).__init__()
		self.ids = {}
		self.names = {}
		self.getIDs()
		self.getNames()


	def getIDs(self):
		"""docstring for getIDs"""
		for item in data:
			# print(item['id'],item['attributes']['uiName'])
			self.ids[item['id']] = item['attributes']['uiName']


	def getNames(self):
		"""docstring for getNames"""
		for item in data:
			self.names[item['attributes']['uiName']] = item['id']


