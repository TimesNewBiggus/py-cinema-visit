from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
# from app.cinema.bar import CinemaBar


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}"'
              + " " + f"started in hall number {self.number}.")
        for customer in customers:
            Customer.watch_movie(customer,
                                 movie_name)
        print(f'"{movie_name}"' + " " + "ended.")
        print(f"Cleaner {cleaning_staff.name}"
              + " " + f"is cleaning hall number {self.number}.")
