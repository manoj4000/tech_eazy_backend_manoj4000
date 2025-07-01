from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service, schemas

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.post("/")
def add_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    return service.create_vendor(db, vendor)

# Make sure Vendor is imported or defined in schemas.py
@router.get("/", response_model=list[schemas.Vendor])
def list_vendors(db: Session = Depends(get_db)):
    return service.get_vendors(db)


@router.post("/login", response_model=schemas.Vendor)
def login(vendor: schemas.VendorLogin, db: Session = Depends(get_db)):
    result = service.login_vendor(db, vendor.email, vendor.password)
    if not result:
        return {"error": "Invalid credentials"}
    return result
