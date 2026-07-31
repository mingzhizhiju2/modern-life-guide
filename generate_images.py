import os, json, urllib.request

api_key = "sk-ZaIvmumDAFVw1XpOqfDFOXJp8vLOObC5"
api_base = "https://token.sensenova.cn/v1"
model = "sensenova-u1-fast"

img_dir = "/c/Users/明智之举251/modern-life-guide/assets/sun-protection"
os.makedirs(img_dir, exist_ok=True)

def generate_and_save(prompt, filename, size="1664x2496"):
    url = f"{api_base}/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": 1
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    resp = urllib.request.urlopen(req, timeout=120)
    data = json.loads(resp.read().decode())
    img_url = data["data"][0]["url"]

    img_path = os.path.join(img_dir, filename)
    urllib.request.urlretrieve(img_url, img_path)
    file_size = os.path.getsize(img_path)
    print(f"Saved: {filename} ({file_size} bytes)")

# 1. Cover image - portrait 2:3
cover_prompt = (
    "一张极简风格的科普封面图。画面主体是一件深色 T 恤，"
    "周围用简洁的线条和图标表示紫外线被面料阻挡的意象——"
    "几条彩色光线射向衣服，被布料表面的纹理反弹回去。"
    "背景是纯色的米白色或浅灰色，"
    "整体风格像科普插画的扁平化矢量图，"
    "线条干净利落，色调温暖，"
    "构图居中，给人科学、可信、友好的感觉。"
)
generate_and_save(cover_prompt, "cover.png", "1664x2496")
print("Cover image done.")

# 2. Header image - landscape 16:9
header_prompt = (
    "一张横向的科普信息图。画面展示三种紫外线（UVA、UVB、UVC）"
    "的示意图——三条不同颜色的光线从上方射向地球，"
    "UVC 被臭氧层挡住，UVB 部分透过，UVA 大部分透过，"
    "最终到达地面。用不同颜色的光带和标注区分三种紫外线，"
    "背景简洁，"
    "风格扁平化矢量插画，"
    "科学准确但视觉友好。"
)
generate_and_save(header_prompt, "header.png", "2752x1536")
print("Header image done.")

# 3. Sun protection principle diagram - 3:4
principle_prompt = (
    "一张科普原理示意图。展示紫外线照射到衣服面料上的三个过程："
    "第一层——光线散射（箭头被反弹），"
    "第二层——纤维吸收（光线进入纤维消失），"
    "第三层——面料表面反射（光线在表面反弹）。"
    "用分步骤的箭头和图标清晰展示，"
    "每个过程配一个简单的图标和说明文字占位框。"
    "背景简洁，扁平化矢量风格，"
    "颜色用蓝色和橙色对比。"
)
generate_and_save(principle_prompt, "principle.png", "1760x2368")
print("Principle diagram done.")

# 4. Comparison chart - 3:4
comparison_prompt = (
    "一张横向对比信息图。展示三种不同面料的防晒效果对比："
    "左边是白色亚麻（稀疏织法，紫外线大量穿透），"
    "中间是白色棉布（中等密度，部分穿透），"
    "右边是深色聚酯纤维（密实织法，紫外线被阻挡）。"
    "每种面料用简单的几何图案表示织法密度，"
    "用光线箭头表示紫外线穿透情况。"
    "扁平化矢量插画风格，"
    "配色简洁清晰，科普教育风格。"
)
generate_and_save(comparison_prompt, "comparison.png", "1760x2368")
print("Comparison diagram done.")

print("All images generated.")
