from fastapi import HTTPException
from typing import List
from app.schemas.fire_report import FireReport

# In-memory data store (for demo purposes)
fire_reports: List[FireReport] = []

def get_fire_reports() -> List[FireReport]:
    return fire_reports

def create_fire_report(report: FireReport) -> FireReport:
    for r in fire_reports:
        if r.id == report.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    fire_reports.append(report)
    return report

def get_fire_report(report_id: int) -> FireReport:
    for report in fire_reports:
        if report.id == report_id:
            return report
    raise HTTPException(status_code=404, detail="Report not found")

def update_fire_report(report_id: int, updated: FireReport) -> FireReport:
    for i, report in enumerate(fire_reports):
        if report.id == report_id:
            fire_reports[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Report not found")

def delete_fire_report(report_id: int):
    for i, report in enumerate(fire_reports):
        if report.id == report_id:
            del fire_reports[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Report not found")
