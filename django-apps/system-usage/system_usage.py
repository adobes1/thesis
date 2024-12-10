import psutil

def get_system_usage():
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count(logical=False)  # Physical cores
    logical_cores = psutil.cpu_count(logical=True)  # Logical cores (including hyperthreads)

    # Memory usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_total = memory.total
    memory_used = memory.used
    memory_available = memory.available

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    disk_total = disk.total
    disk_used = disk.used
    disk_free = disk.free

    print(f"CPU Usage: {cpu_percent}% (Physical cores: {cpu_cores}, Logical cores: {logical_cores})")
    print(f"Memory Usage: {memory_percent}% (Total: {memory_total / 1e9:.2f} GB, Used: {memory_used / 1e9:.2f} GB, Available: {memory_available / 1e9:.2f} GB)")
    print(f"Disk Usage: {disk_percent}% (Total: {disk_total / 1e9:.2f} GB, Used: {disk_used / 1e9:.2f} GB, Free: {disk_free / 1e9:.2f} GB)")

if __name__ == "__main__":
    get_system_usage()
