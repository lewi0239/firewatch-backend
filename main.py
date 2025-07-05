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

# Fire Reports


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


# My Bags
@app.get("/mybags", response_model=List[MyBag])
def get_mybags():
    return mybags


@app.post("/mybags", response_model=MyBag)
def create_mybag(mybag: MyBag):
    for m in mybags:
        if m.id == mybag.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    mybags.append(mybag)
    return mybag


@app.get("/mybags/{bag_id}", response_model=MyBag)
def get_mybag(bag_id: int):
    for bag in mybags:
        if bag.id == bag_id:
            return bag
    raise HTTPException(status_code=404, detail="Bag not found")


@app.put("/mybags/{bag_id}", response_model=MyBag)
def update_mybag(bag_id: int, updated: MyBag):
    for i, bag in enumerate(mybags):
        if bag.id == bag_id:
            mybags[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Bag not found")


@app.delete("/mybags/{bag_id}")
def delete_mybag(bag_id: int):
    for i, bag in enumerate(mybags):
        if bag.id == bag_id:
            del mybags[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Bag not found")


# My Family
@app.get("/myfamily", response_model=List[MyFamily])
def get_myfamily():
    return myfamily


@app.post("/myfamily", response_model=MyFamily)
def create_myfamily(myfamily: MyFamily):
    for m in myfamily:
        if m.id == myfamily.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    myfamily.append(myfamily)
    return myfamily


@app.get("/myfamily/{family_id}", response_model=MyFamily)
def get_myfamily(family_id: int):
    for family in myfamily:
        if family.id == family_id:
            return family
    raise HTTPException(status_code=404, detail="Family not found")


@app.put("/myfamily/{family_id}", response_model=MyFamily)
def update_myfamily(family_id: int, updated: MyFamily):
    for i, family in enumerate(myfamily):
        if family.id == family_id:
            myfamily[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Family not found")


@app.delete("/myfamily/{family_id}")
def delete_myfamily(family_id: int):
    for i, family in enumerate(myfamily):
        if family.id == family_id:
            del myfamily[i]
            return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Family not found")
