## ============================================================
## 终幕与制作人员
## ============================================================

label ending_credits:
    scene black with dissolve
    stop music fadeout 2.0
    play music "audio/bgm_main.ogg" fadein 2.0

    ""

    centered "《败北女角太多了！～青春挽回作战～》"
    centered "—— END ——"

    centered "感谢游玩"
    centered "原作：雨森たきび《敗北女角太多了！》"
    centered "视觉小说改编制作"

    centered "STAFF"
    centered "剧本/设计：dacmh"
    centered "引擎：Ren'Py"

    centered "「我们败北女角，永不认输。」"
    centered "——文艺社全员"

    ""

    menu:
        "返回主菜单":
            return
        "重新开始":
            $ yn_aff = 0
            $ sy_aff = 0
            $ xj_aff = 0
            $ by_aff = 0
            $ max_aff = 0
            $ zmx_aff = 0
            $ js_aff = 0
            $ route_flag = ""
            jump start
