"""Model for individual log entries."""

from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator


class LogEntry(BaseModel):
    """Represents a single parsed log entry with validation."""

    ip: str = Field(..., description="IP address of the client")
    timestamp: Optional[datetime] = Field(None, description="Timestamp of the log entry")
    method: str = Field(..., description="HTTP method (GET, POST, etc.)")
    path: str = Field(..., description="Requested URL path")
    status: int = Field(..., description="HTTP status code")
    size: int = Field(0, description="Response size in bytes")
    user_agent: str = Field(..., description="User agent string")

    @field_validator("size", mode="before")
    @classmethod
    def parse_size(cls, v: Union[str, int]) -> int:
        """Parse size from string or int, handling '-' as 0."""
        if isinstance(v, str):
            if v in ("-", ""):
                return 0
            return int(v)
        return v

    @field_validator("timestamp", mode="before")
    @classmethod
    def parse_timestamp(cls, v: Union[str, datetime]) -> Optional[datetime]:
        """Parse timestamp from string using Apache format."""
        if isinstance(v, str):
            try:
                # Handle Apache format: 10/Oct/2000:13:55:36 -0700
                return datetime.strptime(v, "%d/%b/%Y:%H:%M:%S %z")
            except ValueError:
                return None
        return v
