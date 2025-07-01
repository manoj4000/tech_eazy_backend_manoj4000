# Zero Mile Delivery API

A modern, RESTful API for managing vendors, drivers, parcels, and delivery assignments. Built for last-mile delivery platforms.

---

## Features

- **Vendor Management:** Register, list, and authenticate vendors.
- **Driver Management:** Register, list, and authenticate drivers with vehicle details.
- **Parcel Management:** Create, list, and assign parcels.
- **Assignment:** Assign parcels to drivers manually or automatically.
- **Delivery Status:** Track and update parcel delivery status.

---

## API Endpoints

### Vendors

- `GET /api/vendors/`  
    List all vendors.

- `POST /api/vendors/`  
    Register a new vendor.

- `POST /api/vendors/login`  
    Vendor login.

### Drivers

- `GET /api/drivers/`  
    List all drivers and their vehicles.

- `POST /api/drivers/`  
    Register a new driver with vehicle details.

- `POST /api/drivers/login`  
    Driver login.

### Parcels

- `GET /api/parcels/`  
    List all parcels.

- `POST /api/parcels/`  
    Create a new parcel.

- `GET /api/parcels/vendor/{vendor_id}`  
    List parcels by vendor.

- `GET /api/parcels/driver/{driver_id}`  
    List parcels by driver.

### Assignments

- `POST /api/assign/`  
    Assign parcels to a driver.

- `GET /api/assign/{driver_id}`  
    Get parcels assigned to a driver.

- `POST /api/assign/auto-assign`  
    Auto-assign parcels to drivers.

### Routes

- `GET /api/routes/plan`  
    Dummy route planning endpoint.

### Delivery Status

- `PATCH /api/status/{id}`  
    Update delivery status for a parcel.

- `GET /api/status/{id}`  
    Get delivery status for a parcel.

---

## Data Models

### Vendor

```json
{
    "id": 1,
    "name": "Vendor Name",
    "contact_number": "1234567890",
    "email": "vendor@example.com"
}
```

### DriverVehicle

```json
{
    "id": 1,
    "name": "Driver Name",
    "contact_number": "1234567890",
    "email": "driver@example.com",
    "available": true,
    "vehicle_type": "Bike",
    "vehicle_capacity": 10
}
```

### Parcel

```json
{
    "id": 1,
    "customer_name": "Customer",
    "size": "Medium",
    "weight": 2.5,
    "delivery_status": "Pending"
}
```

---

## Quick Start

1. **Clone the repository**
2. **Install dependencies**
3. **Run the API server**

---

## License

MIT

---

> **Zero Mile Delivery API** — Fast, flexible, and ready for your logistics needs.