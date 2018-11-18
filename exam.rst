=========================================
 Senior Software Engineer Technical Test
=========================================

#. Language choosed - Python 3 (List prime numbers between 2 an 100)

#. Detect a loop in a LinkedList

	* Function for doing this without memory consumption for this case, must consider validation for a possible loops before insertion of new nodes. Likewise, protect the way the "ref" values are accessed for preventing loops.

Code repository using `Github <https://github.com/jianleon/AlertLogicTechnicalTest>`_.

#. Considering the information granted and the main goal of the project, we must consider for this case:

	* Server capacity for data extraction

		- How much stress can the server process.
		- How fast the server respond to basic queries for data extraction
		- How much data can be extracted when server is not being used and when it is. This information can let us to know, how much information we can process during the day and how much at night.

	* Data structure in Databases:

		- What possible structure has the fields in DB (Existent columns and fields data types).
		- Which fields where saved in a mandatory way and which did not. (Knowking this, we can create validation cases when the information is being extracted)
		- Validate data formats. (Ex. "People's names" with no numbers or special characters",
		"Phone numbers" with only numbers or considering the plus (+) for indicatives, ...)

	* Possible milestones

	 	1- Create stress tests to servers and document the results when information is being extracted. (Stress tests must be made when server is being used normally and when it is not). Use SQL queries with big limit value until find a very low response from server.

	 	2- Using documentation as guide. Define a serie of SQL queries for extract information from servers (Possibly SELECT * with defined limit). As a result, document the structure found in the tables fields from servers. (Depending of the team size, we can destinate some devs for each server). Additionally, document the structure of the data found, its structure, and the ways it was saved before. 

	 	3- Define an structure for the local database that will save the data. Considering the documentation made in step 2.

	 	4- According with the result of the possible server structure:
	 		- Start coding funtions that process the possible fields that can be find in queries. (Validate all the formats found and convert them to the required for our database if neccessary)
	 		- Exclude or clean data with missing information.
	 		- Define requests to extract maximum of data that can be get in a simple request without risk of timeouts or exhaust the server cursors.
	 		- Define a log and notification system, for not considered data found in queries.
	 		- After success data validation, we can insert or update into our local database, the proccessed rows.

	 	5- Define a log and a notification system to advice when a no considered case is found.

	 	6- Define a schedule job for data extraction considering the results in the stress tests. (Data should start being extracted from the oldest to the newest) This can be made with unix crontab.

	 	7- Monitor the db actual state for asserting that is being pull correctly.

	 * Considerations

	 	- What to do if a not considered case is found. (Should the system keep processing and just report the novelty or it should stop saving the last processed field until validate the non considered case).
	 	- The scheduler job must be located in a server with very good capacity for huge processing.
	 	- With the COUNT from SQL, we can estimate how much time could it take to extract all the information, in an ideal environment. So, according to the time for pulling the information in the project, we can estimate if with our capacity is enough to extract all the information in given time or we should consider distribute processing for extracting the information.
