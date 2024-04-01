from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import asyncio
async def index(request):
    
    # return HttpResponse("this is home")
    # array = ['1', '3', '2', '4']
    # array.sort(reverse=True)
    # txt = "Nguyen Hoang Nam"
    # x = txt.count("Nam")
    # print(x)
    # print(array)
    # print(len(array))
    # print(json.dumps({"name": "John", "age": 30}))
    # print(json.dumps(["apple", "bananas"]))
    # print(json.dumps(("apple", "bananas")))
    # print(json.dumps("hello"))
    # print(json.dumps(42))
    # print(json.dumps(31.76))
    # print(json.dumps(True))
    # print(json.dumps(False))
    # print(json.dumps(None))
    
    # x = {
    # "name": "John",
    # "age": 30,
    # "married": True,
    # "divorced": False,
    # "children": ("Ann","Billy"),
    # "pets": None,
    # "cars": [
    #     {"model": "BMW 230", "mpg": 27.5},
    #     {"model": "Ford Edge", "mpg": 24.1}
    # ]
    # }

    # print(json.dumps(x))

    # mystr = "banana"
    # myit = iter(mystr)

    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    # print(next(myit))
    return render(request,"home.html")


