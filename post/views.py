from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView, YearArchiveView, MonthArchiveView
from . models import Novel, Chapter, Diary_Category, Diary_Contents
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.



class TopPageListView(ListView):
	model = Diary_Contents
	template_name = 'home.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['recommend_novel1'] = Novel.objects.get(pk = 1)
		context['recommend_novel2'] = Novel.objects.get(pk = 2)
		return context
	def get_queryset(self):
		return Diary_Contents.objects.order_by('created_at').reverse()[:5]

class NovelListView(ListView):
	model = Novel
	template_name = 'all_novels.html'


class ChapterListView(ListView):
	model = Chapter
	template_name = 'all_chapters.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['target_novel'] = Novel.objects.get(pk = self.kwargs.get('title'))
		return context
	def get_queryset(self):
		return Chapter.objects.filter(title= self.kwargs.get('title'))


class ChapterContentsView(TemplateView):
	template_name = 'chapter_contents.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		target_chapter = Chapter.objects.get(pk = self.kwargs.get('pk'))
		context['target_novel'] = Novel.objects.get( title = target_chapter.title )
		target_novel_title = target_chapter.title
		
		before_chapter_id = target_chapter.chapter_id -1
		next_chapter_id = target_chapter.chapter_id +1
		
		try:
			context['before_chapter'] = Chapter.objects.get(title = target_novel_title, chapter_id = before_chapter_id)
		except (ObjectDoesNotExist):
			context['before_chapter'] = None
		
		try:
			context['next_chapter'] = Chapter.objects.get(title = target_novel_title, chapter_id = next_chapter_id)
		except (ObjectDoesNotExist):
			context['next_chapter'] = None
		
		context['target_chapter'] = target_chapter
		return context



class DiaryTopView(ListView):
	model = Diary_Contents
	template_name = 'diary.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['diary_filter'] = "diary_top"
		return context
	
	def get_queryset(self):
		return Diary_Contents.objects.order_by('created_at').reverse()[:5]


class DiaryContentsView(DetailView):
	model = Diary_Contents
	template_name = 'diary_contents.html'



class DiaryByCategoryView(ListView):
	model = Diary_Contents
	template_name = 'diary.html'
	paginate_by = 5
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['diary_filter'] = "category"
		return context
	
	def get_queryset(self):
		return Diary_Contents.objects.filter(category = self.kwargs.get('category')).order_by('created_at').reverse()



class DiaryByYearView(YearArchiveView):
	model = Diary_Contents
	date_field = 'created_at'
	template_name = 'diary.html'
	paginate_by = 5
	make_object_list = True
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['diary_filter'] = "year"
		return context


class DiaryByYearAndMonthView(MonthArchiveView):
	model = Diary_Contents
	date_field = 'created_at'
	template_name = 'diary.html'
	paginate_by = 5
	make_object_list = True
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['diary_filter'] = "yearAndMonth"
		return context


class ContactFormView(FormView):
	template_name = 'contact_form.html'
	form_class = ContactForm
	success_url = reverse_lazy('contact_result')

	def form_valid(self, form):
		form.send_email()
		return super().form_valid(form)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['contact_result'] = ""
		return context


class ContactResultView(FormView):
	template_name = 'contact_form.html'
	form_class = ContactForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['contact_result'] = "問い合わせ正常終了"
		return context
