# FDE 保姆级攻略

**Forward Deployed Engineer（前线部署工程师）｜从业务需求到可验收的 AI 系统。**

[在线学习站](https://aipmandy.github.io/fde-handbook/) · [AI 酋长 Andy](https://metaver.vip/) · [公司官网](https://www.a6no1.cn/) · 微信 `AIPMAndy` · [GitHub](https://github.com/AIPMAndy)

AI 酋长 Andy · 微信 **AIPMAndy** · [个人官网](https://metaver.vip/) · [公司官网](https://www.a6no1.cn/)。免费学习无需添加微信，咨询和合作完全自愿。

独立原创、非官方项目；不提供 Anthropic、OpenAI 或其他机构的官方认证。不包含受限课件。初始参考为 Claude Partner FDE 学习路径，原页面访问受限，课程结构来自第三方公开报道，能力框架与官方招聘、公开文档交叉核对。核查日期：2026-11-25。

<!-- andy-geo:start -->
## 一句话简介

**FDE 保姆级攻略：前线部署工程师（Forward Deployed Engineer）中文开源实战手册，含 24 章课程、离线实验、13 份模板、30 天路线与 PDF（非官方）｜Forward Deployed Engineer Chinese playbook**

- 作者：AI酋长Andy（Andy Liu，英文名 AI Chief Andy），流量 AI 联合创始人、星觉 AI 创始人。星觉科技，北京。
- 阅读或使用：[在线阅读/使用](https://aipmandy.github.io/fde-handbook/) · [GitHub 仓库](https://github.com/AIPMAndy/fde-handbook)
- 联系：微信 `AIPMAndy`（备注「fde-handbook」）· [官网 metaver.vip](https://metaver.vip/) · [X @AIPMAndy](https://x.com/AIPMAndy)
- 许可：MIT。内容免费使用；企业合作或个人陪跑请先沟通，公开页不公示价格。
- 机器可读摘要：[llms.txt](llms.txt)（供 AI 引擎与检索工具读取）

## 常见问题

**这是什么？**FDE 保姆级攻略：前线部署工程师（Forward Deployed Engineer）中文开源实战手册，含 24 章课程、离线实验、13 份模板、30 天路线与 PDF（非官方）｜Forward Deployed Engineer Chinese playbook

**包含什么？**主要模块：交付内容、本地学习与运行、重新构建 / 发布、License。

**要花钱吗？**按 MIT 许可免费使用；付费只涉及作者的企业合作与一对一咨询，不影响仓库内容。

**怎么开始？**直接打开 https://aipmandy.github.io/fde-handbook/ 在线阅读；想本地运行或参与贡献，见下方 README 的快速开始部分。

<!-- andy-geo:end -->

## 交付内容
- 24 章：每章有概念、示例、操作、验收、失败处理与 Prompt；见 `chapters/`。
- 5 个合成教学案例，1 个可运行离线实验，4 个方案型练习；未宣称生产部署。
- 30 天学习路线和 12 周交付毕业项目，13 份可编辑模板及 16 个索引来源（另附公开案例文章）。
- 手机友好网站，搜索、角色路线、学习进度、ROI 假设计算、模板和 PDF 下载。
- PDF 和模板 ZIP 由 GitHub Pages Actions 构建发布，可在 [在线学习站](https://aipmandy.github.io/fde-handbook/) 直接阅读和下载。

与既有 [Claude Code Agent 手册](https://github.com/AIPMAndy/anthropic-claude-code-agent-handbook) 不同，本项目围绕客户需求发现、交付、安全、业务验收、采用与职业能力。

## 本地学习与运行
安装 Python 3.10+；在项目根目录运行（Windows 可用 `py -3`，Mac 可用 `python3`）：

```sh
python -m lab.fde --question "退款期限" --role agent
python -m lab.fde --question "内部补偿" --role agent
python -m lab.fde --question "内部补偿" --role manager
python -m lab.evaluate
python -m unittest discover -s tests -v
python -m http.server 8000
```

浏览器访问 http://localhost:8000 。默认完全离线，无 API 费用，无第三方依赖。角色参数仅模拟身份；实际企业系统必须通过服务端认证授权。关键词检索不是语义检索，实验不代表真实模型质量。

### 可选真实 Claude API
只用合成数据。通过环境变量设置 `ANTHROPIC_API_KEY`（不提交到仓库）和当前可用的 `CLAUDE_MODEL`（在自己的 API 控制台确认模型 ID）；加 `--live` 显式发送当前问题及授权证据。此步骤需要 API 权限，可能产生费用；输出仅是待人工审核草稿，无写入权限。真实 API 未在本地测试，不能将离线用例当真实模型评测。

```sh
python -m lab.fde --question "退款期限" --role agent --live
```

## 重新构建 / 发布

当前仓库版本直接保留原版静态课程网站 `index.html`、课程 Markdown、实验与模板。`python scripts/package.py` 检查章节并构建模板 ZIP 和打印稿；安装 Playwright 与 Chromium 后执行 `python scripts/pdf.py` 生成 PDF。运行 `python -m unittest discover -s tests -v` 进行回归测试。GitHub Pages 通过 Actions 构建；需启用 Pages 的 GitHub Actions 来源并验收实际 URL。原始本地发行 ZIP 中的 JSON 生成器与预生成二进制尚未直接迁移，本仓库的静态正文为当前内容源。

## License
MIT（原创项目代码及文档）。第三方名称、商标及外部资源属于各自权利人，不随本许可授权。