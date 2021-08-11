import pytest
from django.urls import reverse

from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-list')
    resp = api_client.get(url)
    course_id = resp.json()[0].get('id')

    assert resp.status_code == 200
    assert len(resp.data) == 1
    assert Course(id=course_id) == course[0]


@pytest.mark.django_db
def test_get_courses(api_client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)

    assert resp.status_code == 200
    assert len(resp.data) == 3


@pytest.mark.django_db
def test_filters_courses_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)

    course_id = resp.json()[0].get('id')
    course_filter = Course.objects.filter(id=course_id)

    assert resp.status_code == 200
    assert len(resp.data) == 3
    assert courses[0].id == course_filter[0].id


@pytest.mark.django_db
def test_filters_courses_name(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)

    course_name = resp.json()[0].get('name')
    course_filter = Course.objects.filter(name=course_name)

    assert resp.status_code == 200
    assert len(resp.data) == 3
    assert courses[0].name == course_filter[0].name


@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        'name': 'Python'
    }
    url = reverse('courses-list')
    resp = api_client.post(url, data=data)

    assert resp.status_code == 201
    assert resp.data['name'] == 'Python'


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    data = {
        'name': 'Python'
    }
    courses = course_factory(_quantity=1)
    url = reverse('courses-list')
    resp = api_client.patch(url + str(courses[0].id) + '/', data=data)

    assert resp.status_code == 200
    assert resp.data['name'] == 'Python'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    courses = course_factory(_quantity=3)

    counts_objects = Course.objects.count()

    url = reverse('courses-list')
    resp = api_client.delete(url + str(courses[0].id) + '/')

    assert resp.status_code == 204
    assert counts_objects - 1 == Course.objects.count()
