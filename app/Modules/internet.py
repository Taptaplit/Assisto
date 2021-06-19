import speedtest

class SpeedTest():
    def __init__(self):
        self.speedInit = speedtest.Speedtest()
        
    def getBestServer(self):
        self.speedInit.get_servers()
        self.bestServer = self.speedInit.get_best_server()
        
    def download_upload(self):
        self.download_speed = self.speedInit.download() / 1024 / 1024
        self.download_speed = f"{self.download_speed:.2f}"
        self.upload_speed = self.speedInit.upload() / 1024 / 1024
        self.upload_speed = f"{self.upload_speed:.2f}"
        return self.download_speed, self.upload_speed