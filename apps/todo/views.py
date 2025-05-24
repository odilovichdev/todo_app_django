from django.shortcuts import render
from django.views import View
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class ExampleGETView(View):
    def get(self,request):
        return HttpResponse("Hello, This is a GET request")


@method_decorator(csrf_exempt, "dispatch")
class ExampleQueryParamView(View):
    def get(self, request, *args, **kwargs):
        name = request.GET.get("name", "Default GET")
        return HttpResponse(f"Hello, This is a Query param: GET: {name}")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "Default POST")
        return HttpResponse(f"Hello, This is a Query param: POST: {name}")

@method_decorator(csrf_exempt, name="dispatch")
class ExamplePOSTHeaderView(View):
    def post(self, request, *args, **kwargs):
        headers = request.headers
        print(headers.get("User-Agent", "Unknown"))
        print(headers.get("Accept-Language", "Unknown"))
        return HttpResponse(f"Hello, This is a Header view: {headers}")


@method_decorator(csrf_exempt, name="dispatch")
class ExamplePATCHPathParamView(View):
    def patch(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        name = kwargs.get("name")
        print(f"User_id: {user_id}")
        print(f"Name: {name}")
        return HttpResponse(f"Hello, This is a Path param: args: {args}, kwargs: {kwargs}")


@method_decorator(csrf_exempt, name="dispatch")
class ExamplePUTBodyView(View):

    # @csrf_exempt
    # def dispatch(self, request, *args, **kwargs):
    #     # Custom logic before dispatching to the method
    #     print("Custom logic before dispatch")
    #     return super().dispatch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        body = request.body.decode("UTF-8")
        print(body)
        return HttpResponse(f"Hello, This is a put body: {body}")
