class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        all_income = 0
        for car in cars:
            income = self.calculate_washing_price(car)
            self.wash_single_car(car)
            all_income += income

        return all_income

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            diff = self.clean_power - car.clean_mark
            average, dist = self.average_rating, self.distance_from_city_center
            price = car.comfort_class * diff * average / dist
            return round(price, 1)
        else:
            return 0.0

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        average, count = self.average_rating, self.count_of_ratings
        self.average_rating = (average * count + rate) / (count + 1)
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1
