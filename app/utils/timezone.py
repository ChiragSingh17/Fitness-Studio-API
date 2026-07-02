"""Timezone utilities"""
from datetime import datetime
import pytz
from app.config import settings


def get_ist_timezone():
    """Get IST timezone object"""
    return pytz.timezone(settings.TIMEZONE)


def convert_to_ist(dt: datetime) -> datetime:
    """Convert datetime to IST"""
    if dt.tzinfo is None:
        # Assume UTC if no timezone
        dt = pytz.UTC.localize(dt)
    
    ist_tz = get_ist_timezone()
    return dt.astimezone(ist_tz)


def get_current_ist_time() -> datetime:
    """Get current time in IST"""
    ist_tz = get_ist_timezone()
    return datetime.now(ist_tz)


def convert_to_utc(dt: datetime) -> datetime:
    """Convert datetime to UTC"""
    if dt.tzinfo is None:
        # Assume IST if no timezone
        ist_tz = get_ist_timezone()
        dt = ist_tz.localize(dt)
    
    return dt.astimezone(pytz.UTC)
