import requests
import os
import json

# 1. 从 GitHub Secrets 环境变量中安全读取 API KEY
API_KEY = os.getenv("MIMO_KEY") 
URL = "import requests
import os
import json

# 1. 从 GitHub Secrets 环境变量中安全读取 API KEY
API_KEY = os.getenv("MIMO_API_KEY") 
URL = "https://api.mimo.xiaomi.com/v2.5/chat/completions"

# 2. 你的 30 道题库汇总数据（示例，请按此格式补全其余题目）
quiz_data = [
    {"id": 1, "q": "副驾驶归属权", "opt_a": "另一半的专属位，严禁异性入座", "opt_b": "只是个座位，顺路载人很正常"},
    {"id": 2, "q": "手机社交边界", "opt_a": "互换密码，甚至可以随时互查", "opt_b": "保留绝对隐私，信任比查手机重要"},
    {"id": 3, "q": "前任留存物品", "opt_a": "必须全部清理，断绝一切念想", "opt_b": "昂贵或有纪念意义的可保留，不代表还爱"},
    {"id": 4, "q": "异性闺蜜/兄弟", "opt_a": "婚后/恋爱后应保持物理距离，减少独处", "opt_b": "认识得比你早，纯友谊不该受限"},
    # ... 请在此处继续添加剩余的题目
]

def generate_xhs_content():
    if not API_KEY:
        print("错误：未找到 MIMO_KEY，请检查 GitHub Secrets 设置。")
        return

    all_posts = []

    for item in quiz_data:
        print(f"正在深度解析题目 {item['id']}: {item['q']}...")

        # 3. 针对小红书风格定制的精细化 Prompt
        prompt = f"""
        你是一个拥有百万粉丝的小红书情感博主，擅长写那种'让评论区吵起来'的深度价值观对比。
        
        【题目背景】：{item['q']}
        【观点A】：{item['opt_a']}
        【观点B】：{item['opt_b']}
        
        请根据以上内容生成一篇小红书笔记：
        1. [爆款标题]：要求包含“镜像坦白局”、“价值观对齐”、“情侣必测”等关键词，要扎心。
        2. [正文逻辑]：
           - 用一句话描述这种冲突发生的真实生活场景（要有呼吸感）。
           - 深度分析：为什么选A的人其实在追求“安全感”，而选B的人在追求“边界感”。
           - 犀利锐评：用一句话总结两人的镜像同步率（例如：如果是AB组合，那就是“火星撞地球”）。
        3. [互动引导]：引导大家点击测试链接，并在评论区站队。
        4. [话题标签]：#镜像坦白局 #情侣日常 #恋爱价值观 #小红书爆款
        
        注意：语气要亲切但深刻，多用 Emoji。
        """

        payload = {
            "model": "mimLM-v2.5-pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.85
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(URL, json=payload, headers=headers)
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content']
            all_posts.append({"question_id": item['id'], "xhs_content": content})
        except Exception as e:
            print(f"题目 {item['id']} 生成失败: {e}")

    # 4. 将生成的 30 套文案汇总保存
    with open("xhs_final_posts.json", "w", encoding="utf-8") as f:
        json.dump(all_posts, f, ensure_ascii=False, indent=4)
    
    print("✅ 30道题目的小红书定制文案已全部生成至 xhs_final_posts.json！")

if __name__ == "__main__":
    generate_xhs_content()"

# 2. 你的 30 道题库汇总数据（示例，请按此格式补全其余题目）
quiz_data = [
    {"id": 1, "q": "副驾驶归属权", "opt_a": "另一半的专属位，严禁异性入座", "opt_b": "只是个座位，顺路载人很正常"},
    {"id": 2, "q": "手机社交边界", "opt_a": "互换密码，甚至可以随时互查", "opt_b": "保留绝对隐私，信任比查手机重要"},
    {"id": 3, "q": "前任留存物品", "opt_a": "必须全部清理，断绝一切念想", "opt_b": "昂贵或有纪念意义的可保留，不代表还爱"},
    {"id": 4, "q": "异性闺蜜/兄弟", "opt_a": "婚后/恋爱后应保持物理距离，减少独处", "opt_b": "认识得比你早，纯友谊不该受限"},
    # ... 请在此处继续添加剩余的题目
]

def generate_xhs_content():
    if not API_KEY:
        print("错误：未找到 MIMO_KEY，请检查 GitHub Secrets 设置。")
        return

    all_posts = []

    for item in quiz_data:
        print(f"正在深度解析题目 {item['id']}: {item['q']}...")

        # 3. 针对小红书风格定制的精细化 Prompt
        prompt = f"""
        你是一个拥有百万粉丝的小红书情感博主，擅长写那种'让评论区吵起来'的深度价值观对比。
        
        【题目背景】：{item['q']}
        【观点A】：{item['opt_a']}
        【观点B】：{item['opt_b']}
        
        请根据以上内容生成一篇小红书笔记：
        1. [爆款标题]：要求包含“镜像坦白局”、“价值观对齐”、“情侣必测”等关键词，要扎心。
        2. [正文逻辑]：
           - 用一句话描述这种冲突发生的真实生活场景（要有呼吸感）。
           - 深度分析：为什么选A的人其实在追求“安全感”，而选B的人在追求“边界感”。
           - 犀利锐评：用一句话总结两人的镜像同步率（例如：如果是AB组合，那就是“火星撞地球”）。
        3. [互动引导]：引导大家点击测试链接，并在评论区站队。
        4. [话题标签]：#镜像坦白局 #情侣日常 #恋爱价值观 #小红书爆款
        
        注意：语气要亲切但深刻，多用 Emoji。
        """

        payload = {
            "model": "mimLM-v2.5-pro",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.85
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(URL, json=payload, headers=headers)
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content']
            all_posts.append({"question_id": item['id'], "xhs_content": content})
        except Exception as e:
            print(f"题目 {item['id']} 生成失败: {e}")

    # 4. 将生成的 30 套文案汇总保存
    with open("xhs_final_posts.json", "w", encoding="utf-8") as f:
        json.dump(all_posts, f, ensure_ascii=False, indent=4)
    
    print("✅ 30道题目的小红书定制文案已全部生成至 xhs_final_posts.json！")

if __name__ == "__main__":
    generate_xhs_content()
