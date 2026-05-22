## ============================================================
## 画面定义
## ============================================================

## 确认框
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    frame:
        style_prefix "confirm"
        xalign 0.5 yalign 0.5
        xpadding 40 ypadding 30
        has vbox:
            spacing 20
            text message:
                text_align 0.5
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 40
                textbutton "是":
                    action yes_action
                textbutton "否":
                    action no_action

style confirm_frame:
    background Frame([Solid("#1a1a2ecc")], 10, 10)
style confirm_button:
    size_group "confirm"
style confirm_button_text:
    size 24

## 存档/读档
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("{} 页"), auto=_("自动存档"), quick=_("快速存档"))
    use game_menu(title):
        fixed:
            if title == "保存":
                add FileScreenshot(1) xpos 1540 ypos 70
            elif title == "读取":
                add FileScreenshot(1) xpos 1540 ypos 70
            vbox:
                xpos 60 ypos 100
                hbox:
                    textbutton _("<") action FilePagePrevious()
                    textbutton page_name_value
                    textbutton _(">") action FilePageNext()
                grid 2 3:
                    xpos 40 ypos 60
                    spacing 30
                    for i in range(1, 7):
                        frame:
                            style_prefix "slot"
                            xsize 420 ysize 260
                            has vbox
                            textbutton _("存档 %d") % i:
                                action FileAction(i)
                            add FileScreenshot(i) xalign 0.5
                            text FileTime(i, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空槽位"))

## 游戏菜单
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    frame:
        background Solid("#1a1a2e")
        if scroll == "viewport":
            viewport:
                yinitial yinitial
                scrollbars "vertical"
                has vbox
                transclude
        else:
            transclude
    textbutton _("返回"):
        style_prefix "return"
        action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_frame:
    xsize 1920 ysize 1080
style game_menu_label:
    xalign 0.5 ypos 20
    size 40
style return_button:
    xpos 40 ypos 40
