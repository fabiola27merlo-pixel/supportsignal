from fastapi import FastAPI, HTTPException

app = FastAPI()


system_health = {
    "crm-sync": {
        "status": "degraded",
        "error_rate": 0.18,
        "p95_latency_ms": 2300,
        "active_incident": False,
        "affected_region": "us-east",
    },
    "authentication": {
        "status": "healthy",
        "error_rate": 0.01,
        "p95_latency_ms": 180,
        "active_incident": False,
        "affected_region": None,
    },
}


@app.get("/v1/system-context/{service}")
def get_system_health(service: str):

    if service not in system_health:
        raise HTTPException(
            status_code=404,
            detail=f"Service '{service}' not found"
        )

    health = system_health[service]

    return {
        "service": service,
        **health,
    }