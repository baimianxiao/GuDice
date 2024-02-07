# -*- encoding:utf-8 -*-
import os, sys
import json
from GuDice import Classify, API, Event, PluginManager
from flask import Flask, request
from gevent import pywsgi

app = Flask(__name__)


# 根目录
@app.route('/', methods=['POST', 'GET'])
def bot():
    data = request.data.decode('utf-8')
    data_json = json.loads(data)
    # 把区获取到的数据转为JSON格式。
    data = Classify(data_json).result()
    Manager.plugin_event(data,bot)
    return {"status": "ok", "retcode": 0}


def server_start(mode="", host="127.0.0.1", port=5900):
    if mode == "debug":
        app.run(debug=True)
        print("测试环境")
    else:
        try:
            server = pywsgi.WSGIServer((host, port), app)
            print("post服务器已启动：http://" + host + ":" + str(port))
            server.serve_forever()
        except OSError:
            print("端口被占用，请修改端口")
            input("回车关闭")


if __name__ == "__main__":
    Manager = PluginManager()
    Manager.plugin_registered()
    bot=API("127.0.0.1",5700)
    server_start()
