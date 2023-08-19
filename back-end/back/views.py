from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from back.serializers import CourseSerializer, ExamSerializer, SectorSerializer, SubjectSerializer, YearSerializer
from .models import Exam, Year, Sector, Subject, Course

@api_view(['GET'])
def get_years_with_sectors(request):
    years = Year.objects.all()
    data = []
    for year in years:
        sectors = Sector.objects.filter(year=year)
        sectors_data = [{"id": sector.id, "name": sector.name} for sector in sectors]
        year_data = {
            "id": year.id,
            "name": year.name,
            "sectors": sectors_data
        }
        data.append(year_data)
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def get_subjects_by_sector(request, sector_id):
    try:
        sector = Sector.objects.get(id=sector_id)
        subjects = Subject.objects.filter(sector=sector)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    except Sector.DoesNotExist:
        return Response(status=404)
    
@api_view(['GET'])
def get_courses_and_exams_by_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        courses = Course.objects.filter(subject=subject)
        exams = Exam.objects.filter(subject=subject)

        course_serializer = CourseSerializer(courses, many=True)
        exam_serializer = ExamSerializer(exams, many=True)

        data = {
            'courses': course_serializer.data,
            'exams': exam_serializer.data
        }

        return Response(data)
    except Subject.DoesNotExist:
        return Response(status=404)
    
@api_view(['GET'])
def get_years(request):
    years = list(Year.objects.values())
    return JsonResponse(years, safe=False)

@api_view(['GET'])
def get_subjects(request):
    subjects = list(Subject.objects.values())
    return JsonResponse(subjects, safe=False)

@api_view(['GET'])
def get_courses(request):
    courses = list(Course.objects.values())
    return JsonResponse(courses, safe=False)

@api_view(['GET'])
def get_sectors(request):
    sectors = list(Sector.objects.values())
    return JsonResponse(sectors, safe=False)

@api_view(['GET'])
def get_exams(request):
    Exams = list(Exam.objects.values())
    return JsonResponse(Exams, safe=False)

@api_view(['GET'])
def get_year(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    serializer = YearSerializer(year)
    return Response(serializer.data)


@api_view(['GET'])
def get_sector(request, sector_id):
    sector = get_object_or_404(Sector, id=sector_id)
    serializer = SectorSerializer(sector)
    return Response(serializer.data)

@api_view(['GET'])
def get_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    serializer = SubjectSerializer(subject)
    return Response(serializer.data)

@api_view(['GET'])
def get_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
@api_view(['GET'])
def get_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    serializer = CourseSerializer(exam)
    return Response(serializer.data)

def url_list(request):
    urls = [
        ('Admin', reverse('admin:index')),
        ('Years', reverse('get_years')),
        ('Subjects', reverse('get_subjects')),
        ('Courses', reverse('get_courses')),
        ('Sectors', reverse('get_sectors')),
        ('Exams', reverse('get_Exams')),
        ('Years with Sectors', reverse('get_years_with_sectors')),
        ('get subjects by sector', reverse('get_subjects_by_sector', args=[1])),
        ('get courses and exams by subject', reverse('get_courses_and_exams_by_subject', args=[1])),
        # Add more URLs as needed
    ]
    return render(request, 'url_list.html', {'urls': urls})
