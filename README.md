
- Python 3.12
- Docker  

### Local setup

After cloning the repo:

1. configure environment at .env

2. Configure secrets

   Create secrets_.py file, 
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

   create audios at '/audios/' out of .wav, create prompt-associations to audios at '/prompt-associations'


