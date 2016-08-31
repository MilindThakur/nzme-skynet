# coding=utf-8
import argparse

from nzme_skynet.core.layout.layoutscreenshot import LayoutScreenshot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", help="json file with list of urls")
    parser.add_argument("--devices", help="comma separated device names, by default takes snapshot on all devices")
    parser.add_argument("--folder", help="path to save screenshots, by default saved to a folder SCREENSHOT in the same directory")
    args = parser.parse_args()

    sc = LayoutScreenshot(args.urls, args.devices, args.folder)
    sc.take_screenshot()
