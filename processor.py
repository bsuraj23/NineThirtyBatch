
import os
import sys
import time
import platform
try:
    import psutil
except Exception:
    psutil = None

def cpu_name():
    name = platform.processor()
    if not name:
        try:
            uname = platform.uname()
            if uname.processor:
                name = uname.processor
        except Exception:
            pass
    return name or "Unknown CPU"
def system_info():
    print("=== System Info ===")
    print(f"Python: {sys.version.split()[0]}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU: {cpu_name()}")
    print(f"Logical CPUs: {os.cpu_count()}")
    if psutil:
        try:
            physical = psutil.cpu_count(logical=False)
            print(f"Physical cores: {physical}")
            freq = psutil.cpu_freq()
            if freq:
                print(f"CPU freq: current {freq.current:.0f} MHz (min {freq.min:.0f}, max {freq.max:.0f})")
        except Exception:
            pass
    print()

def live_usage(seconds=3):
    if not psutil:
        print("psutil not installed; skipping live CPU/memory usage. Install with: pip install psutil")
        print()
        return
    print("=== Live CPU/Memory Usage ===")
    for _ in range(seconds):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        print(f"CPU: {cpu:5.1f}%   RAM used: {mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB")
    print()
def benchmark_sum_squares(n=5_000_000):
    print("=== Benchmark: sum of squares ===")
    print(f"Problem size: n={n:,}")
    t0 = time.perf_counter()
    total = sum(i*i for i in range(n))
    elapsed = time.perf_counter() - t0
    print(f"Result checksum: {total % 1_000_000_007}")
    print(f"Time: {elapsed:.3f} s  |  Throughput: {n/elapsed:,.0f} iterations/s")
    print()
    return elapsed

def main():
    system_info()
    live_usage(seconds=3)
    benchmark_sum_squares()

if __name__ == "__main__":
    main()
