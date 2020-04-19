## Halite 4
docker build -t halite:0.2 .
docker run -v {directorio del proyecto}:/usr/src/ halite:0.2 | python run_environment.py