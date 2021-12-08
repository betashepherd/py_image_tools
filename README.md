# python image tools


#### Env Init:
```

conda create --name openpilot python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda activate openpilot
pip install Pillow


python scale.py

```

#### Make CA:
```
$ openssl genrsa -out rootCA.key 2048
$ openssl req -x509 -new -nodes -key rootCA.key -days 3650 -out rootCA.pem -subj "/C=CN/ST=BJ/L=HaiDian/O=xyz.com/OU=RD Center/CN=App Name/emailAddress=app-rootca@xyz.com"
```

#### Make cert:
```
$ openssl genrsa -out server.key 2048
$ openssl req -new -key server.key -out server.csr -subj "/C=CN/ST=BJ/L=HaiDian/O=xyz.com/OU=RD Center/CN=App Name/emailAddress=app-rootca@xyz.com"
$ openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 500
```
