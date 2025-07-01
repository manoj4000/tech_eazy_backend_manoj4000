from fastapi import APIRouter

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.get("/plan")
def dummy_plan():
    return {"message": "Route planning logic will be added here."}
