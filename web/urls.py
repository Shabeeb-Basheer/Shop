from django.urls import path, include
from . import views
from django.views.generic import TemplateView
 
app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("project/", views.projects, name="project"),
    path("products/", views.products, name="products"),
    path("blog-grid/", views.blog_grid, name="blog-grid"),
    path("blog_details/<str:slug>/", views.blog_details, name="blog_details"),
    path("project_detail/<str:slug>/", views.project_detail, name="project_detail"),
    path("product_details/<str:slug>/", views.product_detail, name="product_details"),
    
   
]