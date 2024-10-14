
- Python 3.12
- Docker  

### Local setup

After cloning the repo:

1. Setup env

```bash
# Python virtual env
python3 -m venv venv (Linux)
pytho -m venv venv (Windows)
source venv/bin/activate
```

```bash
# Env variables
# Copy example file, change values if needed
cp .env.example .env (Linux)
copy .env.example .env  (Windows)
```

2. Configure secrets

   Create secrets.py file, 
   define AUDIO_ANALYZER_SECRET_KEY, OPENAI_ANALYZER_API_KEY

3. Build and run the docker container

```
docker-compose up -d --build    
```

4. Migrate database

```
docker-compose exec web python manage.py migrate --noinput
```

5. Check if the installation succeeds by opening the [http://localhost:<WEB_PORT>/]() 

6. Try it out

create audios at '/audios/', create prompt-associations to audios at '/prompt-associations'


