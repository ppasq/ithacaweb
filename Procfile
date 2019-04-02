release: yes "yes" | python manage.py migrate
web: uwsgi --http-socket=:$PORT --master --workers=2 --threads=8 --die-on-term --wsgi-file=ithacaweb/wsgi_production.py  --static-map /media/=/app/ithacaweb/media/ --offload-threads 1
