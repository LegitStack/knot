FROM continuumio/anaconda3

# make room for knot
RUN mkdir /app && \
    cd /app && \
    chmod -R 777 /app && \
    mkdir /app/knot && \
    cd /app/knot && \
    chmod -R 777 /app/knot

# install knot and requirements
ADD . /app
RUN pip install -r /app/requirements.txt && /conda/bin/python /app/setup.py develop
WORKDIR /app/knot/web
