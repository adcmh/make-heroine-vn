## ============================================================
## 角色定义 - 败北女角太多了！～青春挽回作战～
## ============================================================

## ---- 主角 ----
define WZ = Character("温水和彦", color="#7ec8e3")

## ---- 可攻略女主角 ----
define YN = Character("八奈见杏菜", color="#ffa07a")
define SY = Character("烧盐柠檬", color="#ffd700")
define XJ = Character("小鞠知花", color="#dda0dd")
define BY = Character("白玉璃子", color="#ffb6c1")
define MAX = Character("马剃天爱星", color="#ff6347")

## ---- 配角 ----
define JS = Character("温水佳树", color="#98fb98")
define ZMX = Character("志喜屋梦子", color="#c0c0c0")
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

## ============================================================
## 占位立绘（素材补全后可替换为实际png路径）
## ============================================================
image wz default = Placeholder("boy")
image yn default = Placeholder("girl")
image yn smile = Placeholder("girl")
image yn blush = Placeholder("girl")
image yn angry = Placeholder("girl")
image yn sad = Placeholder("girl")
image sy default = Placeholder("girl")
image sy smile = Placeholder("girl")
image sy sad = Placeholder("girl")
image sy sport = Placeholder("girl")
image xj default = Placeholder("girl")
image xj shy = Placeholder("girl")
image xj angry = Placeholder("girl")
image xj cry = Placeholder("girl")
image by default = Placeholder("girl")
image by smile = Placeholder("girl")
image by serious = Placeholder("girl")
image max default = Placeholder("girl")
image max serious = Placeholder("girl")
image max blush = Placeholder("girl")
image js default = Placeholder("girl")
image js smile = Placeholder("girl")
image zmx default = Placeholder("girl")

## ============================================================
## 占位背景（素材补全后可替换为实际jpg路径）
## ============================================================
image bg classroom = Placeholder("bg")
image bg hallway = Placeholder("bg")
image bg clubroom = Placeholder("bg")
image bg rooftop = Placeholder("bg")
image bg restaurant = Placeholder("bg")
image bg shrine = Placeholder("bg")
image bg station = Placeholder("bg")
image bg gym = Placeholder("bg")
image bg library = Placeholder("bg")
image bg printroom = Placeholder("bg")
image bg infirmary = Placeholder("bg")
image bg track = Placeholder("bg")
image bg bridge = Placeholder("bg")
image bg cafe = Placeholder("bg")
image bg beach = Placeholder("bg")
image bg wedding = Placeholder("bg")
