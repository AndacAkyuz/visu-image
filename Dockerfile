FROM python:3.8

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN apt-get autoremove -y python
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt update && apt install -y libsm6 libxext6
WORKDIR /opt/project
ADD . /opt/project
RUN apt update -y && apt install -y cmake
RUN pip install -r requirements.txt
CMD ["jupyter","notebook","--ip=0.0.0.0","--no-browser","--allow-root"]