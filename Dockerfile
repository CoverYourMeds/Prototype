FROM python:3.6-stretch
MAINTAINER Devin Matte <devinmatte@mail.rit.edu>

RUN mkdir /opt/coveryourmeds

ADD requirements.txt /opt/coveryourmeds

WORKDIR /opt/coveryourmeds

RUN apt-get -yq update && \
    apt-get -yq install libsasl2-dev libssl-dev && \
    pip install -r requirements.txt && \
    apt-get -yq clean all

ADD . /opt/coveryourmeds

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get -yq update && \
    apt-get -yq install nodejs npm yarn && \
    yarn install && \
    npm install -g gulp && \
    gulp && \
    rm -rf node_modules && \
    apt-get -yq remove nodejs npm yarn && \
    apt-get -yq clean all

CMD ["gunicorn", "CoverYourMeds:app", "--bind=0.0.0.0:8080", "--access-logfile=-"]
