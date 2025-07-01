from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime
from fastapi import HTTPException

def create_vendor(db: Session, vendor: schemas.VendorCreate):
    db_vendor = models.Vendor(name=vendor.name)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
def get_vendors(db: Session):
    return db.query(models.Vendor).all()

def login_vendor(db: Session, email: str, password: str):
    vendor = db.query(models.Vendor).filter(
        models.Vendor.email == email,
        models.Vendor.password == password  # No hashing — not secure
    ).first()

    return vendor

def create_driver_vehicle(db: Session, driver_vehicle: schemas.DriverVehicleCreate):
    db_driver_vehicle = models.DriverVehicle(**driver_vehicle.dict())
    db.add(db_driver_vehicle)
    db.commit()
    db.refresh(db_driver_vehicle)
    return db_driver_vehicle
def get_driver_vehicles(db: Session):
    return db.query(models.DriverVehicle).all()

def login_driver_vehicle(db: Session, email: str, password: str):
    driver_vehicle = db.query(models.DriverVehicle).filter(
        models.DriverVehicle.email == email,
        models.DriverVehicle.password == password  # No hashing — not secure
    ).first()

    return driver_vehicle
def create_parcel(db: Session, parcel: schemas.ParcelCreate):
    db_parcel = models.Parcel(**parcel.dict())
    db.add(db_parcel)
    db.commit()
    db.refresh(db_parcel)
    return db_parcel

def get_parcels(db: Session):
    return db.query(models.Parcel).all()

def get_parcels_by_vendor(db: Session, vendor_id: int):
    parcels = db.query(models.Parcel).filter(models.Parcel.vendor_id == vendor_id).all()
    if not parcels:
        raise HTTPException(status_code=404, detail=f"No parcels found for vendor ID {vendor_id}.")
    return parcels
def get_parcels_by_driver(db: Session, driver_id: int):
    parcels = db.query(models.Parcel).filter(models.Parcel.driver_id == driver_id).all()
    if not parcels:
        raise HTTPException(status_code=404, detail=f"No parcels found for driver ID {driver_id}.")
    return parcels

def update_status(db: Session, parcel_id: int, status: str):
    parcel = db.get(models.Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail=f"Parcel with ID {parcel_id} not found.")

    parcel.delivery_status = status

    # If not delivered, reset time/date
    if status.lower() != "delivered":
        parcel.date_delivered = None
        parcel.delivery_time = None

    db.commit()
    db.refresh(parcel)

    return {
        "message": f"Status updated to '{status}'",
        "parcel_id": parcel.id,
        "delivery_status": parcel.delivery_status
    }


def date_delivered(db: Session, parcel_id: int, delivered_date: datetime):
    parcel = db.get(models.Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail=f"Parcel with ID {parcel_id} not found.")
    
    parcel.date_delivered = delivered_date.strftime('%Y-%m-%d')
    db.commit()


def time_delivered(db: Session, parcel_id: int, delivered_time: datetime.time):
    parcel = db.get(models.Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail=f"Parcel with ID {parcel_id} not found.")
    
    parcel.delivery_time = delivered_time.strftime('%H:%M:%S')
    db.commit()