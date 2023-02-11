FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/Xnuxer2/TygerPyro /home/TygerPyro/
WORKDIR /home/TygerPyro

RUN wget https://raw.githubusercontent.com/Xnuxer2/TygerPyro/main/requirements.txt \
    && pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt \
    && rm requirements.txt
CMD bash start

