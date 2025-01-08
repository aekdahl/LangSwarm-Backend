import os

def spin_up_service(app):
    port = int(os.getenv("APP_PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
