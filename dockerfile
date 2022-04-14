FROM python
WORKDIR /tests
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD pytest -s /tests/ --alluredir results