from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory data store (for demo purposes)
fire_reports = []
mybags = []
myfamily = []


class FireReport(BaseModel):
    id: int
    location: str
    description: str
    status: str  # e.g., "active", "contained", "resolved"


class MyBag(BaseModel):
    id: int
    name: str
    description: str
    items: List[str]


class MyFamily(BaseModel):
    id: int
    name: str
    description: str
    members: List[str]


@app.get("/fire-reports", response_model=List[FireReport])
def get_fire_reports():
    return fire_reports


@app.post("/fire-reports", response_model=FireReport)
def create_fire_report(report: FireReport):
    for r in fire_reports:
        if r.id == report.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    fire_reports.append(report)
    return report


@app.get("/fire-reports/{report_id}", response_model=FireReport)
def get_fire_report(report_id: int):
    for report in fire_reports:
        if report.id == report_id:
            return report
    raise HTTPException(status_code=404, detail="Report not found")


@app.put("/fire-reports/{report_id}", response_model=FireReport)
def update_fire_report(report_id: int, updated: FireReport):
    for i, report in enumerate(fire_reports):
        if report.id == report_id:
            fire_reports[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Report not found")


@app.delete("/fire-reports/{report_id}")
def delete_fire_report(report_id: int):
    for i, report in enumerate(fire_reports):
        if report.id == report_id:
            del fire_reports[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Report not found")
