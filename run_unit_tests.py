#!/usr/bin/env python
import os
import sys 
import django
from django.conf import settings
from django.test.utils import get_runner


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.unit_tests'
    os.environ['ROME_BDR_SERVER'] ='ttwr_rome_example.org'
    os.environ['ROME_PID_PREFIX'] ='testsuite'
    os.environ['ROME_BDR_IDENTITY'] ='ID1'
    os.environ['ROME_BDR_AUTH_CODE'] = '12345'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['unit_tests'])
    sys.exit(bool(failures))