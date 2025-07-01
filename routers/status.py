from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
import service, schemas

router = APIRouter(prefix="/status", tags=["Delivery Status"])


@router.patch("/{id}")
def update_delivery_status(id: int, status: schemas.StatusUpdate, db: Session = Depends(get_db)):
    result = service.update_status(db, id, status.delivery_status)

    # If status is 'delivered', update date/time fields
    if status.delivery_status.lower() == "delivered":
        now = datetime.utcnow()
        service.date_delivered(db, id, now)
        service.time_delivered(db, id, now.time())

    return result


@router.get("/{id}", response_model=schemas.Parcel)
def get_delivery_status(id: int, db: Session = Depends(get_db)):
    parcel = service.get_parcels(db)
    for p in parcel:
        if p.id == id:
            return p
    return {"error": "Parcel not found"}
