# coding=utf-8
import argparse
from datetime import datetime
import json
from collections import defaultdict
from nzme_skynet.core.layout.urlvalidation import validate_images
from nzme_skynet.core.layout.urlvalidation import validate_links
from nzme_skynet.core.layout.urlvalidation import validate_js_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="url or comma separated list of urls")
    parser.add_argument("-f", "--folder", help="folder name to save results to")
    parser.add_argument("--checkimages", action="store_true", help="validate images on url(s)")
    parser.add_argument("--checklinks", action="store_true", help="validate links on url(s)")
    parser.add_argument("--checkjs", action="store_true", help="validate js on url(s)")
    parser.add_argument("--checkall", action="store_true", help="validate all on url(s)")
    args = parser.parse_args()
    image_errors = []
    link_errors = []
    js_errors = []
    results = defaultdict(dict)
    list_urls = args.urls.split(',')
    for url in list_urls:
        if not args.folder:
            print "URL : " + url
        if args.checkall:
            args.checklinks = args.checkjs = args.checkimages = True
        if args.checklinks:
            link_errors = validate_links(url)
            if args.folder:
                results[url]['Link Errors:'] = str(link_errors)
            else:
                print "Links Error: " + str(link_errors)
        if args.checkimages:
            image_errors = validate_images(url)
            if args.folder:
                results[url]['Image Errors:'] = str(image_errors)
            else:
                print "Image Error: " + str(image_errors)
        if args.checkjs:
            js_errors = validate_js_error(url)
            if args.folder:
                results[url]['JS Errors:'] = str(js_errors)
            else:
                print "JS Error: " + str(js_errors)

    if args.folder:
        create_folder_and_write_result_to_file(args.folder, results)


def create_folder_and_write_result_to_file(results_path, result):
    filename = results_path + "/%s_%s.json" % ("val_results", datetime.now().strftime("%Y%m%d-%H%M%S"))
    with open(filename, 'w') as output:
        json.dump(result, output, sort_keys=True, indent=4)
