#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Radim Rehurek <radimrehurek@seznam.cz>
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html

"""
Automated tests for checking transformation algorithms (the models package).
"""

import numpy as np
import six


class TestBaseTopicModel(object):
    def testPrintTopic(self):
        topics = self.model.show_topics(formatted=True)
        for topic_no, topic in topics:
            self.assertTrue(isinstance(topic_no, int))
            self.assertTrue(isinstance(topic, str) or isinstance(topic, unicode))  # noqa:F821

    def testPrintTopics(self):
        topics = self.model.print_topics()

        for topic_no, topic in topics:
            self.assertTrue(isinstance(topic_no, int))
            self.assertTrue(isinstance(topic, str) or isinstance(topic, unicode))  # noqa:F821

    def testShowTopic(self):
        topic = self.model.show_topic(1)

        for k, v in topic:
            self.assertTrue(isinstance(k, six.string_types))
            self.assertTrue(isinstance(v, (np.floating, float)))

    def testShowTopics(self):
        topics = self.model.show_topics(formatted=False)

        for topic_no, topic in topics:
            self.assertTrue(isinstance(topic_no, int))
            self.assertTrue(isinstance(topic, list))
            for k, v in topic:
                self.assertTrue(isinstance(k, six.string_types))
                self.assertTrue(isinstance(v, (np.floating, float)))

    def testGetTopics(self):
        topics = self.model.get_topics()
        vocab_size = len(self.model.id2word)
        for topic in topics:
            self.assertTrue(isinstance(topic, np.ndarray))
            self.assertEqual(topic.dtype, np.float64)
            self.assertEqual(vocab_size, topic.shape[0])
            self.assertAlmostEqual(np.sum(topic), 1.0, 5)
