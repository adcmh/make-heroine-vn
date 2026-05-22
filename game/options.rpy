## 游戏选项配置

init python:
    ## 标题与版本
    gui.game_title = "败北女角太多了！～青春挽回作战～"
    config.name = "負けヒロインが多すぎる！"
    config.version = "1.0.0"

    ## 画面分辨率
    gui.init(1920, 1080)

    ## 存档
    config.has_autosave = True
    config.autosave_on_quit = True
    config.autosave_on_choice = True
    config.autosave_slots = 5

    ## 快进
    config.skip_delay = 30
    config.skip_indicator = True
    config.skip_music = False

    ## 转场
    config.default_transition = dissolve
    config.enter_transition = dissolve
    config.exit_transition = dissolve

    ## 窗口标题
    config.window_title = "败北女角太多了！～青春挽回作战～"

    ## 存档文件名
    config.save_directory = "MakeHeroine-1682428446"

    ## 语言
    config.language = None
    gui.language = "schinese"

    ## 字体
    gui.default_font = "SourceHanSansSC-Regular.otf"
    gui.text_font = "SourceHanSansSC-Regular.otf"
    gui.name_text_font = "SourceHanSansSC-Bold.otf"

    ## 文字速度
    preferences.text_cps = 50
    preferences.afm_time = 15

    ## 自动前进
    config.default_afm_time = 5.0

    ## 日志功能
    config.history_length = 100

    ## 回滚
    config.rollback_enabled = True
    config.hard_rollback_limit = 50

    ## 语音
    config.auto_voice = None

    ## 转换后处理
    config.quit_action = Quit(confirm=True)

    ## 鼠标光标
    config.mouse = None

    gui.show_name = True
    gui.textbox_height = 240
    gui.name_xpos = 40
    gui.name_ypos = 850
    gui.dialogue_xpos = 60
    gui.dialogue_ypos = 920
    gui.dialogue_width = 1800
