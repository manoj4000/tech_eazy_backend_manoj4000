from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service, schemas

router = APIRouter(prefix="/parcels", tags=["Parcels"])

@router.post("/")
def add_parcel(parcel: schemas.ParcelCreate, db: Session = Depends(get_db)):
    return service.create_parcel(db, parcel)

@router.get("/")
def list_parcels(db: Session = Depends(get_db)):
    return service.get_parcels(db)

@router.get("/vendor/{vendor_id}")
def get_parcels_by_vendor(vendor_id: int, db: Session = Depends(get_db)):
        return service.get_parcels_by_vendor(db, vendor_id)

@router.get("/driver/{driver_id}")
def get_parcels_by_driver(driver_id: int, db: Session = Depends(get_db)):
        return service.get_parcels_by_driver(db, driver_id)
