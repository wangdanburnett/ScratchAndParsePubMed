import urllib2
import re
import time
import json
import os
import random

count=0
left= len(range(2015,2000,-1))
for year in xrange(2015,2000,-1):#year from 2000 to 2015 
	count+=1
	left-=1
	print 'Year:',str(year-1),'to',str(year)
	print 'Number:',str(count)
	print 'Left:',str(left)
	t=time.time()
	url="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&mindate="+str(year-1)+"/01/01&maxdate="+str(year)+"/01/01&retmax=10000000"
	outfile_name='id_list_per_year/'+str(year-1)+'_to_'+str(year)+'.json'
	if os.path.exists(outfile_name) and os.path.isfile(outfile_name) and os.path.getsize(outfile_name):
		print 'Existed!'
		pass
	else:
		f = urllib2.urlopen(url).read()
		pattern=re.compile('<Id>([\d]+)</Id>')
		id_list=pattern.findall(f)
		print 'Count:',str(len(id_list))
		outfile=open(outfile_name,'w')
		data=json.dumps(id_list,indent=4,sort_keys=True,encoding='utf-8',ensure_ascii=False)
		outfile.write(data)
		outfile.close()

	print 'Consuming time:',str(time.time()-t)
	print
	
	#time.sleep(random.randint(0,10))
