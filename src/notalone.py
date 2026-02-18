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

	def login(
			self,
			login: str,
			password: str) -> dict:
		data = {
			"apiKey": self.api_key,
			"login": login,
			"password": password
		}
		response = self.session.post(
			f"{self.api}/auth", data=data).json()
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
			"apiKey": self.api_key,
			"login": login,
			"email": email,
			"password": password,
			"nickname": nickname,
			"gender": gender
		}
		return self.session.post(
			f"{self.api}/register", data=data).json()

	def get_user_info(self, user_id: int) -> dict:
		data = {
			"apiKey": self.api_key,
			"userID": user_id
		}
		return self.session.post(
			f"{self.api}/getUser", data=data).json()

	def get_user_rooms(self, user_id: int) -> dict:
		data = {
			"apiKey": self.api_key,
			"userID": user_id
		}
		return self.session.post(
			f"{self.api}/getUserRooms", data=data).json()

	def get_user_favorites(
			self,
			user_id: int,
			status: int = 0,
			page: int = 1) -> dict:
		data = {
			"apiKey": self.api_key,
			"userID": user_id,
			"status": status,
			"page": page
		}
		return self.session.post(
			f"{self.api}/getUserFavorites", data=data).json()

	def get_catalog(
			self,
			page: int = 1,
			category: str = "anime",
			genres: str = "детектив,боевик",
			years: str = "2010,2022") -> dict:
		data = {
			"apiKey": self.api_key,
			"page": page,
			"category": category,
			"genres": genres,
			"years": years
		}
		return self.session.post(
			f"{self.api}/getCatalog", data=data).json()

	def get_catalog_item(self, item_id: int) -> dict:
		data = {
			"apiKey": self.api_key,
			"itemID": item_id
		}
		return self.session.post(
			f"{self.api}/getCatalogItem", data=data).json()

	def get_catalog_newest(self, page: int = 1) -> dict:
		data = {
			"apiKey": self.api_key,
			"page": page
		}
		return self.session.post(
			f"{self.api}/getCatalogNewest", data=data).json()

	def get_catalog_popular(self, page: int = 1) -> dict:
		data = {
			"apiKey": self.api_key,
			"page": page
		}
		return self.session.post(
			f"{self.api}/getCatalogPopular", data=data).json()

	def search_catalog(self, query: str) -> dict:
		data = {
			"apiKey": self.api_key,
			"query": query
		}
		return self.session.post(
			f"{self.api}/catalogSearch", data=data).json()

	def get_genres(self) -> dict:
		data = {
			"apiKey": self.api_key
		}
		return self.session.post(
			f"{self.api}/getGenres", data=data).json()

	def get_countries(self) -> dict:
		data = {
			"apiKey": self.api_key
		}
		return self.session.post(
			f"{self.api}/getCountries", data=data).json()
