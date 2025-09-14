from django.shortcuts import render
from datetime import date

all_posts =[
    {
        "slug":"learning-django",
        "title":"django course",
        "author":"ali pourfereydoon",
        "image":"python.png",
        "date":date(2025, 5,5),
        "short_description":"this is django course in rctnetwork",
        "content":"ali pourfereydoon is a programer"
    },
        {
        "slug":"learning-python",
        "title":"python course",
        "author":"ali pourfereydoon2",
        "image":"django.png",
        "date":date(2025,11,14),
        "short_description":"this is python course in rctnetwork",
        "content":"ali pourfereydoon is a programer"
    },
    {
        "slug":"learning-java",
        "title":"java course",
        "author":"ali pourfereydoon2",
        "image":"django.png",
        "date":date(2025,11,16),
        "short_description":"this is java course in rctnetwork",
        "content":"ali pourfereydoon is a programer"
    }
]

def get_date(post):
    return post['date']


def index(request):
    sorted_post= sorted(all_posts , key=get_date)
    lateste_post = sorted_post[-2:]
    return render(request,'blog/index.html',{"post":lateste_post})

def posts(request):
    return render(request,'blog/all-posts.html') 

def singlepost(request,slug):
    return render(request,'blog/post_detail.html')       
