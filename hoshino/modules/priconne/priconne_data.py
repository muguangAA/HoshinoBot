'''
本文件配置公主连接Re:dive的相关游戏数据
'''


class _PriconneData:
    # 遵照格式： id: [台服官译简体, 日文原名, 英文名(罗马音), 常见别称, 带错别字的别称等]
    # 若暂无台服官译则用日文原名占位，台日用全角括号，英文用半角括号
    CHARA = {   
        1000: ["未知角色", "未知キャラ", "Unknown"],
        1001: ["日和", "ヒヨリ", "Hoyori", "猫拳"],
        1002: ["优衣", "ユイ", "Yui", "种田", "普田", "由衣", "结衣", "ue"],
        1003: ["怜", "レイ", "Rei", "剑圣", "普怜", "伶"],
        1004: ["禊", "ミソギ", "Misogi", "炸弹", "炸弹人", "未奏希"],
        1005: ["茉莉", "マツリ", "Matsuri", "跳跳虎", "老虎", "虎", "🐅"],
        1006: ["茜里", "アカリ", "Akari", "妹法", "妹妹法"],
        1007: ["宫子", "ミヤコ", "Miyako", "布丁", "布", "🍮"],
        1008: ["雪", "ユキ", "Yuki", "小雪", "镜子", "伪娘", "男孩子", "男孩纸"],
        1009: ["杏奈", "アンナ", "Anna", "中二", "煤气罐"],
        1010: ["真步", "マホ", "Maho", "狐狸", "真扎", "咕噜灵波", "真步"],
        1011: ["璃乃", "リノ", "Rino", "妹弓"],
        1012: ["初音", "ハツネ", "Hatsune", "hego", "星法", "星星法", "⭐法"],
        1013: ["七七香", "ナナカ", "Nanaka", "娜娜卡", "77k", "77香"],
        1014: ["霞", "カスミ", "Kasumi", "侦探", "杜宾犬", "驴", "驴子"],
        1015: ["美里", "ミサト", "Misato", "圣母"],
        1016: ["铃奈", "スズナ", "Suzuna", "暴击弓", "暴弓", "爆击弓", "爆弓", "政委"],
        1017: ["香织", "カオリ", "Kaori", "狗子", "狗", "狗拳", "🐶", "🐕"],
        1018: ["伊绪", "イオ", "Io", "老师", "魅魔"],

        1020: ["美美", "ミミ", "Mimi", "兔子", "兔兔", "萝卜霸断剑", "人参霸断剑", "天兔霸断剑", "🐇", "🐰"],
        1021: ["胡桃", "クルミ", "Kurumi", "铃铛", "🔔"],
        1022: ["依里", "ヨリ", "Yori", "姐法", "姐姐法"],
        1023: ["绫音", "アヤネ", "Ayane", "熊锤"],

        1025: ["铃莓", "スズメ", "Suzume", "女仆", "妹抖"],
        1026: ["铃", "リン", "Rin", "松鼠", "🐿"],
        1027: ["惠理子", "エリコ", "Eriko", "病娇"],
        1028: ["咲恋", "サレン", "Saren", "充电宝", "青梅竹马", "幼驯染", "院长", "园长"],
        1029: ["望", "ノゾミ", "Nozomi", "偶像", "小望"],
        1030: ["妮诺", "ニノン", "Ninon", "扇子"],
        1031: ["忍", "シノブ", "Shinobu", "普忍", "鬼父", "💀"],
        1032: ["秋乃", "アキノ", "Akino", "哈哈剑"],
        1033: ["真阳", "マヒル", "Mahiru", "奶牛", "🐄"],
        1034: ["优花梨", "ユカリ", "Yukari", "黄骑", "酒鬼", "奶骑", "圣骑", "🍺"],

        1036: ["镜华", "キョウカ", "Kyouka", "小仓唯", "xcw", "小苍唯", "8岁", "八岁", "喷水萝", "八岁喷水萝", "8岁喷水萝"],
        1037: ["智", "トモ", "Tomo", "卜毛"],
        1038: ["栞", "シオリ", "Shiori", "tp弓", "TP弓", "小栞", "白虎弓", "白虎妹"],

        1040: ["碧", "アオイ", "Aoi", "香菜", "香菜弓", "绿毛弓", "毒弓"],

        1042: ["千歌", "チカ", "Chika", "绿毛奶"],
        1043: ["真琴", "マコト", "Makoto", "狼", "🐺"],
        1044: ["伊莉亚", "イリヤ", "Iriya", "伊利亚", "伊莉雅", "伊利雅", "yly", "吸血鬼", "那个女人"],
        1045: ["空花", "クウカ", "Kuuka", "抖m", "抖"],
        1046: ["珠希", "タマキ", "Tamaki", "猫剑"],
        1047: ["纯", "ジュン", "Jun", "黑骑", "saber", "SABER"],
        1048: ["美冬", "ミフユ", "Mifuyu", "子龙", "赵子龙"],
        1049: ["静流", "シズル", "Shizuru", "姐姐"],
        1050: ["美咲", "ミサキ", "Misaki", "大眼", "👀", "👁️", "👁"],
        1051: ["深月", "ミツキ", "Mitsuki", "眼罩", "抖s"],
        1052: ["莉玛", "リマ", "Rima", "草泥马", "羊驼"],
        1053: ["莫妮卡", "モニカ", "Monika", "毛二力"],
        1054: ["纺希", "ツムギ", "Tsumugi", "裁缝", "蜘蛛侠", "🕷️", "🕸️"],
        1055: ["步未", "アユミ", "Ayumi", "路人", "路人妹"],
        1056: ["流夏", "ルカ", "Ruka", "大姐", "大姐头"],
        1057: ["吉塔", "ジータ", "Jiita", "团长", "吉他"],
        1058: ["贪吃佩可", "ペコリーヌ", "Pecoriinu", "吃货", "佩可", "公主", "饭团", "🍙"],
        1059: ["可可萝", "コッコロ", "Kokkoro", "可可罗", "妈", "普白"],
        1060: ["凯留", "キャル", "Kyaru", "黑猫", "臭鼬", "凯露", "普黑"],
        1061: ["矛依未", "ムイミ", "Muimi", "夏娜", "511", "无意义"],

        1063: ["亚里莎", "アリサ", "Arisa", "鸭梨瞎", "瞎子", "亚里沙", "鸭梨傻", "亚丽莎", "亚莉莎", "瞎子弓", "🍐🦐"],

        1065: ["カヤ", "カヤ", "Kaya"],
        1066: ["イノリ", "イノリ", "Inori"],
        1067: ["ホマレ", "ホマレ", "Homare"],
        1068: ["拉比林斯达", "ラビリスタ", "Rabirisuta", "迷宫女王", "晶"],
        1069: ["真那", "マナ", "Mana", "霸瞳皇帝", "霸瞳", "千里真那"],
        1070: ["似似花", "ネネカ", "Neneka", "变貌大妃", "nnk", "448", "捏捏卡", "变貌", "大妃"],
        1071: ["克莉丝提娜", "クリスティーナ", "Kurisutiina", "Christina", "Cristina", "誓约女君", "克总", "女帝", "克"],

        1073: ["拉基拉基", "ラジニカーント", "Kajinigaanto", "Rajiraji", "跳跃王", "垃圾垃圾"],

        1075: ["贪吃佩可(夏日)", "ペコリーヌ(サマー)", "Pekoriinu(Summer)", "水吃", "水饭", "水吃货", "水佩可", "水公主", "水饭团", "水🍙", "泳吃", "泳饭", "泳吃货", "泳佩可", "泳公主", "泳饭团", "泳🍙", "泳装吃货", "泳装公主", "泳装饭团", "泳装🍙", "佩可(夏日)"],
        1076: ["可可萝(夏日)", "コッコロ(サマー)", "Kokkoro(Summer)", "水白", "水可", "水可可", "水可可萝", "水可可罗", "泳装可可萝", "泳装可可罗"],
        1077: ["铃莓(夏日)", "スズメ(サマー)", "Suzume(Summer)", "水女仆", "水妹抖"],
        1078: ["凯留(夏日)", "キャル(サマー)", "Kyaru(Summer)", "水黑", "水黑猫", "水臭鼬", "泳装黑猫", "泳装臭鼬", "潶"],
        1079: ["珠希(夏日)", "タマキ(サマー)", "Tamaki(Summer)", "水猫剑", "水猫"],
        1080: ["美冬(夏日)", "ミフユ(サマー)", "Mifuyu(Summer)", "水子龙", "水美冬"],
        1081: ["忍(万圣节)", "シノブ(ハロウィン)", "Shinobu(Halloween)", "万圣忍", "瓜忍", "🎃忍", "🎃💀"],
        1082: ["宫子(万圣节)", "ミヤコ(ハロウィン)", "Miyako(Halloween)", "万圣布丁", "狼丁", "狼布丁", "万圣🍮", "🐺🍮", "万圣宫子"],
        1083: ["美咲(万圣节)", "ミサキ(ハロウィン)", "Misaki(Halloween)", "万圣美咲", "万圣大眼"],
        1084: ["千歌(圣诞节)", "チカ(クリスマス)", "Chika(Xmas)", "圣诞千歌", "圣千", "蛋鸽"],
        1085: ["胡桃(圣诞节)", "クルミ(クリスマス)", "Kurumi(Xmas)", "圣诞胡桃", "圣诞铃铛"],
        1086: ["绫音(圣诞节)", "アヤネ(クリスマス)", "Ayane(Xmas)", "圣诞熊锤", "蛋锤"],
        1087: ["日和(新年)", "ヒヨリ(ニューイヤー)", "Hiyori(NewYear)", "新年日和", "春猫"],
        1088: ["优衣(新年)", "ユイ(ニューイヤー)", "Yui(NewYear)", "新年优衣", "春田", "新年由衣"],
        1089: ["怜(新年)", "レイ(ニューイヤー)", "Rei(NewYear)", "春剑", "春怜", "春伶"],
        1090: ["惠理子(情人节)", "エリコ(バレンタイン)", "Eriko(Valentine)", "情人节病娇", "恋病", "情病", "恋病娇", "情病娇"],
        1091: ["静流(情人节)", "シズル(バレンタイン)", "Shizuru(Valentine)" "情人节静流", "情姐", "情人节姐姐"],
        1092: ["安", "アン", "An", "胖安", "55kg"],
        1093: ["露", "ルゥ", "Ruu", "逃课女王"],
        1094: ["古蕾娅", "グレア", "Gurea", "龙姬", "古雷娅", "古蕾亚", "古雷亚"],
        1095: ["空花(大江户)", "クウカ(オーエド)", "Kuuka(Ooedo)", "江户空花", "江户抖m", "江m", "江花"],
        1096: ["妮诺(大江户)", "ニノン(オーエド)", "Ninon(Ooedo)", "江户扇子", "忍扇"],
        1097: ["雷姆", "レム", "Remu", "蕾姆"],
        1098: ["拉姆", "ラム", "Ramu"],
        1099: ["爱蜜莉雅", "エミリア", "Emiria", "艾米莉亚", "emt", "EMT"],
        1100: ["铃奈(夏日)", "スズナ(サマー)", "Suzuna(Summer)", "瀑击弓", "水爆", "水爆弓", "水暴", "瀑", "水暴弓", "瀑弓", "泳装暴弓", "泳装爆弓"],
        1101: ["伊绪(夏日)", "イオ(サマー)", "Io(Summer)", "水魅魔", "水老师", "泳装魅魔", "泳装老师"],
        1102: ["美咲(夏日)", "ミサキ(サマー)", "Misaki(Summer)", "水大眼", "泳装大眼"],
        1103: ["咲恋(夏日)", "サレン(サマー)", "Saren(Summer)", "水电", "泳装充电宝", "泳装咲恋", "水着咲恋", "水电站", "水电宝", "水充"],
        1104: ["真琴(夏日)", "マコト(サマー)", "Makoto(Summer)", "水狼", "浪", "水🐺"],
        1105: ["香织(夏日)", "カオリ(サマー)", "Kaori(Summer)", "水狗", "泃", "水🐶", "水🐕"],
        1106: ["真步(夏日)", "マホ(サマー)", "Maho(Summer)", "水狐狸", "水真步", "水maho", "水壶"],
        1107: ["碧(插班生)", "アオイ(編入生)", "Aoi(Hennyuusei)", "生菜", "新香菜"],
        1108: ["克萝依", "クロエ", "Kuroe", "华哥"],
        1109: ["琪爱儿", "チエル", "Chieru", "切露", "茄露", "茄噜", "切噜"],
        1110: ["优妮", "ユニ", "Yuni"],
        1111: ["镜华(万圣节)", "キョウカ(ハロウィン)", "Kyouka(Halloween)", "万圣镜华", "万圣小仓唯", "万圣xcw", "猫仓唯", "黑猫仓唯", "mcw", "猫唯", "猫仓", "喵唯"],
        1112: ["禊(万圣节)", "ミソギ(ハロウィン)", "Misogi(Halloween)", "万圣炸弹人", "瓜炸弹人", "万圣炸弹", "万圣炸", "瓜炸"],
        1113: ["美美(万圣节)", "ミミ(ハロウィン)", "Mimi(Halloween)", "万圣兔", "万圣兔子", "万圣兔兔", "绷带兔", "绷带兔子", "万圣美美", "绷带美美", "万圣🐰", "绷带🐰", "🎃🐰", "万圣🐇", "绷带🐇", "🎃🐇"],
        1114: ["露娜", "ルナ", "Runa", "露仓唯", "露cw"],
        1115: ["克莉丝提娜(圣诞节)", "クリスティーナ(クリスマス)", "Kurisutiina(Xmas)", "Christina(Xmas)", "Cristina(Xmas)", "圣诞克", "圣诞克总", "圣诞女帝", "蛋克"],
        1116: ["望(圣诞节)", "ノゾミ(クリスマス)", "Nozomi(Xmas)", "圣诞望", "圣诞偶像", "蛋偶像", "蛋望"],
        1117: ["伊莉亚(圣诞节)", "イリヤ(クリスマス)", "Iriya(Xmas)", "圣诞伊莉亚", "圣诞伊利亚", "圣诞伊莉雅", "圣诞伊利雅", "圣诞yly", "圣诞吸血鬼"],

        1119: ["可可萝(新年)", "コッコロ(ニューイヤー)", "Kokkoro(NewYear)", "春可可", "春白", "新年妈", "春妈"],
        1120: ["凯留(新年)", "キャル(ニューイヤー)", "Kyaru(NewYear)", "春凯留", "春黑猫", "春黑", "春臭鼬", "新年凯留", "新年黑猫", "新年臭鼬"],
        1121: ["铃莓(新年)", "スズメ(ニューイヤー)", "Suzume(NewYear)", "春铃莓", "春女仆", "春妹抖", "新年铃莓", "新年女仆", "新年妹抖"],
        1122: ["霞(魔法少女)", "カスミ(マジカル)", "Kasumi(MagiGirl)", "魔法少女霞", "魔法侦探", "魔法杜宾犬", "魔法驴", "魔法驴子"],
        1123: ["栞(魔法少女)", "シオリ(マジカル)", "Shiori(MagiGirl)", "魔法少女栞", "魔法tp弓", "魔法TP弓", "魔法小栞", "魔法白虎弓", "魔法白虎妹", "魔法白虎"],





        # =================================== #




        1804: ["贪吃佩可(公主)", "ペコリーヌ(プリンセス)", "Pekoriinu(Princess)", "公主吃", "公主饭", "公主吃货", "公主佩可", "公主饭团", "公主🍙", "命运高达", "高达", "命运公主", "高达公主"],
    }
