# Director Skills 仓库骨架设计

## 目标

创建一个公开、可安装、可持续扩展的 AI 视频导演 Skills 仓库。仓库沿用 `kangarooking-skills` 的核心组织方式：根 README 作为索引，每个可安装 Skill 使用独立的根级目录，并以 `SKILL.md` 作为入口。

## 决策

第一版采用“骨架先行”方案：先发布品牌定位、仓库规范、MIT 许可证、贡献说明和通用 Skill 模板。首个 `travel-skill` 只放置范围说明，不放置虚假完成的 `SKILL.md`。这样能保持首次发布简洁，同时避免用户把未经真实案例验证的流程当作可用 Skill。

每个后续 Skill 可按需包含 `scripts/`、`references/` 和 `templates/`，但不预先建立空目录。发布标准强调可执行输出、真实案例、边界声明和密钥扫描。根 README 明确区分“计划中”与“可用”，并使用固定安装 URL 模式。

## 验收

- GitHub 仓库为 `kangarooking/director-skills`，可见性为 Public，默认分支为 `main`。
- README、LICENSE、CONTRIBUTING、Skill 模板和文旅范围说明可从远端读取。
- 仓库不包含密钥、空的可安装 Skill 或未验证的完成声明。
