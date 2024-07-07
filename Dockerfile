FROM python:3.8

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev python3-venv \
    && apt-get clean

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip


COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000


SHELL ["/bin/bash", "-c"]
ENV PATH="/opt/venv/bin:$PATH"
RUN echo 'source /opt/venv/bin/activate' >> /etc/bash.bashrc

CMD ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "INFRACTION_REGISTER.wsgi:application"]
