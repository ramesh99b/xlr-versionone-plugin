#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys, traceback
from versionone.VersionOneClient import VersionOneClient

try:
   data = {}
   v1Client = VersionOneClient.create_v1Client( versionOneServer )
   v1Client.updateStoryStatus( ticket, status )
   whereClause="Number='%s'" % ticket
   results = v1Client.getStories( whereClause )
   asset = results['Assets'][0]
   data['Name'] = asset['Attributes']['Name']['value']
   data['Number'] = asset['Attributes']['Number']['value']
   data['Status'] = asset['Attributes']['Status.Name']['value']
   print( data )
except :
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)
   # End try