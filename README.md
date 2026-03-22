# Recommedation Engine

## How to run

### Backend

```bash
$ pip3 install -r requirement.txt
$ uvicorn app.main:app --reload
```

Note: Backend server runs on port 8000, so access the server at localhsot:8000


### Frontend

```bash
$ cd web
$ python3 -m http.server 5500
```

Note: Frontend server runs on port 5500, so access the server at localhost:5500 on chrome/firefox.