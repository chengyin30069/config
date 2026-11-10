# Niri 使用說明
登出後在登入畫面選 Niri。現有 Hyprland 設定保留。

Super=Windows 鍵。Return 開 kitty；Space 開 wofi；Shift+C 關視窗；Shift+Q 登出（有確認）；Ctrl+Space 切換浮動；F 全螢幕；X 電源選單；Shift+S 區域截圖；Shift+N 通知中心；Alt+L 鎖定。
H/J/K/L 左下上右；1–0 切換固定工作區 1–10；Shift+1–0 移動視窗；左右鍵及滾輪切換工作區；T 前往 magic；Shift+T 移動到 magic；Tab 返回上一工作區。
音量、麥克風靜音、亮度、Alt+Shift+[ / ] 及媒體鍵沿用原設定。
額外：O 總覽；R 切換欄寬；[ / ] 合併或拆出視窗；Print 截圖；Ctrl+Print 螢幕截圖；Alt+Print 視窗截圖。
Super+滑鼠左鍵拖動、右鍵調整大小使用 niri 內建行為。

DMS 在 niri 中接管面板、通知、桌布、鎖屏及閒置：300 秒鎖屏，330 秒關螢幕，不自動休眠。Hyprlock 原設定保留給 Hyprland。
桌布由啟動時的 DMS IPC 指定為原 Hyprpaper 圖片。wofi 沿用既有 CSS，kitty 沿用既有設定。

差異：niri 使用捲動平鋪，無 dwindle、Hyprland 模糊或覆蓋式特殊工作區；magic 是一般工作區。觸控板沿用自然捲動，工作區手勢依 niri 原生行為。
X11 相容服務已安裝（見下方更新）。
設定已通過 niri validate；需登入 Niri 驗證實際畫面與 DMS 通知、鎖屏。

## 滿寬視窗與 Steam
預設與欄寬預設值均為 100%，置中顯示；欄內多視窗使用分頁顯示。Super+H/L 或 [ / ] 切換左右視窗，Super+J/K 切換同欄視窗。現有視窗已調整滿寬。
已安裝 xwayland-satellite；下次登入 niri 自動啟用 X11 相容服務。目前工作階段已手動啟動並開啟 Steam。

## 方向鍵更新
Super+H/L 或左右鍵：切換同工作區左右視窗。Super+J/K 或下/上鍵：切換下一個/上一個工作區。
