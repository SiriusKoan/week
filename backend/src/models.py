from pydantic import BaseModel


class TimeCell(BaseModel):
    day: int
    start_time: int
    end_time: int
    location: str
    name: str


class Timetable(BaseModel):
    name: str
    timetable: list[TimeCell]
