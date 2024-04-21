*Requires Python 3.11.0 (might work with other versions but who knows 🙉)

How to use:

	1. Do a "pip install -r requirements. txt" (preferably on a venv).
	2. Run "python main.py" on your terminal of preference.



Notes: This server has only 4 routes, they are:


	/ac_info/get/all_entries ->  gets all the entries on the db
	/ac_info/get/first_entry -> gets the first entry from the db
	/ac_info/get/last_entry -> gets the last entry from the db
	/ac_info/get/new_entry -> adds a new entry to the db


** You can edit the host:port location by changing the variables in ./configurations/server_config.py

