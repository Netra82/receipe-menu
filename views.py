from django.shortcuts import render
import json

json_file = open(r'C:\Users\Admin\Desktop\Djangooo\recipe j\recipe.json')
json_data = json_file.read()
recipes = json.loads(json_data)
# recipes = data['recipes']

def recipes_view(request):
    context = {
        'recipes' : recipes
    }
    return render(request,'index.html',context)

def recipe_view(request,id):
    recipe = recipes[id-1]
    context = {
        'recipe' : recipe
    }
    return render(request,'recipe.html',context)






# Create your views here.
