from fastapi import FastAPI
from routers import vendors, parcels, routes, assign, status, drivers
from database import Base, engine
import models  # Make sure this imports all your models so Base knows them

app = FastAPI(title="Zero Mile Delivery API")

# ✅ Auto-create tables only if they don't exist — runs at startup
@app.on_event("startup")
def startup():
    print("🔧 Checking and creating DB tables (if missing)...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables are ready.")

# ✅ Include routers with /api prefix
app.include_router(vendors.router, prefix="/api")
app.include_router(drivers.router, prefix="/api")
app.include_router(parcels.router, prefix="/api")
app.include_router(routes.router, prefix="/api")
app.include_router(assign.router, prefix="/api")
app.include_router(status.router, prefix="/api")
