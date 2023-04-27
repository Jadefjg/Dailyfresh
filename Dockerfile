FROM python:3.9.10
COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
ENV PYTHONPATH=/app/:$PYTHONPATH
ENTRYPOINT ["python","app.py"]