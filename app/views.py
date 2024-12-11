from django.shortcuts import render
from django.views.generic import View
#-------------------------------------------------------------------------------------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#-------------------------------------------------------------------------------------------------------------------------------
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from app.models import *
from app.mixin import *
import json
#-------------------------------------------------------------------------------------------------------------------------------
from app.utils import *
import requests
from app.forms import *

@method_decorator(csrf_exempt,name="dispatch")
class cbv_json(http_data,mxied_serializers,View):
    def get(self,request,*args,**kwargs):
        emp=employees.objects.all()
        json_data=self.serializers(emp)
        return HttpResponse(json_data,content_type="application/json")
    
    
    def post(self,request,*args,**kwargs):
        data=request.body
        user=valid_data(data)
        if not user:
            dict=json.dumps({"msg":"some error data"})
            return self.datacontent_httpresops(dict,status=404)
        
        form=employee_data(json.loads(data))

        if form.is_valid():
            form.save(commit=True)
            dict=json.dumps({"msg":"resours stored succesfully"})
            return self.datacontent_httpresops(dict)
        if form.errors:
            dict=json.dumps(form.errors)
            return self.datacontent_httpresops(dict,status=404)


#------------------------------------------------------------------------------------------------------------------------------------

@method_decorator(csrf_exempt,name="dispatch")
class cbv_json1(http_data,mxied_serializers,View):

    def get(self,request,id,*args,**kwargs):
        try:
            emp=employees.objects.get(eno=id)
        except Exception:
            json_data=json.dumps({"msg":"id is not avaliable"})
            return self.datacontent_httpresops(json_data)
        
        json_data=self.serializers([emp,])
        return self.datacontent_httpresops(json_data)
    



    def put(self,request,id,*args,**kwargs):
        emp=self.get_objects_all(id)
        if emp is None:
            json_data=json.dumps({"msg":"id is not avalle"})
            return self.datacontent_httpresops(json_data,status=400)
        data=request.body
        user=valid_data(data)
        if not user:
            json_data=json.dumps({"msg":"please provide json data"})
            return self.datacontent_httpresops(json_data,status=400)
        prives_data=json.loads(data)
        current_data={
            "eno":emp.eno,
            "ename":emp.ename,
            "esal":emp.esal,
            "eaddress":emp.eaddress,
        }
        current_data.update(prives_data)
        form=employee_data(current_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            dict=json.dumps({"msg":"resours stored succesfully"})
            return self.datacontent_httpresops(dict)
        if form.errors:
            dict=json.dumps(form.errors)
            return self.datacontent_httpresops(dict,status=404)
        

    
    def delete(self,request,id,*args,**kwargs):
        emp=self.get_objects_all(id)
        if emp is None:
            json_data=json.dumps({"msg":"id is not avalle"})
            return self.datacontent_httpresops(json_data,status=400)
        #t=emp.delete() return type is tuple
        #print(t)
        status=emp.delete()[0]
        if status==1:
            json_data=json.dumps({"msg":"deleted successfuly"})
            return self.datacontent_httpresops(json_data)
        
        json_data=json.dumps({"msg":"not ableto delete try again"})
        return self.datacontent_httpresops(json_data,status=400)
    

    
