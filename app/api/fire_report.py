from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.fire_report import FireReport
from app.crud import crud_fire_report

router = APIRouter()

@router.get("/fire-reports", response_model=List[FireReport])
def get_fire_reports():
    return crud_fire_report.get_fire_reports()

@router.post("/fire-reports", response_model=FireReport)
def create_fire_report(report: FireReport):
    return crud_fire_report.create_fire_report(report)

@router.get("/fire-reports/{report_id}", response_model=FireReport)
def get_fire_report(report_id: int):
    return crud_fire_report.get_fire_report(report_id)

@router.put("/fire-reports/{report_id}", response_model=FireReport)
def update_fire_report(report_id: int, updated: FireReport):
    return crud_fire_report.update_fire_report(report_id, updated)

@router.delete("/fire-reports/{report_id}")
def delete_fire_report(report_id: int):
    return crud_fire_report.delete_fire_report(report_id)
