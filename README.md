<h1 align="center">🎬 导演Skill · Director Skills</h1>

<p align="center"><strong>导演Skill：让 Agent 像导演一样，把创意、剧本、分镜、生成与成片组织成可执行的 AI 视频工作流。</strong></p>

<p align="center">
  <a href="https://github.com/kangarooking/director-skills/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/kangarooking/director-skills?style=for-the-badge&logo=github&color=ffb000"></a>
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent_Skills-Standard-7c3aed?style=for-the-badge">
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge"></a>
</p>

**导演Skill（Director Skills）** 是一套面向 AI 视频创作的开源 Agent Skills。每个 Skill 都是一位专项“AI 导演”，用结构化流程帮助 Agent 完成从需求理解到可交付结果的创作任务。

适用于 Claude Code、Codex，以及其他支持 [Agent Skills](https://agentskills.io/) 开放标准的 Agent。

> 当前状态：导演Skill 已收录 6 个专项 Skill，均为可用，覆盖文旅视频、旅拍照片首帧图生视频、影视资产提示词、动作打戏提示词、角色情绪表演提示词与 Miora 视频生成可靠性工作流。

---

## 📋 Skills

| 名字 | 一句话 | 状态 |
| --- | --- | --- |
| 🏝️ [travel-skill](./travel-skill) | 规划、编写、审阅和修复真实素材与 AI 镜头混合制作的文旅宣传片 | 可用 |
| 📷 [travel-photo-to-video](./travel-photo-to-video) | 将真实旅拍照片组织成文旅分镜，输出统一视觉母版与逐镜头首帧图生视频提示词 | 可用 |
| 🎨 [cinematic-asset-prompts](./cinematic-asset-prompts) | 从剧本提取角色、场景、道具与载具，并输出中英双语视觉资产提示词 | 可用 |
| ⚔️ [action-fight-prompt](./action-fight-prompt) | 设计带时序、动作因果、环境反馈和资产锁定的电影级动作打戏提示词 | 可用 |
| 🎭 [emotion-performance-director](./emotion-performance-director) | 将情绪、台词与潜台词转成按时间展开的可观察微表演提示词 | 可用 |
| 🎞️ [miora-video-studio](./miora-video-studio) | 为 WorkBuddy / Miora 视频生成补充参数闸门、任务轮询、落盘核验与失败恢复 | 可用 |

## 🔎 Skills 说明

### `travel-photo-to-video`

面向已有 1–10 张真实旅拍照片和旅游地点的用户，分析照片中的主体与可动元素，推荐分镜顺序，统一视觉风格，并为每张照片输出可独立复制的首帧图生视频提示词。默认每镜 4 秒，按内容在 3–6 秒内调整，保留首帧的人物、建筑、空间与光线关系，建议逐镜头生成后再剪辑。

### `cinematic-asset-prompts`

适合在正式分镜或视频生成前，把剧本中的角色、场景、道具、载具拆成可复用的视觉资产。它会先统一影调与色彩科学，再输出中英双语提示词，并严格区分角色定妆、场景空镜和道具/载具设定图。

### `action-fight-prompt`

面向近身格斗、怪兽对决、载具追逐、群战和机甲大场面。它用 2–3 秒时序拆段、动作因果链、环境反馈和参考图映射来减少瞬移、穿模与无效动作。该 Skill 只负责提示词设计，不直接提交视频生成任务。

### `emotion-performance-director`

面向真人风格 AI 视频中的角色情绪表演，将抽象情绪、台词和场景语境转成眼神、呼吸、表情、身体与声音的具体表现，并按说话前、说话中、说话后组织时序。默认输出一段可直接插入视频提示词的简洁表演描述，保留原有角色、场景、镜头和台词要求。

### `miora-video-studio`

面向已配置 WorkBuddy / Miora 工具的环境，重点解决“参数是否齐全、任务是否真的完成、成片属于哪个并发作业、规格是否与请求一致”等可靠性问题。仓库内附 `scripts/miora_watch.py`，用于登记、等待、轮询、认领和读取 MP4 文件头；它不包含凭据，也不能替代 Miora 视频生成通道。

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
├── action-fight-prompt/
├── cinematic-asset-prompts/
├── emotion-performance-director/
├── miora-video-studio/
├── travel-photo-to-video/
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
