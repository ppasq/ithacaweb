from django import template
from django.conf import settings

from ithacaweb.blog.models import BlogPage
from ithacaweb.people.models import PersonPage

register = template.Library()


@register.simple_tag
def get_popular_tags(model):
    return model.get_popular_tags()


# settings value
@register.simple_tag
def get_googe_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.simple_tag
def get_next_sibling_by_order(page):
    sibling = page.get_next_siblings().live().first()

    if sibling:
        return sibling.specific


@register.simple_tag
def get_prev_sibling_by_order(page):
    sibling = page.get_prev_siblings().live().first()

    if sibling:
        return sibling.specific


@register.simple_tag
def get_next_sibling_blog(page):
    sibling = BlogPage.objects.filter(date__lt=page.date).order_by('-date').live().first()
    if sibling:
        return sibling.specific


@register.simple_tag
def get_prev_sibling_blog(page):
    sibling = BlogPage.objects.filter(date__gt=page.date).order_by('-date').live().last()
    if sibling:
        return sibling.specific


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.filter
def content_type(value):
    return value.__class__.__name__.lower()



# Person feed for home page
@register.inclusion_tag('ithacaweb/tags/homepage_people_listing.html', takes_context=True)
def homepage_people_listing(context, count=3):
    people = PersonPage.objects.filter(live=True).order_by('?')[:count]
    return {
        'people': people,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Blog feed for home page
@register.inclusion_tag('ithacaweb/tags/homepage_blog_listing.html', takes_context=True)
def homepage_blog_listing(context, count=6):
    blog_posts = BlogPage.objects.live().in_menu().order_by('-date')[:count]
    return {
        'blog_posts': blog_posts,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Work feed for home page
@register.inclusion_tag('ithacaweb/tags/homepage_work_listing.html', takes_context=True)
def homepage_work_listing(context, count=3):
    work = WorkPage.objects.filter(live=True)[:count]
    return {
        'work': work,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



# Format times e.g. on event page
@register.filter
def time_display(time):
    # Get hour and minute from time object
    hour = time.hour
    minute = time.minute

    # Convert to 12 hour format
    if hour >= 12:
        pm = True
        hour -= 12
    else:
        pm = False
    if hour == 0:
        hour = 12

    # Hour string
    hour_string = str(hour)

    # Minute string
    if minute != 0:
        minute_string = "." + str(minute)
    else:
        minute_string = ""

    # PM string
    if pm:
        pm_string = "pm"
    else:
        pm_string = "am"

    # Join and return
    return "".join([hour_string, minute_string, pm_string])
