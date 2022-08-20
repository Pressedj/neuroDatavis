from urllib.request import urlopen

# the site url with lsit of all disorders
url = "https://www.ninds.nih.gov/health-information/disorders"
 
# storing result from urlopen which returns a HTTPResponse object
page = urlopen(url)

#test to see if it works
page

#Extracting the page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

#Check returns entire page
print(html)

div_index = html.find("<div>")

#variables that store index number where the container for disorders starts and ends
dis_container_start = html.find('<div class="view-content row">')
dis_container_end = html.find('<div id="block-ninds-bootstrap-webform')
# not nexessary -> disorders = html.find('<span class="field-content">')
#storing the search into a variable
dis_var_start = '<a href="/health-information/disorders/'
dis_var_end = '</a>'
ninds_list = []
start_disorders = html.find(dis_var, dis_container_start)
end_disorders = html.find('</a>', start_disorders)
ninds_list.append(html[start_disorders:end_disorders])

for start_disorders in dis_container_end:

    ninds_list.append[start_disorders:end_disorders]


start_disorders = html.find(dis_var, dis_container_start)
end_disorders = html.find('</a>', start_disorders)
dis_scraper = html[start_disorders:end_disorders]

#function
dis_container_start = html.find('<div class="view-content row">')
dis_container_end = html.find('<div id="block-ninds-bootstrap-webform')
# not nexessary -> disorders = html.find('<span class="field-content">')
#storing the search into a variable
dis_var_start = '<a href="/health-information/disorders/'
dis_var_end = '</a>'
#End index string values
ninds_list = []
x = dis_container_start
start_disorders = html.find(dis_var, x)
end_disorders = html.find('</a>', start_disorders)
ninds_list.append(html[start_disorders:end_disorders])
for start_disorders in dis_container_end:
    x = end_disorders
    start_disorders = html.find(dis_var, x)
    end_disorders = html.find('</a>', start_disorders)
    ninds_list.append(html[start_disorders:end_disorders])
