# **Browser Proxy**

Skynet uses [Browsermob-proxy](https://github.com/lightbody/browsermob-proxy) with Selenium scripts to capture and export data as HAR file.

For local run, get and unzip the release form browsermob-proxy [release page](https://github.com/lightbody/browsermob-proxy/releases)
To initialise:

        from nzme_skynet.core.proxy.browserproxy import BrowserProxy
        proxy = BrowserProxy(local_run=True, path_to_browsermobproxy_bin=<path>)

To run it in docker mode, add the docker image to selenium grid and run [docker-compose](../docker-compose.yaml):
        
        from nzme_skynet.core.proxy.browserproxy import BrowserProxy
        proxy = BrowserProxy(local_run=False, grid_url="http://localhost:4444/wd/hub")
        
Start the proxy server and browser:

        proxy.start()
        
Visit a URL in browser and create a HAR file:

        har_page = proxy.create_har_page("http://www.google.co.nz, <har_file_name>")
        
To filter the entry by substring in URL:

        match_list = proxy.filter_entry_by_matching_url(har_page, "gstatic.com")
        
To stop the proxy server and browser

        proxy.stop()
        