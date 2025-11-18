import schedule
import time
from threading import Thread
from typing import Dict

def _run_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

_thread_started = False

def schedule_job(payload: Dict) -> str:
    """
    payload example:
    {
      "cron": "daily",  # simple keywords: 'every_minute', 'daily'
      "task": {"tool":"read_file","input":"logs/yesterday.txt"}
    }
    """
    global _thread_started
    task = payload.get("task")
    cron = payload.get("cron", "daily")

    def job():
        # Lazy import to avoid circular imports
        from agents.executor import Executor
        executor = Executor()
        executor.execute([task])

    if cron == "every_minute" or cron == "minute":
        schedule.every(1).minutes.do(job)
    else:
        schedule.every().day.at("08:00").do(job)

    if not _thread_started:
        t = Thread(target=_run_loop, daemon=True)
        t.start()
        _thread_started = True
    return f"Scheduled job: {cron}"
