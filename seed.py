from database import SessionLocal
import models
from datetime import datetime

db = SessionLocal()

# Clear existing data
db.query(models.Parcel).delete()
db.query(models.Vendor).delete()
db.query(models.DriverVehicle).delete()
db.query(models.Route).delete()
db.commit()

# Add Vendors
vendor1 = models.Vendor(
    name="FastParcel Pvt Ltd",
    contact_number="9998887776",
    email="contact@fastparcel.com",
    password="hashedpassword1"
)
vendor2 = models.Vendor(
    name="QuickMove Logistics",
    contact_number="8887776665",
    email="info@quickmove.com",
    password="hashedpassword2"
)
db.add_all([vendor1, vendor2])
db.commit()
db.refresh(vendor1)
db.refresh(vendor2)

# Add DriverVehicles
drivers = [
    models.DriverVehicle(
        name="Driver Alpha",
        contact_number="9000000001",
        email="alpha@drivers.com",
        password="driverpass1",
        available=True,
        vehicle_type="Bike",
        vehicle_capacity=50.0
    ),
    models.DriverVehicle(
        name="Driver Beta",
        contact_number="9000000002",
        email="beta@drivers.com",
        password="driverpass2",
        available=True,
        vehicle_type="Van",
        vehicle_capacity=200.0
    ),
    models.DriverVehicle(
        name="Driver Gamma",
        contact_number="9000000003",
        email="gamma@drivers.com",
        password="driverpass3",
        available=True,
        vehicle_type="Truck",
        vehicle_capacity=1000.0
    )
]
db.add_all(drivers)
db.commit()
for d in drivers:
    db.refresh(d)

# Add Routes
routes = [
    models.Route(area="Area 1", driver_vehicle_id=drivers[0].id),
    models.Route(area="Area 2", driver_vehicle_id=drivers[1].id),
    models.Route(area="Area 3", driver_vehicle_id=drivers[2].id)
]
db.add_all(routes)
db.commit()

# Add Parcels
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
parcels = [
    models.Parcel(
        vendor_id=vendor1.id,
        customer_name="Alice Johnson",
        address="221B Baker St, Area 1",
        contact_number="9876543210",
        size="Small",
        weight=2.1,
        area="Area 1",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor2.id,
        customer_name="Bob Smith",
        address="42 Galaxy Rd, Area 2",
        contact_number="9765432101",
        size="Medium",
        weight=4.0,
        area="Area 2",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor1.id,
        customer_name="Carol White",
        address="71 Pine St, Area 3",
        contact_number="9654321092",
        size="Large",
        weight=8.5,
        area="Area 3",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor2.id,
        customer_name="David Lee",
        address="15 Oak Ave, Area 1",
        contact_number="9543210987",
        size="Small",
        weight=1.8,
        area="Area 1",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor1.id,
        customer_name="Eva Green",
        address="88 Maple Rd, Area 2",
        contact_number="9432109876",
        size="Medium",
        weight=3.2,
        area="Area 2",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor2.id,
        customer_name="Frank Black",
        address="19 Elm St, Area 3",
        contact_number="9321098765",
        size="Large",
        weight=7.9,
        area="Area 3",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor1.id,
        customer_name="Grace Hopper",
        address="100 Tech Park, Area 1",
        contact_number="9210987654",
        size="Small",
        weight=2.5,
        area="Area 1",
        date_created=now
    ),
    models.Parcel(
        vendor_id=vendor2.id,
        customer_name="Henry Ford",
        address="55 Motorway, Area 2",
        contact_number="9109876543",
        size="Medium",
        weight=5.1,
        area="Area 2",
        date_created=now
    )
]
db.add_all(parcels)
db.commit()

db.close()
print("✅ Dummy data inserted successfully!")
