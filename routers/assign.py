from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter(prefix="/assign", tags=["Assignments"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Manually assign parcels to a driver
@router.post("/")
def assign_parcels_to_driver(driver_id: int, parcel_ids: list[int], db: Session = Depends(get_db)):
    driver = db.query(models.DriverVehicle).filter(models.DriverVehicle.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    updated = 0
    for pid in parcel_ids:
        parcel = db.query(models.Parcel).filter(models.Parcel.id == pid).first()
        if parcel:
            parcel.driver_id = driver_id
            parcel.delivery_status = "Assigned"
            updated += 1

    db.commit()
    return {"message": f"{updated} parcels manually assigned to driver {driver.name}."}


# ✅ Get all parcels assigned to a specific driver
@router.get("/{driver_id}")
def get_parcels_by_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(models.DriverVehicle).filter(models.DriverVehicle.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    parcels = db.query(models.Parcel).filter(models.Parcel.driver_id == driver_id).all()
    return {
        "driver": driver.name,
        "total_parcels": len(parcels),
        "parcels": parcels
    }


# ✅ Auto-assign parcels based on driver availability and vehicle capacity
@router.post("/auto-assign")
def auto_assign_parcels(db: Session = Depends(get_db)):
    # Get unassigned parcels
    parcels = db.query(models.Parcel).filter(
        models.Parcel.driver_id == None,
        models.Parcel.delivery_status == "Pending"
    ).order_by(models.Parcel.area).all()

    if not parcels:
        return {"message": "No unassigned parcels found."}

    drivers = db.query(models.DriverVehicle).filter(models.DriverVehicle.available == True).all()
    if not drivers:
        raise HTTPException(status_code=404, detail="No available drivers.")

    assigned_count = 0

    for parcel in parcels:
        for driver in drivers:
            if parcel.driver_id:
                continue  # already assigned

            if parcel.weight <= driver.vehicle_capacity:
                parcel.driver_id = driver.id
                parcel.delivery_status = "Assigned"
                # Optional: make driver unavailable after assignment
                # driver.available = False
                assigned_count += 1
                break  # move to next parcel

    db.commit()

    return {"message": f"✅ Auto-assigned {assigned_count} parcels to available drivers."}
