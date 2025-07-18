from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from skills.models import AddSkills
from reviewsapp.models import Review
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def browse(request):
    sort = request.GET.get('sort', 'username')
    order = request.GET.get('order', 'asc').lower()

    valid_sorts = ['title', 'category', 'average_rating', 'calculated_rating', 'review_count']
    if sort not in valid_sorts:
        sort = 'title'
    if order not in ['asc', 'desc']:
        order = 'asc'

    sort_key = sort if order == 'asc' else f'-{sort}'
    skills = AddSkills.objects.select_related('user') \
        .annotate(calculated_rating=Avg('reviews__rating'), review_count=Count('reviews'))\
        .order_by(sort_key.replace('average_rating', "average_rating").replace('calculated_rating', 'calculated_rating'))
    
    paginator = Paginator(skills, 50)
    page_number = request.GET.get('page', 1)

    try:
        skills_page = paginator.page(page_number)
    except PageNotAnInteger:
        skills_page = paginator.page(1)
    except EmptyPage:
        skills_page = paginator.page(paginator.num_pages)

    print("Requested sort:", sort, "order:", order)
    return render(request, 'browse/browse.html', {
        'skills': skills_page,
        'current_sort': sort,
        'current_order': order,
    })

def skill_view(request, username=None, skill_name=None):
    user = get_object_or_404(User, username=username)
    
    skills_qs = AddSkills.objects.filter(user=user)

    if skill_name:
        skill = get_object_or_404(skills_qs, title=skill_name)
        return render(request, 'browse/skill_detail.html', {
            'user': user,
            'skill': skill,
        })
    else:
        return render(request, 'browse/skills_by_user.html',{
            'user': user,
            'skills': skills_qs,
        })
    
def reverse_skill_view(request, title, username=None):
    skill = get_object_or_404(AddSkills, title=title)

    users_qs = User.objects.filter(addskills_set=skill)

    if username:
        user = get_object_or_404(users_qs, username=username)
        return render(request, 'browse/skill_detail.html', {
            'user': user,
            'skill': skill,
        })

    return render(request, 'browse/user_by_skill.html', {
        'skill': skill,
        'users': users_qs,
    })

def users_by_skill(request, slug):
    skills_qs = AddSkills.objects.filter(slug=slug)

    skills_qs = get_list_or_404(AddSkills, slug=slug)

    users = User.objects.filter(userOffer__slug=slug).distinct()
    skill_ref = skills_qs[0]

    return render(request, 'browse/users_by_skill.html', {
        'skill': skill_ref,
        'users': users,
        'rows': skills_qs
    })