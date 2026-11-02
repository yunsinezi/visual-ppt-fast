# Visual PPT Fast v1.1 · 八图优先

独立轻量 PPT Skill，强调制作效率，但坚持**先给用户八张真实风格图再 A/B 分流**。

## 流程
**了解需求 → 同一代表页的8张不同风格预览 → 用户选风格 → A/B分流 → 快速生成整套 → PPTX检查交付。**

八张图必须同文案、同画幅、不同构图与图像语言，独立生成并展示；不能用一张图裁片、滤镜或文字方案代替。用户可以在选风格时同时回复 A/B；已明确的编辑/动画需求不能被反复追问。正式整套制作前只保留必要的风格 Gate。

A：需要动画或后期逐元素编辑（轻量原生重建），按需动画；B：无需二者，高清静态整页图合成纯图片 PPTX。默认中文、16:9，页数按内容（通常8–12页）。ZIP、PDF 按需。真实文件 QA 不可跳过。

## 使用
> 使用 visual-ppt-fast 制作12页电影推荐PPT。先生成同一内容页的8张不同风格图让我选，再问我 A/B，选完直接批量生成整套。

## 校验
```bash
python scripts/check_workflow.py project.json
python scripts/check_delivery.py deck.pptx --expected 12
python -m unittest discover -s tests -v
```

[状态规范](references/style-first.md) · [原版完整 Skill](https://github.com/yunxinzi/visual-ppt-workflow)

本 Skill 无内置生图或PPTX引擎；所附验证器检查状态声明/部分结构，不代表图像与动画实测。MIT.
