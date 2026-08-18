# Arsenal

Codex skills forged in real AoA Tech work at XJTLU.
西浦 AoA 技术团队在真实工作中沉淀的 Codex skill 兵器库，欢迎取用。

## Skills

| Skill | What it does | 用途 |
|-------|--------------|------|
| [xipu-press](xipu-press/) | Turn raw text and images into print-ready A4 documents in the XJTLU house style (handbooks, briefings, reports, handover docs). | 把一堆文字和图片变成西浦风格的 A4 文档（手册、简报、报告、交接文档），中英双语均可。 |

## Use a skill / 使用

Copy the skill folder into your Codex skills directory:

```bash
cp -R xipu-press ~/.codex/skills/
```

Then just describe the task to Codex — the skill is picked up automatically when it matches.
拷贝后直接向 Codex 描述任务即可，命中场景时会自动调用。

## Add a skill / 收录新 skill

One folder per skill, containing at minimum a `SKILL.md` (name + description in frontmatter), plus optional `scripts/`, `references/`, `assets/`. Keep skills self-contained and reusable by colleagues: no personal paths, no credentials, no one-off content.
每个 skill 一个文件夹，至少包含 `SKILL.md`；保持自包含、可被同事复用：不写个人路径、凭证或一次性内容。
