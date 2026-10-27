[English](README.md) | **简体中文**

# Troy 的规则集合 — 已归档

曾为代理客户端收集、生成的自用分流规则。**仓库已归档并停止维护。** 历史文件可以查看，但不保证准确性、兼容性或远程依赖可用；不再承诺每日更新。

## 当前保留的文件

| 文件 | 分类 |
| --- | --- |
| [Direct.list](Direct.list) | 直连服务 |
| [AsianMedia.list](AsianMedia.list) | 亚洲媒体 |
| [GlobalMedia.list](GlobalMedia.list) | 全球媒体 |
| [Global.list](Global.list) | 全球服务 |
| [GlobalDomain.list](GlobalDomain.list) | 全球服务域名规则 |
| [sgmodule/Troy.sgmodule](sgmodule/Troy.sgmodule) | 历史 Surge 模块 |
| [action/](action/) | 历史 Python 生成脚本 |

旧说明中的 `Reject.conf`、`RejectDomain.conf`、`AppleDomain.conf`、`Qobuz.conf` 和 `ChinaASN.list` 不在当前快照中，不再作为下载入口列出。

## 参考使用

复制到当前配置前先检查规则和上游来源，确认客户端语法与策略组名称，并备份现有可用配置。本仓库不提供代理服务或持续维护的订阅。

相关配置集合见 [Troy](https://github.com/Trovoy/Troy)，同样处于暂停维护状态。历史 Actions 与脚本只作为背景保留，不代表仍提供受支持的自动更新。第三方内容保持原有使用条件；本说明不新增软件许可。
