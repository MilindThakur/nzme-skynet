# coding=utf-8
import argparse
import itertools
import sys

from nzme_skynet.core.layout.urlvalidation import validate_images
from nzme_skynet.core.layout.urlvalidation import validate_links
from nzme_skynet.core.layout.urlvalidation import validate_js_error

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="url or comma separated list of urls")
    parser.add_argument("-f", "--folder", help="folder path to save results to")
    parser.add_argument("--checkimages", help="validate images on url(s)")
    parser.add_argument("--checklinks", help="validate links on url(s)")
    parser.add_argument("--checkjs", help="validate js on url(s)")
    parser.add_argument("--checkall", help="validate all on url(s)")
    args = parser.parse_args()
    images_error = links_error = js_errors = []
    list_urls = args.urls.split(',')
    for url in list_urls:
        if args.checkall:
            args.checklinks = args.checkjs = args.checkimages = True
        if args.checklinks:
            links_error.append(validate_links(url))
        if args.checkimages:
            images_error.append(validate_images(url))
        if args.checkjs:
            js_errors.append(validate_js_error(url))
    print sorted(set(list(itertools.chain.from_iterable(images_error + js_errors + links_error))))