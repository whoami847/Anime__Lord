import psutil
import time

def status_message():
    uptime = time.time() - psutil.boot_time()
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    text = (
        f"Bot Status:\n"
        f"Uptime: {uptime // 3600} hours\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory.percent}%"
    )
    return text
