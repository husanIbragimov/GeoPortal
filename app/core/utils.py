from typing import List

import bcrypt


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# Ranglar gradienti uchun doimiy o'zgaruvchi
COLOR_MAP = ['#f75c02', '#faf202', '#05ff33', '#05fff3', '#05c9ff']


# --- Ranglarni konvertatsiya va interpolatsiya qilish funksiyalari ---

def hex_to_rgb(hex_color: str) -> tuple:
    """Hex rangni (masalan, "#FFA500") RGB tuple ga o‘zgartiradi."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    """RGB tuple ni hex rangga (masalan, "#FFA500") o‘zgartiradi."""
    return '#{:02X}{:02X}{:02X}'.format(*rgb)


def interpolate_color(color1: str, color2: str, t: float) -> str:
    """
    Ikkita hex rang orasida chiziqli interpolatsiya qiladi.

    :param color1: Boshlang'ich rang (hex)
    :param color2: Tugash rang (hex)
    :param t: Interpolatsiya progressi (0 dan 1 gacha)
    :return: Interpolatsiyalangan rang (hex)
    """
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return rgb_to_hex((r, g, b))


def get_gradient_color(normalized_value: float, color_map: List[str]) -> str:
    """
    Normalizatsiyalangan qiymat asosida rang gradientini aniqlaydi.

    :param normalized_value: 0 va 1 oraligʻidagi qiymat
    :param color_map: Ranglar roʻyxati (hex formatda)
    :return: Mos keluvchi rang (hex)
    """
    n = len(color_map)
    if normalized_value <= 0:
        return color_map[0]
    if normalized_value >= 1:
        return color_map[-1]

    segment_length = 1 / (n - 1)
    segment_index = int(normalized_value / segment_length)

    # Agar normalized_value oxirgi segmentga to'g'ri kelsa
    if segment_index >= n - 1:
        return color_map[-1]

    segment_start = segment_index * segment_length
    t = (normalized_value - segment_start) / segment_length
    return interpolate_color(color_map[segment_index], color_map[segment_index + 1], t)


def calculate_color_mapping(values: List[float], color_map: List[str]) -> List[str]:
    """
    Berilgan qiymatlar uchun minimal va maksimal qiymatlar asosida normalizatsiya
    va gradient ranglarni hisoblaydi.

    :param values: Qiymatlar roʻyxati
    :param color_map: Ranglar roʻyxati (hex formatda)
    :return: Har bir qiymatga mos ranglar roʻyxati (hex formatda)
    """
    if not values:
        return []

    min_value = min(values)
    max_value = max(values)

    # Agar barcha qiymatlar teng bo'lsa, oxirgi rangni qaytaramiz
    if max_value == min_value:
        return [color_map[-1]] * len(values)

    mapped_colors = [
        get_gradient_color((value - min_value) / (max_value - min_value), color_map) for value in values
    ]
    return mapped_colors
