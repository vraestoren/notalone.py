from requests import Session

class NotAlone:
    def __init__(self) -> None:
        self.api = "https://api.notalone.tv"
        self.api_key = "odsu6JggH90Z1D69AVCw"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.token = None
        self.user_id = None

    def _post(self, endpoint: str, data: dict = None) -> dict:
        payload = {
            "apiKey": self.api_key
        }
        if data:
            payload.update(data)
        return self.session.post(f"{self.api}{endpoint}", data=payload).json()

    def login(self, login: str, password: str) -> dict:
        data = {
            "login": login,
            "password": password
        }
        response = self._post("/auth", data)
        if "token" in response["data"]:
            self.token = response["data"]["token"]
            self.user_id = response["data"]["id"]
        return response

    def register(
            self,
            login: str,
            email: str,
            password: str,
            nickname: str,
            gender: str = "male") -> dict:
        data = {
            "login": login,
            "email": email,
            "password": password,
            "nickname": nickname,
            "gender": gender
        }
        return self._post("/register", data)

    def get_user_info(self, user_id: int) -> dict:
        data = {
            "userID": user_id
        }
        return self._post("/getUser", data)

    def get_user_rooms(self, user_id: int) -> dict:
        data = {
            "userID": user_id
        }
        return self._post("/getUserRooms", data)

    def get_user_favorites(
            self,
            user_id: int,
            status: int = 0,
            page: int = 1) -> dict:
        data = {
            "userID": user_id,
            "status": status,
            "page": page
        }
        return self._post("/getUserFavorites", data)

    def get_catalog(
            self,
            page: int = 1,
            category: str = "anime",
            genres: str = "детектив,боевик",
            years: str = "2010,2022") -> dict:
        data = {
            "page": page,
            "category": category,
            "genres": genres,
            "years": years
        }
        return self._post("/getCatalog", data)

    def get_catalog_item(self, item_id: int) -> dict:
        data = {
            "itemID": item_id
        }
        return self._post("/getCatalogItem", data)

    def get_catalog_newest(self, page: int = 1) -> dict:
        data = {
            "page": page
        }
        return self._post("/getCatalogNewest", data)

    def get_catalog_popular(self, page: int = 1) -> dict:
        data = {
            "page": page
        }
        return self._post("/getCatalogPopular", data)

    def search_catalog(self, query: str) -> dict:
        data = {
            "query": query
        }
        return self._post("/catalogSearch", data)

    def get_genres(self) -> dict:
        return self._post("/getGenres")

    def get_countries(self) -> dict:
        return self._post("/getCountries")
