from urllib.request import urlopen

# the site url with list of all disorders
url = "https://www.ninds.nih.gov/health-information/disorders"

# storing result from urlopen which returns a HTTPResponse object
page = urlopen(url)

# test to see if it works
page

# Extracting the page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Test Check below returns entire page
#print(html)

div_index = html.find("<div>")


dis_container_start = html.find('<div class="view-content row">')
dis_container_end = html.find('<div id="block-ninds-bootstrap-webform')
# not nexessary -> disorders = html.find('<span class="field-content">')
#storing the search into a variable
dis_var_start = '<a href="/health-information/disorders/'
dis_var_end = '</a>'
#End index string values
ninds_list = []
x = dis_container_start
start_disorders = html.find(dis_var_start, x)
end_disorders = html.find(dis_var_end, start_disorders)
ninds_list.append(html[start_disorders:end_disorders])
for i in range(276) :
    x = end_disorders
    start_disorders = html.find(dis_var_start, x)
    end_disorders = html.find(dis_var_end, start_disorders)
    ninds_list.append(html[start_disorders:end_disorders])
    #print(ninds_list)
    #print(x)
    #print(len(ninds_list))
print(ninds_list)
# print each element on a separate line)
print(*ninds_list, sep='\n')

import json
print('Starting')
with open(r"C:\Users\Juniper\Desktop\git\phd_proj\Python_proj\names.json", 'w') as fp:
        
    json.dump(ninds_list, fp)
print('complete')

with open(r"C:\Users\Juniper\Desktop\git\phd_proj\Python_proj\names.json", 'rb') as fp:
    stored_n = json.load(fp)

    print(stored_n)

