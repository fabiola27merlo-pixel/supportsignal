from fastapi import FastAPI, HTTPException

app = FastAPI()


system_health = {
    "crm-sync": {
        "US": {
            "status": "degraded",
            "error_rate": 0.18,
            "p95_latency_ms": 2300,
            "active_incident": False,
            "affected_region": "US",
        },
        "Europe": {
            "status": "healthy",
            "error_rate": 0.03,
            "p95_latency_ms": 850,
            "active_incident": False,
            "affected_region": None,
        },
    },
    "authentication": {
        "US": {
            "status": "healthy",
            "error_rate": 0.01,
            "p95_latency_ms": 180,
            "active_incident": False,
            "affected_region": None,
        },
    },
}


@app.get("/v1/system-context/{service}")
def get_system_health(service: str, region: str):

    if service not in system_health:
        raise HTTPException(
            status_code=404,
            detail=f"Service '{service}' not found",
        )

    if region not in system_health[service]:
        raise HTTPException(
            status_code=404,
            detail=f"Region '{region}' not found for service '{service}'",
        )

    health = system_health[service][region]

    return {
        "service": service,
        "region": region,
        **health,
    }