from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime
import service, schemas

router = APIRouter(prefix="/status", tags=["Delivery Status"])


@router.patch("/{id}")
def update_delivery_status(id: int, status: schemas.StatusUpdate, db: Session = Depends(get_db)):
    result = service.update_status(db, id, status.delivery_status)

    now = datetime.utcnow()
    # Save date and time only when delivered
    if status.delivery_status.lower() == "delivered":
        service.date_delivered(db, id, now)
        service.time_delivered(db, id, now.time())
    # Handle other statuses: failed, dispatched, pending
    elif status.delivery_status.lower() in ["failed", "dispatched", "pending"]:
        # Optionally, clear delivery date/time if not delivered
        service.clear_delivery_datetime(db, id)

    return result



@router.get("/{id}", response_model=schemas.Parcel)
def get_delivery_status(id: int, db: Session = Depends(get_db)):
    parcel = service.get_parcels(db)
    for p in parcel:
        if p.id == id:
            return p
    return {"error": "Parcel not found"}
