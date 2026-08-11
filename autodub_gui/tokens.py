"""Design token — nguồn sự thật DUY NHẤT về màu, khoảng cách và bo góc.

Mọi file giao diện đều lấy màu từ đây. Cấm viết mã màu hex ở nơi khác.
"""
from __future__ import annotations

# -- Nền (Obsidian Dark Theme) ----------------------------------------
BG_APP          = "#0B0C0E"   # nền cửa sổ chính - đen sâu
BG_SIDEBAR      = "#0F1115"   # thanh điều hướng bên - xám đậm đá phiến
BG_MAIN         = "#0B0C0E"   # vùng nội dung chính
BG_PANEL        = "#16181D"   # nền của các thẻ / khung nhóm
BG_PANEL_HOVER  = "#1F222B"   # trạng thái rê chuột qua thẻ
BG_INPUT        = "#16181D"   # nền ô nhập liệu

# Nền phụ trợ
BG_INPUT_DISABLED = "#0F1115"
BG_BUTTON         = "#1F222B"  # nút mặc định
BG_BUTTON_PRESSED = "#2C313D"  # khi nhấn nút
BG_VIDEO          = "#060708"  # vùng chiếu video
BG_SELECTED       = "#4F46E5"  # mục đang chọn (Indigo)
BG_SELECTED_SOFT  = "rgba(79, 70, 229, 0.12)"  # màu chọn nhẹ (hover, badges)

# -- Viền (Tinh tế, siêu mảnh) ----------------------------------------
BORDER_SUBTLE   = "rgba(255, 255, 255, 0.06)"   # đường phân chia rất mảnh
BORDER_DEFAULT  = "rgba(255, 255, 255, 0.12)"   # viền mặc định của thẻ
BORDER_ACTIVE   = "#4F46E5"                      # viền khi focus
BORDER_BUTTON   = "rgba(255, 255, 255, 0.10)"   # viền nút bấm
BORDER_DANGER   = "#EF4444"
BORDER_UPLOAD   = "#4F46E5"

# -- Màu thương hiệu & Trạng thái --------------------------------------
PRIMARY         = "#4F46E5"   # Indigo chính
PRIMARY_HOVER   = "#6366F1"   # Indigo sáng
PRIMARY_DARK    = "#4338CA"
PRIMARY_GRAD_B  = "#4F46E5"
PRIMARY_GRAD_B_HOVER = "#6366F1"
PRIMARY_DISABLED_BG  = "#16181D"

# -- Màu nhấn bổ trợ --------------------------------------------------
ACCENT_BLUE     = "#3B82F6"
ACCENT_PURPLE   = "#8B5CF6"
ACCENT_PURPLE_HOVER = "#A78BFA"

# -- Chữ (Spacious & High-Contrast) -----------------------------------
TEXT_PRIMARY    = "#F9FAFB"   # chữ chính (trắng kem)
TEXT_SECONDARY  = "#9CA3AF"   # chữ phụ (xám)
TEXT_MUTED      = "#6B7280"   # chữ mờ
TEXT_DISABLED   = "#4B5563"
TEXT_ON_ACCENT  = "#FFFFFF"

# -- Trạng thái hệ thống ----------------------------------------------
SUCCESS         = "#10B981"   # xanh lục hiện đại
WARNING         = "#F59E0B"   # vàng cam hổ phách
DANGER          = "#EF4444"   # đỏ san hô
PROCESSING      = "#3B82F6"

# Nền huy hiệu tương ứng (opacity thấp)
SUCCESS_BG      = "rgba(16, 185, 129, 0.15)"
WARNING_BG      = "rgba(245, 158, 11, 0.15)"
DANGER_BG       = "rgba(239, 68, 68, 0.15)"
PROCESSING_BG   = "rgba(59, 130, 246, 0.15)"
NEUTRAL_BG      = "rgba(255, 255, 255, 0.08)"
PURPLE_BG       = "rgba(139, 92, 246, 0.15)"

# -- Dải thời gian & Waveform ------------------------------------------
WAVEFORM         = "#4F46E5"
WAVEFORM_LIGHT   = "rgba(79, 70, 229, 0.20)"
PLAYHEAD         = "#F43F5E"
SUB_BLOCK_BG     = "#16181D"
SUB_BLOCK_BORDER = "rgba(255, 255, 255, 0.08)"
SUB_BLOCK_TEXT   = "#9CA3AF"
RULER_TEXT       = "#6B7280"

# Tracks đa kênh
TRACK_ORIGINAL      = "#8B5CF6"
TRACK_ORIGINAL_BG   = "#16181D"
TRACK_VOICE         = "#10B981"
TRACK_VOICE_BG      = "rgba(16, 185, 129, 0.12)"
TRACK_MUSIC         = "#EC4899"
TRACK_MUSIC_BG      = "#16181D"
TRACK_VIDEO_BG      = "#0F1115"
TRACK_LABEL_BG      = "#0F1115"
TRACK_LABEL_BORDER  = "rgba(255, 255, 255, 0.06)"

# -- Khung xem trước & Phụ đề -----------------------------------------
PREVIEW_CANVAS_BG   = "#060708"
PREVIEW_GUIDE       = "#4F46E5"
PREVIEW_BLUR_EDGE   = "#F59E0B"
PREVIEW_EMPTY_BG    = "#16181D"
PREVIEW_EMPTY_TEXT  = "#6B7280"
LOG_BG              = "#0F1115"

# Màu chữ phụ đề mặc định khi xuất
SUBTITLE_TEXT_DEFAULT      = "#FFFFFF"
SUBTITLE_OUTLINE_DEFAULT   = "#000000"
SUBTITLE_HIGHLIGHT_DEFAULT = "#F59E0B"
SUBTITLE_BOXFILL_DEFAULT   = "#000000"

# -- Thanh cuộn & Tiến trình -----------------------------------------
STEP_DONE_BG        = "#4F46E5"
STEP_UPCOMING_BG    = "#1F222B"
STEP_UPCOMING_TEXT  = "#6B7280"

TRACK_BG        = "#0F1115"
SCROLL_HANDLE_HOVER = "#374151"
BRAND_LOGO_BG   = "rgba(79, 70, 229, 0.10)"

# -- Thẻ giọng đọc & Chip ---------------------------------------------
CHIP_BG            = "#16181D"
CHIP_BG_ACTIVE     = "rgba(79, 70, 229, 0.15)"
CHIP_BORDER_ACTIVE = "#4F46E5"
VOICE_SELECTED_BG  = "rgba(79, 70, 229, 0.08)"
SECTION_LABEL      = "#4B5563"

AVATAR_GRADIENTS = (
    ("#4F46E5", "#8B5CF6"),
    ("#EC4899", "#8B5CF6"),
    ("#3B82F6", "#4F46E5"),
    ("#10B981", "#06B6D4"),
    ("#F59E0B", "#EF4444"),
    ("#8B5CF6", "#EC4899"),
)

# -- Màu bán trong suốt (QSS rgba) ------------------------------------
NAV_SEL_GRAD_A  = "rgba(79, 70, 229, 255)"  # nền đặc hẳn cho nav selected
NAV_SEL_GRAD_B  = "rgba(79, 70, 229, 255)"
NAV_HOVER_BG    = "rgba(255, 255, 255, 0.04)"
MODAL_OVERLAY   = "rgba(0, 0, 0, 200)"
DURATION_BADGE_BG = "rgba(0, 0, 0, 180)"
UPLOAD_GRAD_A   = "rgba(79, 70, 229, 0.05)"
UPLOAD_GRAD_B   = "rgba(139, 92, 246, 0.05)"
DRAG_ACTIVE_BG  = "rgba(79, 70, 229, 0.12)"
PLAYER_BAR_BG   = "rgba(15, 17, 21, 230)"
SUBTITLE_BOX_BG = "rgba(0, 0, 0, 150)"

# -- Bo góc (Modern Rounded Corners) ----------------------------------
RADIUS_SM = 6
RADIUS_MD = 10
RADIUS_LG = 14
RADIUS_XL = 20

# -- Khoảng cách ------------------------------------------------------
SP_1, SP_2, SP_3, SP_4, SP_5, SP_6, SP_8 = 4, 8, 12, 16, 20, 24, 32

# -- Kiểu chữ ---------------------------------------------------------
FONT_STACK = '"Inter", "Segoe UI W01", "Segoe UI", Arial, sans-serif'
FONT_MONO = '"JetBrains Mono", "Fira Code", "Consolas", monospace'
FS_PAGE_TITLE   = 26
FS_SECTION      = 18
FS_CARD_TITLE   = 14
FS_BODY         = 13
FS_LABEL        = 12
FS_META         = 11
FS_BADGE        = 10

# -- Kích thước cố định -----------------------------------------------
SIDEBAR_W        = 240
SIDEBAR_W_COMPACT = 210
SIDEBAR_W_ICON   = 70
NAV_ITEM_H       = 42
HEADER_H         = 76
CARD_MIN_W       = 250

# -- Đổ bóng ----------------------------------------------------------
SHADOW_BLUR   = 30
SHADOW_Y      = 10
SHADOW_ALPHA  = 40


def rgba(hex_color: str, alpha: float) -> str:
    """Đổi mã hex '#rrggbb' thành chuỗi 'rgba(r,g,b,a)' dùng trong QSS."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha:.3f})"
