FROM python:3.8

WORKDIR /code


COPY install.txt .

RUN pip install -r install.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN chmod +x .

COPY . .

CMD ["bash", "run.sh"]