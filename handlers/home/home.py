#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado
import tornado.locale
import markdown
import os

from handlers.base import BaseHandler

# AWS S3 Configuration

class HomeHandler(BaseHandler):
    def get(self):
        BaseHandler.initialize(self)
        self.title = "CHEC"
        self.render("home/home.html", title = self.title)
