FROM fuzzers/atheris:2.0.7-python3.9
COPY src/syscallName_fuzz.py ./syscallNameFuzz.py
RUN apt-get update && apt-get install -y libgmp3-dev
RUN pip3 install cairo-lang

ENTRYPOINT []
CMD ["python3" "./syscallNameFuzz.py"]
