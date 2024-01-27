from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home_page(Request):
   msg=''
   if(Request.method=="POST"):
     c=Contact()
     c.name=Request.POST.get('name')
     c.email=Request.POST.get('email')
     c.phone=Request.POST.get('phone')
     c.subject=Request.POST.get('subject')
     c.message=Request.POST.get('message')
     c.save()
     msg="Done"
   gallery=Gallery.objects.all()
   paginator = Paginator(gallery, 12)  # Show 6 products per page
   page = Request.GET.get('page')

   try:
       gallery = paginator.page(page)
   except PageNotAnInteger:
       # If page is not an integer, deliver the first page.
       gallery = paginator.page(1)
   except EmptyPage:
        # If page is out of range, deliver the last page of results.
        gallery = paginator.page(paginator.num_pages)
   data=Blog.objects.all()
   paginator = Paginator(data, 5)  # Show 10 posts per page

   page_number = Request.GET.get('page')
   page_posts = paginator.get_page(page_number)
   current_page = page_posts.number
   total_pages = paginator.num_pages
   page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
   return render(Request,'index.html',{'msg':msg,'page_posts':page_posts,'page_range': page_range,'gallery':gallery})

def blog_details(Request,title,id):
   data=Blog.objects.get(id=id)
   return render(Request,'single.html',{'data':data})
