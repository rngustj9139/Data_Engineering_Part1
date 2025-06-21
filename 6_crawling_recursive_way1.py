def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath