from idm import IDMan

downloader = IDMan()
url = "https://edx-video.net/MITX60012016-V000700/MITX60012016-V000700_1_.m3u8"
downloader.download(url, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)