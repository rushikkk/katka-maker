FROM python:3.6
COPY . /
#RUN apk update && apk upgrade && \
#    apk add --no-cache bash git
RUN pip install pip --upgrade
#RUN pip install -r requirements.txt
RUN pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
CMD [ "python", "bot.py" ]
