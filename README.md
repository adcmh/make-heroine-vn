# 败北女角太多了！～青春挽回作战～

基于《敗北女角太多了！》原作改编的 Ren'Py 视觉小说。

## 技术信息

- **引擎**: Ren'Py 8.5.2
- **分辨率**: 1920x1080
- **语言**: 简体中文

## 游戏概要

- **共通线**: 8 章（序章 → 第八章）
- **可攻略角色**: 5 人 + 2 隐藏路线 + 1 修罗场结局
- **总结局数**: 18 个（每角色 3 结局 + 3 特殊结局）

### 路线一览

| 路线 | 角色 | 结局数 | 主题 |
|------|------|--------|------|
| 八奈见杏菜 | 吃货损友 | 3 | 食欲与恋心 |
| 烧盐柠檬 | 田径王牌 | 3 | 奔跑的理由 |
| 小鞠知花 | 内向腐女 | 3 | 从壳里爬出来 |
| 白玉璃子 | 心机学妹 | 3 | 假面下的真心 |
| 马剃天爱星 | 学生会长 | 3 | 认真的喜欢 |
| 志喜屋梦子 | 丧尸学姐 | 1 | 隐藏线 |
| 温水佳树 | 兄控妹妹 | 1 | 隐藏线 |
| 女性公敌 | 全员 | 1 | 修罗场 |

## 素材准备

### 立绘
将角色立绘放入 `game/images/sprites/`，按 `characters.rpy` 中定义的名称命名：
```
yn_default.png, yn_smile.png, yn_angry.png, yn_sad.png, yn_blush.png  (八奈见)
sy_default.png, sy_smile.png, sy_sad.png, sy_sport.png                 (烧盐)
xj_default.png, xj_shy.png, xj_angry.png, xj_cry.png                   (小鞠)
by_default.png, by_smile.png, by_serious.png                           (白玉)
max_default.png, max_serious.png, max_blush.png                        (天爱星)
js_default.png, js_smile.png                                           (佳树)
wz_default.png                                                         (温水)
zmx_default.png                                                        (志喜屋)
```
- 推荐格式：PNG，透明背景
- 当前 `人物立绘/` 目录下的 JPG 图片需处理（去背景→导出 PNG）

### 背景图
放入 `game/images/bg/`，名称参考 `characters.rpy` 中的 `image bg_*` 定义。

### 音乐/BGM
放入 `game/audio/`，FLAC 需转换为 OGG 格式：
```bash
ffmpeg -i "输入.flac" -acodec libvorbis -q:a 5 "输出.ogg"
```
当前可用音乐：
- `LOVE 2000（八奈见人物曲）.flac` → 转换为 `bgm_main.ogg`
- `结尾曲（可当插曲）.flac` → 转换为 `bgm_romance.ogg`

## 运行

1. 用 Ren'Py Launcher 打开本项目文件夹
2. 点击「启动工程」

或直接：将本文件夹拖到 Ren'Py.exe 上。

## 文件结构

```
败犬女主/
├── project.json
└── game/
    ├── script.rpy              # 共通线 (8章)
    ├── characters.rpy          # 角色定义 + 好感度系统
    ├── options.rpy             # 游戏设置
    ├── gui.rpy                 # GUI 配置
    ├── screens.rpy             # 界面定义
    ├── routes/
    │   ├── yanaami.rpy         # 八奈见线
    │   ├── yakishio.rpy        # 烧盐线
    │   ├── komari.rpy          # 小鞠线
    │   ├── shiratama.rpy       # 白玉线
    │   ├── tengoku.rpy         # 天爱星线
    │   ├── shikishi.rpy        # 志喜屋隐藏线
    │   ├── kaju.rpy            # 佳树线
    │   ├── harem.rpy           # 修罗场结局
    │   └── ending.rpy          # 终幕/STAFF
    ├── images/
    │   ├── sprites/            # 角色立绘
    │   └── bg/                 # 背景图
    └── audio/                  # BGM/音效
```
