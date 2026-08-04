<h1 align="center">🎬 导演Skill · Director Skills</h1>

<p align="center"><strong>导演Skill：让 Agent 像导演一样，把创意、剧本、分镜、生成与成片组织成可执行的 AI 视频工作流。</strong></p>

<p align="center">
  <a href="https://github.com/kangarooking/director-skills/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/kangarooking/director-skills?style=for-the-badge&logo=github&color=ffb000"></a>
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-Standard-7c3aed?style=for-the-badge">
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge"></a>
</p>

**导演Skill（Director Skills）** 是一套面向 AI 视频创作的开源 Agent Skills。每个 Skill 都是一位专项“AI 导演”，用结构化流程帮助 Agent 完成从需求理解到可交付结果的创作任务。

适用于 Claude Code、Codex，以及其他支持 [Agent Skills](https://agentskills.io/) 开放标准的 Agent。

> 当前状态：导演Skill 已收录首个专项 Skill `travel-skill`。

---

## 📋 Skills

| 名字 | 一句话 | 状态 |
| --- | --- | --- |
| 🏝️ [travel-skill](./travel-skill) | 规划、编写、审阅和修复真实素材与 AI 镜头混合制作的文旅宣传片 | 可用 |

## 🎬 一个导演Skill 应该做什么

- 理解创作目标、受众、平台、时长与制作约束
- 完成创意定位、叙事结构、视觉风格和镜头设计
- 输出可直接生成的分段提示词、首尾帧衔接和一致性锚点
- 检查事实、版权、文化表达、模型能力与交付边界
- 通过可重复的验收标准评估画面、连续性和成片完整度

## 🗂️ 仓库结构

```text
director-skills/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── templates/
│   └── SKILL.template.md
└── <skill-name>/
    ├── SKILL.md
    ├── scripts/       # 可选：可执行脚本
    ├── references/    # 可选：方法、规范与评估标准
    └── templates/     # 可选：可复用交付模板
```

## 📦 安装方式

当某个 Skill 状态标记为“可用”后，在 Claude Code、Codex 等工具中可以直接说：

```text
帮我安装这个 skill：https://github.com/kangarooking/director-skills/tree/main/<skill-name>
```

也可以手动安装：

```bash
git clone https://github.com/kangarooking/director-skills.git

# Codex
mkdir -p ~/.codex/skills
cp -R director-skills/<skill-name> ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R director-skills/<skill-name> ~/.claude/skills/
```

## ✅ 发布标准

一个 Skill 只有在满足以下条件后，才会在目录中标记为“可用”：

1. 包含合法 frontmatter 和完整的 `SKILL.md`。
2. 写清触发场景、输入、输出、步骤和边界。
3. 需要工具或脚本时，提供安装与错误处理说明。
4. 至少跑通一个真实案例，并保留可复查的验收结果。
5. 不伪造生成结果，不隐藏模型、平台、版权或资料限制。

## 🤝 贡献

欢迎提交新的导演 Skill、案例、评估方法和实用工具。开始前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 📜 开源许可

本项目以 [MIT License](./LICENSE) 开源。使用第三方模型、素材、字体或工具时，仍需遵守对应条款。
