## Introduction

I went a bit overboard with this.  I wanted to create the API separate from the front end.  I also wanted the front end to function more like an app on the same page than separate app.  Honestly to just get this done quicker, I would have just used the Django admin panel or just Django forms and templates to generate everything.

Also wasted a bit of time on a charting API which did not yield any results.  Let me know if you have any problems with starting up.

Unfortunately I did not have time to write any tests for this, or further validation.

## Install dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start the server

Run migrations and start the server (must be on port 5000 as it is unfortunately hardcoded)

```
python manage.py migrate
python manage.py runserver 5000
```

## Start the front end

```
cd frontend/vue-carbon
npm run dev
```

The project should run on `http://localhost:8080`
