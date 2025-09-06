from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

app = FastAPI(title="User Input API", version="1.0.0")

class UserInput(BaseModel):
    name: str
    message: str
    data: Dict[str, Any] = {}

class APIResponse(BaseModel):
    status: str
    response: str
    processed_data: Dict[str, Any]

@app.get("/")
async def root():
    return {"message": "Welcome to the User Input API"}

@app.post("/process", response_model=APIResponse)
async def process_user_input(user_input: UserInput):
    try:
        processed_message = f"Hello {user_input.name}! Your message '{user_input.message}' has been received."
        
        processed_data = {
            "original_message": user_input.message,
            "message_length": len(user_input.message),
            "user_name": user_input.name,
            "additional_data": user_input.data
        }
        
        return APIResponse(
            status="success",
            response=processed_message,
            processed_data=processed_data
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)