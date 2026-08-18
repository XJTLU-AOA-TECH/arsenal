# Arsenal

Codex skills forged in real AoA Tech work at XJTLU.
西浦 AoA 技术团队在真实工作中沉淀的 Codex skill 兵器库，欢迎取用。

## Skills

| Skill | What it does | 用途 |
|-------|--------------|------|
| [xipu-press](xipu-press/) | Turn raw text and images into print-ready A4 documents in the XJTLU house style (handbooks, briefings, reports, handover docs). | 把一堆文字和图片变成西浦风格的 A4 文档（手册、简报、报告、交接文档），中英双语均可。 |

## Use a skill / 使用

**Codex** — just tell Codex:

> Install the skill `xipu-press` from the GitHub repo XJTLU-AOA-TECH/arsenal.
> （跟 Codex 说：从 GitHub 仓库 XJTLU-AOA-TECH/arsenal 安装 xipu-press 这个 skill。）

Codex's built-in skill-installer downloads it into `~/.codex/skills/`; it takes effect from the next turn. Public repo, no login needed.

**Claude Code** — ask Claude Code to do the same, or run:

```bash
git clone --depth 1 https://github.com/XJTLU-AOA-TECH/arsenal.git
cp -R arsenal/xipu-press ~/.claude/skills/
```

Both tools read the same SKILL.md skill format, so the skill behaves the same in either.
两个工具读取同一种 SKILL.md 标准格式，效果一致。

**Updating / 更新**：skills do not auto-sync. To pick up a newer version, delete the old folder and install again.
skill 不会自动同步；更新时删掉旧目录重新安装一次即可。

## Add a skill / 收录新 skill

One folder per skill, containing at minimum a `SKILL.md` (name + description in frontmatter), plus optional `scripts/`, `references/`, `assets/`. Keep skills self-contained and reusable by colleagues: no personal paths, no credentials, no one-off content.
每个 skill 一个文件夹，至少包含 `SKILL.md`；保持自包含、可被同事复用：不写个人路径、凭证或一次性内容。
