"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY INDONESIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "INDONESIAN"
HANDLE = "@velocityindonesian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'id',
 'name': 'Indonesian',
 'native_name': 'Bahasa Indonesia',
 'history_key': 'indonesian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'id-ID-ArdiNeural',
 'native_fallback_voice': 'id-ID-GadisNeural',
 'native_engine': 'edge',
 'native_lang_code': 'id',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'BAHASA INDONESIA',
 'translit_label': 'SAY IT LIKE',
 'flag': 'id',
 'greeting': 'Halo!',
 'encouragement': 'Luar biasa!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivasi',
 'Love': 'Cinta',
 'Success': 'Sukses',
 'Wisdom': 'Kebijaksanaan',
 'Happiness': 'Kebahagiaan',
 'Self Improvement': 'Perbaikan Diri',
 'Gratitude': 'Syukur',
 'Friendship': 'Persahabatan',
 'Hope': 'Harapan',
 'Creativity': 'Kreativitas',
 'Inner Peace': 'Kedamaian Batin',
 'Confidence': 'Percaya Diri',
 'Perseverance': 'Kegigihan',
 'Inspiration': 'Inspirasi',
 'Positive Life': 'Hidup Positif',
 'Courage': 'Keberanian',
 'Kindness': 'Kebaikan',
 'Patience': 'Kesabaran',
 'Forgiveness': 'Pengampunan',
 'Strength': 'Kekuatan',
 'Joy': 'Kegembiraan',
 'Balance': 'Keseimbangan',
 'Growth': 'Pertumbuhan',
 'Purpose': 'Tujuan',
 'Mindfulness': 'Kesadaran Penuh',
 'Travel & Airport': 'Perjalanan & Bandara',
 'Ordering Food & Dining': 'Memesan Makanan & Makan',
 'Shopping & Prices': 'Belanja & Harga',
 'Asking for Directions': 'Bertanya Arah',
 'Hotel & Accommodation': 'Hotel & Akomodasi',
 'Daily Routine': 'Rutinitas Harian',
 'Meeting People & Greetings': 'Bertemu Orang & Salam',
 'Emergency & Health': 'Darurat & Kesehatan',
 'Public Transportation': 'Transportasi Umum',
 'Work & Office': 'Pekerjaan & Kantor',
 'Weather & Small Talk': 'Cuaca & Obrolan Ringan',
 'Coffee Shop & Bakery': 'Kedai Kopi & Toko Roti',
 'Family & Home': 'Keluarga & Rumah',
 'Hobbies & Free Time': 'Hobi & Waktu Luang',
 'Dating & Romance': 'Kencan & Romansa',
 'Phone Calls & Messages': 'Panggilan Telepon & Pesan',
 'Banking & Money': 'Perbankan & Uang',
 'Doctor & Pharmacy': 'Dokter & Apotek',
 'Sports & Fitness': 'Olahraga & Kebugaran',
 'Celebrations & Parties': 'Perayaan & Pesta',
 'Feelings & Emotions': 'Perasaan & Emosi',
 'Agreeing & Disagreeing': 'Setuju & Tidak Setuju',
 'Making Plans': 'Membuat Rencana',
 'Common Native Slang': 'Slang Umum Penduduk Asli',
 'Cultural Traditions': 'Tradisi Budaya'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnindonesian',
 '#indonesianlessons',
 '#indonesianforbeginners',
 '#languagelearning',
 '#indonesianvocabulary',
 '#velocityindonesian',
 '#dailyindonesian',
 '#indonesian',
 '#learnlanguages',
 '#speakindonesian']
# ==== HASHTAGS END ====
