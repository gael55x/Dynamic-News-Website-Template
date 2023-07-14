from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

import re
import markdown
import json

from .models import User, Post_Category, Post, ApprovedPost



def index(request):
    # Retrieve all approved posts
    approved_posts = ApprovedPost.objects.select_related('post').all()

    # Retrieve the latest 5 approved posts marked as trending
    trending_posts = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True).order_by('-time_posted')[:5]

    # Retrieve the latest 9 approved posts
    latest_posts = ApprovedPost.objects.select_related('post').order_by('-time_posted')[:9]

    # Retrieve the latest 4 approved posts
    all_posts = ApprovedPost.objects.select_related('post').order_by('-time_posted')[:4]

    context = {
        'approved_posts': approved_posts,
        'latest_posts': latest_posts,  # Updated variable name
        'trending_posts': trending_posts,
        'all_posts': all_posts,
    }

    return render(request, 'news/index.html', context)



"""Render posts in Category1"""


def Category1(request):
    # Retrieve the latest 5 approved posts marked as trending in the Category1 category
    trending_posts_category1 = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True, post__category__title='Category1'
    ).order_by('-time_posted')[:5]

    # Retrieve all approved posts in the Category1 category
    all_posts_category1 = ApprovedPost.objects.select_related('post').filter(
        post__category__title='Category1'
    ).order_by('-time_posted')

    paginator = Paginator(all_posts_category1, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trending_posts_category1': trending_posts_category1,
        'page_obj': page_obj,
    }

    return render(request, 'news/category1.html', context)


"""Render posts in Category2"""


def Category2(request):
    # Retrieve the latest 5 approved posts marked as trending in the category2
    trending_posts_category2 = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True, post__category__title='Category2'
    ).order_by('-time_posted')[:5]

    # Retrieve all approved posts in the category2
    all_posts_category2 = ApprovedPost.objects.select_related('post').filter(
        post__category__title='Category2'
    ).order_by('-time_posted')

    paginator = Paginator(all_posts_category2, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trending_posts': trending_posts_category2,
        'page_obj': page_obj,
    }

    return render(request, 'news/category2.html', context)


"""Render posts in Category3"""


def Category3(request):
    # Retrieve the latest 5 approved posts marked as trending in Category3
    trending_posts = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True, post__category__title='Category3'
    ).order_by('-time_posted')[:5]

    # Retrieve all approved posts in Category3
    all_posts = ApprovedPost.objects.select_related('post').filter(
        post__category__title='Category3'
    ).order_by('-time_posted')

    paginator = Paginator(all_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trending_posts': trending_posts,
        'page_obj': page_obj,
    }

    return render(request, 'news/category3.html', context)


"""Render posts in Category4"""


def Category4(request):
    # Retrieve the latest 5 approved posts marked as trending in Category4
    trending_posts_category4 = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True, post__category__title='Category4'
    ).order_by('-time_posted')[:5]

    # Retrieve all approved posts in Category4
    all_posts_category4 = ApprovedPost.objects.select_related('post').filter(
        post__category__title='Category4'
    ).order_by('-time_posted')

    paginator = Paginator(all_posts_category4, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trending_posts': trending_posts_category4,
        'page_obj': page_obj,
    }

    return render(request, 'news/category4.html', context)


"""Render posts in Category5"""


def Category5(request):
    # Retrieve the latest 5 approved posts marked as trending in Category5
    trending_posts_category5 = ApprovedPost.objects.select_related('post').filter(
        post__if_trending=True, post__category__title='Category5'
    ).order_by('-time_posted')[:5]

    # Retrieve all approved posts in Category5
    all_posts_category5 = ApprovedPost.objects.select_related('post').filter(
        post__category__title='Category5'
    ).order_by('-time_posted')

    paginator = Paginator(all_posts_category5, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'trending_posts': trending_posts_category5,
        'page_obj': page_obj,
    }

    return render(request, 'news/category5.html', context)



@login_required
def Create_Post(request):
    if request.method == 'POST':
        # Process the submitted form data
        category_id = request.POST['category']
        title = request.POST['title']
        if_trending = request.POST.get('is_trending', False) == 'on'
        image = request.FILES['image']
        introduction = request.POST['introduction']
        details = request.POST['details']

        # Create a new post instance
        category = Post_Category.objects.get(id=category_id)
        post = Post(
            user=request.user,
            category=category,
            if_trending=if_trending,
            title=title,
            image=image,
            introduction=introduction,
            details=details,
            admin_evaluation=True,
        )
        post.save()

        # Render the post pending approval
        return render(request, 'news/pending_post.html', {'post_id': post.id})

    else:
        # Retrieve the categories for the form dropdown
        categories = Post_Category.objects.all()

        context = {'categories': categories}
        return render(request, 'news/create_article.html', context)


"""For pending articles waiting for approval"""


@login_required
def Post_pending(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse({'message': 'Post not found'}, status=404)

        if post.admin_evaluation:
            response_data = {
                'message': 'Post is pending evaluation by admins. Please contact the News staff for the pending evaluation. Thank you for your patience',
                'title': post.title,
                'category': post.category.title
            }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({'message': 'Post is not pending evaluation'}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=400)



"""Profile"""


@login_required
def Profile(request):
    user = request.user
    date_joined = user.date_joined

    # Get the latest posts created by the user
    user_posts = Post.objects.filter(user=user).order_by('-id')
    
    # Get the draft posts pending evaluation and not yet approved
    draft_posts = Post.objects.filter(
        user=user, admin_evaluation=True, approvedpost__isnull=True
    ).order_by('-id')

    # Get the approved posts
    approved_posts = Post.objects.filter(user=user).exclude(
        approvedpost__isnull=True).order_by('-id')

    # Get the details of the first approved post (if available)
    first_approved_post = approved_posts.first()
    details_html = ""
    related_content = []
    if first_approved_post:
        approved_post = get_object_or_404(ApprovedPost, post=first_approved_post)
        details_html = markdown_to_html(approved_post.post.details)
        related_content = Post.objects.filter(
            category=approved_post.post.category,
            approvedpost__isnull=False
        ).exclude(id=approved_post.post.id).order_by('?')[:3]
    
    # Pagination for user_posts
    user_posts_paginator = Paginator(user_posts, 10)
    user_posts_page_number = request.GET.get('user_posts_page')
    user_posts_page = user_posts_paginator.get_page(user_posts_page_number)

    # Pagination for draft_posts
    draft_posts_paginator = Paginator(draft_posts, 10)
    draft_posts_page_number = request.GET.get('draft_posts_page')
    draft_posts_page = draft_posts_paginator.get_page(draft_posts_page_number)

    # Pagination for approved_posts
    approved_posts_paginator = Paginator(approved_posts, 10)
    approved_posts_page_number = request.GET.get('approved_posts_page')
    approved_posts_page = approved_posts_paginator.get_page(
        approved_posts_page_number)

    context = {
        'user': user,
        'user_posts': user_posts_page,
        'draft_posts': draft_posts_page,
        'approved_posts': approved_posts_page,
        'date_joined': date_joined,
    }

    return render(request, 'news/profile.html', context)



"""Article(post) details in News"""


def Post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    related_content = Post.objects.filter(
        category=post.category,
        approvedpost__isnull=False
    ).exclude(id=post.id).order_by('?')[:3]

    # Convert post.details from Markdown to HTML
    details_html = markdown_to_html(post.details)

    # Case: draft post
    try:
        approved_post1 = ApprovedPost.objects.get(post_id=post_id)
        time_posted = approved_post1.time_posted
    except ObjectDoesNotExist:
        time_posted = "N/A"

    context = {
        'author': post.user.username,
        'post_id': post_id,
        # Assuming a OneToOneField relationship exists
        'time_posted': time_posted,
        'category': post.category.title,
        'title': post.title,
        'image': post.image.url,
        'introduction': post.introduction,
        'details': details_html,
        'related_content': related_content,
    }

    # Case: Delete Post
    if request.method == 'POST' and post.user == request.user:
        # Store the title and category before deleting the post
        deleted_title = post.title
        deleted_category = post.category.title

        # Delete the post
        post.delete()

        # Use f-string formatting to include the deleted post details in the success message
        success_message = f'Your article titled "{deleted_title}" in the category "{deleted_category}" has been deleted successfully.'

        return render(request, 'news/success.html', {'message': success_message})

    return render(request, 'news/post_details.html', context)


def registration_check(request):
    # Check the registration status of the user
    if request.user.is_active and request.user.if_journalist:
        return JsonResponse({'status': 'success', 'message': 'Registration successful! You can now log in.'})
    else:
        return JsonResponse({'status': 'pending', 'message': 'Your registration is pending approval by the administrators. Please call the News staff for your registration approval. Then, you will receive an email notification from the News staff once your account is approved. Thank you for your patience.'})


def register(request):
    if request.method == 'POST':
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "news/register.html", {
                "message": "Passwords must match."
            })

        # Check if a user with the same username already exists
        username = request.POST["username"]
        if User.objects.filter(username=username).exists():
            return render(request, "news/register.html", {
                "message": "Username already exists."
            })

        # Create a new User instance
        user = User(
            username=request.POST["username"],
            if_journalist=False,
        )
        user.set_password(password)
        user.is_active = False  # Inactive until approved by admins
        user.save()

        # Notify admins for approval
        notify_admins(request, user)

        # Render the registration_pending.html template
        return render(request, 'news/registration_pending.html')
    else:
        return render(request, 'news/register.html')


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None and user.if_journalist:
            login(request, user)
            return redirect('news:index')
        else:
            # Check if user exists
            if not User.objects.filter(username=username).exists():
                messages.error(request, "No such user exists.")
            else:
                messages.error(request, "Invalid username and/or password.")
            return render(request, 'news/login.html')
    else:
        return render(request, 'news/login.html')

# General purpose function

# requires strict optimization and testing


def markdown_to_html(markdown_text):
    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)

    # Apply stylistic effect to the first letter of the essay
    html = re.sub(
        r'^(.*?<p>)(.)(.*)',
        r'\1<span class="first-letter">\2</span>\3',
        html,
        count=1,
        flags=re.DOTALL
    )

    return html


def notify_admins(request, user):
    message = f"A new user, {user.username}, has registered and is pending approval."
    messages.info(request, message)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("news:index"))


def delete_account(request):
    pass

def change_password(request):
    pass