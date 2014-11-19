## Description

Linode DynDNS Updater
by Jed Smith <jed@jedsmith.org>

For customers of Linode that use the Linode DNS manager.
Released into the public domain.

Requires Python 3.0 or above.  Python 2.6 may work.
Contains directions in the script (which you'll have to edit anyway).

## Usage

# First, the resource ID that contains the 'home' record you created above. If
# the URI while editing that A record looks like this:
#
#  linode.com/members/dns/resource_aud.cfm?DomainID=98765&ResourceID=123456
#                                                                    ^
# You want 123456. The API key MUST have write access to this resource ID.
#
RESOURCE = os.getenv("RESOURCE_ID")

# The domain ID is required  by `domain.resource.list`. You get this ID
# by using the `domain.list` action.
#
DOMAINID = os.getenv("DOMAIN_ID")
#
#
# Your Linode API key.  You can generate this by going to your profile in the
# Linode manager.  It should be fairly long.
#
KEY = os.getenv("API_KEY")

