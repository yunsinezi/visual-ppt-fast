# STYLE-FIRST 状态规范（Fast v1.1）

`brief → style_generate → style_await_selection → route → make_A / make_B → qa → delivered`

1. `style_generate` 同一正式代表页（同文案/比例/参考材料）独立生成 `previews/style-01.png` 到 `style-08.png` 八张不同风格图片。
2. `style_await_selection` 八张已实际生成**并展示给用户**后，才询问要选哪一种风格；严禁提前正式制作。
3. `route` 必须拥有用户选定的风格编号 1–8，然后才能确认 A/B。之前已说过的偏好只记录，不提前分流；同一回复可包含风格编号和 A/B。
4. `make_A` 按需原生可编辑/动画；`make_B` 逐页整图、纯图片 PPTX。用户已有明确 A/B 不重复问。
5. `qa` 和 `delivered` 核实实际文件，不将 JSON 内的声明冒充已生成的图片。

状态示例（声明而非证据）：

```json
{
 "stage":"style_await_selection",
 "representative_slide_id":"slide-03",
 "preview_slide_copy":"八张图共用的正式中文内容",
 "aspect_ratio":"16:9",
 "preview_images":["previews/style-01.png","previews/style-02.png","previews/style-03.png","previews/style-04.png","previews/style-05.png","previews/style-06.png","previews/style-07.png","previews/style-08.png"],
 "previews_displayed":true,
 "selected_style":null,
 "branch":null
}
```
