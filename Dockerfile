# 使用官方的 Python 镜像作为基础镜像
FROM dockerpull.com/python:3.10-slim

# install required ubuntu packages
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends osra libopenbabel7 libpotrace0 && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到容器中的 /app 目录
COPY . /app

# 安装应用程序所需的依赖项
RUN pip install flask

# 对外暴露端口 5000
EXPOSE 5000

# 运行 Flask 应用程序
CMD ["python", "app.py"]