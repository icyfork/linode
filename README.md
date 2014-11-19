## Description

Linode DynDNS Updater by Jed Smith <jed@jedsmith.org>.

The environment support was adapted by Anh K. Huynh <kyanh@theslinux.org>.

## Requirement

Requires Python 3.0 or above.

## Usage

0. You'll probably have to edit the shebang above.

1. In the Linode DNS manager, edit your zone (must be master) and create
   an A record for your home computer.  You can name it whatever you like;
   I call mine 'home'.  Fill in 0.0.0.0 for the IP.

2. Save it.

3. Go back and edit the A record you just created. Make a note of the
   ResourceID in the URI of the page while editing the record.

4. Gather `ResourceID`: the resource ID that contains the 'home' record
   you created above. If the URI while editing that A record looks like this:

   ````
   http://linode.com/members/dns/resource_aud.cfm?DomainID=98765&ResourceID=123456
   ````

   You want 123456. The API key MUST have write access to this resource ID.

6. Get the domain ID is required  by `domain.resource.list`.
   You get this ID by using the `domain.list` action.

   ````
   $ curl -s "https://api.linode.com/?api_key=YOUR_KEY&action=domain.list"
   {
     "DOMAIN" : "example.net",
     "DOMAINID" : 654321,
     "STATUS" : 1
   }
   ````

6.  Now you export the environments and use them

    ````
    $ export DOMAIN_ID=654321
    $ export RESOURCE_ID=12345
    $ export API_KEY=YOUR_KEY
    $ export DEBUG=Yes
    $ python LinodeDynDNS.py
    ````

## License

Public domain
