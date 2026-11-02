# Visual PPT Fast · 骨干高速版

一个强调**提效和出图速度**的独立 Agent Skill。它保留必要的内容设计与交付校验，删除原完整版中的大量人审 Gate 和高成本分层要求。

## 默认工作流

**PLAN → MAKE → PACK & CHECK**

- 不强制八套风格预览、B1/B2 对照或全稿审核。
- 用户要求明确时直接制作，未指定时默认中文、16:9、8–12 页。
- 优先每页整图生成，默认交付能直接展示的**纯图片版 PPTX**；图片内文字不具备逐元素编辑性。
- 用户明确要求可编辑/动画时，只增加必要实现，不重启完整复杂流程；如果能力不足要说明。
- 只做关键 QA：文件确实存在、页数、空白/黑块、文字和裁切。
- ZIP、PDF、工程文件按需提供，不默认制造大量附件。

## 安装

将本文件夹放入支持 Agent Skills 的工具技能目录；入口是 `SKILL.md`，且文件夹名称与 `name: visual-ppt-fast` 相同。安装和启用的具体方式依平台而异。

## 示例调用

> 用 visual-ppt-fast 做一份 10 页的《你的名字》课堂推荐 PPT，低剧透，16:9，图文均衡。直接制作，不用先提供八套预览。交付 PPTX。

## 基础校验

```bash
python scripts/check_delivery.py my-deck.pptx --expected 10
python -m unittest discover -s tests -v
```

检查器只负责 PPTX 文件结构、页数和空白对象风险，**不能证明动画能播放、文字无误或实际画面质量达标**。

## 与完整版的关系

完整版：<https://github.com/yunxinzi/visual-ppt-workflow>（视觉探索、审核、分层及复杂 QA）。

本项目为独立的精简工作流，**不修改原仓库**。实际生图和 PPTX 构建依赖宿主已有工具。

MIT License.
