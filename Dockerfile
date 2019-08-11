FROM python:3
ADD 01_my_script.py /
RUN pip install pystrich
CMD [ "python", "./01_my_script.py" ]
