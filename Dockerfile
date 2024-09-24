FROM alpine:latest

ARG USER
ARG USERID
ARG GROUPID

ENV WD="/home/$USER"
ENV JUPYTER_PATH="$WD/.local/share/jupyter"
ENV JUPYTER_CONFIG_DIR="$WD/work/.jupyter"
ENV JUPYTER_RUNTIME_DIR="$WD/.jupyter-runtime/"
ENV LANGUAGE_COMPLEXITY_ENV="$WD/language-complexity"
ENV ENV="$WD/.ashrc"

RUN apk add --no-cache wget git bash nano build-base linux-headers gcc python3-dev py3-pip && ln -sf python3 /usr/bin/python
RUN echo 'INPUT ( libldap.so )' > /usr/lib/libldap_r.so

RUN addgroup --gid $GROUPID $USERNAME || echo $GROUPID already exists
RUN adduser -D -u $USERID -h "$WD" -s /bin/bash $USER $USER

USER $USER
COPY ./requirements.txt "$WD/requirements.txt"
USER $USER
RUN python -m venv "$LANGUAGE_COMPLEXITY_ENV"
USER $USER
RUN bash -c ". $LANGUAGE_COMPLEXITY_ENV/bin/activate ; pip3 install -r $WD/requirements.txt"
USER $USER
RUN echo ". $LANGUAGE_COMPLEXITY_ENV/bin/activate" >> "$ENV"
USER $USER
RUN mkdir -p "$WD/work"
WORKDIR "$WD/work"
CMD sh
