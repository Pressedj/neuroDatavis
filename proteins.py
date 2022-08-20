from urllib.request import urlopen

# the site url with list of all disorders
url = r'file:///C:\Users\short\Desktop\phd_proj\Python_proj\HPA.htm'
#url2 = "https://www.proteinatlas.org/search/protein_class:Nervous+system+diseases"

# storing result from urlopen which returns a HTTPResponse object
page = urlopen(url)
#page2 = urlopen(url2)

# test to see if it works
page
#page2

## Extracting the page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

#html_bytee = page2.read()
#html2 = html_bytee.decode("utf-8")
# Check returns entire page
#print(html)
#Works

#Now to the nitty gritty
div_index = html.find('class="tda"')
#div_index2 = html2.find('class="tda"')

print(div_index)
#print(div_index2)


protein_container_start = html.find('class="tda"><b')
print(protein_container_start)
protein_container_end = html.find('</a></td><td class="center nowrap">')
print(protein_container_end)
print(html[protein_container_start:protein_container_end])
# Result
#class="tda"><b>AANAT</b></a></td><td class="wrap maxwidth">
#<a href="/ENSG00000129673-AANAT" class="tda">Aralkylamine N-acetyltransferase
#Getting the list
pro_list = []
startQuery = 'class="tda"><b'
endQuery = '</a></td><td class="center nowrap">'
startIndex = html.find(startQuery)
x = startIndex
start_protein = html.find(startQuery, x)
print(start_protein)
end_protein = html.find(endQuery, start_protein)
print(end_protein)
pro_list.append(html[start_protein:end_protein])
for i in range(48) :
    x = end_protein
    start_protein = html.find(startQuery, x)
    print(start_protein)
    end_protein = html.find(endQuery, start_protein)
    print(end_protein)
    pro_list.append(html[start_protein:end_protein])
print(pro_list)
#    ninds_list.append(html[start_disorders:end_disorders])
#    #print(ninds_list)
#    #print(x)
#    #print(len(ninds_list))
#dis_container_end = html.find('<div id="block-ninds-bootstrap-webform')
## not nexessary -> disorders = html.find('<span class="field-content">')
##storing the search into a variable
#dis_var_start = '<a href="/health-information/disorders/'
#dis_var_end = '</a>'
##End index string values
#ninds_list = []
#x = dis_container_start
#start_disorders = html.find(dis_var_start, x)
#end_disorders = html.find(dis_var_end, start_disorders)
#ninds_list.append(html[start_disorders:end_disorders])

#print (ninds_list)