"""
Registering tool functions here. Tools must accept a single 'input' parameter
and return a JSON-serializable result (string/dict).
"""
from tools.email_tool import send_email
from tools.pdf_tool import summarize_pdf
from tools.google_sheets_tool import update_sheet
from tools.web_scraper_tool import scrape_website
from tools.file_ops_tool import read_file, write_file
from tools.scheduler import schedule_job

TOOL_REGISTRY = {
    "send_email": send_email,
    "summarize_pdf": summarize_pdf,
    "update_sheet": update_sheet,
    "scrape_website": scrape_website,
    "read_file": read_file,
    "write_file": write_file,
    "schedule_job": schedule_job,
}
