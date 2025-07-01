from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    contact_number = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    parcels = relationship("Parcel", back_populates="vendor")


class Parcel(Base):
    __tablename__ = "parcels"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    customer_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    size = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    area = Column(String, nullable=False)
    delivery_status = Column(String, default="Pending")
    date_created = Column(String, nullable=False)
    delivery_time = Column(String, nullable=True)
    date_delivered = Column(String, nullable=True)
    driver_id = Column(Integer, ForeignKey("driver_vehicles.id"), nullable=True)
    

    vendor = relationship("Vendor", back_populates="parcels")


class DriverVehicle(Base):
    __tablename__ = "driver_vehicles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    available = Column(Boolean, default=True)
    vehicle_type = Column(String, nullable=False)
    vehicle_capacity = Column(Float, nullable=False)
    


class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    area = Column(String, nullable=False)
    driver_vehicle_id = Column(Integer, ForeignKey("driver_vehicles.id"), nullable=False)

    driver_vehicle = relationship("DriverVehicle")
