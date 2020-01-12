from urllib import parse
from django import template
from django.shortcuts import resolve_url
from post.models import Diary_Category, Diary_Contents 
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('diary_archives.html')
def render_diary_links():
	return {
		'dates': Diary_Contents.objects.dates('created_at', 'month', order='DESC'),
		'category_list' : Diary_Category.objects.all()
	}
	print(category_list)


@register.simple_tag
def get_return_link(request):
	top_page = resolve_url('diary_top')
	referer = request.environ.get('HTTP_REFERER')
	if referer:
		parse_result = parse.urlparse(referer)
		if request.get_host() == parse_result.netloc:
			return referer
	return top_page
