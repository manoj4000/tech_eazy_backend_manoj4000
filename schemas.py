from pydantic import BaseModel
from typing import Optional

class VendorCreate(BaseModel):
    name: str
    contact_number: str
    email: str
    password: str
    address: Optional[str] = None
    

class Vendor(BaseModel):
    id: int
    name: str
    contact_number: str
    email: str

class VendorLogin(BaseModel):
    email: str
    password: str
   
class DriverVehicleCreate(BaseModel):
    name: str
    contact_number: str
    email: str
    password: str
    available: bool
    vehicle_type: str
    vehicle_capacity: float

class DriverVehicle(BaseModel):
    id: int
    name: str
    contact_number: str
    email: str
    available: bool
    vehicle_type: str
    vehicle_capacity: float

class DriverVehicleLogin(BaseModel):
    email: str
    password: str

class DriverVehicle(BaseModel):
    id: int
    name: str
    contact_number: str
    email: str
    available: bool
    vehicle_type: str
    vehicle_capacity: float

class ParcelCreate(BaseModel):
    vendor_id: int
    customer_name: str
    address: str
    contact_number: str
    size: str
    weight: float
    area: str

class Parcel(BaseModel):
    id: int
    customer_name: str
    size: str
    weight: float
    delivery_status: str

class ParcelAssignment(BaseModel):
    id: int
    customer_name: str
    contact_number: str
    address: str
    delivery_status: str
    weight: float
    size: str

class StatusUpdate(BaseModel):
    delivery_status: str
    delivery_date: Optional[str] = None
    delivery_time: Optional[str] = None
