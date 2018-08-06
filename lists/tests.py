# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from lists.views import home_page
from django.core import urlresolvers

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = urlresolvers.resolve('/')
        self.assertEqual(found.func, home_page)
