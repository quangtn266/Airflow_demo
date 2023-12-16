FROM python:3.8-slim

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

COPY scripts/rank_movies.py /usr/local/bin/rank-movies
RUN chmod +x /usr/local/bin/rank-movies

ENV PATH="/usr/local/bin:${PATH}"