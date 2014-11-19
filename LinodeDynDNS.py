#!/usr/bin/env python
#
# Easy Python3 Dynamic DNS
# By Jed Smith <jed@jedsmith.org> 4/29/2009
# This code and associated documentation is released into the public domain.
#
try:
	import os
	from json import load
	from urllib.parse import urlencode
	from urllib.request import urlretrieve
except Exception as excp:
	exit("Couldn't import the standard library. Are you running Python 3?")

RESOURCE = os.getenv("RESOURCE_ID")
DOMAINID = os.getenv("DOMAIN_ID")
KEY = os.getenv("API_KEY")
GETIP = "http://myip.dnsdynamic.com/"
API = "https://api.linode.com/?api_key={0}&resultFormat=JSON"
DEBUG = os.getenv("DEBUG") or False

def execute(action, parameters):
	# Execute a query and return a Python dictionary.
	uri = "{0}&action={1}".format(API.format(KEY), action)
	if parameters and len(parameters) > 0:
		uri = "{0}&{1}".format(uri, urlencode(parameters))
	if DEBUG:
		print("-->", uri)
	file, headers = urlretrieve(uri)
	if DEBUG:
		print("<--", file)
		print(headers, end="")
		print(open(file).read())
		print()
	json = load(open(file), encoding="utf-8")
	if len(json["ERRORARRAY"]) > 0:
		err = json["ERRORARRAY"][0]
		raise Exception("Error {0}: {1}".format(int(err["ERRORCODE"]),
			err["ERRORMESSAGE"]))
	return load(open(file), encoding="utf-8")

def ip():
	if DEBUG:
		print("-->", GETIP)
	file, headers = urlretrieve(GETIP)
	if DEBUG:
		print("<--", file)
		print(headers, end="")
		print(open(file).read())
		print()
	return open(file).read().strip()

def main():
	try:
		res = execute("domain.resource.list", {"ResourceID": RESOURCE, "DomainID": DOMAINID})["DATA"]
		if(len(res)) == 0:
			raise Exception("No such resource?".format(RESOURCE))
		public = ip()
		res = res[0]
		if res["TARGET"] != public:
			old = res["TARGET"]
			request = {
				"ResourceID": res["RESOURCEID"],
				"DomainID": res["DOMAINID"],
				"Name": res["NAME"],
				"Type": res["TYPE"],
				"Target": public,
				"TTL_Sec": res["TTL_SEC"]
			}
			execute("domain.resource.update", request)
			print("OK {0} -> {1}".format(old, public))
			return 1
		else:
			print("OK")
			return 0
	except Exception as excp:
		print("FAIL {0}: {1}".format(type(excp).__name__, excp))
		return 2

if __name__ == "__main__":
	exit(main())
