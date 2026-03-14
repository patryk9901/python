class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        self.title = title
        if(self.title.strip()) == "":
            raise ValueError("Title cannot be empty")
        self.year = year
        if self.year < 1895:
            raise ValueError("Year must be 1895 or later")
        self.director = director
        if(self.director.strip()) == "":
            raise ValueError("Director cannot be empty")
        self.duration = duration
        if self.duration <= 0:
            raise ValueError("Duration must be positive")

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.items:
            return "Media Catalogue (empty)."
        result = f"Media Catalogue ({len(self.items)} items):\n\n"
        for index, item in enumerate(self.items, start=1):
            result += f"{index}. {item}\n"
        return result

    def add(self, media_item):
        if not isinstance(media_item, (Movie, TVSeries)):
            raise MediaError("Only Movie or TVSeries instances can be added", media_item)
        self.items.append(media_item)

class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        self.seasons = seasons
        if self.seasons <= 0:
            raise ValueError("Seasons must be 1 or greater")
        self.total_episodes = total_episodes
        if self.total_episodes <= 0:
            raise ValueError("Total episodes must be 1 or greater")
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"

class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message,obj):
        super().__init__(message)
        self.obj = obj

catalogue = MediaCatalogue()
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    series2 = TVSeries('Game of Thrones', 2011, 'David Benioff & D.B. Weiss', 57, 8, 73)
    catalogue.add(movie1)
    catalogue.add(movie2)
    catalogue.add(series1)
    catalogue.add(series2)
    print(catalogue)
except ValueError as e:
    print(f"Validation Error: {e}")