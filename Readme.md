使用說明
----
1. `Backstage_check` 需與 `chromedriver.exe` 放在同一層
2. 執行時間約 `130s`
3. 執行完成會產生 `Backstage_check_YYYY-MM-DD.txt`

chromedriver version
----
94.0.4606.61

Page List
----
+ 登入
+ 主頁
+ 帳務-遊戲績效
+ 帳務-遊戲績效(小時)
+ 帳務-遊戲績效(機器人)
+ 帳務-彩金績效
+ 帳務-刮刮樂績效
+ 帳務-遊戲排行
+ 帳務-錯誤帳務
+ 玩家-玩家資訊-玩家資訊
+ 玩家-玩家資訊-玩家帳戶
+ 玩家-玩家查詢
+ 玩家-玩家狀態
+ 玩家-Ban玩家
+ 玩家-遊戲紀錄
+ 玩家-交易紀錄
+ 玩家-熱門遊戲
+ 玩家-遊戲留存率
+ 玩家-玩家遊戲存檔
+ 玩家-裝置統計
+ 玩家-錢包轉換
+ 玩家-錢包查詢
+ 彩金-彩金(中獎名單)
+ 彩金-群組設定
+ 彩金-代理商獎池設定
+ 彩金-彩金設定
+ 彩金-獎池範圍佇列
+ 活動-活動設定(刮刮樂設定)
+ 活動-群組設定
+ 活動-玩家查詢
+ 活動-中獎名單
+ 活動-中獎績效
+ 活動-活動模組
+ 活動-活動派彩
+ 活動-排行榜活動設定
+ 活動-排行榜中獎名單
+ 大廳-遊戲設定
+ 大廳-玩家查詢-玩家資訊
+ 大廳-玩家查詢-玩家升級
+ 大廳-玩家查詢-玩家徽章收集
+ 大廳-玩家查詢-玩家徽章兌換
+ 大廳-遊戲類別-今日精選
+ 大廳-遊戲類別-遊戲類別
+ 大廳-信件發送
+ 大廳-金幣設定
+ 大廳-金幣帳務
+ 配置-我的控制台
+ 配置-代理商管理
+ 配置-API 管理-API 申請管理
+ 配置-API 管理-使用者管理
+ 配置-API 管理-註冊金鑰管理
+ 配置-帳號管理
+ 配置-遊戲配置-老虎機設定
+ 配置-遊戲配置-魚機設定
+ 配置-遊戲配置-百家樂設定
+ 配置-遊戲配置-拉密設定
+ 配置-遊戲配置-棋牌設定
+ 配置-遊戲配置-街機設定
+ 配置-遊戲配置-遊戲管理
+ 配置-遊戲配置-拉密遊戲管理
+ 配置-大廳排序
+ 配置-權限設定-功能權限
+ 配置-權限設定-功能使用者
+ 配置-權限設定-代理商權限
+ 配置-系統設定-主機資訊
+ 配置-系統設定-網域資訊
+ 配置-系統設定-資料庫設定
+ 配置-系統設定-白名單
+ 配置-系統設定-地區白名單
+ 配置-系統日誌-系統日誌
+ 配置-系統日誌-登入日誌
+ 配置-系統日誌-API 日誌
+ 配置-系統日誌-伺服器日誌

pages.py 內容說明
----
+ dict name = `page_list`
+ page_list {頁面名稱: ['頁面路徑 or 點擊目標 Xpath', '檢查內容物的 Xpath', '跳頁類型(0/1)']}
+ 跳頁類型
  + 0: 直接轉頁 -> value[0] = 頁面路徑
  + 1: 使用 click() -> value[1] = 點擊目標 Xpath