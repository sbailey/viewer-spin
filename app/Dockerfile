# Use an official Python runtime as a parent image
FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y --no-install-recommends git swig gcc libc-dev make \
            pkg-config zlib1g-dev wcslib-dev libwcs5 libcfitsio-dev \
            libcfitsio-bin libgsl-dev netpbm libnetpbm10-dev libcairo2 libcairo2-dev

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -v --trusted-host pypi.python.org -r requirements.txt
COPY requirements2.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements2.txt

RUN git clone http://github.com/legacysurvey/decals-web viewer

WORKDIR /app/viewer

COPY uwsgi-docker.sh /app/viewer
COPY settings.py /app/viewer/viewer/
ADD secrets secrets

RUN mkdir -p /project/projectdirs/cosmo/webapp/viewer/data \
    /global/projecta/projectdirs/cosmo/work \
    /global/projecta/projectdirs/cosmo/data \
    /global/project/projectdirs/cosmo/work  \
    /global/project/projectdirs/cosmo/data

EXPOSE 5000

CMD [ "./uwsgi-docker.sh" ]

## Define environment variable
#ENV NAME World
