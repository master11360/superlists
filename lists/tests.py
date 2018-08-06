# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from lists.views import home_page
from django.core import urlresolvers
from django.http import HttpRequest
from django.template import loader

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = urlresolvers.resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = loader.render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
