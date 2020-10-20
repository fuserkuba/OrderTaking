FROM python:3.8
ADD api_rest/ /api_rest
WORKDIR /api_rest
RUN apt-get upgrade
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]