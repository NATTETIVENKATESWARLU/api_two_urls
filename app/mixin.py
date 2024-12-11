from django.core.serializers import serialize
import json
from app.models import *

from django.http import HttpResponse

class mxied_serializers(object):
    def serializers(self,qr):
        json_data=serialize("json",qr)
        data=json.loads(json_data)
        data1=[]
        for i in data:
            data1.append(i["fields"])

        json_data=json.dumps(data1)
        return json_data



class http_data(object):
    def datacontent_httpresops(self,json_data,status=200):
        return HttpResponse(json_data,content_type="application/json",status=status)
    

    def get_objects_all(self,id):
        try:
            emp=employees.objects.get(eno=id)
        except Exception:
            emp=None
        return emp
    