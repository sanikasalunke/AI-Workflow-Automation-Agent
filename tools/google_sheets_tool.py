"""
Example Google Sheets updater. Requires service account JSON.
For quick testing you can replace with local CSV writing.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def update_sheet(payload: dict) -> dict:
    """
    payload: {
      "service_account_path": "secrets/sa.json",
      "sheet_name": "MySheet",
      "worksheet": "Sheet1",
      "values": [["a","b"],["c","d"]]
    }
    """
    sa_path = payload.get("service_account_path")
    if not sa_path or not os.path.exists(sa_path):
        raise ValueError("Service account JSON not found. Provide path in payload.")

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(sa_path, scope)
    client = gspread.authorize(creds)
    sheet_name = payload.get("sheet_name")
    worksheet = payload.get("worksheet", "Sheet1")
    values = payload.get("values", [])

    sh = client.open(sheet_name)
    ws = sh.worksheet(worksheet)
    ws.append_rows(values)
    return {"status": "ok", "appended": len(values)}
