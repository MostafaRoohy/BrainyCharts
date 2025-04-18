from typing import List, Dict, Optional, Literal


OnePointShapes = Literal[
    "emoji", "text", "icon", "anchored_text", "anchored_note", "note",
    "sticker", "arrow_up", "arrow_down", "flag", "vertical_line",
    "horizontal_line", "long_position", "short_position"
]

MultiPointShapes = Literal[
    "triangle", "curve", "table", "circle", "ellipse", "path", "polyline",
    "extended", "signpost", "double_curve", "arc", "price_label", "price_note",
    "arrow_marker", "cross_line", "horizontal_ray", "trend_line", "info_line",
    "trend_angle", "arrow", "ray", "parallel_channel", "disjoint_angle",
    "flat_bottom", "anchored_vwap", "pitchfork", "schiff_pitchfork_modified",
    "schiff_pitchfork", "balloon", "comment", "inside_pitchfork", "pitchfan",
    "gannbox", "gannbox_square", "gannbox_fixed", "gannbox_fan", "fib_retracement",
    "fib_trend_ext", "fib_speed_resist_fan", "fib_timezone", "fib_trend_time",
    "fib_circles", "fib_spiral", "fib_speed_resist_arcs", "fib_channel",
    "xabcd_pattern", "cypher_pattern", "abcd_pattern", "callout", "text_note",
    "triangle_pattern", "3divers_pattern", "head_and_shoulders", "fib_wedge",
    "elliott_impulse_wave", "elliott_triangle_wave", "elliott_triple_combo",
    "elliott_correction", "elliott_double_combo", "cyclic_lines", "time_cycles",
    "sine_line", "forecast", "date_range", "price_range", "date_and_price_range",
    "bars_pattern", "ghost_feed", "projection", "rectangle", "rotated_rectangle",
    "brush", "highlighter", "regression_trend", "fixed_range_volume_profile"
]
