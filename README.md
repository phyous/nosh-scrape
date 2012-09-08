nosh-scrape
=====

My first python program.
Created using Python 2.7.1.

This is a python script that can be run from the command line that grabs the menu items from Nosh restaurant pages.
Examples include: http://www.nosh.com/restaurant/2630123, http://www.nosh.com/restaurant/2659001

The script takes a restaurant url as an argument, fetches the html from the page, parses just the menu item
information out and writes it to a .csv file. Menu item name is the first value in the csv row, and the
description (if it exists), is the second value. An output file in the same directory named after the id of the
restaurant will be generated.

**Usage Instructions**

1. Install pip using instructions here:
>http://www.pip-installer.org/en/latest/installing.html

2. Install required packages using pip
>pip install -r requirements.txt

3. Run script using nosh.com restaurant url
>python nosh_scrape.py http://www.nosh.com/restaurant/2630123

4. Output file generated is the id of the restaurant
>cat 2630123.csv

**Example Error cases**

* No id found
```text
python nosh_scrape.py www.google.com
Url doesn't end with resturant id (www.google.com):
Ex: http://www.nosh.com/restaurant/<id>
```

* Bad url
```text
python nosh_scrape.py bad.url.23232
Error parsing url, please check formatting matches (http|s)://<address>/<resource>
```

* Server error
```text
python nosh_scrape.py http://www.nosh.com/restaurant/1337
Error connecting to url (http://www.nosh.com/restaurant/1337):
HTTP Error 500: Internal Server Error
```