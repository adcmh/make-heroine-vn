## ============================================================
## 角色定义 - 败北女角太多了！～青春挽回作战～
## ============================================================

## ---- 主角 ----
define WZ = Character("温水和彦", color="#7ec8e3", image="wz")

## ---- 可攻略女主角 ----
define YN = Character("八奈见杏菜", color="#ffa07a", image="yn")
define SY = Character("烧盐柠檬", color="#ffd700", image="sy")
define XJ = Character("小鞠知花", color="#dda0dd", image="xj")
define BY = Character("白玉璃子", color="#ffb6c1", image="by")
define MAX = Character("马剃天爱星", color="#ff6347", image="max")

## ---- 配角 ----
define JS = Character("温水佳树", color="#98fb98", image="js")
define ZMX = Character("志喜屋梦子", color="#c0c0c0", image="zmx")
define FYH = Character("放虎原云雀", color="#b8860b")
define YJ = Character("樱井弘人", color="#87ceeb")
define YZM = Character("月之木古都", color="#ee82ee")
define YM = Character("玉木慎太郎", color="#9370db")
define GX = Character("甘夏古奈美", color="#f0e68c")
define XB = Character("小拔小夜", color="#ff69b4")

## ---- 旁白 ----
define NAR = Character(None, kind=nvl)

## ============================================================
## 好感度系统
## ============================================================
default yn_aff = 0       # 八奈见好感
default sy_aff = 0       # 烧盐好感
default xj_aff = 0       # 小鞠好感
default by_aff = 0       # 白玉好感
default max_aff = 0      # 天爱星好感
default zmx_aff = 0      # 志喜屋好感
default js_aff = 0       # 佳树好感
default route_flag = ""  # 当前攻略路线
default common_progress = 0  # 共通线进度标记

## ============================================================
## 立绘定义 (占位路径，替换为实际素材)
## ============================================================
# 温水
image wz default = "images/sprites/wz_default.png"

# 八奈见
image yn default = "images/sprites/yn_default.png"
image yn smile = "images/sprites/yn_smile.png"
image yn angry = "images/sprites/yn_angry.png"
image yn sad = "images/sprites/yn_sad.png"
image yn blush = "images/sprites/yn_blush.png"

# 烧盐
image sy default = "images/sprites/sy_default.png"
image sy smile = "images/sprites/sy_smile.png"
image sy sad = "images/sprites/sy_sad.png"
image sy sport = "images/sprites/sy_sport.png"

# 小鞠
image xj default = "images/sprites/xj_default.png"
image xj shy = "images/sprites/xj_shy.png"
image xj angry = "images/sprites/xj_angry.png"
image xj cry = "images/sprites/xj_cry.png"

# 白玉
image by default = "images/sprites/by_default.png"
image by smile = "images/sprites/by_smile.png"
image by serious = "images/sprites/by_serious.png"

# 天爱星
image max default = "images/sprites/max_default.png"
image max serious = "images/sprites/max_serious.png"
image max blush = "images/sprites/max_blush.png"

# 佳树
image js default = "images/sprites/js_default.png"
image js smile = "images/sprites/js_smile.png"

# 志喜屋
image zmx default = "images/sprites/zmx_default.png"

## ============================================================
## 背景图定义 (占位路径)
## ============================================================
image bg classroom = "images/bg/classroom.jpg"
image bg hallway = "images/bg/hallway.jpg"
image bg clubroom = "images/bg/clubroom.jpg"
image bg rooftop = "images/bg/rooftop.jpg"
image bg restaurant = "images/bg/restaurant.jpg"
image bg shrine = "images/bg/shrine.jpg"
image bg station = "images/bg/station.jpg"
image bg gym = "images/bg/gym.jpg"
image bg library = "images/bg/library.jpg"
image bg printroom = "images/bg/printroom.jpg"
image bg infirmary = "images/bg/infirmary.jpg"
image bg track = "images/bg/track.jpg"
image bg bridge = "images/bg/bridge.jpg"
image bg cafe = "images/bg/cafe.jpg"
image bg beach = "images/bg/beach.jpg"
image bg wedding = "images/bg/wedding.jpg"

## ============================================================
## BGM定义 (占位路径)
## ============================================================
define audio.bgm_main = "audio/bgm_main.ogg"
define audio.bgm_sad = "audio/bgm_sad.ogg"
define audio.bgm_tense = "audio/bgm_tense.ogg"
define audio.bgm_romance = "audio/bgm_romance.ogg"
define audio.bgm_happy = "audio/bgm_happy.ogg"
