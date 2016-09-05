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
    parser.add_argument("urls", help="url or comma separated list of urls, encased in single or double quotes")
    parser.add_argument("--checkimages", action="store_true", help="validate images on url(s)")
    parser.add_argument("--checklinks", action="store_true", help="validate links on url(s)")
    parser.add_argument("--checkjs", action="store_true", help="validate js on url(s)")
    parser.add_argument("--checkall", action="store_true", help="validate all on url(s)")
    parser.add_argument("-f", "--folder", help="folder name to save results to")
    args = parser.parse_args()
    results = defaultdict(dict)
    list_urls = args.urls.split(',')
    for url in list_urls:
        if not args.folder:
            print 'URL : ' + url
        if args.checkall:
            args.checklinks = args.checkjs = args.checkimages = True
        if args.checklinks:
            if args.folder:
                results[url]['Link Errors:'] = str(validate_links(url))
            else:
                print 'Link Errors: ' + str(validate_links(url))
        if args.checkimages:
            if args.folder:
                results[url]['Image Errors:'] = str(validate_images(url))
            else:
                print 'Image Errors: ' + str(validate_images(url))
        if args.checkjs:
            if args.folder:
                results[url]['JS Errors:'] = str(validate_js_error(url))
            else:
                print 'JS Errors: ' + str(validate_js_error(url))
    if args.folder:
        create_folder_and_write_result_to_file(args.folder, results)


def create_folder_and_write_result_to_file(results_path, result):
    filename = results_path + "/%s_%s.json" % ("val_results", datetime.now().strftime("%Y%m%d-%H%M%S"))
    with open(filename, 'w') as output:
        json.dump(result, output, sort_keys=True, indent=4)
