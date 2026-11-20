import json
from pathlib import Path


source = Path(__file__).resolve().parent
suite = source.parents[2]
master = (source / "page.html.in").read_text(encoding="utf-8")

templates = {
    "script": (
        "text-to-script/assets/script.html",
        {"title": "剧本模板", "items": [
            {"original": "她推开房门，发现信已送到。", "text": "室内。她推门进来。桌上的信封写着她的名字。"},
        ]},
    ),
    "video": (
        "script-to-storyboard/assets/video.html",
        {"title": "视频提示词模板", "items": [
            {"text": "【段落001】\n【总时长：3秒】\n\n---\n\n〈以当版一整段正式视频提示词替换本条，保留段内字段与空行。〉\n【段落结束｜001】"},
        ]},
    ),
    "assets": (
        "short-drama-storyboard/assets/assets.html",
        {"title": "资产模板", "grouped": False, "items": [
            {"category": "人设", "imageNames": ["示例人物（常服版）"], "text": "【人设图1｜示例人物】\n【生图提示词】：\n〈本条完整人设正文〉"},
            {"category": "场景", "imageNames": ["示例场景（日景）"], "text": "【权威场景设定1｜示例场景（日景）】\n【场景设定】：\n〈本条完整场景正文〉"},
            {"category": "道具", "imageNames": ["示例道具"], "text": "【道具图1｜示例道具】\n〈本条完整道具正文与版本〉"},
            {"category": "人物位置图", "group": "跨段共用图", "text": "[位置图1｜示例场景（日景）]\n【人物】：示例人物\n【场景】：示例场景（日景）\n[生图提示词]：\n〈本条完整位置图正文及版本〉"},
        ]},
    ),
}

for kind, (relative, payload) in templates.items():
    target = suite / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, ensure_ascii=False, indent=2).replace("<", "\\u003c")
    result = master.replace("@@KIND@@", kind).replace("@@TITLE@@", payload["title"]).replace("@@PAYLOAD@@", encoded)
    target.write_bytes(result.encode("utf-8"))
