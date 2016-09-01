# coding=utf-8
import argparse
import os
from datetime import datetime

from nzme_skynet.core.layout.urlvalidation import validate_images
from nzme_skynet.core.layout.urlvalidation import validate_links
from nzme_skynet.core.layout.urlvalidation import validate_js_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="url or comma separated list of urls")
    parser.add_argument("--checkimages", action="store_true", help="validate images on url(s)")
    parser.add_argument("--checklinks", action="store_true", help="validate links on url(s)")
    parser.add_argument("--checkjs", action="store_true", help="validate js on url(s)")
    parser.add_argument("--checkall", action="store_true", help="validate all on url(s)")
    args = parser.parse_args()
    image_errors = []
    link_errors = []
    js_errors = []
    list_urls = args.urls.split(',')
    for url in list_urls:
        print "URL : " + url
        if args.checkall:
            args.checklinks = args.checkjs = args.checkimages = True
        if args.checklinks:
            link_errors = validate_links(url)
            print "Links Error: " + str(link_errors)
        if args.checkimages:
            image_errors = validate_images(url)
            print "Image Error: " + str(image_errors)
        if args.checkjs:
            js_errors = validate_js_error(url)
            print "JS Error: " + str(js_errors)

