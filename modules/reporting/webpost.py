    # Copyright (C) 2010-2014 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import json

from lib.cuckoo.common.abstracts import Report
from bson.objectid import ObjectId
# from lib.cuckoo.common.exceptions import CuckooReportError

import requests

class ComplexEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, ObjectId):
             return str(obj)
         return json.JSONEncoder.default(self, obj)

class Webpost(Report):
    """POST analysis results to url in JSON format."""
    
    def post(self,fileId,reportData):
        
        data= {
            'fileId': fileId,
            'reportData': reportData
        }
        
        headers = {'content-type': 'application/json'}
        encoding = self.options.get("encoding", "utf-8")
        
        r = requests.post(self.URL_ENDPOINT, data=json.dumps(data, sort_keys=False, encoding=encoding, cls=ComplexEncoder), headers=headers)
        r.raise_for_status()

    def run(self, results):

        if 'file' not in results['target']:
                return

        self.URL_ENDPOINT = self.options.get("url", "")
        fileitems = results['target']['file']
        fileId    = fileitems['name']

        # try:
        self.post(fileId,results)
        # except Exception, e:
        #     print "Failed to submit webpost report to %s for %s: %s" % (self.URL_ENDPOINT,fileId,e)
        #     pass