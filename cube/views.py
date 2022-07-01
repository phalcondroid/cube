from django.shortcuts import render, redirect
from .models import ShapeEntity

def index(request, shape_id = 1):
  shape_list = ShapeEntity.objects.all()
  shape = ShapeEntity.objects.get(pk = shape_id)
  context = {
      'shape_list': shape_list,
      'shape': shape
  }
  return render(request, 'cube/index.html', context)

def save(request, shape_id):
  # raise Exception("jaja -> " + str(request.POST.get('check_new', False)))
  if (request.POST.get('check_new', False) == "1"):
    shape = ShapeEntity()
  else:
    shape = ShapeEntity.objects.get(pk = shape_id)

  shape.name = request.POST['name']
  shape.width = request.POST['width']
  shape.height = request.POST['height']
  shape.depth = request.POST['depth']
  shape.save()
  return redirect("/cube/" + str(shape.id))
