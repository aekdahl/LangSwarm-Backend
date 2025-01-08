from fastapi import FastAPI
from app.api import setup_routes
from app.spinup import spin_up_service

app = FastAPI()

# Set up routes
setup_routes(app)

if __name__ == "__main__":
    # Spin-up logic (can be configured via environment variables)
    spin_up_service(app)
