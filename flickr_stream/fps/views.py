import cjson
import logging
import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView



logger = logging.getLogger(__name__)

def shorten_text(text):
    """ reduce the words in the title """
    if len(text) < 20:
        return text
    return ' '.join(text.split()[0:5])

def reduce_tags(tags):
    """some of the tags are to long so lets filter"""
    return [tag for tag in tags.split() if len(tag) < 8]

def fetch_photos(tags=None):
    """fetch flickr feed and format it, filter by tags if supplied.
    This should be updated to handle connection errors and bad json data"""
    url_tags = ''
    if tags:
        url_tags = '&tags=%s' % tags
    response = requests.get(settings.FLICKR_URL + url_tags) 

    flickr_data = []
    for row in cjson.decode(response.text)['items']:
        flickr_data.append({
            'title': shorten_text(row['title']),
            'title_full': row['title'],
            'link': row['link'],
            'author': row['link'].split('/')[-3],
            'tags': reduce_tags(row['tags']),
            'image': row['media']['m']
        })
    return flickr_data

def PhotosJSON(request):
    """json approch, i am just returning the html so i can make changes in a single place"""
    return HttpResponse(
        cjson.encode(fetch_photos(request.GET.get('tags'))),
        content_type='application/json')

class PhotosView(TemplateView):
    """partial view for access via ajax"""
    template_name = 'photo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PhotosView, self).get_context_data(*args, **kwargs)
        context['feed'] = fetch_photos(self.request.GET.get('tags'))
        return context

class HomeView(TemplateView):
    """the main page"""
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['feed'] = fetch_photos(self.request.GET.get('tags'))
        context['tags'] = self.request.GET.get('tags', '')
        return context
