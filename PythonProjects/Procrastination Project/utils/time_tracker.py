import time
import psutil
from config import TIME_LIMITS

class TimeTracker:
    def __init__(self):
        self.start_times = {}
        self.usage_times = {app: 0 for app in TIME_LIMITS['apps']}
        self.web_usage_times = {site: 0 for site in TIME_LIMITS['websites']}
        self.active_websites = {}  # Track active website times

    def track_time(self):
        while True:
            # Track app usage
            for app, limit in TIME_LIMITS['apps'].items():
                if any(app in p.info['name'] for p in psutil.process_iter(['name'])):
                    if app not in self.start_times:
                        self.start_times[app] = time.time()
                    else:
                        self.usage_times[app] += time.time() - self.start_times[app]
                        self.start_times[app] = time.time()
                    
                    if self.usage_times[app] >= limit:
                        self.notify_user(app, limit)

                else:
                    self.start_times.pop(app, None)

            # Track website usage (simplified example, real implementation would require monitoring network traffic)
            # Placeholder logic for tracking websites
            for site, limit in TIME_LIMITS['websites'].items():
                if site in self.active_websites:
                    self.web_usage_times[site] += time.time() - self.active_websites[site]
                    self.active_websites[site] = time.time()

                    if self.web_usage_times[site] >= limit:
                        self.notify_user(site, limit)

            time.sleep(1)

    def notify_user(self, name, limit):
        print(f"Time's up for {name}! You were allotted {limit // 60} minutes. Please take a break.")
        if "exe" in name:  # It's an application
            for proc in psutil.process_iter():
                if name in proc.name():
                    proc.kill()

    def add_app(self, app, limit):
        TIME_LIMITS['apps'][app] = limit
        self.usage_times[app] = 0

    def add_website(self, site, limit):
        TIME_LIMITS['websites'][site] = limit
        self.web_usage_times[site] = 0
