from db.models import MovieSession, Movie, CinemaHall
from django.db.models import QuerySet
import datetime


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
    )
    return movie_session


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    sessions = MovieSession.objects.all()
    if session_date:
        try:
            session_date = (
                datetime.datetime.strptime(session_date, "%Y-%m-%d").date()
            )
            sessions = sessions.filter(show_time__date=session_date)
        except ValueError:
            raise ValueError("Invalid date format")
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession:

    movie_session = MovieSession.objects.get(id=session_id)

    if movie_id:
        movie_session.movie = Movie.objects.get(id=movie_id)

    if show_time:
        movie_session.show_time = show_time

    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()