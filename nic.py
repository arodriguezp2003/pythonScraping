import urllib2
from bs4 import BeautifulSoup
import os



class NicChile():
	def trabajar(self):
		print "scraping NIC"
		of = open('domain.text', 'w')
		url = 'https://www.nic.cl/registry/Ultimos.do?t=1m'

		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page)

		du = soup.findAll("table")[1].findAll("tr")

		for dato in du:
			if dato.find("a"):
				of.write(dato.find("a").text.encode("utf-8")+'\n')
				
		

