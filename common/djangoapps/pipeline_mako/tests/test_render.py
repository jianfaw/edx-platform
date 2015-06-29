"""Tests for rendering functions in the mako pipeline. """

from django.test import TestCase
from pipeline_mako import require_js_path


class RequireJSPathTest(TestCase):
    """Test RequireJS path handling. """

    def test_require_js_path(self):
        result = require_js_path('js/vendor/jquery.min.js')
        self.assertEqual(result, 'js/vendor/jquery.min')
