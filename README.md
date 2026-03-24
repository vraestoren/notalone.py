<h1>
  <img src="https://camo.githubusercontent.com/10bb2ac9d90906d755b9e73c858dc9b07f4dfa0222e7e0dcbc3cb1258d4e29bc/68747470733a2f2f7765622e617263686976652e6f72672f7765622f3230323330313135313535343234696d5f2f68747470733a2f2f6e6f74616c6f6e652e74762f696d616765732f6c6f676f2e706e67" width="28" style="vertical-align:middle;" />
  notalone.py
</h1>

> Web-API wrapper for [notalone.tv](https://notalone.tv) — a Russian website to watch anime, movies, and other content together with friends.

## Example
```python
from notalone import NotAlone

client = NotAlone()
client.login(login="example@gmail.com", password="password")
```

## Methods

### Auth
| Method | Description |
|--------|-------------|
| `login(login, password)` | Sign in and store session token |
| `register(login, email, password, nickname, gender)` | Create a new account |

### User
| Method | Description |
|--------|-------------|
| `get_user_info(user_id)` | Get user profile info |
| `get_user_rooms(user_id)` | Get rooms the user is in |
| `get_user_favorites(user_id, status, page)` | Get user's favorite titles |

### Catalog
| Method | Description |
|--------|-------------|
| `get_catalog(page, category, genres, years)` | Browse catalog with filters |
| `get_catalog_item(item_id)` | Get details for a specific title |
| `get_catalog_newest(page)` | Get newest titles |
| `get_catalog_popular(page)` | Get popular titles |
| `search_catalog(query)` | Search titles by name |
| `get_genres()` | Get list of all genres |
| `get_countries()` | Get list of all countries |
