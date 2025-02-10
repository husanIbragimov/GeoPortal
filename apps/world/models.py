from django.contrib.gis.db import models


class Country(models.Model):
    featurecla = models.CharField(max_length=19, null=True)
    scalerank = models.IntegerField(null=True)
    labelrank = models.IntegerField(null=True)
    sovereignt = models.CharField(max_length=32, null=True)
    sov_a3 = models.CharField(max_length=3, null=True)
    adm0_dif = models.IntegerField(null=True)
    level = models.IntegerField(null=True)
    type = models.CharField(max_length=17, null=True)
    tlc = models.CharField(max_length=1, null=True)
    admin = models.CharField(max_length=32, null=True)
    adm0_a3 = models.CharField(max_length=3, null=True)
    geou_dif = models.IntegerField(null=True)
    geounit = models.CharField(max_length=32, null=True)
    gu_a3 = models.CharField(max_length=3, null=True)
    su_dif = models.IntegerField(null=True)
    subunit = models.CharField(max_length=32, null=True)
    su_a3 = models.CharField(max_length=3, null=True)
    brk_diff = models.IntegerField(null=True)
    name = models.CharField(max_length=29, null=True)
    name_long = models.CharField(max_length=32, null=True)
    brk_a3 = models.CharField(max_length=3, null=True)
    brk_name = models.CharField(max_length=32, null=True)
    brk_group = models.CharField(max_length=17, null=True)
    abbrev = models.CharField(max_length=16, null=True)
    postal = models.CharField(max_length=4, null=True)
    formal_en = models.CharField(max_length=52, null=True)
    formal_fr = models.CharField(max_length=35, null=True)
    name_ciawf = models.CharField(max_length=33, null=True)
    note_adm0 = models.CharField(max_length=11, null=True)
    note_brk = models.CharField(max_length=63, null=True)
    name_sort = models.CharField(max_length=31, null=True)
    name_alt = models.CharField(max_length=10, null=True)
    mapcolor7 = models.IntegerField(null=True)
    mapcolor8 = models.IntegerField(null=True)
    mapcolor9 = models.IntegerField(null=True)
    mapcolor13 = models.IntegerField(null=True)
    pop_est = models.FloatField(null=True)
    pop_rank = models.IntegerField(null=True)
    pop_year = models.IntegerField(null=True)
    gdp_md = models.IntegerField(null=True)
    gdp_year = models.IntegerField(null=True)
    economy = models.CharField(max_length=26, null=True)
    income_grp = models.CharField(max_length=23, null=True)
    fips_10 = models.CharField(max_length=3, null=True)
    iso_a2 = models.CharField(max_length=5, null=True)
    iso_a2_eh = models.CharField(max_length=3, null=True)
    iso_a3 = models.CharField(max_length=3, null=True)
    iso_a3_eh = models.CharField(max_length=3, null=True)
    iso_n3 = models.CharField(max_length=3, null=True)
    iso_n3_eh = models.CharField(max_length=3, null=True)
    un_a3 = models.CharField(max_length=4, null=True)
    wb_a2 = models.CharField(max_length=3, null=True)
    wb_a3 = models.CharField(max_length=3, null=True)
    woe_id = models.IntegerField(null=True)
    woe_id_eh = models.IntegerField(null=True)
    woe_note = models.CharField(max_length=99, null=True)
    adm0_iso = models.CharField(max_length=3, null=True)
    adm0_diff = models.CharField(max_length=1, null=True)
    adm0_tlc = models.CharField(max_length=3, null=True)
    adm0_a3_us = models.CharField(max_length=3, null=True)
    adm0_a3_fr = models.CharField(max_length=3, null=True)
    adm0_a3_ru = models.CharField(max_length=3, null=True)
    adm0_a3_es = models.CharField(max_length=3, null=True)
    adm0_a3_cn = models.CharField(max_length=3, null=True)
    adm0_a3_tw = models.CharField(max_length=3, null=True)
    adm0_a3_in = models.CharField(max_length=3, null=True)
    adm0_a3_np = models.CharField(max_length=3, null=True)
    adm0_a3_pk = models.CharField(max_length=3, null=True)
    adm0_a3_de = models.CharField(max_length=3, null=True)
    adm0_a3_gb = models.CharField(max_length=3, null=True)
    adm0_a3_br = models.CharField(max_length=3, null=True)
    adm0_a3_il = models.CharField(max_length=3, null=True)
    adm0_a3_ps = models.CharField(max_length=3, null=True)
    adm0_a3_sa = models.CharField(max_length=3, null=True)
    adm0_a3_eg = models.CharField(max_length=3, null=True)
    adm0_a3_ma = models.CharField(max_length=3, null=True)
    adm0_a3_pt = models.CharField(max_length=3, null=True)
    adm0_a3_ar = models.CharField(max_length=3, null=True)
    adm0_a3_jp = models.CharField(max_length=3, null=True)
    adm0_a3_ko = models.CharField(max_length=3, null=True)
    adm0_a3_vn = models.CharField(max_length=3, null=True)
    adm0_a3_tr = models.CharField(max_length=3, null=True)
    adm0_a3_id = models.CharField(max_length=3, null=True)
    adm0_a3_pl = models.CharField(max_length=3, null=True)
    adm0_a3_gr = models.CharField(max_length=3, null=True)
    adm0_a3_it = models.CharField(max_length=3, null=True)
    adm0_a3_nl = models.CharField(max_length=3, null=True)
    adm0_a3_se = models.CharField(max_length=3, null=True)
    adm0_a3_bd = models.CharField(max_length=3, null=True)
    adm0_a3_ua = models.CharField(max_length=3, null=True)
    adm0_a3_un = models.IntegerField(null=True)
    adm0_a3_wb = models.IntegerField(null=True)
    continent = models.CharField(max_length=23, null=True)
    region_un = models.CharField(max_length=10, null=True)
    subregion = models.CharField(max_length=25, null=True)
    region_wb = models.CharField(max_length=26, null=True)
    name_len = models.IntegerField(null=True)
    long_len = models.IntegerField(null=True)
    abbrev_len = models.IntegerField(null=True)
    tiny = models.IntegerField(null=True)
    homepart = models.IntegerField(null=True)
    min_zoom = models.FloatField(null=True)
    min_label = models.FloatField(null=True)
    max_label = models.FloatField(null=True)
    label_x = models.FloatField(null=True)
    label_y = models.FloatField(null=True)
    ne_id = models.BigIntegerField(null=True)
    wikidataid = models.CharField(max_length=8, null=True)
    name_ar = models.CharField(max_length=67, null=True)
    name_bn = models.CharField(max_length=83, null=True)
    name_de = models.CharField(max_length=35, null=True)
    name_en = models.CharField(max_length=36, null=True)
    name_es = models.CharField(max_length=36, null=True)
    name_fa = models.CharField(max_length=55, null=True)
    name_fr = models.CharField(max_length=39, null=True)
    name_el = models.CharField(max_length=72, null=True)
    name_he = models.CharField(max_length=62, null=True)
    name_hi = models.CharField(max_length=84, null=True)
    name_hu = models.CharField(max_length=38, null=True)
    name_id = models.CharField(max_length=36, null=True)
    name_it = models.CharField(max_length=32, null=True)
    name_ja = models.CharField(max_length=48, null=True)
    name_ko = models.CharField(max_length=42, null=True)
    name_nl = models.CharField(max_length=30, null=True)
    name_pl = models.CharField(max_length=38, null=True)
    name_pt = models.CharField(max_length=35, null=True)
    name_ru = models.CharField(max_length=67, null=True)
    name_sv = models.CharField(max_length=30, null=True)
    name_tr = models.CharField(max_length=32, null=True)
    name_uk = models.CharField(max_length=79, null=True)
    name_ur = models.CharField(max_length=47, null=True)
    name_vi = models.CharField(max_length=53, null=True)
    name_zh = models.CharField(max_length=33, null=True)
    name_zht = models.CharField(max_length=33, null=True)
    fclass_iso = models.CharField(max_length=24, null=True)
    tlc_diff = models.CharField(max_length=1, null=True)
    fclass_tlc = models.CharField(max_length=30, null=True)
    fclass_us = models.CharField(max_length=30, null=True)
    fclass_fr = models.CharField(max_length=15, null=True)
    fclass_ru = models.CharField(max_length=15, null=True)
    fclass_es = models.CharField(max_length=12, null=True)
    fclass_cn = models.CharField(max_length=24, null=True)
    fclass_tw = models.CharField(max_length=15, null=True)
    fclass_in = models.CharField(max_length=14, null=True)
    fclass_np = models.CharField(max_length=24, null=True)
    fclass_pk = models.CharField(max_length=15, null=True)
    fclass_de = models.CharField(max_length=15, null=True)
    fclass_gb = models.CharField(max_length=15, null=True)
    fclass_br = models.CharField(max_length=12, null=True)
    fclass_il = models.CharField(max_length=15, null=True)
    fclass_ps = models.CharField(max_length=12, null=True)
    fclass_sa = models.CharField(max_length=15, null=True)
    fclass_eg = models.CharField(max_length=24, null=True)
    fclass_ma = models.CharField(max_length=24, null=True)
    fclass_pt = models.CharField(max_length=15, null=True)
    fclass_ar = models.CharField(max_length=12, null=True)
    fclass_jp = models.CharField(max_length=15, null=True)
    fclass_ko = models.CharField(max_length=15, null=True)
    fclass_vn = models.CharField(max_length=12, null=True)
    fclass_tr = models.CharField(max_length=15, null=True)
    fclass_id = models.CharField(max_length=24, null=True)
    fclass_pl = models.CharField(max_length=15, null=True)
    fclass_gr = models.CharField(max_length=12, null=True)
    fclass_it = models.CharField(max_length=15, null=True)
    fclass_nl = models.CharField(max_length=15, null=True)
    fclass_se = models.CharField(max_length=15, null=True)
    fclass_bd = models.CharField(max_length=24, null=True)
    fclass_ua = models.CharField(max_length=12, null=True)
    geom = models.MultiPolygonField(srid=-1)

    def __str__(self): return self.name


# Auto-generated `LayerMapping` dictionary for Country model
country_mapping = {
    'featurecla': 'featurecla',
    'scalerank': 'scalerank',
    'labelrank': 'LABELRANK',
    'sovereignt': 'SOVEREIGNT',
    'sov_a3': 'SOV_A3',
    'adm0_dif': 'ADM0_DIF',
    'level': 'LEVEL',
    'type': 'TYPE',
    'tlc': 'TLC',
    'admin': 'ADMIN',
    'adm0_a3': 'ADM0_A3',
    'geou_dif': 'GEOU_DIF',
    'geounit': 'GEOUNIT',
    'gu_a3': 'GU_A3',
    'su_dif': 'SU_DIF',
    'subunit': 'SUBUNIT',
    'su_a3': 'SU_A3',
    'brk_diff': 'BRK_DIFF',
    'name': 'NAME',
    'name_long': 'NAME_LONG',
    'brk_a3': 'BRK_A3',
    'brk_name': 'BRK_NAME',
    'brk_group': 'BRK_GROUP',
    'abbrev': 'ABBREV',
    'postal': 'POSTAL',
    'formal_en': 'FORMAL_EN',
    'formal_fr': 'FORMAL_FR',
    'name_ciawf': 'NAME_CIAWF',
    'note_adm0': 'NOTE_ADM0',
    'note_brk': 'NOTE_BRK',
    'name_sort': 'NAME_SORT',
    'name_alt': 'NAME_ALT',
    'mapcolor7': 'MAPCOLOR7',
    'mapcolor8': 'MAPCOLOR8',
    'mapcolor9': 'MAPCOLOR9',
    'mapcolor13': 'MAPCOLOR13',
    'pop_est': 'POP_EST',
    'pop_rank': 'POP_RANK',
    'pop_year': 'POP_YEAR',
    'gdp_md': 'GDP_MD',
    'gdp_year': 'GDP_YEAR',
    'economy': 'ECONOMY',
    'income_grp': 'INCOME_GRP',
    'fips_10': 'FIPS_10',
    'iso_a2': 'ISO_A2',
    'iso_a2_eh': 'ISO_A2_EH',
    'iso_a3': 'ISO_A3',
    'iso_a3_eh': 'ISO_A3_EH',
    'iso_n3': 'ISO_N3',
    'iso_n3_eh': 'ISO_N3_EH',
    'un_a3': 'UN_A3',
    'wb_a2': 'WB_A2',
    'wb_a3': 'WB_A3',
    'woe_id': 'WOE_ID',
    'woe_id_eh': 'WOE_ID_EH',
    'woe_note': 'WOE_NOTE',
    'adm0_iso': 'ADM0_ISO',
    'adm0_diff': 'ADM0_DIFF',
    'adm0_tlc': 'ADM0_TLC',
    'adm0_a3_us': 'ADM0_A3_US',
    'adm0_a3_fr': 'ADM0_A3_FR',
    'adm0_a3_ru': 'ADM0_A3_RU',
    'adm0_a3_es': 'ADM0_A3_ES',
    'adm0_a3_cn': 'ADM0_A3_CN',
    'adm0_a3_tw': 'ADM0_A3_TW',
    'adm0_a3_in': 'ADM0_A3_IN',
    'adm0_a3_np': 'ADM0_A3_NP',
    'adm0_a3_pk': 'ADM0_A3_PK',
    'adm0_a3_de': 'ADM0_A3_DE',
    'adm0_a3_gb': 'ADM0_A3_GB',
    'adm0_a3_br': 'ADM0_A3_BR',
    'adm0_a3_il': 'ADM0_A3_IL',
    'adm0_a3_ps': 'ADM0_A3_PS',
    'adm0_a3_sa': 'ADM0_A3_SA',
    'adm0_a3_eg': 'ADM0_A3_EG',
    'adm0_a3_ma': 'ADM0_A3_MA',
    'adm0_a3_pt': 'ADM0_A3_PT',
    'adm0_a3_ar': 'ADM0_A3_AR',
    'adm0_a3_jp': 'ADM0_A3_JP',
    'adm0_a3_ko': 'ADM0_A3_KO',
    'adm0_a3_vn': 'ADM0_A3_VN',
    'adm0_a3_tr': 'ADM0_A3_TR',
    'adm0_a3_id': 'ADM0_A3_ID',
    'adm0_a3_pl': 'ADM0_A3_PL',
    'adm0_a3_gr': 'ADM0_A3_GR',
    'adm0_a3_it': 'ADM0_A3_IT',
    'adm0_a3_nl': 'ADM0_A3_NL',
    'adm0_a3_se': 'ADM0_A3_SE',
    'adm0_a3_bd': 'ADM0_A3_BD',
    'adm0_a3_ua': 'ADM0_A3_UA',
    'adm0_a3_un': 'ADM0_A3_UN',
    'adm0_a3_wb': 'ADM0_A3_WB',
    'continent': 'CONTINENT',
    'region_un': 'REGION_UN',
    'subregion': 'SUBREGION',
    'region_wb': 'REGION_WB',
    'name_len': 'NAME_LEN',
    'long_len': 'LONG_LEN',
    'abbrev_len': 'ABBREV_LEN',
    'tiny': 'TINY',
    'homepart': 'HOMEPART',
    'min_zoom': 'MIN_ZOOM',
    'min_label': 'MIN_LABEL',
    'max_label': 'MAX_LABEL',
    'label_x': 'LABEL_X',
    'label_y': 'LABEL_Y',
    'ne_id': 'NE_ID',
    'wikidataid': 'WIKIDATAID',
    'name_ar': 'NAME_AR',
    'name_bn': 'NAME_BN',
    'name_de': 'NAME_DE',
    'name_en': 'NAME_EN',
    'name_es': 'NAME_ES',
    'name_fa': 'NAME_FA',
    'name_fr': 'NAME_FR',
    'name_el': 'NAME_EL',
    'name_he': 'NAME_HE',
    'name_hi': 'NAME_HI',
    'name_hu': 'NAME_HU',
    'name_id': 'NAME_ID',
    'name_it': 'NAME_IT',
    'name_ja': 'NAME_JA',
    'name_ko': 'NAME_KO',
    'name_nl': 'NAME_NL',
    'name_pl': 'NAME_PL',
    'name_pt': 'NAME_PT',
    'name_ru': 'NAME_RU',
    'name_sv': 'NAME_SV',
    'name_tr': 'NAME_TR',
    'name_uk': 'NAME_UK',
    'name_ur': 'NAME_UR',
    'name_vi': 'NAME_VI',
    'name_zh': 'NAME_ZH',
    'name_zht': 'NAME_ZHT',
    'fclass_iso': 'FCLASS_ISO',
    'tlc_diff': 'TLC_DIFF',
    'fclass_tlc': 'FCLASS_TLC',
    'fclass_us': 'FCLASS_US',
    'fclass_fr': 'FCLASS_FR',
    'fclass_ru': 'FCLASS_RU',
    'fclass_es': 'FCLASS_ES',
    'fclass_cn': 'FCLASS_CN',
    'fclass_tw': 'FCLASS_TW',
    'fclass_in': 'FCLASS_IN',
    'fclass_np': 'FCLASS_NP',
    'fclass_pk': 'FCLASS_PK',
    'fclass_de': 'FCLASS_DE',
    'fclass_gb': 'FCLASS_GB',
    'fclass_br': 'FCLASS_BR',
    'fclass_il': 'FCLASS_IL',
    'fclass_ps': 'FCLASS_PS',
    'fclass_sa': 'FCLASS_SA',
    'fclass_eg': 'FCLASS_EG',
    'fclass_ma': 'FCLASS_MA',
    'fclass_pt': 'FCLASS_PT',
    'fclass_ar': 'FCLASS_AR',
    'fclass_jp': 'FCLASS_JP',
    'fclass_ko': 'FCLASS_KO',
    'fclass_vn': 'FCLASS_VN',
    'fclass_tr': 'FCLASS_TR',
    'fclass_id': 'FCLASS_ID',
    'fclass_pl': 'FCLASS_PL',
    'fclass_gr': 'FCLASS_GR',
    'fclass_it': 'FCLASS_IT',
    'fclass_nl': 'FCLASS_NL',
    'fclass_se': 'FCLASS_SE',
    'fclass_bd': 'FCLASS_BD',
    'fclass_ua': 'FCLASS_UA',
    'geom': 'MULTIPOLYGON',
}
