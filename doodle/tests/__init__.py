# -*- coding: utf-8 -*-

from doodle.config import CONFIG


if not CONFIG.TEST:
    raise EnvironmentError('cannot execute tests in %s environment' % CONFIG.__name__)
