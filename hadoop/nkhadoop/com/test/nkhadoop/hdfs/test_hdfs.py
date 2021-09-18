from hdfs import Client

# 借助 web http 操作
client = Client("http://192.168.43.101:9870")

#client.makedirs("/abc")

x = client.list("/", status=True)
print(x[0][0])

xxx = client.status("/")
print(xxx)