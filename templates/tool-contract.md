# 工具契约
工具名：read_policy
输入：question（字符串，1–200 字）；服务端身份，不信任客户端 role。
输出：status、evidence_id、excerpt（无权限不返回内容）。
权限：最小授权，读写分离；记录最少必要的审计事件。
错误：invalid_input、no_evidence、denied、timeout；失败默认拒绝。
审计字段：request_id、认证主体 ID、工具名、结果状态、耗时（不记录秘密）。
测试：合法、匿名、越权、过期、注入、超长。
