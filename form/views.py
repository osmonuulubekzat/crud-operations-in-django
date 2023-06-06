from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import get_object_or_404


# Create your views here.
def Index(request):
    data = Product.objects.all()
    context = {"context": data}
    return render(request, "index.html", context)


def My_Forms(request):
    forms = Forms()
    if request.method == "POST":
        myforms = Forms(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect("index")
    return render(request, "form.html", {"form": forms})


def Update(request, pk):
    data = Product.objects.get(id=pk)
    forms = Forms(instance=data)

    if request.method == "POST":
        this_forms = Forms(request.POST, instance=data)
        if this_forms.is_valid():
            this_forms.save()
            return redirect("index")
    context = {"form": forms}
    return render(request, "form.html", context)


def Delete(request, pk):
    data = get_object_or_404(Product, pk=pk)
    # data = Product.objects.get(id=pk)
    data.delete()
    # if request.method == "POST":
    #     data.delete()
    return redirect("index")
