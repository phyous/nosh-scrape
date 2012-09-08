__author__ = 'pyoussef'
import lxml.html
import urllib2
from dict_unicode_writer import DictUnicodeWriter
import sys
import re

# Check input parameters
if sys.argv.__len__() != 2:
    print("Usage: python nosh_scrape.py <url>")
    sys.exit()
url = sys.argv[1]
csv_name_match = re.findall("(\\d+)", sys.argv[1])
if not csv_name_match:
    print("Url doesn't end with resturant id (%s):\nEx: %s" % (url, "http://www.nosh.com/restaurant/<id>"))
    sys.exit()
csv_path = csv_name_match[-1] + ".csv"

# Request url html
try:
    response = urllib2.urlopen(url)
except urllib2.HTTPError as e:
    print("Error connecting to url (%s):\n%s" % (url, str(e)))
    sys.exit()
except (ValueError, urllib2.URLError) as e:
    print("Error parsing url, please check formatting matches (http|s)://<address>/<resource>")
    sys.exit()
except:
    print "Unexpected error, please contact developer:\n", sys.exc_info()[0]
body = response.fp.read()

# Find menu items
doc = lxml.html.fromstring(body)
menu_items = doc.xpath("//td[@class='ow-check-in-m']")
if not menu_items:
    print("No menu found for url (%s)" % (url))
    sys.exit()

# write menu item names & descriptions to csv
print("Writing to file: %s ..." % (csv_path))
f = open(csv_path,'wb')
f.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
csvWriter = DictUnicodeWriter(f,["name","description"])
for item in menu_items:
    name = item.xpath("div[@class='ow-check-in-mi']")[0].getchildren()[0].text
    description_node = item.xpath("div[@class='ow-check-in-review']")
    if description_node == []:
        description = ""
    else:
        description = description_node[0].getchildren()[0].text
    csvWriter.writerow({"name": unicode(name), "description": unicode(description)})