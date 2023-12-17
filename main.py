from flask import Flask, jsonify, request, Response
import requests
import os
import json

app = Flask(__name__)


VERSION = '0.0.4'
UPDATE_INFO = '再次增加错误提示'

@app.route('/api/getPandoraNextLicUsage', methods=['GET'])
def get_pandora_next_lic_usage():
    # 向 Pandora Next API 发起请求
    response = requests.get(f'https://dash.pandoranext.com/api/{license_id}/usage')
    if response.status_code == 200:
        data = response.json()
        
        # 解析 TTL
        ttl_seconds = int(data.get('ttl', 0))
        hours = ttl_seconds // 3600
        minutes = (ttl_seconds % 3600) // 60
        seconds = ttl_seconds % 60
        
        # 更新数据
        data['ttl'] = f"{hours}小时{minutes}分钟{seconds}秒"

        # 保护license_id参数，仅显示前后3位
        data['license_id'] = f"{license_id[:3]}***{license_id[-3:]}"

        # 保护ip参数，隐藏中间部分
        ip = data['ip']
        ip = ip.split('.')
        ip[2] = '*'
        ip[1] = '*'
        ip = '.'.join(ip)
        data['ip'] = ip


        return jsonify(data)
    else:
        print(f"无法从 Pandora Next 获取数据，状态码：{response.status_code}, 响应：{response.text}")
        print(f"请求地址：https://dash.pandoranext.com/api/{license_id}/usage，可以尝试用相同的出口ip手动访问该链接")
        return jsonify({"error": "无法从 Pandora Next 获取数据"}), 500

if __name__ == '__main__':
    global license_id
    license_id = os.getenv('PANDORA_LICENSE_ID')
    print(f"License ID: {license_id}")
    if not license_id:
        # 退出
        print("未设置 Pandora License ID 环境变量")
        exit(1)
    print(f"Version: {VERSION}")
    print(f"Update Info: {UPDATE_INFO}")
    app.run(host='0.0.0.0', port=23333)
