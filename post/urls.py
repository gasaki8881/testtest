
from django.urls import path

from . import views


urlpatterns = [
	path('', views.TopPageListView.as_view(), name='home'),
	path('all_novels', views.NovelListView.as_view(), name='all_novels'),
	path('<int:title>/all_chapters', views.ChapterListView.as_view(), name='all_chapters'),
	path('chapter_contents/<int:pk>', views.ChapterContentsView.as_view(), name='chapter_contents'),
	path('diary', views.DiaryTopView.as_view(), name='diary_top'),
	path('diary/contents/<int:pk>', views.DiaryContentsView.as_view(), name='diary_contents'),
	path('diary/by_category/<int:category>', views.DiaryByCategoryView.as_view(), name='diary_by_categry'),
	path('diary/archive/<int:year>', views.DiaryByYearView.as_view(), name='diary_archive'),
	path('diary/archive/<int:year>/<int:month>', views.DiaryByYearAndMonthView.as_view(month_format='%m'), name='diary_archive'),
	path('contact', views.ContactFormView.as_view(), name='contact'),
	path('contact/result', views.ContactResultView.as_view(), name='contact_result'),
]
