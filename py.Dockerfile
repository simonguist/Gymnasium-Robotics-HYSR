# A Dockerfile that sets up a full gym-robotics install with test dependencies
ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION
RUN apt-get -y update && apt-get install -y unzip libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev xvfb patchelf ffmpeg cmake swig

# Download mujoco
RUN mkdir /root/.mujoco && \
    cd /root/.mujoco  && \
    curl -O https://www.roboti.us/download/mjpro150_linux.zip && \
    unzip mjpro150_linux.zip && \
    curl -o /root/.mujoco/mjkey.txt https://roboti.us/file/mjkey.txt

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/.mujoco/mjpro150/bin

COPY . /usr/local/gym/
WORKDIR /usr/local/gym/

RUN pip install "mujoco_py>=1.50, <2.0"
RUN pip install . && pip install -r test_requirements.txt

ENTRYPOINT ["/usr/local/gym/bin/docker_entrypoint"]
