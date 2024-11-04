import json
from django.shortcuts import render
from .forms import ContactForm,ProductForm
from django.http import HttpResponse
from .models import Project,Product,Blog,CustomerFeedback,Client
def index(request):
    indexp = Product.objects.all()[:4]
    blogp = Blog.objects.all()[:4]
    feedback = CustomerFeedback.objects.all()[:3]
    projectp = Project.objects.all()[:3]
    
    clients = Client.objects.all()
    context = {
        "is_index": True,
        "indexp": indexp,
        "blogp": blogp,
        "feedback": feedback,
        "projectp": projectp,
        "clients": clients,
        
    }
    return render(request, "web/index.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

def projects(request):
    projects = Project.objects.all()
    context = {"is_projects": True,
               "projects": projects}
    return render(request, "web/project.html", context)

def products(request):
    products = Product.objects.all()
    context = {"is_products": True,
               "products": products}
    return render(request, "web/products.html", context)

def blog_grid(request):
    blog = Blog.objects.all()
    context = {"is_products": True,
               "blog": blog}
    return render(request, "web/blog_grid.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogp = Blog.objects.all()
    context = {
        "is_blog": True,
        "blog": blog,
        "blogp": blogp,
    }
    return render(request, "web/blog_details.html", context)

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        "is_blog": True,
        "project": project,
    }
    return render(request, "web/project_details.html", context)

def product_detail(request, slug):
    form = ProductForm(request.POST or None)
    product = Product.objects.get(slug=slug)
     
    if request.method == "POST":
        if form.is_valid():
            product_enquiry = form.save(commit=False)
            product_enquiry.product = product
            product_enquiry.save()
           
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    
    context = {
            "is_product": True,
            "product": product,
            "form": form,
        }
    return render(request, "web/product_details.html", context)



