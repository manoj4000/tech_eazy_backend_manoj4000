from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service, schemas

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/")
def add_driver_vehicle(driver_vehicle: schemas.DriverVehicleCreate, db: Session = Depends(get_db)):
    return service.create_driver_vehicle(db, driver_vehicle)

# Make sure driver is imported or defined in schemas.py
@router.get("/", response_model=list[schemas.DriverVehicle])
def list_driver_vehicles(db: Session = Depends(get_db)):
    return service.get_driver_vehicles(db)

@router.post("/login", response_model=schemas.DriverVehicle)
def login(driver: schemas.DriverVehicleLogin, db: Session = Depends(get_db)):
    result = service.login_driver_vehicle(db, driver.email, driver.password)
    if not result:
        return {"error": "Invalid credentials"}
    return result
