# 思维协作 / Thinking Collaboration

当你和AI反复沟通，任务却没推进，这套Skill帮助检查目标、依据、前提与推进方式，再把判断落实到下一步动作。

它是LONG在真实项目中迭代的协作指令，不是新模型，也不保证任务必然成功。当前版本包含多种按需使用的方法；“目标校准、目标收敛、证据思维、问题重构”是视频里的四个理解入口，不是固定顺序问卷。

## 安装

- [ ] 使用支持Agent Skills的客户端，例如Codex或Claude Code。
- [ ] 命令行安装需Node.js/npx；手工安装只需解压ZIP。

```bash
npx skills add Lonc2100/thinking-collaboration --skill thinking-collaboration
```

手工安装：下载Release的 `thinking-collaboration-v1.0.0.zip`，解压后把整个 `thinking-collaboration` 文件夹放进客户端的Skills目录；Codex可使用 `~/.codex/skills/`。文件夹内应直接能找到 `SKILL.md`，不是再套一层同名文件夹。重新加载客户端并检查技能是否出现。普通ChatGPT聊天不会因为下载ZIP而自动获得此能力。

## 你可以直接这样说

> 请用思维协作Skill，帮我看一下我现在卡在哪里，下一步应该怎么解决。当前情况是……我想要的结果是……已经试过……

目标不清：帮我把想要的结果和完成条件说清楚。反复返修：守住这轮目标，先处理真正阻碍它的问题。AI说完成：核对实际产物和用途证据。反复无效：检查前提或问题定义是否需要调整。

## 当前版本与视频

v1.0.0首次公开包保留本机当前执行正文。“目标收敛”在当前版本中重点是结果、范围与完成口径；视频中路线、速度、形式的讲解偏向实现条件。不能把这套方法当成AI擅自换目标的授权。

## 边界

只在关键缺口出现时介入，不每轮跑全套；不代替写作、代码、知识整理等专业流程，不自动执行跨对话后台任务，不保证爆款、商业收益或所有项目有效。技能被客户端发现不等于每次调用效果已验证。

## 包内容与验证

`SKILL.md`是入口，`references/methods.md`是方法库，`agents/`提供展示信息，`assets/`提供图标。版本与检查记录在manifest和reports中，不含本人的项目对话、录音或账号凭据。

本地结构验证可使用 qiaomu-meta-skill 的 `python scripts/validate_skill.py <本目录>`；仓库的 `python -m unittest discover -s tests` 只核对包结构及关键边界，不证明实际推理效果。触发样例和检查报告注明机械检查的范围。

## Troubleshooting

找不到技能：检查客户端是否支持Skills、目录层级和是否重新加载。没有触发：明确写出 `thinking-collaboration`，附当前任务和卡点。回答泛泛：补充原始结果、预期和失败尝试，要求给出具体下一步；不要只重复方法名。若仍失败，请记录当前版本、客户端和具体输出再反馈。

## License

MIT，Copyright (c) 2026 LONG / Lonc2100。方法名称是任务协作中的通俗称呼；通用方法不主张原创发明。
