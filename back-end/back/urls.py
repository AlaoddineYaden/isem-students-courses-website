from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf.urls.static import static

from back import settings
from .views import get_courses_and_exams_by_subject, get_subjects_by_sector, get_years_with_sectors, url_list
from back.views import get_course, get_courses, get_exam, get_exams, get_sector, get_sectors, get_subject, get_subjects, get_year, get_years

urlpatterns = [
    path('url_list/', url_list, name='url_list'),
    path('', lambda request: redirect('admin/')),
    path('admin/', admin.site.urls),

    path('get_years_with_sectors/', get_years_with_sectors, name='get_years_with_sectors'),
    path('get_subjects_by_sector/<int:sector_id>/', get_subjects_by_sector, name='get_subjects_by_sector'),
    path('get_courses_and_exams_by_subject/<int:subject_id>/', get_courses_and_exams_by_subject, name='get_courses_and_exams_by_subject'),
 
    path('years/', get_years, name='get_years'),
    path('subjects/', get_subjects, name='get_subjects'),
    path('courses/', get_courses, name='get_courses'),
    path('sectors/', get_sectors, name='get_sectors'),
    path('Exams/', get_exams, name='get_Exams'),

    path('year/<int:year_id>/', get_year, name='get_year'),
    path('sector/<int:sector_id>/', get_sector, name='get_sector'),
    path('subject/<int:subject_id>/', get_subject, name='get_subject'),
    path('course/<int:course_id>/', get_course, name='get_course'),
    path('exam/<int:exam_id>/', get_exam, name='get_exam'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


