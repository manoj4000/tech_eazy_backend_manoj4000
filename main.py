from fastapi import FastAPI
from routers import vendors, parcels, routes, assign, status, drivers
from database import Base, engine
import models  # Make sure this imports all your models so Base knows them
from fastapi.responses import JSONResponse

app = FastAPI(title="Zero Mile Delivery API")

# ✅ Auto-create tables only if they don't exist — runs at startup
@app.on_event("startup")
def startup():
    print("🔧 Checking and creating DB tables (if missing)...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables are ready.")

@app.get("/api/check")
def health_check():

    # Check DB connection
    db_status = "unknown"
    try:
        with engine.connect() as conn:
            conn.execute(sqlalchemy.text("SELECT 1"))
        db_status = "connected"
    except OperationalError:
        db_status = "disconnected"

    # Hostname
    hostname = socket.gethostname()

    # App status
    return JSONResponse(
        content={
            "status": "✅ API is running",
            "db_status": db_status,
            "hostname": hostname,
        },
        status_code=200
    )

@app.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to Zero Mile Delivery API! 🚚"}, status_code=200)

# ✅ Include routers with /api prefix
app.include_router(vendors.router, prefix="/api")
app.include_router(drivers.router, prefix="/api")
app.include_router(parcels.router, prefix="/api")
app.include_router(routes.router, prefix="/api")
app.include_router(assign.router, prefix="/api")
app.include_router(status.router, prefix="/api")
