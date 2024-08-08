from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from materials.models import Lesson, Course, Test, AttemptAnswer
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="tedt@tru.ru")
        self.user_ = User.objects.create(email="tedtsss@tru.ru")
        self.course = Course.objects.create(name="Pyton - only", owner=self.user)
        self.lesson = Lesson.objects.create(
            name="Основы программирования", course=self.course, owner=self.user
        )
        self.test = Test.objects.create(
            owner=self.user,
            lesson=self.lesson,
            correct_answer="конкатенация",
            description="Сложение строк?",
            name="Строки",
        )
        self.attempt_answer = AttemptAnswer.objects.create(
            answer="конкатенация", test=self.test, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        response = self.client.get("http://127.0.0.1:8000/course/1/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)
        self.assertEqual(data.get("owner"), self.user.pk)

    def test_course_update(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {"name": "Python - с нуля", "owner": self.user_.pk}
        response = self.client.patch(url, data)
        data_ = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data_.get("name"), "Python - с нуля")
        self.assertEqual(data_.get("owner"), self.user_.pk)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("owner"), self.user.pk)
        self.assertEqual(data.get("course"), self.course.pk)

    def test_lesson_update(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        data = {"name": "основы Pyton", "owner": self.user_.pk}
        response = self.client.patch(url, data)
        data_ = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data_.get("name"), "основы Pyton")
        self.assertEqual(data_.get("owner"), self.user_.pk)

    def test_test_retrieve(self):
        url = reverse("materials:test-detail", args=(self.test.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.test.name)
        self.assertEqual(data.get("owner"), self.user.pk)
        self.assertEqual(data.get("lesson"), self.lesson.pk)
        self.assertEqual(data.get("correct_answer"), self.test.correct_answer)
        self.assertEqual(data.get("description"), self.test.description)

    def test_test_update(self):
        url = reverse("materials:test-detail", args=(self.test.pk,))
        data = {
            "name": "операции со строками",
            "owner": self.user_.pk,
            "correct_answer": "к-онкатенация",
            "description": "как называется сложение строк",
        }
        response = self.client.patch(url, data)
        data_ = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data_.get("name"), "операции со строками")
        self.assertEqual(data_.get("owner"), self.user_.pk)
        self.assertEqual(data.get("correct_answer"), "к-онкатенация")
        self.assertEqual(data.get("description"), "как называется сложение строк")
