---
name: travel-skill
description: 规划、编写、审阅和修复由真实授权素材与 AI 生成镜头混合制作的电影级文旅宣传片。用于文旅短片创意简报、场景图筛选、首帧空间分析、分镜脚本、画面内容提示词、人物动作、导演级运镜、自然动机布光、转场与尾帧衔接、Seedance 2.0/可灵/Midjourney 提示词、生成结果诊断、时间线与合规风险检查；尤其适用于需要写实、辽阔、自由感和角色剧情连续性的项目。
---

# AI 文旅电影导演

把提示词当作可执行的摄影调度，不把它写成镜头愿望清单。先确认故事、素材和首帧所允许的空间，再设计画面内容、人物动作、摄影机和光线。

## 选择工作模式

- **规划**：输出创意方向、真实/AI 素材分工、风险和待补素材。
- **编写**：输出分镜、逐镜生成包或模型提示词。
- **局部修改**：只改用户指定镜头，保留镜号及未授权变更。
- **诊断**：先分析生成视频或首尾帧，只报告原因与修改方案；除非用户要求，否则不重写全片。
- **完整制片**：依次执行下述流程并在关键节点暂停确认。

## 强制原则

1. 让运镜服从故事主体、人物动作和信息揭示，不为炫技移动摄影机。
2. 把输入首帧视为当前生成片段的空间事实。先分析画面内容，再写人物动作和运镜。
3. 不让首帧中不存在、也没有可见进入路径的草、道路、门窗、人物、建筑或遮挡物凭空出现。
4. 每次生成只安排一个主运镜，最多增加一个方向连续、物理可达的衔接动作。
5. 先写摄影机起点、轨迹、速度、跟随对象和落点，再写镜头、光线与情绪。
6. 图生视频优先描述“哪些元素动、怎么动、摄影机怎么动、最后停在哪里”；不要重新发明画面。
7. 光线必须有可解释来源。先确定环境曝光，再塑造主体；锁定曝光和白平衡。
8. 跨地点默认拆成两个生成片段，用声音桥、动作/形状匹配或剪辑连接；不要把地点变形伪装成长镜头。
9. 参考图是人物身份与服装连续性的依据。只有缺少参考图或用户要求时，才建立额外人物设定表。
10. 授权、肖像、宗教与民俗问题只做明确风险提醒，不擅自替用户判定已获授权。

## 完整工作流

### 1. 建立项目约束

记录目标、受众、平台、总时长、画幅、叙事主线、情绪、真实素材、参考人物、图片模型、视频模型及单次时长。Seedance 2.0 和可灵均可使用首尾帧；默认只在确有落点控制需要时使用尾帧。

完整项目读取 [workflow-and-gates.md](references/workflow-and-gates.md)，并复制 [project-brief.md](assets/templates/project-brief.md)。

### 2. 制定素材策略

优先让真实授权素材承担地貌、雪山、湖泊、峡谷、村落、动物和人文纪实；让 AI 承担固定角色剧情、难以补拍的动作和受控转场。记录水印、分辨率、黑边、来源、人物与文化风险。

### 3. 审计每张首帧

在写任何画面内容提示词或运镜前，完整读取 [source-frame-spatial-audit.md](references/source-frame-spatial-audit.md)，填写 [shot-manifest.yaml](assets/templates/shot-manifest.yaml) 中的空间字段。

必须回答：

- 前景、中景、背景中已经存在什么？
- 主体、出入口、可见路径和遮挡物在哪里？
- 摄影机当前高度、角度、方向与可达终点是什么？
- 哪些画面内容允许自然发生，哪些会造成凭空生成？
- 规定时长内，人物动作和摄影机是否能物理完成？

缺少关键首帧时，先列出待补场景图，不用文字强迫模型创建未知空间。

### 4. 写分镜与生成包

按“叙事目标 → 分时段画面内容 → 景别与构图 → 人物动作 → 摄影机调度 → 光影 → 声音/台词 → 尾帧”的顺序写。画面内容必须分时段，但各时段描述同一连续空间中的状态变化，不能写成多个剪辑镜头。

运镜前完整读取 [camera-motion-library.md](references/camera-motion-library.md)；布光前完整读取 [motivated-lighting-library.md](references/motivated-lighting-library.md)；涉及跨镜衔接时读取 [transitions-and-continuity.md](references/transitions-and-continuity.md)。

### 5. 适配生成模型

完整读取 [model-recipes.md](references/model-recipes.md)。中文描述中保留准确英文术语。Midjourney 提示词控制在用户或模型给定字符数内；Seedance 2.0 与可灵的单段时长以当前任务参数为准，不假定永远为 15 秒。

采用三轮迭代：

1. 只测试主体动作和一个主运镜。
2. 增加景别、速度、构图落点。
3. 再加入焦段、光线和首帧中真实存在的前景。

出现乱镜头时，先删掉第二条轨迹和无关风格词，不继续堆形容词。

### 6. 质检与修改

用 [failure-catalog.md](references/failure-catalog.md) 对生成结果做空间、动作、运镜、人物、光线、连续性、技术和风险八类检查。运行：

```bash
python3 scripts/lint_prompt.py prompt.txt --model seedance --max-chars 0
python3 scripts/validate_timeline.py storyboard.md --max-shot-seconds 15
python3 scripts/lint_shot_manifest.py shot-manifest.yaml
```

修复局部镜头时保持镜号稳定；只更新时间码和明确受影响的依赖。

## 关键确认点

完整制片默认在以下节点暂停：

1. 创意方向与叙事主线。
2. 真实/AI 素材分工与风险清单。
3. 首帧空间审计及前三个试验镜头。
4. 全部分镜与逐镜生成包。
5. 生成结果质检与最终剪辑建议。

用户明确要求批量执行时可以减少确认，但不得跳过首帧空间审计。

## 输出合同

单镜修改时只输出该镜；完整项目优先输出：

1. `00-project-brief.md`
2. `01-asset-register.csv`
3. `02-visual-reference.md`
4. `03-storyboard.md`
5. `04-shot-manifest.yaml`
6. `05-generation-prompts.md`
7. `06-generation-log.csv`
8. `07-qc-report.md`

西藏项目还必须读取 [tibet-reference.md](references/tibet-reference.md)。
