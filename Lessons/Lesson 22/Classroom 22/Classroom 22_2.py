# Create a class Movie, use TypedDict to view Movie as a dict.
from typing import TypedDict
class Movie(TypedDict):
    tittle : str
    time_run: float
    Genre: str
mov1 = Movie(tittle='Storm',time_run=1.55,Genre='Drama')
print(mov1)