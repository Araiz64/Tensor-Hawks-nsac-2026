from pydantic import BaseModel, Field
from typing import List

class SimulationInput(BaseModel):
    selected_rocket: str = Field(..., description="Rocket option: 'Tensor Rocket', 'Space Launch System SLS', or 'SpaceX Falcon 9'")
    target_destination: str = Field(..., description="Destination: 'Mars', 'Jupiter', or 'Saturn'")
    total_fuel_mass_kg: float = Field(..., gt=0)
    payload_mass_kg: float = Field(5000.0, ge=0)
    instruments_ids: List[str] = Field(default_factory=lambda: ["INS_MAG_01", "INS_RAD_02"])
    budget_limit_usd: float = Field(..., gt=0)

class TelemetryOutput(BaseModel):
    provided_delta_v: float
    required_delta_v: float
    provided_power_au: float
    data_latency_seconds: float

class SimulationResponse(BaseModel):
    telemetry: TelemetryOutput
    mission_status: str
    mission_log: List[str]