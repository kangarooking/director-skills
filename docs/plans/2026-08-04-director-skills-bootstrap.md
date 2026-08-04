# Director Skills Bootstrap Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create and publish the public `kangarooking/director-skills` repository with a reusable Agent Skill structure and an honestly labeled travel-skill roadmap entry.

**Architecture:** Keep installable Skills as independent top-level directories with `SKILL.md` entrypoints, matching the organization used by `kangarooking-skills`. Store contributor scaffolding under `templates/`, and do not create an installable `travel-skill` entrypoint until its workflow is validated with a real case.

**Tech Stack:** Markdown, Git, GitHub CLI, Agent Skills frontmatter.

---

### Task 1: Create repository documentation

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CONTRIBUTING.md`
- Create: `.gitignore`

**Step 1:** Write the repository positioning, catalog, installation pattern, release criteria, and contribution rules.

**Step 2:** Run `rg -n "api[_-]?key|token|password|secret" -i .` and inspect every match for credential leakage.

**Step 3:** Verify every relative Markdown link resolves to an existing file.

### Task 2: Create reusable Skill scaffolding

**Files:**
- Create: `templates/SKILL.template.md`
- Create: `travel-skill/README.md`

**Step 1:** Add a generic Skill template with frontmatter, workflow, quality checks, safety, and resource routing.

**Step 2:** Add the first Skill roadmap without an incomplete `SKILL.md`.

**Step 3:** Confirm `find travel-skill -name SKILL.md` returns no result.

### Task 3: Initialize and validate Git history

**Files:** All repository files.

**Step 1:** Run `git init -b main`.

**Step 2:** Run Markdown-link, frontmatter-template, secret-pattern, and whitespace checks.

**Step 3:** Commit with `git commit -m "chore: bootstrap director skills repository"`.

### Task 4: Publish and verify GitHub repository

**Files:** Git remote metadata only.

**Step 1:** Run `gh repo create kangarooking/director-skills --public --description "Open-source Agent Skills for AI video directing, from cultural tourism films to complete production workflows." --source=. --remote=origin --push`.

**Step 2:** Read repository metadata through the GitHub API and verify Public visibility and `main` as the default branch.

**Step 3:** Read back the remote root tree and README, and compare the local and remote commit IDs.
