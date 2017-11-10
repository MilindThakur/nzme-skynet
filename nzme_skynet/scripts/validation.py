# coding=utf-8
import argparse
import logging
import logging.config
from datetime import datetime
import json
from collections import defaultdict
from nzme_skynet.core.layout.urlvalidation import validate_images
from nzme_skynet.core.layout.urlvalidation import validate_links
from nzme_skynet.core.layout.urlvalidation import validate_js_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="url or comma separated list of urls, encased in single or double quotes")
    parser.add_argument("--checkimages", action="store_true", help="validate images on url(s)")
    parser.add_argument("--checklinks", action="store_true", help="validate links on url(s)")
    parser.add_argument("--checkjs", action="store_true", help="validate js on url(s)")
    parser.add_argument("--checkall", action="store_true", help="validate all on url(s)")
    parser.add_argument("-f", "--folder", help="folder name to save results to")
    args = parser.parse_args()
    results = defaultdict(dict)
    list_urls = args.urls.split(',')
    if args.folder:
        setup_logging(args.folder)
    for url in list_urls:
        if args.checkall:
            log('Checking all for URL : ' + url)
            args.checklinks = args.checkjs = args.checkimages = True
        if args.checklinks:
            log('Checking Links for URL : ' + url)
            results[url]['Link Errors:'] = str(validate_links(url))
        if args.checkimages:
            log('Checking images for URL : ' + url)
            results[url]['Image Errors:'] = str(validate_images(url))
        if args.checkjs:
            log('Checking JS errors for URL : ' + url)
            results[url]['JS Errors:'] = str(validate_js_error(url))
    log("Results:")
    log(json.dumps(results, sort_keys=True, indent=4))


def setup_logging(filename):
    logging.basicConfig(filename=filename+"/%s_%s" % ("val_results", datetime.now().strftime("%Y%m%d-%H%M%S")+".log")
                        , level=logging.INFO)


def log(log_entry):
    print log_entry
    if len(logging.root.handlers) > 1:
        logging.info(log_entry)
