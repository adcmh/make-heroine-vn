## GUI 界面配置

init python:
    gui.init(1920, 1080)

    ## 中文字体（必须，否则汉字不显示）
    gui.default_font = "msyh.ttc"
    gui.text_font = "msyh.ttc"
    gui.name_text_font = "msyh.ttc"
    gui.interface_text_font = "msyh.ttc"

    ## 色彩主题
    gui.accent_color = '#ffa07a'
    gui.idle_color = '#888888'
    gui.idle_small_color = '#aaaaaa'
    gui.hover_color = '#ffa07a'
    gui.selected_color = '#ffffff'
    gui.insensitive_color = '#8888887f'

    ## 字体大小
    gui.text_size = 28
    gui.name_text_size = 36
    gui.interface_text_size = 28
    gui.label_text_size = 40
    gui.notify_text_size = 24
    gui.title_text_size = 56
    gui.choice_button_text_size = 28

    ## 文本框
    gui.textbox_height = 240
    gui.name_xpos = 60
    gui.name_ypos = 850
    gui.dialogue_xpos = 80
    gui.dialogue_ypos = 920
    gui.dialogue_width = 1760

    ## 透明度
    gui.dialogue_text_alpha = 1.0
    gui.name_text_alpha = 1.0

    ## 边框
    gui.button_width = None
    gui.button_height = 56

    ## 存档槽
    gui.slot_button_width = 300
    gui.slot_button_height = 220
    gui.slot_spacing = 20
