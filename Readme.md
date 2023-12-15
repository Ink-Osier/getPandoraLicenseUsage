## 项目简介

本项目是为了方便用户获取 PandoraNext License 使用情况而创建的，用户可以通过本项目获取到自己的 License 使用情况，以及用量的重置时间。

## 用法

1. git clone 本项目到本地

2. 进入项目目录，修改 `docker-compose.yml` 中的 `PANDORA_LICENSE_ID` 变量为自己的 License ID

3. 运行 `docker-compose up -d` 启动容器

## 调用方法

默认请求地址：`http://ip:53333/api/getPandoraNextLicUsage`

预期响应：

```json
{
    "current":<当前用量>,
    "ip":"<授权IP>",
    "license_id":"<证书ID>",
    "total":"<总用量>",
    "ttl":"1\u5c0f\u65f624\u5206\u949f1\u79d2" # 预期重置时间
}
```

## 更新日志

### 0.0.2

- 隐藏 ip 地址的中间两位